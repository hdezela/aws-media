Summary:       The Ogg bitstream file format library
Name:          libogg
Epoch:         2
Version:       1.3.2
Release:       1%{?dist}
Group:         System Environment/Libraries
License:       BSD
URL:           http://www.xiph.org/
Source:        http://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.xz

%description
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams.

%package devel
Summary:       Files needed for development using libogg
Group:         Development/Libraries
Requires:      libogg = %{epoch}:%{version}-%{release}
Requires:      pkgconfig
Requires:      automake

%description devel
Libogg is a library used for manipulating Ogg bitstreams. The
libogg-devel package contains the header files and documentation
needed for development using libogg.

%package devel-docs
Summary:       Documentation for developing Ogg applications
Group:         Development/Libraries
BuildArch:     noarch

%description devel-docs
Documentation for developing applications with libogg

%prep
%setup -q

%build
sed -i "s/-O20/$RPM_OPT_FLAGS/" configure
sed -i "s/-ffast-math//" configure
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

rm -rf _installed_docs
mv $RPM_BUILD_ROOT%{_docdir}/%{name} _installed_docs
#mv _installed_docs/ogg _installed_docs/libogg

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS CHANGES COPYING README
%{_libdir}/libogg.so.*

%files devel
%dir %{_includedir}/ogg
%{_includedir}/ogg/ogg.h
%{_includedir}/ogg/os_types.h
%{_includedir}/ogg/config_types.h
%{_libdir}/libogg.so
%{_libdir}/pkgconfig/ogg.pc
%{_datadir}/aclocal/ogg.m4

%files devel-docs
%doc _installed_docs/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libogg 1.3.2
- Based on CentOS: libogg-1.3.0-7.el7.src.rpm
