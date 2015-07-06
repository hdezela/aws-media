Summary:           H.265/HEVC encoder
Name:              x265
Version:           1.7
Release:           1%{?dist}
URL:               http://x265.org/
License:           GPLv2+ and BSD
Source0:           https://bitbucket.org/multicoreware/x265/downloads/%{name}_%{version}.tar.gz
Patch1:            x265-test-shared.patch
Patch4:            x265-detect_cpu_armhfp.patch
BuildRequires:     cmake
BuildRequires:     yasm

%description
The primary objective of x265 is to become the best H.265/HEVC encoder
available anywhere, offering the highest compression efficiency and the
highest performance on a wide variety of hardware platforms.

This package contains the command line encoder.

%package libs
Summary:           H.265/HEVC encoder library

%description libs
The primary objective of x265 is to become the best H.265/HEVC encoder
available anywhere, offering the highest compression efficiency and the
highest performance on a wide variety of hardware platforms.

This package contains the shared library.

%package devel
Summary:           H.265/HEVC encoder library development files
Requires:          %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The primary objective of x265 is to become the best H.265/HEVC encoder
available anywhere, offering the highest compression efficiency and the
highest performance on a wide variety of hardware platforms.

This package contains the shared library development files.

%prep
%setup -q -n x265_%{version}
%patch1 -p1 -b .ts
%patch4 -p1 -b .armhfp

%build
%cmake -G "Unix Makefiles" \
 -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DENABLE_PIC:BOOL=ON \
 -DENABLE_TESTS:BOOL=ON \
 source
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/libx265.a
install -Dpm644 COPYING %{buildroot}%{_docdir}/COPYING

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} test/TestBench

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/x265

%files libs
%dir %{_docdir}
%{_docdir}/COPYING
%{_libdir}/libx265.so.59

%files devel
%doc doc/*
%{_includedir}/x265.h
%{_includedir}/x265_config.h
%{_libdir}/libx265.so
%{_libdir}/pkgconfig/x265.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with x265 1.7
- Based on Fedora: x265-1.6-1.fc22.src
