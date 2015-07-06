Name:          SDL
Version:       1.2.15
Release:       1%{?dist}
Summary:       A cross-platform multimedia library
Group:         System Environment/Libraries
URL:           http://www.libsdl.org/
License:       LGPLv2+
Source0:       %{name}-%{version}_repackaged.tar.gz
Source1:       SDL_config.h
Patch0:        SDL-1.2.12-multilib.patch
Patch1:        SDL-1.2.10-GrabNotViewable.patch
Patch2:        SDL-1.2.15-x11-Bypass-SetGammaRamp-when-changing-gamma.patch
Patch3:        SDL-1.2.15-const_XData32.patch
Patch4:        SDL-1.2.15-add_sdl_config_man.patch
BuildRequires: alsa-lib-devel
BuildRequires: audiofile-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: nasm
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device.

%package devel
Summary:       Files needed to develop Simple DirectMedia Layer applications
Group:         Development/Libraries
Requires:      SDL%{?_isa} = %{version}-%{release}
Requires:      alsa-lib-devel

%description devel
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device. This
package provides the libraries, include files, and other resources needed for
developing SDL applications.

%package static
Summary:       Files needed to develop static Simple DirectMedia Layer applications
Group:         Development/Libraries
Requires:      SDL-devel%{?_isa} = %{version}-%{release}

%description static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device. This
package provides the static libraries needed for developing static SDL
applications.

%prep
%setup -q -b0
%patch0 -p1 -b .multilib
%patch1 -p0 -b .grabnotviewable
%patch2 -p1 -b .gamma
%patch3 -p1 -b .XData32
%patch4 -p1 -b .sdl_config_man

for F in CREDITS; do 
    iconv -f iso8859-1 -t utf-8 < "$F" > "${F}.utf"
    touch --reference "$F" "${F}.utf"
    mv "${F}.utf" "$F"
done

sed -i -e 's/.*AM_PATH_ESD.*//' configure.in
cp -p %{_datadir}/automake-*/config.{sub,guess} build-scripts

%build
aclocal
libtoolize
autoconf
%configure \
    --disable-video-svga \
    --disable-video-ggi \
    --disable-video-aalib \
    --enable-sdl-dlopen \
    --disable-arts \
    --disable-esd \
    --enable-pulseaudio-shared \
    --enable-alsa \
    --disable-video-ps3 \
    --disable-rpath \
    --disable-video-x11 \
    --disable-x11-shared \
    --disable-dga \
    --disable-video-dga \
    --disable-video-x11-dgamouse \
    --disable-video-x11-vm \
    --disable-video-x11-xv \
    --disable-video-x11-xinerama \
    --disable-video-x11-xme \
    --disable-video-x11-xrandr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

mv %{buildroot}/%{_includedir}/SDL/SDL_config.h %{buildroot}/%{_includedir}/SDL/SDL_config-%{_arch}.h
install -m644 %{SOURCE1} %{buildroot}/%{_includedir}/SDL/SDL_config.h

rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc BUGS COPYING CREDITS README-SDL.txt
%{_libdir}/lib*.so.*

%files devel
%doc README docs.html docs/html docs/index.html TODO WhatsNew
%{_bindir}/*-config
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/sdl.pc
%{_includedir}/SDL
%{_datadir}/aclocal/*
%{_mandir}/man1/*
%{_mandir}/man3/SDL*.3*

%files static
%{_libdir}/lib*.a

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with SDL 1.2.15
- Based on CentOS: SDL-1.2.15-11.el7.src.rpm
