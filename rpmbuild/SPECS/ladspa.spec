Name:           ladspa
Version:        1.13
Release:        1%{?dist}
Summary:        Linux Audio Developer's Simple Plug-in API, examples and tools
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.ladspa.org/
Source:         http://www.ladspa.org/download/%{name}_sdk_%{version}.tgz
Patch1:         ladspa-1.13-plugindir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl
BuildRequires:  gcc-c++

%description
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

This package contains the example plug-ins and tools from the LADSPA SDK.

%package devel
Summary:       Linux Audio Developer's Simple Plug-in API
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
ladspa-devel contains the ladspa.h header file.

Definitive technical documentation on LADSPA plug-ins for both the host
and plug-in is contained within copious comments within the ladspa.h
header file.

%prep
%setup -q -n ladspa_sdk
%patch1 -p0 -b .plugindir
perl -pi -e 's/^(CFLAGS.*)-O3(.*)/$1\$\(RPM_OPT_FLAGS\)$2 -DPLUGINDIR=\$\(PLUGINDIR\)/' src/makefile
perl -pi -e 's/-mkdirhier/-mkdir -p/' src/makefile

cd doc
perl -pi -e "s!HREF=\"ladspa.h.txt\"!href=\"file:///usr/include/ladspa.h\"!" *.html

%build
cd src
PLUGINDIR=\\\"%{_libdir}/ladspa\\\" make targets %{?_smp_mflags} LD="ld --build-id"

%install
rm -rf $RPM_BUILD_ROOT

cd src
make install \
  INSTALL_PLUGINS_DIR=$RPM_BUILD_ROOT%{_libdir}/ladspa \
  INSTALL_INCLUDE_DIR=$RPM_BUILD_ROOT%{_includedir} \
  INSTALL_BINARY_DIR=$RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ladspa/rdf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc/COPYING
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*.so
%{_bindir}/analyseplugin
%{_bindir}/applyplugin
%{_bindir}/listplugins
%{_datadir}/ladspa

%files devel
%defattr(-,root,root,-)
%doc doc/*.html
%{_includedir}/ladspa.h

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with ladspa 1.13
- Based on CentOS: ladspa-1.13-15.fc23.src.rpm
