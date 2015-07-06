Name:          openal-soft
Version:       1.16.0
Release:       1%{?dist}
Summary:       Open Audio Library
Group:         System Environment/Libraries
License:       LGPLv2+
URL:           http://kcat.strangesoft.net/openal.html
Source0:       http://kcat.strangesoft.net/openal-releases/openal-soft-%{version}.tar.bz2
Patch0:        openal-soft-arm_neon-only-for-32bit.patch
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
#BuildRequires: portaudio-devel
BuildRequires: cmake
#BuildRequires: qt-devel
Obsoletes:     openal <= 0.0.10
Provides:      openal = %{version}

%description
OpenAL Soft is a cross-platform software implementation of the OpenAL 3D
audio API. Its built off of the open-sourced Windows version available
originally from the SVN repository at openal.org. OpenAL provides
capabilities for playing audio in a virtual 3d environment. Distance
attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, low-pass filters, and reverb, are available through the
EFX extension. It also facilitates streaming audio, multi-channel buffers,
and audio capture.

%package devel
Summary:       Development files for %{name}
Group:         Development/Libraries
Requires:      %{name}%{?_isa} = %{version}-%{release}
Obsoletes:     openal-devel <= 0.0.10
Provides:      openal-devel = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

#%package qt
#Summary:       Qt frontend for configuring OpenAL Soft
#Group:         Applications/System
#Requires:      %{name}%{?_isa} = %{version}-%{release}

#%description qt
#The %{name}-qt package contains alsoft-config, a Qt-based tool
#for configuring OpenAL features.

%prep
%setup -q
%patch0 -p1

%build
%cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
install -Dpm644 alsoftrc.sample %{buildroot}%{_sysconfdir}/openal/alsoft.conf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_bindir}/openal-info
%{_libdir}/libopenal.so.*
%dir %{_sysconfdir}/openal
%config(noreplace) %{_sysconfdir}/openal/alsoft.conf
%dir %{_datarootdir}/openal
%{_datarootdir}/openal/alsoftrc.sample
%dir %{_datarootdir}/openal/hrtf
%{_datarootdir}/openal/hrtf/default-44100.mhr
%{_datarootdir}/openal/hrtf/default-48000.mhr

%files devel
%{_bindir}/makehrtf
%{_includedir}/*
%{_libdir}/libopenal.so
%{_libdir}/pkgconfig/openal.pc

#%files qt
#%{_bindir}/alsoft-config

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with openal-soft 1.16.0
- Based on Fedora: openal-soft-1.16.0-7.fc23.src
