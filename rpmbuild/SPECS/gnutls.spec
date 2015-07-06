Summary:           A TLS protocol implementation
Name:              gnutls
Version:           3.4.2
Release:           1%{?dist}
License:           GPLv3+ and LGPLv2+
Group:             System Environment/Libraries
URL:               http://www.gnutls.org/
Source0:           ftp://ftp.gnutls.org/gcrypt/gnutls/%{name}-%{version}.tar.xz
Source1:           libgnutls-config
Source3:           gnutls-cp-DEFAULT-F21.settings
Source4:           gnutls-cp-DEFAULT-F22.settings
Source5:           gnutls-cp-DEFAULT.settings
Source6:           gnutls-cp-EMPTY.settings
Source7:           gnutls-cp-FUTURE-F21.settings
Source8:           gnutls-cp-FUTURE-F22.settings
Source9:           gnutls-cp-FUTURE.settings
Source10:          gnutls-cp-LEGACY-F21.settings
Source11:          gnutls-cp-LEGACY-F22.settings
Source12:          gnutls-cp-LEGACY.settings
Source13:          gnutls-cp-config
Source14:          gnutls-cp-update-crypto-policies
Patch1:            gnutls-3.2.7-rpath.patch
Patch3:            gnutls-3.1.11-nosrp.patch
Patch4:            gnutls-3.4.1-default-policy.patch
Patch5:            gnutls-3.4.2-internals.patch
BuildRequires:     p11-kit-devel >= 0.21.3
BuildRequires:     gettext-devel
BuildRequires:     zlib-devel
BuildRequires:     readline-devel
BuildRequires:     libtasn1-devel >= 4.3
BuildRequires:     libtool
BuildRequires:     automake
BuildRequires:     autoconf
BuildRequires:     texinfo
BuildRequires:     autogen-libopts-devel >= 5.18
BuildRequires:     autogen
BuildRequires:     nettle-devel >= 3.1.1
BuildRequires:     trousers-devel >= 0.3.11.2
BuildRequires:     libidn-devel
BuildRequires:     gperf
BuildRequires:     unbound-devel
BuildRequires:     unbound-libs
Requires:          p11-kit-trust
Requires:          libtasn1 >= 4.3
Provides:          bundled(gnulib) = 20130424

%description
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 

%package c++
Summary:           The C++ interface to GnuTLS
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description c++
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 

%package devel
Summary:           Development files for the %{name} package
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          %{name}-c++%{?_isa} = %{version}-%{release}
Requires:          %{name}-dane%{?_isa} = %{version}-%{release}
Requires:          pkgconfig
Requires(post):    /sbin/install-info
Requires(preun):   /sbin/install-info

%description devel
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 
This package contains files needed for developing applications with
the GnuTLS library.

%package utils
License:           GPLv3+
Summary:           Command line tools for TLS protocol
Group:             Applications/System
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          %{name}-dane%{?_isa} = %{version}-%{release}

%description utils
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 
This package contains command line TLS client and server and certificate
manipulation tools.

%package dane
Summary:           A DANE protocol implementation for GnuTLS
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description dane
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 
This package contains library that implements the DANE protocol for verifying
TLS certificates through DNSSEC.

%prep
%setup -q
%patch1 -p1 -b .rpath
%patch3 -p1 -b .nosrp
%patch4 -p1 -b .default-policy
%patch5 -p1 -b .internals

sed 's/gnutls_srp.c//g' -i lib/Makefile.in
sed 's/gnutls_srp.lo//g' -i lib/Makefile.in
rm -f lib/minitasn1/*.c lib/minitasn1/*.h
rm -f src/libopts/*.c src/libopts/*.h src/libopts/compat/*.c src/libopts/compat/*.h 
sed -i -e 's|sys_lib_dlsearch_path_spec="/lib /usr/lib|sys_lib_dlsearch_path_spec="/lib /usr/lib %{_libdir}|g' configure

%build
CFLAGS="$RPM_OPT_FLAGS -Wl,-z,lazy"
export CFLAGS

%configure --with-libtasn1-prefix=%{_prefix} \
  --with-included-libcfg \
  --disable-static \
  --disable-openssl-compatibility \
  --disable-srp-authentication \
  --disable-non-suiteb-curves \
  --with-system-priority-file=%{_sysconfdir}/crypto-policies/back-ends/gnutls.config \
  --with-default-trust-store-pkcs11="pkcs11:model=p11-kit-trust;manufacturer=PKCS%2311%20Kit" \
  --disable-guile \
  --with-unbound-root-key-file=/var/lib/unbound/root.key \
  --enable-dane \
  --disable-rpath

make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_bindir}/srptool
rm -f $RPM_BUILD_ROOT%{_bindir}/gnutls-srpcrypt
cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/libgnutls-config
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/srptool.1
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/*srp*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/guile/2.0/guile-gnutls*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/guile/2.0/guile-gnutls*.la

mkdir -p -m 755 %{buildroot}%{_datadir}/crypto-policies/profiles
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/
install -p -m 755 %{SOURCE14} %{buildroot}%{_bindir}/update-crypto-policies
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/crypto-policies/profiles
install -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/crypto-policies/profiles
install -p -m 644 %{SOURCE5} %{buildroot}%{_datadir}/crypto-policies/profiles
install -p -m 644 %{SOURCE6} %{buildroot}%{_datadir}/crypto-policies/profiles
install -p -m 644 %{SOURCE7} %{buildroot}%{_datadir}/crypto-policies/profiles
install -p -m 644 %{SOURCE8} %{buildroot}%{_datadir}/crypto-policies/profiles
install -p -m 644 %{SOURCE9} %{buildroot}%{_datadir}/crypto-policies/profiles
install -p -m 644 %{SOURCE10} %{buildroot}%{_datadir}/crypto-policies/profiles
install -p -m 644 %{SOURCE11} %{buildroot}%{_datadir}/crypto-policies/profiles
install -p -m 644 %{SOURCE12} %{buildroot}%{_datadir}/crypto-policies/profiles
install -p -m 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/crypto-policies/config

%find_lang gnutls

%check
make check %{?_smp_mflags}

%post -p /sbin/ldconfig
%post c++ -p /sbin/ldconfig
%{_bindir}/update-crypto-policies --no-check

%postun c++ -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
if [ -f %{_infodir}/gnutls.info.gz ]; then
    /sbin/install-info %{_infodir}/gnutls.info.gz %{_infodir}/dir || :
fi

%preun devel
if [ $1 = 0 -a -f %{_infodir}/gnutls.info.gz ]; then
   /sbin/install-info --delete %{_infodir}/gnutls.info.gz %{_infodir}/dir || :
fi

%post dane -p /sbin/ldconfig

%postun dane -p /sbin/ldconfig

%files -f gnutls.lang
%defattr(-,root,root,-)
%{_libdir}/libgnutls.so.30*
%doc README AUTHORS NEWS THANKS
%license COPYING COPYING.LESSER
%dir %{_sysconfdir}/crypto-policies/
%config(noreplace) %{_sysconfdir}/crypto-policies/config
%dir %{_datadir}/crypto-policies/
%{_bindir}/update-crypto-policies
%{_datadir}/crypto-policies/profiles/
%{!?_licensedir:%global license %%doc}
%license COPYING.LESSER

%files c++
%{_libdir}/libgnutlsxx.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/libgnutls*-config
%{_includedir}/*
%{_libdir}/libgnutls*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
%{_infodir}/gnutls*
%{_infodir}/pkcs11-vision*

%files utils
%defattr(-,root,root,-)
%{_bindir}/certtool
%{_bindir}/tpmtool
%{_bindir}/ocsptool
%{_bindir}/psktool
%{_bindir}/p11tool
%{_bindir}/crywrap
%{_bindir}/danetool
%{_bindir}/gnutls*
%{_mandir}/man1/*
%doc doc/certtool.cfg

%files dane
%defattr(-,root,root,-)
%{_libdir}/libgnutls-dane.so.*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with gnutls 3.4.2
- Based on Fedora: gnutls-3.4.2-2.fc23.src.rpm
- Enabled dane and disabled guile by default
- Crypto-policies included in package
