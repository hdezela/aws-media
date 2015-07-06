Name:              libcroco
Summary:           A CSS2 parsing library
Version:           0.6.8
Release:           1%{?dist}
License:           LGPLv2
Group:             System Environment/Libraries
Source0:           http://download.gnome.org/sources/libcroco/0.6/%{name}-%{version}.tar.xz
Patch0:            libcroco-0.6.1-multilib.patch
BuildRequires:     pkgconfig
BuildRequires:     glib2-devel
BuildRequires:     libxml2-devel

%description
CSS2 parsing and manipulation library for GNOME

%package devel
Summary:           Libraries and include files for developing with libcroco
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}
Requires:          glib2-devel
Requires:          libxml2-devel

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with libcroco.

%prep
%setup -q
%patch0 -p1 -b .multilib

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING COPYING.LIB NEWS README 
%{_bindir}/csslint-0.6
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/libcroco-0.6
%{_bindir}/croco-0.6-config
%{_libdir}/pkgconfig/libcroco-0.6.pc
%{_datadir}/gtk-doc/html/libcroco

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libcroco 0.6.8
- Based on Fedora: libcroco-0.6.8-7.fc23.src
