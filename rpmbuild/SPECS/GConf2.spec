Summary:           A process-transparent configuration system
Name:              GConf2
Version:           3.2.6
Release:           1%{?dist}
License:           LGPLv2+ and GPLv2+
Group:             System Environment/Base
URL:               http://projects.gnome.org/gconf/
Source0:           http://download.gnome.org/sources/GConf/3.2/GConf-%{version}.tar.xz
Source1:           macros.gconf2
Patch0:            GConf-gettext.patch
Patch1:            drop-spew.patch
Patch2:            GConf-shebang.patch
Patch99:           workaround-crash.patch
Patch100:          pkill-hack.patch
BuildRequires:     libxml2-devel >= 2.4.12
BuildRequires:     libxslt-devel
BuildRequires:     glib2-devel >= 2.25.9
BuildRequires:     gtk-doc >= 0.9
BuildRequires:     pkgconfig >= 0.14
BuildRequires:     gettext
BuildRequires:     intltool
BuildRequires:     polkit-devel >= 0.92
BuildRequires:     dbus-glib-devel >= 0.8
BuildRequires:     gobject-introspection-devel >= 0.6.7
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     libtool
Requires:          dbus
Requires:          /usr/bin/killall
Conflicts:         GConf2-dbus
Provides:          GConf2-gtk = 3.2.6-6
Obsoletes:         GConf2-gtk < 3.2.6-6

%description
GConf is a process-transparent configuration database API used to
store user preferences. It has pluggable backends and features to
support workgroup administration.

%package devel
Summary:           Headers and libraries for GConf development
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}
Requires:          libxml2-devel >= 2.4.12
Requires:          glib2-devel >= 2.25.9
Requires:          pkgconfig
Requires:          automake
Conflicts:         GConf2-dbus-devel

%description devel
GConf development package. Contains files needed for doing
development using GConf.

%prep
%setup -q -n GConf-%{version}
%patch0 -p1 -b .gettext
%patch1 -p1 -b .drop-spew
%patch2 -p1 -b .shebang
%patch99 -p1 -b .workaround-crash
%patch100 -p1 -b .pkill-hack

autoreconf -i -f

%build
%configure --disable-static --enable-defaults-service --disable-orbit --with-gtk=3.0

sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

make

%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gconf/gconf.xml.system
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/rpm-state/gconf
mkdir -p $RPM_BUILD_ROOT%{_datadir}/GConf/gsettings

install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/GConf/2/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la

mkdir -p $RPM_BUILD_ROOT%{_datadir}/GConf/gsettings

%find_lang %name

%post
/sbin/ldconfig

if [ $1 -gt 1 ]; then
    if ! grep -F -q gconf.xml.system %{_sysconfdir}/gconf/2/path; then
        sed -i -e 's@xml:readwrite:$(HOME)/.gconf@&\n\n# Location for system-wide settings.\nxml:readonly:/etc/gconf/gconf.xml.system@' %{_sysconfdir}/gconf/2/path
    fi
fi

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc COPYING NEWS README
%config(noreplace) %{_sysconfdir}/gconf/2/path
%dir %{_sysconfdir}/gconf
%dir %{_sysconfdir}/gconf/2
%dir %{_sysconfdir}/gconf/gconf.xml.defaults
%dir %{_sysconfdir}/gconf/gconf.xml.mandatory
%dir %{_sysconfdir}/gconf/gconf.xml.system
%dir %{_sysconfdir}/gconf/schemas
%{_bindir}/gconf-merge-tree
%{_bindir}/gconftool-2
%{_bindir}/gsettings-data-convert
%doc %{_mandir}/man1/gsettings-data-convert.1*
%{_sysconfdir}/xdg/autostart/gsettings-data-convert.desktop
%{_libexecdir}/gconfd-2
%{_libdir}/*.so.*
%{_libdir}/GConf/2/*.so
%dir %{_datadir}/sgml
%{_datadir}/sgml/gconf
%{_datadir}/GConf
%{_mandir}/man1/*
%dir %{_libdir}/GConf
%dir %{_libdir}/GConf/2
%{_sysconfdir}/rpm/macros.gconf2
%{_sysconfdir}/dbus-1/system.d/org.gnome.GConf.Defaults.conf
%{_libexecdir}/gconf-defaults-mechanism
%{_datadir}/polkit-1/actions/org.gnome.gconf.defaults.policy
%{_datadir}/dbus-1/system-services/org.gnome.GConf.Defaults.service
%{_datadir}/dbus-1/services/org.gnome.GConf.service
%dir %{_localstatedir}/lib/rpm-state/
%{_localstatedir}/lib/rpm-state/gconf/
%{_libdir}/gio/modules/libgsettingsgconfbackend.so
%{_libdir}/girepository-1.0

%files devel
%{_libdir}/*.so
%{_includedir}/gconf
%{_datadir}/aclocal/*.m4
%{_datadir}/gtk-doc/html/gconf
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0
%{_bindir}/gsettings-schema-convert
%doc %{_mandir}/man1/gsettings-schema-convert.1*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with GConf2 3.2.6
- Based on CentOS: GConf2-3.2.6-8.el7.src.rpm
