Name:           fdk-aac
Version:        0.1.4
Release:        1%{?dist}
Summary:        Fraunhofer AAC Codec
License:        ASL 2.0
URL:            http://sourceforge.net/projects/opencore-amr
Source0:        http://downloads.sourceforge.net/opencore-amr/%{name}-%{version}.tar.gz

%description
A standalone library of the Fraunhofer FDK AAC code from Android.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Libraries and header files for developing applications that use fdk-aac.

%prep
%setup -q

%build
autoreconf -fiv
%configure \
  --disable-silent-rules \
  --disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog NOTICE
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc documentation/*.pdf
%dir %{_includedir}/fdk-aac
%{_includedir}/fdk-aac/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with fdk-aac 0.1.4
- New spec file
