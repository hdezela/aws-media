%define         smallversion 0.4

Name:           libvisual
Version:        0.4.0
Release:        1%{?dist}
Epoch:          1
Summary:        Abstraction library for audio visualisation plugins
Group:          Applications/Multimedia
License:        LGPLv2+
URL:            http://libvisual.sf.net
Source0:        http://dl.sf.net/libvisual/libvisual-%{version}.tar.gz
BuildRequires:  xorg-x11-proto-devel
Patch0:         libvisual-0.4.0-better-altivec-detection.patch
Patch1:         libvisual-0.4.0-inlinedefineconflict.patch
Patch2:         libvisual-0.4.0-format-security.patch

%description
Libvisual is an abstraction library that comes between applications and
audio visualisation plugins.

Often when it comes to audio visualisation plugins or programs that create
visuals they do depend on a player or something else, basically there is no
general framework that enable application developers to easy access cool
audio visualisation plugins. Libvisual wants to change this by providing
an interface towards plugins and applications, through this easy to use
interface applications can easily access plugins and since the drawing is
done by the application it also enables the developer to draw the visual
anywhere he wants.

%package devel
Summary:        Development files for libvisual
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Libvisual is an abstraction library that comes between applications and
audio visualisation plugins.

This package contains the files needed to build an application with libvisual.

%prep
%setup -q
%patch0 -p1 -b .altivec-detection
%patch1 -p1 -b .inlinedefineconflict
%patch2 -p1 -b .format-security

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}-%{smallversion}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}-%{smallversion}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc README NEWS TODO AUTHORS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}-%{smallversion}

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libvisual 0.4.0
- Based on Fedora: libvisual-0.4.0-18.fc23.src.rpm
