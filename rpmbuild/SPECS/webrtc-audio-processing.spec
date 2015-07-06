Name:           webrtc-audio-processing
Version:        0.1
Release:        1%{?dist}
Summary:        Library for echo cancellation
License:        BSD
URL:            http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:        http://freedesktop.org/software/pulseaudio/webrtc-audio-processing/%{name}-%{version}.tar.xz
Patch0:         webrtc-fix-typedefs-on-other-arches.patch

%description
%{name} is a library derived from Google WebRTC project that 
provides echo cancellation functionality. This library is used by for example
PulseAudio to provide echo cancellation.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .typedef

%build
%configure \
  --with-package-name='Fedora Webrtc-audio-processing package' \
  --with-package-origin='http://download.fedoraproject.org' \
  --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING NEWS AUTHORS PATENTS
%{_libdir}/*.so.*

%files devel
%{_libdir}/libwebrtc_audio_processing.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/webrtc_audio_processing/

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with webrtc-audio-processing 0.1
- Based on CentOS: webrtc-audio-processing-0.1-5.el7.src.rpm
