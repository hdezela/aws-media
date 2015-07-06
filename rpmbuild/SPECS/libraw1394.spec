Summary:        Library providing low-level IEEE-1394 access
Name:           libraw1394
Version:        2.1.0
Release:        2%{?dist}
License:        LGPLv2+
Group:          System Environment/Libraries
Source:         http://www.kernel.org/pub/linux/libs/ieee1394/%{name}-%{version}.tar.xz
URL:            http://www.dennedy.org/libraw1394/
ExcludeArch:    s390 s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  autoconf automake libtool kernel-headers

%description
The libraw1394 library provides direct access to the IEEE-1394 bus.
Support for both the obsolete ieee1394 interface and the new firewire
intererface are included, with run-time detection of the active stack.

%package devel
Summary:        Development libs for libraw1394
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}, pkgconfig

%description devel
Development libraries needed to build applications against libraw1394.

%prep
%setup -q

%build
%configure --disable-static
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libraw1394.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%doc COPYING.LIB README NEWS
%{_bindir}/dumpiso
%{_bindir}/sendiso
%{_bindir}/testlibraw
%{_libdir}/libraw1394.so.*
%{_mandir}/man1/dumpiso.1.gz
%{_mandir}/man1/sendiso.1.gz
%{_mandir}/man1/testlibraw.1.gz
%{_mandir}/man5/isodump.5.gz

%files devel
%defattr(-,root,root,0755)
%doc doc/libraw1394.sgml
%{_includedir}/libraw1394/
%{_libdir}/libraw1394.so
%{_libdir}/pkgconfig/libraw1394.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Rpath removed from libtool

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libraw1394 2.1.0
- Based on CentOS: libraw1394-2.1.0-2.el7.src.rpm
