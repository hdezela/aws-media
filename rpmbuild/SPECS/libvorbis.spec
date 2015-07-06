%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary:       The Vorbis General Audio Compression Codec
Name:          libvorbis
Version:       1.3.5
Release:       1%{?dist}
Epoch:         1
Group:         System Environment/Libraries
License:       BSD
URL:           http://www.xiph.org/
Source:        http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.xz
BuildRequires: libogg-devel >= 2:1.1

%description
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates.

The libvorbis package contains runtime libraries for use in programs
that support Ogg Vorbis.

%package devel
Summary:       Development tools for Vorbis applications
Group:         Development/Libraries
Requires:      libogg-devel >= 2:1.1
Requires:      %{name} = %{epoch}:%{version}-%{release}
Obsoletes:     vorbis-devel

%description devel
The libvorbis-devel package contains the header files and documentation
needed to develop applications with Ogg Vorbis.

%package devel-docs
Summary:       Documentation for developing Vorbis applications
Group:         Development/Libraries
Requires:      %{name}-devel = %{epoch}:%{version}-%{release}
BuildArch:     noarch

%description devel-docs
Documentation for developing applications with libvorbis.

%prep

%setup -q
sed -i "s/-O20/$RPM_OPT_FLAGS/" configure
sed -i "s/-ffast-math//" configure
sed -i "s/-mcpu=750//" configure

%build
%configure --with-ogg-libraries=%{_libdir} --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install docdir=%{_pkgdocdir}
install -pm 644 -t $RPM_BUILD_ROOT%{_pkgdocdir} AUTHORS COPYING README
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make check

%files
%defattr(-,root,root)
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/COPYING
%{_libdir}/libvorbis.so.*
%{_libdir}/libvorbisfile.so.*
%{_libdir}/libvorbisenc.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/vorbis
%{_libdir}/libvorbis.so
%{_libdir}/libvorbisfile.so
%{_libdir}/libvorbisenc.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/vorbis.m4

%files devel-docs
%defattr(-,root,root)
%{_pkgdocdir}/*
%exclude %{_pkgdocdir}/COPYING
%exclude %{_pkgdocdir}/doxygen-build.stamp

%clean 
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with vorbis 1.3.5
- Based on CentOS: libvorbis-1.3.3-8.el7.src.rpm
