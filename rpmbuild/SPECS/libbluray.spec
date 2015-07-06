Name:           libbluray
Version:        0.8.1
Release:        1%{?dist}
Summary:        Library to access Blu-Ray disks for video playback 
License:        LGPLv2+
URL:            http://www.videolan.org/developers/libbluray.html
Source0:        ftp://ftp.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:         libbluray-0.8.0-no_doxygen_timestamp.patch
BuildRequires:  java7-devel >= 1:1.7.0 
BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  libxml2-devel
BuildRequires:  doxygen
BuildRequires:  texlive-latex
BuildRequires:  graphviz
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel

%description
This package is aiming to provide a full portable free open source bluray
library, which can be plugged into popular media players to allow full bluray
navigation and playback on Linux. It will eventually be compatible with all
current titles, and will be easily portable and embeddable in standard players
such as mplayer and vlc.

%package bdj
Summary:        BDJ support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       java >= 1:1.7.0
Requires:       jpackage-utils
Obsoletes:      libbluray-java < 0.4.0-2
Provides:       libbluray-java = %{version}-%{release}

%description    bdj
The %{name}-bdj package contains the jar file needed to add BD-J support to
%{name}.
BD-J support is still considered alpha.

%package utils
Summary:        Test utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
The %{name}-utils package contains test utilities for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .no_timestamp

%build
export JDK_HOME="%{_jvmdir}/java-1.7.0"
%configure --disable-static \
  --disable-doxygen-pdf \
  --disable-doxygen-ps \
  --enable-doxygen-html \
  --enable-examples \
  --enable-udf \
  --enable-bdjava

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}
make doxygen-doc
rm -f doc/doxygen/html/installdox 

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

for i in bdjo_dump bdsplice clpi_dump hdmv_test index_dump libbluray_test \
         list_titles mobj_dump mpls_dump sound_dump
do install -Dp -m 0755 .libs/$i $RPM_BUILD_ROOT%{_bindir}/$i; done;

install -Dp -m755 .libs/bdj_test %{buildroot}%{_bindir}/bdj_test;

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING README.txt
%{_libdir}/*.so.*

%files bdj
%{_javadir}/libbluray-j2se-%{version}.jar

%files utils
%{_bindir}/*

%files devel
%doc doc/doxygen/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libbluray.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libbluray 0.8.1
- Based on Fedora: libbluray-0.8.0-3.fc23.src.rpm
