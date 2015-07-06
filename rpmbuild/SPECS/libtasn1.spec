%global            debug_package %{nil}

Summary:	         The ASN.1 library used in GNUTLS
Name:              libtasn1
Version:           4.5
Release:	         1%{?dist}
License:	         GPLv3+ and LGPLv2+
Group:             System Environment/Libraries
URL:               http://www.gnu.org/software/libtasn1/
Source0:           http://ftp.gnu.org/gnu/libtasn1/%name-%version.tar.gz
Source1:           http://ftp.gnu.org/gnu/libtasn1/%name-%version.tar.gz.sig
Patch1:            libtasn1-3.4-rpath.patch
BuildRequires:     bison
BuildRequires:     pkgconfig
BuildRequires:     valgrind
Provides:          bundled(gnulib) = 20130324
Obsoletes:         %{name} < %{version}

%description
A library that provides Abstract Syntax Notation One (ASN.1, as specified
by the X.680 ITU-T recommendation) parsing and structures management, and
Distinguished Encoding Rules (DER, as per X.690) encoding and decoding functions.

%package devel
Summary:           Files for development of applications which will use libtasn1
Group:             Development/Libraries
Requires:          %name = %version-%release
Requires:          pkgconfig
Requires(post):    /sbin/install-info
Requires(postun):  /sbin/install-info
Obsoletes:         %{name}-devel < %{version}

%description devel
This package contains files for development of applications which will
use libtasn1.

%package tools
Summary:           Some ASN.1 tools
Group:             Applications/Text
License:           GPLv3+
Requires:          %name = %version-%release
Obsoletes:         %{name}-tools < %{version}

%description tools
This package contains simple tools that can decode and encode ASN.1
data.

%prep
%setup -q

%patch1 -p1 -b .rpath

%build
%configure --disable-static --disable-silent-rules
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
touch doc/stamp_docs

make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install
rm -f $RPM_BUILD_ROOT{%_libdir/*.la,%_infodir/dir}

%check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
test -f %_infodir/%name.info.gz && \
	/sbin/install-info --info-dir=%_infodir %_infodir/%name.info || :

%preun devel
test "$1" = 0 -a -f %_infodir/%name.info.gz && \
	/sbin/install-info --info-dir=%_infodir --delete %_infodir/%name.info || :

%files
%defattr(-,root,root,-)
%doc doc/TODO doc/*.pdf
%{!?_licensedir:%global license %%doc}
%license COPYING*
%doc AUTHORS NEWS README THANKS
%_libdir/*.so.6*

%files tools
%defattr(-,root,root,-)
%_bindir/asn1*
%_mandir/man1/asn1*

%files devel
%defattr(-,root,root,-)
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*
%_infodir/*.info.*
%_mandir/man3/*asn1*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libtasn1 4.5
- Based on Fedora: libtasn1-4.5-2.fc23.src
- Rpaths removed
- Tests disabled since they don't work without rpath (tried valgrind, didn't work either)
