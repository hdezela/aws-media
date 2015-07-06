%global _hardened_build 1

Name:          libwebp
Version:       0.4.3
Release:       2%{?dist}
Group:         Development/Libraries
URL:           http://webmproject.org/
Summary:       Library and tools for the WebP graphics format
License:       BSD
Source0:       http://downloads.webmproject.org/releases/webp/%{name}-%{version}.tar.gz
Source1:       libwebp_jni_example.java
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: giflib-devel
BuildRequires: libtiff-devel
BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: swig
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: freeglut-devel

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package tools
Group:         Development/Tools
Summary:       The WebP command line tools

%description tools
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package devel
Group:         Development/Libraries
Summary:       Development files for libwebp, a library for the WebP format
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package java
Group:         Development/Libraries
Summary:       Java bindings for libwebp, a library for the WebP format
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      java-headless
Requires:      jpackage-utils

%description java
Java bindings for libwebp.

%prep
%setup -q

%build
autoreconf -vif
%ifarch aarch64
export CFLAGS="%{optflags} -frename-registers"
%endif
%configure --disable-static --enable-libwebpmux \
           --enable-libwebpdemux --enable-libwebpdecoder

make %{?_smp_mflags}

cp %{SOURCE1} .
cd swig
rm -rf libwebp.jar libwebp_java_wrap.c
mkdir -p java/com/google/webp
swig -ignoremissing -I../src -java \
    -package com.google.webp  \
    -outdir java/com/google/webp \
    -o libwebp_java_wrap.c libwebp.swig

gcc %{optflags} -shared -fPIC \
    -I/usr/lib/jvm/java/include \
    -I/usr/lib/jvm/java/include/linux \
    -I../src \
    -L../src/.libs -lwebp libwebp_java_wrap.c \
    -o libwebp_jni.so

cd java
javac com/google/webp/libwebp.java
jar cvf ../libwebp.jar com/google/webp/*.class

%install
%make_install
find "%{buildroot}/%{_libdir}" -type f -name "*.la" -delete

mkdir -p %{buildroot}/%{_libdir}/%{name}-java
cp swig/*.jar swig/*.so %{buildroot}/%{_libdir}/%{name}-java/

%post -n %{name} -p /sbin/ldconfig

%postun -n %{name} -p /sbin/ldconfig

%files tools
%{_bindir}/cwebp
%{_bindir}/dwebp
%{_bindir}/gif2webp
%{_bindir}/webpmux
%{_bindir}/vwebp
%{_mandir}/man*/*

%files -n %{name}
%doc README PATENTS NEWS AUTHORS
%license COPYING
%{_libdir}/%{name}.so.5*
%{_libdir}/%{name}decoder.so.1*
%{_libdir}/%{name}demux.so.1*
%{_libdir}/%{name}mux.so.1*

%files devel
%{_libdir}/%{name}*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files java
%doc libwebp_jni_example.java
%{_libdir}/%{name}-java/

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libwebp 0.4.3
- Based on libwebp-0.4.3-2.fc23.src.rpm
