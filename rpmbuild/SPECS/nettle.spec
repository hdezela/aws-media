Name:              nettle
Version:           3.1.1
Release:           1%{?dist}
Summary:           A low-level cryptographic library
Group:             Development/Libraries
License:           LGPLv3+ or GPLv2+
URL:               http://www.lysator.liu.se/~nisse/nettle/
Source0:           http://www.lysator.liu.se/~nisse/archive/%{name}-%{version}.tar.gz
Patch0:		    nettle-3.1.1-remove-ecc-testsuite.patch
BuildRequires:     gmp-devel
BuildRequires:     m4
BuildRequires:     texinfo-tex
BuildRequires:     texlive-dvips
Requires(post):    info
Requires(preun):   info

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%package devel
Summary:           Development headers for a low-level cryptographic library
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}
Requires:          gmp-devel%{?_isa}

%description devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.  This package contains the files needed for developing 
applications with nettle.

%prep
%setup -q
sed s/ggdb3/g/ -i configure
sed 's/ecc-192.c//g' -i Makefile.in
sed 's/ecc-224.c//g' -i Makefile.in
%patch0 -p1

%build
%configure --enable-shared
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
make install-shared DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_infodir}
install -p -m 644 nettle.info $RPM_BUILD_ROOT%{_infodir}/
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libnettle.so.6.*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libhogweed.so.4.*
%check
make check

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYINGv2 COPYING.LESSERv3
%{_infodir}/nettle.info.gz
%{_bindir}/nettle-lfib-stream
%{_bindir}/pkcs1-conv
%{_bindir}/sexp-conv
%{_bindir}/nettle-hash
%{_bindir}/nettle-pbkdf2
%{_libdir}/libnettle.so.6
%{_libdir}/libnettle.so.6.*
%{_libdir}/libhogweed.so.4
%{_libdir}/libhogweed.so.4.*

%files devel
%doc descore.README nettle.html nettle.pdf
%license COPYINGv2 COPYING.LESSERv3
%{_includedir}/nettle
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_libdir}/pkgconfig/hogweed.pc
%{_libdir}/pkgconfig/nettle.pc

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :
/sbin/ldconfig

%preun
if [ $1 = 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%postun -p /sbin/ldconfig

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with nettle 3.1.1
- Based on Fedora: nettle-3.1.1-2.fc23.src.rpm
