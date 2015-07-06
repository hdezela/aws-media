Name:          wavpack
Summary:       A completely open audiocodec
Version:       4.75.0
Release:       1%{?dist}
License:       BSD
Group:         Applications/Multimedia
Url:           http://www.wavpack.com/
Source0:       http://www.wavpack.com/%{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

%package devel
Summary:       WavPack - development files
Group:         Development/Libraries
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig

%description devel
Files needed for developing apps using wavpack

%prep
%setup -q

%build
autoreconf -ivf
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/*
%{_libdir}/libwavpack.so.*
%{_mandir}/man1/wavpack.1*
%{_mandir}/man1/wvgain.1*
%{_mandir}/man1/wvunpack.1*
%doc AUTHORS COPYING

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libwavpack.so
%doc ChangeLog README

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with wavpack 4.75.0
- Based on Fedora: wavpack-4.70.0-5.fc23.src
