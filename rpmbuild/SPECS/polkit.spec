Summary:           An authorization framework
Name:              polkit
Version:           0.112
Release:           1%{?dist}
License:           LGPLv2+
Group:             System Environment/Libraries
URL:               http://www.freedesktop.org/wiki/Software/polkit
Source0:           http://www.freedesktop.org/software/polkit/releases/%{name}-%{version}.tar.gz
Patch0:            polkit-0.112-XDG_RUNTIME_DIR.patch
Patch1:            polkit-0.112-PolkitAgentSession-race.patch
BuildRequires:     glib2-devel >= 2.30.0
BuildRequires:     expat-devel
BuildRequires:     pam-devel
BuildRequires:     gtk-doc
BuildRequires:     intltool
BuildRequires:     gobject-introspection-devel
BuildRequires:     mozjs17
Requires:          dbus
Requires(pre):     shadow-utils
Requires(post):    /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
Obsoletes:         PolicyKit <= 0.10
Provides:          PolicyKit = 0.11
Conflicts:         polkit-gnome < 0.97
Obsoletes:         polkit-desktop-policy < 0.103
Provides:          polkit-desktop-policy = 0.103
Obsoletes:         polkit-js-engine < 0.110-4
Provides:          polkit-js-engine = %{version}-%{release}

%description
polkit is a toolkit for defining and handling authorizations.  It is
used for allowing unprivileged processes to speak to privileged
processes.

%package devel
Summary:           Development files for polkit
Group:             Development/Libraries
Requires:          %name = %{version}-%{release}
Requires:          %name-docs = %{version}-%{release}
Requires:          glib2-devel
Obsoletes:         PolicyKit-devel <= 0.10
Provides:          PolicyKit-devel = 0.11

%description devel
Development files for polkit.

%package docs
Summary:           Development documentation for polkit
Group:             Development/Libraries
Requires:          %name-devel = %{version}-%{release}
Obsoletes:         PolicyKit-docs <= 0.10
Provides:          PolicyKit-docs = 0.11
BuildArch:         noarch

%description docs
Development documentation for polkit.

%prep
%setup -q
%patch0 -p1 -b .XDG_RUNTIME_DIR
%patch1 -p1 -b .PolkitAgentSession-race

%build
export CFLAGS='-fPIC %optflags'
export LDFLAGS='-pie -Wl,-z,now -Wl,-z,relro'
%configure --enable-gtk-doc \
  --disable-static \
  --enable-introspection \
  --disable-examples \
  --enable-libsystemd-login=no \
  --with-mozjs=mozjs-17.0
make V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang polkit-1

%pre
getent group polkitd >/dev/null || groupadd -r polkitd
getent passwd polkitd >/dev/null || useradd -r -g polkitd -d / -s /sbin/nologin -c "User for polkitd" polkitd
exit 0

%post
/sbin/ldconfig

%preun

%postun
/sbin/ldconfig

%files -f polkit-1.lang
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_libdir}/lib*.so.*
%{_datadir}/man/man1/*
%{_datadir}/man/man8/*
%{_datadir}/dbus-1/system-services/*
#%{_unitdir}/polkit.service
%dir %{_datadir}/polkit-1/
%dir %{_datadir}/polkit-1/actions
%attr(0700,polkitd,root) %dir %{_datadir}/polkit-1/rules.d
%{_datadir}/polkit-1/actions/org.freedesktop.policykit.policy
%dir %{_sysconfdir}/polkit-1
%{_sysconfdir}/polkit-1/rules.d/50-default.rules
%attr(0700,polkitd,root) %dir %{_sysconfdir}/polkit-1/rules.d
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
%{_sysconfdir}/pam.d/polkit-1
%{_bindir}/pkaction
%{_bindir}/pkcheck
%{_bindir}/pkttyagent
%dir %{_prefix}/lib/polkit-1
%{_prefix}/lib/polkit-1/polkitd
%{_libdir}/girepository-1.0/*.typelib

%attr(4755,root,root) %{_bindir}/pkexec
%attr(4755,root,root) %{_prefix}/lib/polkit-1/polkit-agent-helper-1

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_includedir}/*

%files docs
%defattr(-,root,root,-)
%{_datadir}/gtk-doc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with polkit 112
- Based on Centos: polkit-0.112-5.el7.src.rpm
