Name:              gnome-common
Version:           3.14.0
Release:           1%{?dist}
Summary:           Useful things common to building GNOME packages from scratch
Group:             Development/Tools
BuildArch:         noarch
License:           GPLv2+
URL:               https://wiki.gnome.org/Projects/GnomeCommon
Source0:           https://download.gnome.org/sources/%{name}/3.14/%{name}-%{version}.tar.xz
Requires:          automake
Requires:          autoconf
Requires:          autoconf-archive
Requires:          gettext
Requires:          libtool
Requires:          pkgconfig
Requires:          yelp-tools

%description
This package contains sample files that should be used to develop pretty much
every GNOME application.  The programs included here are not needed for running
GNOME apps or building ones from distributed tarballs.  They are only useful
for compiling from git sources or when developing the build infrastructure for
a GNOME application.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}
cp -p doc-build/README doc-README

%install
make DESTDIR=%{buildroot} INSTALL="install -p" install

%files
%doc doc-README ChangeLog README
%license COPYING
%{_bindir}/*
%{_datadir}/aclocal/*
%exclude %{_datadir}/aclocal/ax_*
%{_datadir}/%{name}

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with gnome-common 3.14.0
- Based on Fedora: gnome-common-3.14.0-3.fc23.src
