Name:              mediainfo
Version:           0.7.75
Release:           1%{?dist}
Summary:           Supplies technical and tag information about a video or audio file (CLI)
License:           BSD
Group:             Applications/Multimedia
URL:               http://mediaarea.net/MediaInfo
Source0:           http://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.bz2
BuildRequires:     libmediainfo-devel >= %{version}
BuildRequires:     libzen-devel >= 0.4.31
BuildRequires:     pkgconfig
BuildRequires:     zlib-devel
BuildRequires:     libtool
BuildRequires:     automake
BuildRequires:     autoconf
BuildRequires:     ImageMagick

%description
MediaInfo CLI (Command Line Interface).

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

%prep
%setup -q -n MediaInfo

sed -i 's/.$//' *.txt *.html Release/*.txt

find Source -type f -exec chmod 644 {} ';'
chmod 644 *.html *.txt Release/*.txt

sed -i 's/AC_PROG_LIBTOOL/LT_INIT/' Project/GNU/*/configure.ac

pushd Project/GNU/CLI
    autoreconf -fiv
    sed -i 's/enable_unicode="$(pkg-config --variable=Unicode libzen)"/enable_unicode=yes/' configure
popd

%build
# build CLI
pushd Project/GNU/CLI
    %configure --enable-static=no
    make %{?_smp_mflags}
popd

%install
pushd Project/GNU/CLI
    %make_install
popd

%files
%doc Release/ReadMe_CLI_Linux.txt License.html History_CLI.txt
%{_bindir}/mediainfo

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Removed all gui

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First testwith mediainfo 0.7.75
- Based on Fedora: mediainfo-0.7.74-2.fc23.src.cpio
