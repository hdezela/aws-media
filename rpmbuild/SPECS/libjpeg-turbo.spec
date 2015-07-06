Name:              libjpeg-turbo
Version:           1.4.1
Release:           1%{?dist}
Summary:           A MMX/SSE2 accelerated library for manipulating JPEG image files
License:           IJG
URL:               http://sourceforge.net/projects/libjpeg-turbo
Source0:           http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:            libjpeg-turbo-header-files.patch
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     libtool
BuildRequires:     nasm
Obsoletes:         libjpeg < 6b-47
Obsoletes:         libjpeg < 1.4.0
Provides:          libjpeg = 6b-47%{?dist}

%description
The libjpeg-turbo package contains a library of functions for manipulating JPEG
images.

%package devel
Summary:           Headers for the libjpeg-turbo library
Obsoletes:         libjpeg-devel < 6b-47
Provides:          libjpeg-devel = 6b-47%{?dist}
Requires:          libjpeg-turbo = %{version}-%{release}
Obsoletes:         libjpeg-turbo-static < 1.3.1
Provides:          libjpeg-turbo-static = 1.3.1%{?dist}

%description devel
This package contains header files necessary for developing programs which will
manipulate JPEG files using the libjpeg-turbo library.

%package utils
Summary:           Utilities for manipulating JPEG images
Requires:          libjpeg-turbo = %{version}-%{release}

%description utils
The libjpeg-turbo-utils package contains simple client programs for accessing
the libjpeg functions. It contains cjpeg, djpeg, jpegtran, rdjpgcom and
wrjpgcom. Cjpeg compresses an image file into JPEG format. Djpeg decompresses a
JPEG file into a regular image file. Jpegtran can perform various useful
transformations on JPEG files. Rdjpgcom displays any text comments included in a
JPEG file. Wrjpgcom inserts text comments into a JPEG file.

%package -n turbojpeg
Summary:           TurboJPEG library

%description -n turbojpeg
The turbojpeg package contains the TurboJPEG shared library.

%package -n turbojpeg-devel
Summary:           Headers for the TurboJPEG library
Requires:          turbojpeg = %{version}-%{release}

%description -n turbojpeg-devel
This package contains header files necessary for developing programs which will
manipulate JPEG files using the TurboJPEG library.

%prep
%setup -q
%patch0 -p1 -b .header-files

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name "*.la" -delete

chmod -x README-turbo.txt

rm -fv $RPM_BUILD_ROOT%{_docdir}/%{name}/*

%check
make test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n turbojpeg -p /sbin/ldconfig
%postun -n turbojpeg -p /sbin/ldconfig

%files
%doc README README-turbo.txt change.log ChangeLog.txt
%{_libdir}/libjpeg.so.62*

%files devel
%doc coderules.txt jconfig.txt libjpeg.txt structure.txt example.c
%{_includedir}/jconfig.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpegint.h
%{_includedir}/jpeglib.h
%{_libdir}/libjpeg.so

%files utils
%doc usage.txt wizard.txt
%{_bindir}/cjpeg
%{_bindir}/djpeg
%{_bindir}/jpegtran
%{_bindir}/rdjpgcom
%{_bindir}/tjbench
%{_bindir}/wrjpgcom
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*

%files -n turbojpeg
%{_libdir}/libturbojpeg.so.0*

%files -n turbojpeg-devel
%{_includedir}/turbojpeg.h
%{_libdir}/libturbojpeg.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libjpeg-turbo 1.4.1
- Based on Fedora: libjpeg-turbo-1.4.0-1.fc22.src.rpm
