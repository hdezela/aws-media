Summary:           Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Name:              ffmpeg
Version:           2.7
Release:           1%{?dist}
License:           GPLv3+
Group:             System Environment/Libraries
Source0:           http://ffmpeg.org/releases/ffmpeg-%{version}.tar.gz
URL:               http://ffmpeg.org/
BuildRoot:         %{_tmppath}/%{name}-%{version}
Provides:          ffmpeg = %{version}-%{release}
BuildRequires:     a52dec-devel
BuildRequires:     bzip2-devel
BuildRequires:     faad2-devel
BuildRequires:     fdk-aac-devel
BuildRequires:     faac-devel
BuildRequires:     flac-devel
BuildRequires:     fontconfig-devel
BuildRequires:     freetype-devel
BuildRequires:     frei0r-devel
BuildRequires:     fribidi-devel
BuildRequires:     gnutls-devel
BuildRequires:     gsm-devel
BuildRequires:     imlib2-devel
BuildRequires:     ladspa-devel
BuildRequires:     lame-devel
BuildRequires:     libass-devel
BuildRequires:     libaacplus-devel
BuildRequires:     libbluray-devel
BuildRequires:     libbs2b-devel
BuildRequires:     libcaca-devel
BuildRequires:     libdc1394-devel
BuildRequires:     libdcadec-devel
BuildRequires:     libmodplug-devel
BuildRequires:     libraw1394-devel
BuildRequires:     librtmp-devel
BuildRequires:     libssh-devel
BuildRequires:     libstdc++-devel
BuildRequires:     libtheora-devel
BuildRequires:     libutvideo-devel
BuildRequires:     libv4l-devel
BuildRequires:     libva-devel
BuildRequires:     libvidstab-devel
BuildRequires:     libvdpau-devel
BuildRequires:     libvorbis-devel
BuildRequires:     libvpx-devel
BuildRequires:     libwebp-devel
BuildRequires:     openal-soft-devel
BuildRequires:     opencv-devel
BuildRequires:     opencore-amr-devel
BuildRequires:     openh264-devel
BuildRequires:     openjpeg-devel
BuildRequires:     openssl-devel
BuildRequires:     opus-devel
BuildRequires:     pulseaudio-libs-devel
BuildRequires:     schroedinger-devel
BuildRequires:     SDL-devel
BuildRequires:     shine-devel
BuildRequires:     snappy-devel
BuildRequires:     speex-devel
BuildRequires:     soxr-devel
BuildRequires:     twolame-devel
BuildRequires:     vo-aacenc-devel
BuildRequires:     vo-amrwbenc-devel
BuildRequires:     wavpack-devel
BuildRequires:     xavs-devel
BuildRequires:     x264-devel
BuildRequires:     x265-devel
BuildRequires:     xvidcore-devel
BuildRequires:     yasm
BuildRequires:     zlib-devel
Requires:          %{name}-libs = %{version}-%{release}

%description
FFmpeg is a very fast video and audio converter.

%package libs
Summary:           Library for ffmpeg
Group:             System Environment/Libraries

%description libs
Libraries for ffmpeg

%package devel
Summary:           Development files for %{name}
Group:             Development/Libraries
Requires:          %{name}-libs = %{version}-%{release}

%description devel
Development files for ffmpeg

%prep
%setup -q -n %{name}-%{version}
test -f version.h || echo "#define FFMPEG_VERSION \"%{evr}\"" > version.h

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --shlibdir=%{_libdir} --mandir=%{_mandir} \
  --disable-doc \
  --enable-avfilter \
  --disable-avisynth \
  --disable-debug \
  --enable-gpl \
  --enable-nonfree \
  --enable-postproc \
  --enable-pthreads \
  --enable-runtime-cpudetect \
  --enable-shared \
  --disable-static \
  --disable-stripping \
  --enable-version3 \
  --enable-vdpau \
  --extra-cflags="%{optflags} -fPIC" \
  --enable-bzlib \
  --enable-fontconfig \
  --enable-frei0r \
  --enable-gnutls \
  --enable-ladspa \
  --enable-libaacplus \
  --enable-libass \
  --enable-libbluray \
  --enable-libbs2b \
  --enable-libcaca \
  --enable-libdc1394 \
  --enable-libdcadec \
  --enable-libfaac \
  --enable-libfdk-aac \
  --enable-libfreetype \
  --enable-libfribidi \
  --enable-libgsm \
  --enable-libmodplug \
  --enable-libmp3lame \
  --enable-libopencore-amrnb \
  --enable-libopencore-amrwb \
  --enable-libopencv \
  --enable-libopenh264 \
  --enable-libopenjpeg \
  --enable-libopus \
  --enable-libpulse \
  --enable-librtmp \
  --enable-libschroedinger \
  --enable-libshine \
  --enable-libsoxr \
  --enable-libspeex \
  --enable-libssh \
  --enable-libtheora \
  --enable-libtwolame \
  --enable-libutvideo \
  --enable-libvidstab \
  --enable-libvo-aacenc \
  --enable-libvo-amrwbenc \
  --enable-libvorbis \
  --enable-libvpx \
  --enable-libwavpack \
  --enable-libwebp \
  --enable-libx264 \
  --enable-libx265 \
  --enable-libxavs \
  --enable-libxvid \
  --enable-openal \
  --enable-openssl \
  --enable-avresample

make
pushd doc
rm -f general.html.d platform.html.d git-howto.html.d \
   developer.html.d texi2pod.pl faq.html.d
popd

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} incdir=%{buildroot}%{_includedir}/ffmpeg
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
- Disabled flite (pkconfig can't find it)
- Disabled quvi (pkconfig can't find it)
- Disabled libcdio (it doesn't like the installed version?)

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with ffmpeg 2.7
- Based on CentOS: ffmpeg-2.6.1-1.el7.centos.src.rpm
