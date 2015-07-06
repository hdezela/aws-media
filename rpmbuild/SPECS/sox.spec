Summary:           A general purpose sound file conversion tool
Name:              sox
Version:           14.4.2
Release:           1%{?dist}
License:           GPLv2+ and LGPLv2+ and MIT
Group:             Applications/Multimedia
Source0:           http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:               http://sox.sourceforge.net/
BuildRequires:     libvorbis-devel
BuildRequires:     alsa-lib-devel
BuildRequires:     libtool-ltdl-devel
BuildRequires:     libsamplerate-devel
BuildRequires:     gsm-devel
BuildRequires:     wavpack-devel
BuildRequires:     ladspa-devel
BuildRequires:     libpng-devel
BuildRequires:     flac-devel
BuildRequires:     libao-devel
BuildRequires:     libsndfile-devel
BuildRequires:     libid3tag-devel
BuildRequires:     pulseaudio-libs-devel
BuildRequires:     libtool

%description
SoX (Sound eXchange) is a sound file format converter SoX can convert
between many different digitized sound formats and perform simple
sound manipulation functions, including sound effects.

%package -n sox-devel
Summary:           The SoX sound file format converter libraries
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}
Requires:          pkgconfig

%description -n sox-devel
This package contains the library needed for compiling applications
which will use the SoX sound file format converter.

%prep
%setup -q
autoreconf -vfi

%build
CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64" 
%configure \
  --with-gsm \
  --includedir=%{_includedir}/sox \
  --disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/libsox.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/sox/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/sox/*.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/play
%{_bindir}/rec
%{_bindir}/sox
%{_bindir}/soxi
%{_libdir}/libsox.so.*
%{_mandir}/man1/*
%{_mandir}/man7/*

%files -n sox-devel
%{_includedir}/sox
%{_libdir}/libsox.so
%{_libdir}/pkgconfig/sox.pc
%{_mandir}/man3/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with sox 14.4.2
- Based on Fedora: sox-14.4.2-2.fc23.src
