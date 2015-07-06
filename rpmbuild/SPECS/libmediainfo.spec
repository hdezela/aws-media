Name:              libmediainfo
Version:           0.7.75
Release:           1%{?dist}
Summary:           Library for supplies technical and tag information about a video or audio file
Group:             System Environment/Libraries
License:           BSD
URL:               http://mediaarea.net/MediaInfo
Source0:           http://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.bz2
BuildRequires:     libzen-devel >= 0.4.31
BuildRequires:     zlib-devel
BuildRequires:     doxygen
BuildRequires:     libcurl-devel
BuildRequires:     cmake
BuildRequires:     pkgconfig
Provides:          bundled(md5-plumb)

%description
This package contains the shared library for MediaInfo.
MediaInfo supplies technical and tag information about a video or
audio file.

What information can I get from MediaInfo?
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, SAMI

%package devel
Summary:           Include files and mandatory libraries for development
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          libzen-devel%{?_isa} >= 0.4.29

%description devel
Include files and mandatory libraries for development.

%prep
%setup -q -n MediaInfoLib

cp Release/ReadMe_DLL_Linux.txt ReadMe.txt
mv History_DLL.txt History.txt
sed -i 's/.$//' *.txt Source/Example/*

find . -type f -exec chmod 644 {} ';'

rm -rf Project/MSCS20*

%build
pushd Source/Doc/
    doxygen -u Doxyfile
    doxygen Doxyfile
popd
cp Source/Doc/*.html ./

mkdir Project/CMake/build
pushd Project/CMake/build
    %cmake ..
    make %{?_smp_mflags}
popd

%install
pushd Project/CMake/build
    %make_install
popd

install -m 644 -p Source/MediaInfoDLL/MediaInfoDLL.cs %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 -p Source/MediaInfoDLL/MediaInfoDLL.JNA.java %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 -p Source/MediaInfoDLL/MediaInfoDLL.JNative.java %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 -p Source/MediaInfoDLL/MediaInfoDLL.py %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 -p Source/MediaInfoDLL/MediaInfoDLL3.py %{buildroot}%{_includedir}/MediaInfoDLL

rm -f %{buildroot}%{_libdir}/%{name}.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc History.txt License.html ReadMe.txt
%{_libdir}/%{name}.so.*

%files devel
%doc Changes.txt Documentation.html Doc Source/Example
%{_includedir}/MediaInfo
%{_includedir}/MediaInfoDLL
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/mediainfolib/

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libmediainfo 0.7.75
- Based on Fedora: libmediainfo-0.7.74-2.fc23.src.cpio
