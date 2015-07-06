Name:           libmodman
Version:        2.0.1
Release:        1%{?dist}
Summary:        A simple library for managing C++ modules (plug-ins)
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://code.google.com/p/libmodman/
Source0:        http://libmodman.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake >= 2.8.0
BuildRequires:  zlib-devel

%description
libmodman is a simple library for managing C++ modules (plug-ins).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake >= 2.8.0

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%{cmake}
make VERBOSE=1 %{?_smp_mflags}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmodman-2.0.pc
%{_datadir}/cmake/Modules/Findlibmodman.cmake

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libmodman 2.0.1
- Based on CentOS: libmodman-2.0.1-8.el7.src
