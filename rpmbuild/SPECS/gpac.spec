Name:              gpac
Summary:           MPEG-4 multimedia framework
Version:           0.5.2
Release:           1%{?dist}
License:           LGPLv2+
Group:             System Environment/Libraries
URL:               https://github.com/gpac/gpac
Source0:           https://github.com/gpac/gpac/archive/gpac-%{version}.tar.gz
BuildRequires:     ImageMagick
BuildRequires:     SDL-devel
BuildRequires:     a52dec-devel
BuildRequires:     librsvg2-devel >= 2.5.0
BuildRequires:     libGLU-devel
BuildRequires:     freeglut-devel
BuildRequires:     freetype-devel >= 2.1.4
BuildRequires:     faad2-devel
BuildRequires:     libjpeg-devel
BuildRequires:     libpng-devel >= 1.2.5
BuildRequires:     libmad-devel
BuildRequires:     xvidcore-devel >= 1.0.0
BuildRequires:     ffmpeg-devel
BuildRequires:     libxml2-devel
BuildRequires:     openssl-devel
BuildRequires:     openjpeg-devel
BuildRequires:     pulseaudio-libs-devel
BuildRequires:     zlib-devel
BuildRequires:     libogg-devel
BuildRequires:     libvorbis-devel
BuildRequires:     libtheora-devel
BuildRequires:     libXt-devel
#BuildRequires:     libXpm-devel
BuildRequires:     libXv-devel
BuildRequires:     xmlrpc-c-devel
BuildRequires:     doxygen
BuildRequires:     graphviz
#BuildRequires:     desktop-file-utils
BuildRequires:     opencore-amr-devel
#BuildRequires:     gtk+-devel
#BuildRequires:     gtk2-devel

%description
GPAC is a multimedia framework based on the MPEG-4 Systems standard developed
from scratch in ANSI C.  The original development goal is to provide a clean,
small and flexible alternative to the MPEG-4 Systems reference software.

GPAC features the integration of recent multimedia standards (SVG/SMIL, VRML,
X3D, SWF, 3GPP(2) tools and more) into a single framework. GPAC also features
MPEG-4 Systems encoders/multiplexers, publishing tools for content distribution
for MP4 and 3GPP(2) files and many tools for scene descriptions
(MPEG4 <-> VRML <-> X3D converters, SWF -> MPEG-4, etc).

%package libs
Summary:           Library for %{name}
Group:             System Environment/Libraries

%description libs
The %{name}-libs package contains library for %{name}.

%package devel
Summary:           Development libraries and files for %{name}
Group:             Development/Libraries
Requires:          %{name}-libs = %{version}-%{release}

%description devel
Development libraries and files for gpac.

%package doc
Summary:           Documentation for %{name}
Group:             Documentation

%description  doc
Documentation for %{name}.

%package devel-static
Summary:           Development libraries and files for %{name}
Group:             Development/Libraries
Requires:          %{name}-devel = %{version}-%{release}

%description  devel-static
Static library for gpac.

%prep
%setup -q -n %{name}-%{version}
cp -p doc/ipmpx_syntax.bt doc/ipmpx_syntax.bt.origine
iconv -f ISO-8859-1 -t UTF8 doc/ipmpx_syntax.bt.origine >  doc/ipmpx_syntax.bt
touch -r doc/ipmpx_syntax.bt.origine doc/ipmpx_syntax.bt
rm -rf doc/ipmpx_syntax.bt.origine

%build
%configure \
  --enable-debug \
  --extra-cflags="%{optflags} -fPIC -DPIC -D_FILE_OFFSET_BITS=64 -D_LARGE_FILES -D_LARGEFILE_SOURCE=1 -D_GNU_SOURCE=1 $(pkg-config --cflags libavformat)" \
  --libdir=%{_libdir} \
  --prefix=%{_prefix} \
  --mandir=%{_mandir} \
  --enable-pic \
  --disable-wx \
  --disable-platinum \
  --disable-oss-audio \
  --enable-jack \
  --enable-pulseaudio \
  --enable-amr \
  --disable-static \
  --use-js=no \
  --disable-x11-shm \
  --disable-x11-xv

cp -p config.h include/gpac

make %{?_smp_mflags} all 
make %{?_smp_mflags} sggen

pushd doc
doxygen
popd

%install
make DESTDIR=$RPM_BUILD_ROOT install install-lib INSTFLAGS="-p"

rm -rf $RPM_BUILD_ROOT%{_bindir}/%{osmo}

for b in MPEG4 X3D; do
  pushd applications/generators/${b}
    install -pm 0755 ${b}Gen $RPM_BUILD_ROOT%{_bindir}
  popd
done

touch -r Changelog doc/html-libgpac/*

sed -i -e '/GPAC_CONFIGURATION/d' $RPM_BUILD_ROOT%{_includedir}/gpac/configuration.h
touch -r Changelog $RPM_BUILD_ROOT%{_includedir}/gpac/*.h
touch -r Changelog $RPM_BUILD_ROOT%{_includedir}/gpac/internal/*.h
touch -r Changelog $RPM_BUILD_ROOT%{_includedir}/gpac/modules/*.h
rm $RPM_BUILD_ROOT%{_includedir}/gpac/config.h

mv $RPM_BUILD_ROOT/usr/usr/lib64 $RPM_BUILD_ROOT/usr
rm -rf $RPM_BUILD_ROOT/usr/usr



%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS Changelog COPYING README TODO 
%{_bindir}/DashCast
%{_bindir}/MP4Box
%{_bindir}/MP4Client
%{_bindir}/MPEG4Gen
%{_bindir}/X3DGen
%{_bindir}/MP42TS
%{_datadir}/gpac/
%{_mandir}/man1/*.1.*

%files libs
%defattr(-,root,root,-)
%{_libdir}/libgpac.so.*
%{_libdir}/gpac/

%files doc
%defattr(-,root,root,-)
%doc doc/html-libgpac/*

%files devel
%defattr(-,root,root,-)
%doc doc/CODING_STYLE doc/ipmpx_syntax.bt
%{_includedir}/gpac/
%{_libdir}/libgpac.so

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/libgpac_static.a

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Disabled osmo
- Extra libs included in source tarball
- Moved lib64 dir to correct location

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with gpac 0.5.2
- Based on Fedora: gpac-0.5.1-14.20141206svn.fc22.src
