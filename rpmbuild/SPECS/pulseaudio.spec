%global pa_major   6.0
%global _hardened_build 1
%global bash_completionsdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo '/etc/bash_completion.d')

Name:          pulseaudio
Summary:       Improved Linux Sound Server
Version:       %{pa_major}
Release:       1%{?dist}
License:       LGPLv2+
URL:           http://www.freedesktop.org/wiki/Software/PulseAudio
Source0:       http://freedesktop.org/software/pulseaudio/releases/pulseaudio-%{version}.tar.xz
Source1:       http://freedesktop.org/software/pulseaudio/releases/pulseaudio-%{version}.tar.xz.md5
Source2:       http://freedesktop.org/software/pulseaudio/releases/pulseaudio-%{version}.tar.xz.sha1
Source5:       default.pa-for-gdm
Patch1:        pulseaudio-autostart.patch
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig(bash-completion)
BuildRequires: m4
BuildRequires: libtool-ltdl-devel
BuildRequires: intltool
BuildRequires: pkgconfig
BuildRequires: doxygen
BuildRequires: xmltoman
BuildRequires: tcp_wrappers-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: glib2-devel
BuildRequires: GConf2-devel
BuildRequires: avahi-devel
BuildRequires: libatomic_ops-static
BuildRequires: libatomic_ops-devel
BuildRequires: sbc-devel
BuildRequires: openssl-devel
BuildRequires: orc-devel
BuildRequires: libtdb-devel
BuildRequires: speex-devel >= 1.2
BuildRequires: libasyncns-devel
BuildRequires: json-c-devel
BuildRequires: dbus-devel
BuildRequires: libcap-devel
BuildRequires: pkgconfig(fftw3f)
BuildRequires: webrtc-audio-processing-devel
BuildRequires: pkgconfig(check)
Obsoletes:     padevchooser < 1.0
Requires(pre): shadow-utils
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      rtkit

%description
PulseAudio is a sound server for Linux and other Unix like operating
systems. It is intended to be an improved drop-in replacement for the
Enlightened Sound Daemon (ESOUND).

%package qpaeq
Summary:       Pulseaudio equalizer interface
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      PyQt4
Requires:      dbus-python
%description qpaeq
qpaeq is a equalizer interface for pulseaudio's equalizer sinks.

%package esound-compat
Summary:       PulseAudio EsounD daemon compatibility script
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description esound-compat
A compatibility script that allows applications to call /usr/bin/esd
and start PulseAudio with EsounD protocol modules.

%package module-zeroconf
Summary:        Zeroconf support for the PulseAudio sound server
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-utils

%description module-zeroconf
Zeroconf publishing module for the PulseAudio sound server.

%package module-jack
Summary:        JACK support for the PulseAudio sound server
BuildRequires:  jack-audio-connection-kit-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description module-jack
JACK sink and source modules for the PulseAudio sound server.

%package module-gconf
Summary:        GConf support for the PulseAudio sound server
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description module-gconf
GConf configuration backend for the PulseAudio sound server.

%package libs
Summary:        Libraries for PulseAudio clients
License:        LGPLv2+
Obsoletes:      pulseaudio-libs-zeroconf < 1.1

%description libs
This package contains the runtime libraries for any application that wishes
to interface with a PulseAudio sound server.

%package libs-glib2
Summary:        GLIB 2.x bindings for PulseAudio clients
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description libs-glib2
This package contains bindings to integrate the PulseAudio client library with
a GLIB 2.x based application.

%package libs-devel
Summary:        Headers and libraries for PulseAudio client development
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs-glib2%{?_isa} = %{version}-%{release}
%description libs-devel
Headers and libraries for developing applications that can communicate with
a PulseAudio sound server.

%package utils
Summary:        PulseAudio sound server utilities
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      pulseaudio-utils < 3.0-3

%description utils
This package contains command line utilities for the PulseAudio sound server.

%package gdm-hooks
Summary:        PulseAudio GDM integration
License:        LGPLv2+
Requires:       gdm >= 1:2.22.0
Requires(pre):  gdm

%description gdm-hooks
This package contains GDM integration hooks for the PulseAudio sound server.


%prep
%setup -q -T -b0 -n %{name}-%{version}
%patch1 -p1 -R -b .autostart

sed -i.no_consolekit -e \
  's/^load-module module-console-kit/#load-module module-console-kit/' \
  src/daemon/default.pa.in

%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif

%build
%configure \
  --disable-silent-rules \
  --disable-static \
  --disable-rpath \
  --with-system-user=pulse \
  --with-system-group=pulse \
  --with-access-group=pulse-access \
  --disable-oss-output \
  --disable-alsa \
  --enable-jack \
  --disable-lirc \
  --disable-x11 \
  --disable-bluez4 \
  --disable-bluez5 \
  --disable-systemd-daemon \
  --enable-webrtc-aec \
  --enable-tests

make %{?_smp_mflags} V=1
make doxygen

%install
make install DESTDIR=$RPM_BUILD_ROOT

pushd %{buildroot}%{_bindir}
%if "%{_libdir}" == "/usr/lib"
ln -s padsp padsp-32
%else
cp -a padsp padsp-32
sed -i -e "s|%{_libdir}/pulseaudio/libpulsedsp.so|/usr/lib/pulseaudio/libpulsedsp.so|g" padsp-32
%endif
popd

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/pulse
install -p -m644 -D %{SOURCE5} $RPM_BUILD_ROOT%{_localstatedir}/lib/gdm/.pulse/default.pa

%if "%{bash_completionsdir}" != "/etc/bash_completion.d"
mkdir -p $RPM_BUILD_ROOT%{bash_completionsdir}
mv $RPM_BUILD_ROOT/etc/bash_completion.d/* \
   $RPM_BUILD_ROOT%{bash_completionsdir}/
%endif

rm -fv $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/pulse-%{pa_major}/modules/*.la
rm -fv $RPM_BUILD_ROOT%{_libdir}/pulse-%{pa_major}/modules/module-detect.so
rm -fv $RPM_BUILD_ROOT%{_libdir}/pulse-%{pa_major}/modules/module-hal-detect.so
rm -fv $RPM_BUILD_ROOT%{_libdir}/pulse-%{pa_major}/modules/module-udev-detect.so

%find_lang %{name}

%check
make check %{nil}

%pre
getent group pulse-access >/dev/null || groupadd -r pulse-access
getent group pulse-rt >/dev/null || groupadd -r pulse-rt
getent group pulse >/dev/null || groupadd -f -g 171 -r pulse
if ! getent passwd pulse >/dev/null ; then
    if ! getent passwd 171 >/dev/null ; then
      useradd -r -u 171 -g pulse -d /var/run/pulse -s /sbin/nologin -c "PulseAudio System Daemon" pulse
    else
      useradd -r -g pulse -d /var/run/pulse -s /sbin/nologin -c "PulseAudio System Daemon" pulse
    fi
fi
exit 0

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%posttrans
(grep '^load-module module-cork-music-on-phone$' %{_sysconfdir}/pulse/default.pa > /dev/null && \
 sed -i.rpmsave -e 's|^load-module module-cork-music-on-phone$|load-module module-role-cork|' \
 %{_sysconfdir}/pulse/default.pa
) ||:

%files
%doc README LICENSE GPL LGPL
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %{_sysconfdir}/pulse/default.pa
%config(noreplace) %{_sysconfdir}/pulse/system.pa
%{_sysconfdir}/dbus-1/system.d/pulseaudio-system.conf
%{bash_completionsdir}/*
%{_bindir}/pulseaudio
%{_libdir}/libpulsecore-%{pa_major}.so
%dir %{_libdir}/pulse-%{pa_major}/
%dir %{_libdir}/pulse-%{pa_major}/modules/
%{_libdir}/pulse-%{pa_major}/modules/libcli.so
%{_libdir}/pulse-%{pa_major}/modules/libprotocol-cli.so
%{_libdir}/pulse-%{pa_major}/modules/libprotocol-esound.so
%{_libdir}/pulse-%{pa_major}/modules/libprotocol-http.so
%{_libdir}/pulse-%{pa_major}/modules/libprotocol-native.so
%{_libdir}/pulse-%{pa_major}/modules/libprotocol-simple.so
%{_libdir}/pulse-%{pa_major}/modules/librtp.so
%{_libdir}/pulse-%{pa_major}/modules/libwebrtc-util.so
%{_libdir}/pulse-%{pa_major}/modules/module-cli-protocol-tcp.so
%{_libdir}/pulse-%{pa_major}/modules/module-cli-protocol-unix.so
%{_libdir}/pulse-%{pa_major}/modules/module-cli.so
%{_libdir}/pulse-%{pa_major}/modules/module-combine.so
%{_libdir}/pulse-%{pa_major}/modules/module-combine-sink.so
%{_libdir}/pulse-%{pa_major}/modules/module-dbus-protocol.so
%{_libdir}/pulse-%{pa_major}/modules/module-filter-apply.so
%{_libdir}/pulse-%{pa_major}/modules/module-filter-heuristics.so
%{_libdir}/pulse-%{pa_major}/modules/module-device-manager.so
%{_libdir}/pulse-%{pa_major}/modules/module-loopback.so
%{_libdir}/pulse-%{pa_major}/modules/module-esound-compat-spawnfd.so
%{_libdir}/pulse-%{pa_major}/modules/module-esound-compat-spawnpid.so
%{_libdir}/pulse-%{pa_major}/modules/module-esound-protocol-tcp.so
%{_libdir}/pulse-%{pa_major}/modules/module-esound-protocol-unix.so
%{_libdir}/pulse-%{pa_major}/modules/module-esound-sink.so
%{_libdir}/pulse-%{pa_major}/modules/module-http-protocol-tcp.so
%{_libdir}/pulse-%{pa_major}/modules/module-http-protocol-unix.so
%{_libdir}/pulse-%{pa_major}/modules/module-match.so
%{_libdir}/pulse-%{pa_major}/modules/module-mmkbd-evdev.so
%{_libdir}/pulse-%{pa_major}/modules/module-native-protocol-fd.so
%{_libdir}/pulse-%{pa_major}/modules/module-native-protocol-tcp.so
%{_libdir}/pulse-%{pa_major}/modules/module-native-protocol-unix.so
%{_libdir}/pulse-%{pa_major}/modules/module-null-sink.so
%{_libdir}/pulse-%{pa_major}/modules/module-null-source.so
%{_libdir}/pulse-%{pa_major}/modules/module-pipe-sink.so
%{_libdir}/pulse-%{pa_major}/modules/module-pipe-source.so
%{_libdir}/pulse-%{pa_major}/modules/module-remap-source.so
%{_libdir}/pulse-%{pa_major}/modules/module-rescue-streams.so
%{_libdir}/pulse-%{pa_major}/modules/module-role-ducking.so
%{_libdir}/pulse-%{pa_major}/modules/module-rtp-recv.so
%{_libdir}/pulse-%{pa_major}/modules/module-rtp-send.so
%{_libdir}/pulse-%{pa_major}/modules/module-simple-protocol-tcp.so
%{_libdir}/pulse-%{pa_major}/modules/module-simple-protocol-unix.so
%{_libdir}/pulse-%{pa_major}/modules/module-sine.so
%{_libdir}/pulse-%{pa_major}/modules/module-switch-on-port-available.so
%{_libdir}/pulse-%{pa_major}/modules/module-tunnel-sink-new.so
%{_libdir}/pulse-%{pa_major}/modules/module-tunnel-sink.so
%{_libdir}/pulse-%{pa_major}/modules/module-tunnel-source-new.so
%{_libdir}/pulse-%{pa_major}/modules/module-tunnel-source.so
%{_libdir}/pulse-%{pa_major}/modules/module-volume-restore.so
%{_libdir}/pulse-%{pa_major}/modules/module-suspend-on-idle.so
%{_libdir}/pulse-%{pa_major}/modules/module-default-device-restore.so
%{_libdir}/pulse-%{pa_major}/modules/module-device-restore.so
%{_libdir}/pulse-%{pa_major}/modules/module-stream-restore.so
%{_libdir}/pulse-%{pa_major}/modules/module-card-restore.so
%{_libdir}/pulse-%{pa_major}/modules/module-ladspa-sink.so
%{_libdir}/pulse-%{pa_major}/modules/module-remap-sink.so
%{_libdir}/pulse-%{pa_major}/modules/module-always-sink.so
%{_libdir}/pulse-%{pa_major}/modules/module-console-kit.so
%{_libdir}/pulse-%{pa_major}/modules/module-position-event-sounds.so
%{_libdir}/pulse-%{pa_major}/modules/module-augment-properties.so
%{_libdir}/pulse-%{pa_major}/modules/module-role-cork.so
%{_libdir}/pulse-%{pa_major}/modules/module-sine-source.so
%{_libdir}/pulse-%{pa_major}/modules/module-intended-roles.so
%{_libdir}/pulse-%{pa_major}/modules/module-rygel-media-server.so
%{_libdir}/pulse-%{pa_major}/modules/module-echo-cancel.so
%{_libdir}/pulse-%{pa_major}/modules/module-switch-on-connect.so
%{_libdir}/pulse-%{pa_major}/modules/module-virtual-sink.so
%{_libdir}/pulse-%{pa_major}/modules/module-virtual-source.so
%{_libdir}/pulse-%{pa_major}/modules/module-virtual-surround-sink.so
%{_mandir}/man1/pulseaudio.1*
%{_mandir}/man5/default.pa.5*
%{_mandir}/man5/pulse-cli-syntax.5*
%{_mandir}/man5/pulse-client.conf.5*
%{_mandir}/man5/pulse-daemon.conf.5*
%dir %{_libexecdir}/pulse
%attr(0700, pulse, pulse) %dir %{_localstatedir}/lib/pulse
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_pulseaudio

%files qpaeq
%{_bindir}/qpaeq
%{_libdir}/pulse-%{pa_major}/modules/module-equalizer-sink.so

%files esound-compat
%{_bindir}/esdcompat
%{_mandir}/man1/esdcompat.1.gz

%files module-zeroconf
%{_libdir}/pulse-%{pa_major}/modules/libavahi-wrap.so
%{_libdir}/pulse-%{pa_major}/modules/module-zeroconf-publish.so
%{_libdir}/pulse-%{pa_major}/modules/module-zeroconf-discover.so
%{_libdir}/pulse-%{pa_major}/modules/libraop.so
%{_libdir}/pulse-%{pa_major}/modules/module-raop-discover.so
%{_libdir}/pulse-%{pa_major}/modules/module-raop-sink.so

%files module-jack
%{_libdir}/pulse-%{pa_major}/modules/module-jackdbus-detect.so
%{_libdir}/pulse-%{pa_major}/modules/module-jack-sink.so
%{_libdir}/pulse-%{pa_major}/modules/module-jack-source.so

%files module-gconf
%{_libdir}/pulse-%{pa_major}/modules/module-gconf.so
%{_libexecdir}/pulse/gconf-helper

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs -f %{name}.lang
%doc README LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%config(noreplace) %{_sysconfdir}/pulse/client.conf
%{_libdir}/libpulse.so.0*
%{_libdir}/libpulse-simple.so.0*
%dir %{_libdir}/pulseaudio/
%{_libdir}/pulseaudio/libpulsecommon-%{pa_major}.*
%{_libdir}/pulseaudio/libpulsedsp.*

%post libs-glib2 -p /sbin/ldconfig
%postun libs-glib2 -p /sbin/ldconfig

%files libs-glib2
%{_libdir}/libpulse-mainloop-glib.so.0*

%files libs-devel
%doc doxygen/html
%{_includedir}/pulse/
%{_libdir}/libpulse.so
%{_libdir}/libpulse-mainloop-glib.so
%{_libdir}/libpulse-simple.so
%{_libdir}/pkgconfig/libpulse*.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libpulse.vapi
%{_datadir}/vala/vapi/libpulse.deps
%{_datadir}/vala/vapi/libpulse-mainloop-glib.vapi
%{_datadir}/vala/vapi/libpulse-mainloop-glib.deps
%{_datadir}/vala/vapi/libpulse-simple.deps
%{_datadir}/vala/vapi/libpulse-simple.vapi

%dir %{_libdir}/cmake
%{_libdir}/cmake/PulseAudio/

%files utils
%{_bindir}/pacat
%{_bindir}/pacmd
%{_bindir}/pactl
%{_bindir}/paplay
%{_bindir}/parec
%{_bindir}/pamon
%{_bindir}/parecord
%{_bindir}/padsp
%{_bindir}/padsp-32
%{_bindir}/pasuspender
%{_mandir}/man1/pacat.1.gz
%{_mandir}/man1/pacmd.1.gz
%{_mandir}/man1/pactl.1.gz
%{_mandir}/man1/paplay.1.gz
%{_mandir}/man1/pasuspender.1.gz
%{_mandir}/man1/padsp.1.gz
%{_mandir}/man1/pax11publish.1.gz
%exclude %{_mandir}/man1/start-pulseaudio-x11.1.gz

%files gdm-hooks
%attr(0700, gdm, gdm) %dir %{_localstatedir}/lib/gdm/.pulse
%attr(0600, gdm, gdm) %{_localstatedir}/lib/gdm/.pulse/default.pa

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with pulseaudio 6.0
- Based on pulseaudio-6.0-2.fc21.1.src.rpm
- Disabled alsa, bluetooth and x11
