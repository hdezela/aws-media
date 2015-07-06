%global groupname jackuser
%global pagroup   pulse-rt

Summary:       The Jack Audio Connection Kit
Name:          jack-audio-connection-kit
Version:       1.9.10
Release:       1%{?dist}
License:       GPLv2 and GPLv2+ and LGPLv2+
Group:         System Environment/Daemons
URL:           http://www.jackaudio.org
Source0:       https://dl.dropbox.com/u/28869550/jack-%{version}.tar.bz2
Source1:       %{name}-README.Fedora
Source2:       %{name}-script.pa
Source3:       %{name}-limits.conf
Patch0:        jack-audio-connection-kit-no_date_footer.patch
Patch1:        jack-doxygen-output-dir-fix.patch
Patch2:        jack-apidoc-only.patch
Patch3:        jack-realtime-compat.patch
Patch4:        jack-portnames.patch
Patch5:        jack-ppc64-long.patch
Patch6:        jack-gcc5.patch
BuildRequires: alsa-lib-devel
BuildRequires: dbus-devel
BuildRequires: doxygen
BuildRequires: expat-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: ncurses-devel
BuildRequires: opus-devel
BuildRequires: pkgconfig
BuildRequires: python27
BuildRequires: readline-devel
Requires(pre): shadow-utils
Requires:      pam

%description
JACK is a low-latency audio server, written primarily for the Linux operating
system. It can connect a number of different applications to an audio device, as
well as allowing them to share audio between themselves. Its clients can run in
their own processes (i.e. as a normal application), or can they can run within a
JACK server (i.e. a "plugin").

JACK is different from other audio server efforts in that it has been designed
from the ground up to be suitable for professional audio work. This means that
it focuses on two key areas: synchronous execution of all clients, and low
latency operation.

%package dbus
Summary:       Jack D-Bus launcher
Group:         Applications/Multimedia
Requires:      %{name} = %{version}-%{release}

%description dbus
Launcher to start Jack through D-Bus.


%package devel
Summary:       Header files for Jack
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Header files for the Jack Audio Connection Kit.

%package example-clients
Summary:       Example clients that use Jack 
Group:         Applications/Multimedia
Requires:      %{name} = %{version}-%{release}

%description example-clients
Small example clients that use the Jack Audio Connection Kit.

%prep
%setup -q -n jack-%{version}
%patch0 -p1 -b .nodate
%patch1 -p1 -b .outdir
%patch2 -p1 -b .nointernalapi
%patch3 -p1 -b .priority
%patch4 -p1 -b .portnames
%patch5 -p1 -b .mpd
%patch6 -p1 -b .gcc5

for file in ChangeLog README TODO; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build
export CPPFLAGS="$RPM_OPT_FLAGS -O0"
export PREFIX=%{_prefix}
./waf configure \
  %{?_smp_mflags} \
  --mandir=%{_mandir}/man1 \
  --libdir=%{_libdir} \
  --doxygen \
  --dbus \
  --classic \
  --alsa \
  --clients 256 \
  --ports-per-application=2048

./waf build %{?_smp_mflags} -v

%install
./waf --destdir=$RPM_BUILD_ROOT install

mv $RPM_BUILD_ROOT%{_datadir}/jack-audio-connection-kit/reference .
rm -rf $RPM_BUILD_ROOT%{_datadir}/jack-audio-connection-kit
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d
sed -e 's,@groupname@,%groupname,g; s,@pagroup@,%pagroup,g;' \
    %{SOURCE3} > $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/95-jack.conf
install -p -m644 %{SOURCE1} README.Fedora
install -p -m644 %{SOURCE2} jack.pa
mv $RPM_BUILD_ROOT%{_bindir}/jack_rec $RPM_BUILD_ROOT%{_bindir}/jackrec
chmod 755 $RPM_BUILD_ROOT%{_libdir}/jack/*.so $RPM_BUILD_ROOT%{_libdir}/libjack*.so.*.*.*

%pre
getent group %groupname > /dev/null || groupadd -r %groupname
exit 0

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%doc ChangeLog README README_NETJACK2 TODO
%doc README.Fedora
%doc jack.pa
%{_bindir}/jackd
%{_bindir}/jackrec
%{_libdir}/jack/
%{_libdir}/libjack.so.*
%{_libdir}/libjacknet.so.*
%{_libdir}/libjackserver.so.*
%config(noreplace) %{_sysconfdir}/security/limits.d/*.conf

%{_mandir}/man1/jackrec.1*
%{_mandir}/man1/jackd*.1*

%files dbus
%{_bindir}/jackdbus
%{_datadir}/dbus-1/services/org.jackaudio.service
%{_bindir}/jack_control

%files devel
%doc reference/html/
%{_includedir}/jack/
%{_libdir}/libjack.so
%{_libdir}/libjacknet.so
%{_libdir}/libjackserver.so
%{_libdir}/pkgconfig/jack.pc

%files example-clients
%{_bindir}/alsa_in
%{_bindir}/alsa_out
%{_bindir}/jack_alias
%{_bindir}/jack_bufsize
%{_bindir}/jack_connect
%{_bindir}/jack_disconnect
%{_bindir}/jack_cpu_load
%{_bindir}/jack_evmon
%{_bindir}/jack_freewheel
%exclude %{_mandir}/man1/jack_impulse_grabber.1*
%{_bindir}/jack_latent_client
%{_bindir}/jack_load
%{_bindir}/jack_unload
%{_bindir}/jack_lsp
%{_bindir}/jack_metro
%{_bindir}/jack_midi_dump
%{_bindir}/jack_midi_latency_test
%{_bindir}/jack_midiseq
%{_bindir}/jack_midisine
%{_bindir}/jack_monitor_client
%{_bindir}/jack_net_master
%{_bindir}/jack_net_slave
%{_bindir}/jack_netsource
%{_bindir}/jack_samplerate
%{_bindir}/jack_server_control
%{_bindir}/jack_session_notify
%{_bindir}/jack_showtime
%{_bindir}/jack_simple_client
%{_bindir}/jack_simple_session_client
%{_bindir}/jack_thru
%{_bindir}/jack_transport
%{_bindir}/jack_wait
%{_bindir}/jack_zombie

%{_mandir}/man1/alsa_*.1*
%{_mandir}/man1/jack_bufsize.1*
%{_mandir}/man1/jack_connect.1*
%{_mandir}/man1/jack_disconnect.1*
%{_mandir}/man1/jack_freewheel*.1*
%{_mandir}/man1/jack_load*.1*
%{_mandir}/man1/jack_unload*.1*
%{_mandir}/man1/jack_lsp.1*
%{_mandir}/man1/jack_metro.1*
%{_mandir}/man1/jack_monitor_client.1*
%{_mandir}/man1/jack_netsource.1*
%{_mandir}/man1/jack_samplerate.1*
%{_mandir}/man1/jack_showtime.1*
%{_mandir}/man1/jack_simple_client.1*
%{_mandir}/man1/jack_transport.1*
%{_mandir}/man1/jack_wait.1*

# tests
%{_bindir}/jack_cpu
%{_bindir}/jack_iodelay
%{_bindir}/jack_multiple_metro
%{_bindir}/jack_test

%{_mandir}/man1/jack_iodelay.1*


%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Firewire removed

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with jack-audio-connection-kit 1.9.10
- Based on Fedora: jack-audio-connection-kit-1.9.10-2.fc23.src.rpm
