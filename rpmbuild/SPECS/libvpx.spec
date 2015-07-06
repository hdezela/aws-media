%global somajor     2
%global sominor     0
%global sotiny      0
%global soversion   %{somajor}.%{sominor}.%{sotiny}
%global vpxtarget   x86_64-linux-gcc

Name:               libvpx
Summary:            VP8/VP9 Video Codec SDK
Version:            1.4.0
Release:            1%{?dist}
License:            BSD
Group:              System Environment/Libraries
Source0:            https://libvpx.webm.googlecode.com/archive/v%{version}.tar.gz
Source2:            libvpx.ver
URL:                http://www.webmproject.org/tools/vp8-sdk/
BuildRequires:      yasm
BuildRequires:      doxygen
BuildRequires:      php56-cli

%description
libvpx provides the VP8 SDK, which allows you to integrate your applications 
with the VP8 video codec, a high quality, royalty free, open source codec 
deployed on millions of computers and devices worldwide. 

%package devel
Summary:            Development files for libvpx
Group:              Development/Libraries
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for developing software against 
libvpx.

%package utils
Summary:            VP8 utilities and tools
Group:              Development/Tools
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description utils
A selection of utilities and tools for VP8, including a sample encoder
and decoder.

%prep
%setup -q -n libvpx.webm-v%{version}

%build
./configure --target=%{vpxtarget} \
  --enable-pic \
  --disable-install-srcs \
  --enable-shared \
  --enable-vp8 \
  --prefix=%{_prefix} --libdir=%{_libdir}

sed -i "s|-O3|%{optflags}|g" libs-%{vpxtarget}.mk
sed -i "s|-O3|%{optflags}|g" examples-%{vpxtarget}.mk
sed -i "s|-O3|%{optflags}|g" docs-%{vpxtarget}.mk

make %{?_smp_mflags} verbose=true

%install
make DIST_DIR=%{buildroot}%{_prefix} dist

mv %{buildroot}/usr/docs doc/

pushd %{buildroot}
rm -rf usr/build/ usr/md5sums.txt usr/lib*/*.a usr/CHANGELOG usr/README
mv usr/bin/examples/* usr/bin/
rm -rf usr/bin/examples
mv usr/bin/postproc usr/bin/vp8_postproc
mv usr/bin/simple_decoder usr/bin/vp8_simple_decoder
mv usr/bin/simple_encoder usr/bin/vp8_simple_encoder
mv usr/bin/twopass_encoder usr/bin/vp8_twopass_encoder
chmod 755 usr/bin/*
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS CHANGELOG LICENSE README
%{_libdir}/libvpx.so.*

%files devel
%doc docs/html/
%{_includedir}/vpx/
%{_libdir}/pkgconfig/vpx.pc
%{_libdir}/libvpx.so

%files utils
%{_bindir}/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libvpx 1.4.0
- Based on Fedora: libvpx-1.4.0-2.fc23.src.rpm
