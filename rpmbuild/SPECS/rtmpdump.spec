%global commit dc76f0a8461e6c8f1277eba58eae201b2dc1d06a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20131205

Name:          rtmpdump
Version:       2.4
Release:       1%{?dist}
Summary:       Toolkit for RTMP streams
Group:         Applications/Internet
License:       GPLv2+
URL:           http://rtmpdump.mplayerhq.hu/
Source0:       http://repo.or.cz/w/rtmpdump.git/snapshot/%{commit}.tar.gz
BuildRequires: gnutls-devel
BuildRequires: libgcrypt-devel
BuildRequires: zlib-devel
BuildRequires: nettle-devel

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are supported,
including rtmp://, rtmpt://, rtmpe://, rtmpte://, and rtmps://. 

%package -n librtmp
Summary:       Support library for RTMP streams
Group:         Applications/Internet
License:       LGPLv2+

%description -n librtmp
librtmp is a support library for RTMP streams. All forms of RTMP are supported,
including rtmp://, rtmpt://, rtmpe://, rtmpte://, and rtmps://. 

%package -n librtmp-devel
Summary:       Files for librtmp development
Group:         Applications/Internet
License:       LGPLv2+
Requires:      librtmp%{?_isa} = %{version}-%{release}

%description -n librtmp-devel
librtmp is a support library for RTMP streams. The librtmp-devel package
contains include files needed to develop applications using librtmp.

%prep
%setup -q -n %{name}

%build
make SYS=posix CRYPTO=GNUTLS SHARED=yes OPT="%{optflags}" LIB_GNUTLS="-lgnutls -lgcrypt -ldl"

%install
make CRYPTO=GNUTLS SHARED=yes DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} libdir=%{_libdir} install
rm -f %{buildroot}%{_libdir}/librtmp.a

%post -n librtmp -p /sbin/ldconfig
%postun -n librtmp -p /sbin/ldconfig

%files
%doc COPYING README
%{_bindir}/rtmpdump
%{_sbindir}/rtmpsrv
%{_sbindir}/rtmpgw
%{_sbindir}/rtmpsuck
%{_mandir}/man1/rtmpdump.1*
%{_mandir}/man8/rtmpgw.8*

%files -n librtmp
%doc librtmp/COPYING ChangeLog
%{_libdir}/librtmp.so.1

%files -n librtmp-devel
%{_includedir}/librtmp/
%{_libdir}/librtmp.so
%{_libdir}/pkgconfig/librtmp.pc
%{_mandir}/man3/librtmp.3*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with rtmpdump 2.4 
- Based on Fedora: rtmpdump-2.4-3.20131205.gitdc76f0a.fc22.src
