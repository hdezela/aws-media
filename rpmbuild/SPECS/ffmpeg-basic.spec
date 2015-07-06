Summary:       Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Name:          ffmpeg
Version:       2.7
Release:       0%{?dist}
License:       GPLv3+
Group:         System Environment/Libraries
Source0:       http://ffmpeg.org/releases/ffmpeg-%{version}.tar.gz
URL:           http://ffmpeg.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}
Provides:      ffmpeg = %{version}-%{release}
BuildRequires: bzip2-devel
BuildRequires: imlib2-devel
BuildRequires: libstdc++-devel
BuildRequires: libva-devel
BuildRequires: openssl-devel
BuildRequires: SDL-devel
BuildRequires: yasm
BuildRequires: zlib-devel
Requires:      %{name}-libs = %{version}-%{release}

%package libs
Summary:       Library for ffmpeg
Group:         System Environment/Libraries

%package devel
Summary:       Development files for %{name}
Group:         Development/Libraries
Requires:      %{name}-libs = %{version}-%{release}

%description
FFmpeg is a very fast video and audio converter.

%description devel
Development files for ffmpeg

%description libs
Libraries for ffmpeg

%prep
%setup -q -n %{name}-%{version}
test -f version.h || echo "#define FFMPEG_VERSION \"%{evr}\"" > version.h

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --shlibdir=%{_libdir} --mandir=%{_mandir} \
   --disable-debug \
   --enable-gpl \
   --enable-postproc \
   --enable-pthreads \
   --enable-nonfree \
   --enable-runtime-cpudetect \
   --enable-shared \
   --disable-static \
   --disable-stripping \
   --extra-cflags="-fPIC" \
   --enable-openssl \
   --disable-doc \
   --enable-avresample

make
# remove some zero-length files, ...
pushd doc
rm -f general.html.d platform.html.d git-howto.html.d \
   developer.html.d texi2pod.pl faq.html.d
popd

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} incdir=%{buildroot}%{_includedir}/ffmpeg
# Remove from the included docs
rm -f doc/Makefile
rm -f %{buildroot}/usr/share/doc/ffmpeg/*.html

%clean
rm -rf %{buildroot}

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING* CREDITS README* MAINTAINERS LICENSE* RELEASE doc/ RELEASE_NOTES VERSION
%{_bindir}/*
%{_datadir}/ffmpeg

%files libs
%defattr(-,root,root,-)
%doc COPYING* CREDITS README* MAINTAINERS LICENSE* RELEASE doc/ RELEASE_NOTES VERSION
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc COPYING* CREDITS README* MAINTAINERS LICENSE* RELEASE doc/ RELEASE_NOTES VERSION
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- fPIC as default, AMZ Linux is 64-bit only

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with ffmpeg 2.7
- Based on CentOS: ffmpeg-2.6.1-1.el7.centos.src.rpm
