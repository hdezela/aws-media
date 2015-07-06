Name:              libasyncns
Version:           0.8
Release:           1%{?dist}
Summary:           Asynchronous Name Service Library
License:           LGPLv2+
Group:             System Environment/Libraries
Source0:           http://0pointer.de/lennart/projects/libasyncns/libasyncns-%{version}.tar.gz
Url:               http://0pointer.de/lennart/projects/libasyncns/
BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A small and lightweight library that implements easy to use asynchronous
wrappers around the libc NSS functions getaddrinfo(), res_query() and related.

%package devel
Summary:           Development Files for libasyncns Client Development
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}
Requires:          pkgconfig

%description devel
Development Files for libasyncns Client Development

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;
rm -rf $RPM_BUILD_ROOT/usr/share/doc/libasyncns/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE
%{_libdir}/libasyncns.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/asyncns.h
%{_libdir}/libasyncns.so
%{_libdir}/pkgconfig/libasyncns.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libasyncns 0.8
- Based on CentOS: libasyncns-0.8-7.el7.src.rpm
