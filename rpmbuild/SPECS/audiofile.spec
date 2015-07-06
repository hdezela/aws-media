Summary:           A library for accessing various audio file formats
Name:              audiofile
Version:           0.3.6
Release:           1%{?dist}
Epoch:             1
License:           LGPLv2+ and GPL+ and ASL 2.0
Group:             System Environment/Libraries
Source0:           http://audiofile.68k.org/%{name}-%{version}.tar.gz
URL:               http://audiofile.68k.org/
BuildRequires:     libtool
BuildRequires:     alsa-lib-devel

%description
The Audio File library is an implementation of the Audio File Library
from SGI, which provides an API for accessing audio file formats like
AIFF/AIFF-C, WAVE, and NeXT/Sun .snd/.au files. This library is used
by the EsounD daemon.

Install audiofile if you are installing EsounD or you need an API for
any of the sound file formats it can handle.

%package devel
Summary:           Development files for Audio File applications
Group:             Development/Libraries
Requires:          %{name} = %{epoch}:%{version}-%{release}
Requires:          pkgconfig >= 1:0.8

%description devel
The audiofile-devel package contains libraries, include files, and
other resources you can use to develop Audio File applications.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} LIBTOOL="/usr/bin/libtool"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f docs/Makefile*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING TODO README ChangeLog docs
%{_bindir}/sfconvert
%{_bindir}/sfinfo
%{_libdir}/lib*.so.1*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with audiofile 0.3.6
- Based on CentOS: audiofile-0.3.6-4.el7.src.rpm
