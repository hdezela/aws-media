%global man_ext .gz
%global apriority 99

Summary:           MPEG audio player
Name:              mpg123
Version:           1.22.2
Release:           1%{?dist}
License:           GPLv2+ and LGPLv2
Group:             Applications/Multimedia
URL:               http://mpg123.org/
Source0:           http://downloads.sourceforge.net/mpg123/mpg123-%{version}.tar.bz2
BuildRequires:     libtool-ltdl-devel
BuildRequires:     SDL-devel
BuildRequires:     jack-audio-connection-kit-devel
BuildRequires:     alsa-lib-devel
BuildRequires:     pulseaudio-libs-devel
BuildRequires:     openal-soft-devel
BuildRequires:     doxygen
BuildRequires:     libtool
BuildRequires:     automake
BuildRequires:     autoconf
Requires:          libmpg123%{?_isa} = %{version}-%{release}
Requires(post):    %{_sbindir}/alternatives
Requires(postun):  %{_sbindir}/alternatives
Provides:          mp3-cmdline = %{version}-%{release}

%description
Real time command line MPEG audio player for Layer 1, 2 and Layer3.

%package plugins-pulseaudio
Summary:           Pulseaudio output plug-in for mpg123
Group:             Applications/Multimedia
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description plugins-pulseaudio
Pulseaudio output plug-in for mpg123.

%package plugins-jack
Summary:           JACK output plug-in for mpg123
Group:             Applications/Multimedia
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description plugins-jack
JACK output plug-in for mpg123.

%package plugins-extras
Summary:           Extra output plugins for mpg123
Group:             Applications/Multimedia
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description plugins-extras
Extra (non often used) output plugins for mpg123 which require additional
dependencies to be installed.

%package -n libmpg123
Summary:           MPEG audio Layer 1, 2 and Layer3 library
Group:             System Environment/Libraries

%description -n libmpg123
MPEG audio Layer 1, 2 and Layer3 library.

%package -n libmpg123-devel
Summary:           Development files for mpg123
Group:             Development/Libraries
Requires:          libmpg123%{?_isa} = %{version}-%{release}

%description -n libmpg123-devel
The libmpg123-devel package contains libraries and header files for
developing applications that use libmpg123.

%prep
%setup -q
autoreconf -i -f
iconv -f iso8859-1 -t utf8 AUTHORS -o AUTHORS.utf8
touch -r AUTHORS AUTHORS.utf8
mv AUTHORS.utf8 AUTHORS
echo "HTML_TIMESTAMP=NO" >> doc/doxygen.conf

%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
pushd doc
doxygen doxygen.conf
popd

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
install -m 644 -p doc/man/man3/mpg123*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install -m 644 -p doc/man/man3/MPG123*.3 $RPM_BUILD_ROOT%{_mandir}/man3
mv $RPM_BUILD_ROOT%{_bindir}/mpg123 $RPM_BUILD_ROOT%{_bindir}/mpg123.bin
mv $RPM_BUILD_ROOT%{_mandir}/man1/mpg123.1 \
   $RPM_BUILD_ROOT%{_mandir}/man1/mpg123.bin.1
ln -s mpg123.bin $RPM_BUILD_ROOT%{_bindir}/mpg123
ln -s mpg123.bin $RPM_BUILD_ROOT%{_bindir}/mp3-cmdline
ln -s mpg123.bin.1 $RPM_BUILD_ROOT%{_mandir}/man1/mpg123.1

%post
%{_sbindir}/alternatives \
  --install %{_bindir}/mpg123 mpg321_binlink %{_bindir}/mpg123.bin %{apriority} \
  --slave %{_mandir}/man1/mpg123.1%{man_ext} mpg321_manlink %{_mandir}/man1/mpg123.bin.1%{man_ext} \
  --slave %{_bindir}/mp3-cmdline mpg321_mp3cmdline %{_bindir}/mpg123.bin \
  >/dev/null 2>&1 || :

%postun
if [ "$1" -eq 0 ]; then
  %{_sbindir}/alternatives \
    --remove mpg321_binlink %{_bindir}/mpg123.bin \
    >/dev/null 2>&1 || :
fi

%post -n libmpg123 -p /sbin/ldconfig

%postun -n libmpg123 -p /sbin/ldconfig

%files
%doc README doc/README.remote
%{_bindir}/mpg123.bin
%{_bindir}/mpg123-id3dump
%{_bindir}/mpg123-strip
%{_bindir}/out123
%ghost %{_bindir}/mpg123
%ghost %{_bindir}/mp3-cmdline
%dir %{_libdir}/mpg123
%{_libdir}/mpg123/output_alsa.*
%{_libdir}/mpg123/output_dummy.*
%{_libdir}/mpg123/output_oss.*
%{_mandir}/man1/mpg123.bin.1%{man_ext}
%{_mandir}/man1/out123.1%{man_ext}
%ghost %{_mandir}/man1/mpg123.1%{man_ext}

%files plugins-pulseaudio
%{_libdir}/mpg123/output_pulse.*

%files plugins-jack
%{_libdir}/mpg123/output_jack.*

%files plugins-extras
%{_libdir}/mpg123/output_openal.*
%{_libdir}/mpg123/output_sdl.*

%files -n libmpg123
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libmpg123.so.*

%files -n libmpg123-devel
%doc doc/BENCHMARKING doc/README.gain doc/html doc/examples
%{_includedir}/mpg123.h
%{_libdir}/libmpg123.so
%{_libdir}/pkgconfig/libmpg123.pc
%{_mandir}/man3/*.3*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with mpg123 1.22.2
- Based on Fedora: mpg123-1.19.0-2.fc22.src
