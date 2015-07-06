Name:          opus
Version:       1.1
Release:       1%{?dist}
Summary:       An audio codec for use in low-delay speech and audio communication
Group:         System Environment/Libraries
License:       BSD
URL:           http://www.opus-codec.org/
Source0:       http://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:       http://tools.ietf.org/rfc/rfc6716.txt 
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: doxygen

%description
The Opus codec is designed for interactive speech and audio transmission over 
the Internet. It is designed by the IETF Codec Working Group and incorporates 
technology from Skype's SILK codec and Xiph.Org's CELT codec.

%package devel
Summary:       Development package for opus
Group:         Development/Libraries
Requires:      libogg-devel
Requires:      opus = %{version}-%{release}

%description devel
Files for development with opus.

%prep
%setup -q
cp %{SOURCE1} .

%build
%configure --enable-custom-modes --disable-static

make %{?_smp_mflags} V=1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

find %{buildroot} -type f -name "*.la" -delete
rm -rf %{buildroot}%{_datadir}/doc/opus/html

%check
make check

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README rfc6716.txt
%{_libdir}/libopus.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/html
%{_includedir}/opus
%{_libdir}/libopus.so
%{_libdir}/pkgconfig/opus.pc
%{_datadir}/aclocal/opus.m4
%{_datadir}/man/man3/opus_*.3.gz

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with opus 1.1
- Based on Fedora: opus-1.1-5.fc21.src.rpm
