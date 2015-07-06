%global debug_package %{nil}
%global commit bdd17ee3b1b3

Name:           eigen3
Version:        3.2.5
Release:        1%{?dist}
Summary:        A lightweight C++ template library for vector and matrix math
Group:          Development/Libraries
License:        MPLv2.0 and LGPLv3+ and BSD
URL:            http://eigen.tuxfamily.org/index.php?title=Main_Page
Source0:        eigen-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  atlas-devel
BuildRequires:  fftw-devel
BuildRequires:  glew-devel
BuildRequires:  gmp-devel
BuildRequires:  gsl-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  tex(latex)

%description
%{summary}

%package devel
Summary: A lightweight C++ template library for vector and matrix math
Group:   Development/Libraries
Provides: %{name} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}
BuildArch: noarch

%description devel
%{summary}.

%prep
%setup -q -n eigen-eigen-%{commit}

sed -i 's|LAYOUT_FILE|#LAYOUT_FILE|' doc/Doxyfile.in

%build
mkdir %{_target_platform}
pushd %{_target_platform}

%cmake .. -DBLAS_LIBRARIES="cblas" -DBLAS_LIBRARIES_DIR=%{_libdir}/atlas
popd
make -j1 -C %{_target_platform} %{?_smp_mflags}
make -j1 doc -C %{_target_platform} %{?_smp_mflags}

rm -f %{_target_platform}/doc/html/installdox
rm -f %{_target_platform}/doc/html/unsupported/installdox

%install
rm -rf %{buildroot}
make -j1 install DESTDIR=%{buildroot} -C %{_target_platform}

%check
make -j1 -C %{_target_platform} %{?_smp_mflags} buildtests
make -j1 -C %{_target_platform} %{?_smp_mflags} test ARGS="-V" || exit 0

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root,-)
%doc COPYING.GPL COPYING.LGPL
%doc %{_target_platform}/doc/html
%{_includedir}/eigen3
%{_datadir}/pkgconfig/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- All makes received -j1 to use less memory and compile on smaller instances

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with eigen3 3.2.5
- Based on EPEL: eigen3-3.2.3-1.el6.src.rpm
