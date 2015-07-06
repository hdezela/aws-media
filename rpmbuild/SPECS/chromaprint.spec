Name:              chromaprint
Version:           1.2
Release:           1%{?dist}
Summary:           Library implementing the AcoustID fingerprinting
Group:             System Environment/Libraries
License:           LGPLv2+
URL:               http://www.acoustid.org/chromaprint/
Source0:           https://bitbucket.org/acoustid/%{name}/downloads/%{name}-%{version}.tar.gz
BuildRequires:     cmake
BuildRequires:     fftw-devel >= 3
BuildRequires:     ffmpeg-devel
BuildRequires:     boost-devel
BuildRequires:     gcc-c++
BuildRequires:     taglib-devel
BuildRequires:     pkgconfig
BuildRequires:     boost-devel

%description
Chromaprint library is the core component of the AcoustID project. Its a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n libchromaprint
Summary:           Library implementing the AcoustID fingerprinting
Group:             System Environment/Libraries
Obsoletes:         python-chromaprint < 0.6-3

%description -n libchromaprint
Chromaprint library is the core component of the AcoustID project. Its a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n libchromaprint-devel
Summary:           Headers for developing programs that will use %{name} 
Group:             Development/Libraries
Requires:          libchromaprint%{?_isa} = %{version}-%{release}
Requires:          ffmpeg-devel

%description -n libchromaprint-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}. 

%package fpcalc
Summary:           Chromaprint Audio Fingerprinting Command Line Tool
License:           GPL-2.0+
Group:             Productivity/Multimedia/Sound/Utilities
Requires:          libchromaprint%{?_isa} = %{version}-%{release}
Provides:          fpcalc = %{version}

%description fpcalc
Chromaprint is the core component of the Acoustid project. Its a client-side
library that implements a custom algorithm for extracting fingerprints from any
audio source.
This package contains fpcalc, a command-line tool to perform Chromaprint
fingerprinting.

%prep
%setup -q

%cmake \
 -DCMAKE_SKIP_RPATH=TRUE \
 -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE \
 -DWITH_AVFFT=ON \
 -DBUILD_EXAMPLES=ON

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm  -f %{buildroot}%{_libdir}/lib*.la

%post -n libchromaprint -p /sbin/ldconfig

%postun -n libchromaprint -p /sbin/ldconfig

%files -n libchromaprint
%doc COPYING.txt NEWS.txt README.md
%{_libdir}/lib*.so.*

%files -n libchromaprint-devel
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files fpcalc
%defattr(-,root,root)
%{_bindir}/fpcalc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with chromaprint 1.2
- Based on Fedora: chromaprint-1.2-3.fc23.src
- Enabled fpcalc
