Name:          libproxy
Version:       0.4.11
Release:       1%{?dist}
Summary:       A library handling all the details of proxy configuration
Group:         System Environment/Libraries
License:       LGPLv2+
URL:           http://code.google.com/p/libproxy/
Source0:       http://libproxy.googlecode.com/files/libproxy-%{version}%{?svn}.tar.gz
BuildRequires: python27-devel
BuildRequires: libmodman-devel >= 2.0.1
BuildRequires: cmake >= 2.6.0

%description
libproxy offers the following features:

    * extremely small core footprint (< 35K)
    * no external dependencies within libproxy core
      (libproxy plugins may have dependencies)
    * only 3 functions in the stable external API
    * dynamic adjustment to changing network topology
    * a standard way of dealing with proxy settings across all scenarios
    * a sublime sense of joy and accomplishment 

%package bin
Summary:       Binary to test %{name}
Group:         Applications/System
Requires:      %{name} = %{version}-%{release}

%description bin
The %{name}-bin package contains the proxy binary for %{name}

%package python
Summary:       Binding for %{name} and python
Group:         System Environment/Libraries
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description python
The %{name}-python package contains the python binding for %{name}

%package devel
Summary:       Development files for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%{cmake} \
  -DMODULE_INSTALL_DIR=%{_libdir}/%{name}/%{version}/modules \
  -DWITH_PERL=OFF \
  -DWITH_GNOME3=OFF \
  -DWITH_WEBKIT3=OFF \
  -DWITH_MOZJS=OFF \
   .
make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}/modules

%check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{version}
%dir %{_libdir}/%{name}/%{version}/modules

%files bin
%defattr(-,root,root,-)
%{_bindir}/proxy

%files python
%defattr(-,root,root,-)
%{python_sitelib}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/proxy.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libproxy-1.0.pc
%{_datadir}/cmake/Modules/Findlibproxy.cmake

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Disabled gnome, gtk, kde and mozjs
- Enabled python by default

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libproxy 0.4.11
- Based on CentOS: libproxy-0.4.11-6.el7.src
