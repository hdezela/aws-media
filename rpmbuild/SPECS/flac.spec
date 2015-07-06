Summary:       An encoder/decoder for the Free Lossless Audio Codec
Name:          flac
Version:       1.3.1
Release:       1%{?dist}
License:       BSD and GPLv2+ and GFDL
Group:         Applications/Multimedia
Source0:       http://downloads.xiph.org/releases/flac/flac-%{version}.tar.xz
Patch1:        flac-cflags.patch
URL:           http://www.xiph.org/flac/
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: libogg-devel
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: doxygen

%description
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package contains the command-line tools and documentation.

%package libs
Summary:       Libraries for the Free Lossless Audio Codec
Group:         System Environment/Libraries
Obsoletes:     flac < 1.2.1-11

%description libs
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package contains the FLAC libraries.

%package devel
Summary:       Development libraries and header files from FLAC
Group:         Development/Libraries
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      pkgconfig

%description devel
This package contains all the files needed to develop applications that
will use the Free Lossless Audio Codec.

%prep
%setup -q
%patch1 -p1 -b .cflags

%build
./autogen.sh -V

export CFLAGS="%{optflags} -funroll-loops"
%configure \
  --disable-xmms-plugin \
  --disable-silent-rules \
  --disable-thorough-tests

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

mv %{buildroot}%{_docdir}/flac* ./flac-doc
mkdir -p flac-doc-devel
mv flac-doc{/html/api,-devel}
rm flac-doc/FLAC.tag

rm %{buildroot}%{_libdir}/*.la

%check
make -C test check FLAC__TEST_LEVEL=0 &> /dev/null

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%doc flac-doc/*
%{_bindir}/flac
%{_bindir}/metaflac
%{_mandir}/man1/*

%files libs
%doc AUTHORS COPYING* README
%{_libdir}/*.so.*

%files devel
%doc flac-doc-devel/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*.m4

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with flac 1.3.1
- Based on Fedora: flac-1.3.1-3.fc23.src.rpm
