Name:          rtkit
Version:       0.5
Release:       1%{?dist}
Summary:       Realtime Policy and Watchdog Daemon
Group:         System Environment/Base
License:       GPLv3+ and BSD
URL:           http://git.0pointer.de/?p=rtkit.git
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:      dbus
Requires:      polkit
BuildRequires: dbus-devel >= 1.2
BuildRequires: libcap-devel
BuildRequires: polkit-devel
Source0:       http://0pointer.de/public/%{name}-%{version}.tar.gz
Patch0:        0001-SECURITY-Pass-uid-of-caller-to-polkit.patch

%description
RealtimeKit is a D-Bus system service that changes the
scheduling policy of user processes/threads to SCHED_RR (i.e. realtime
scheduling mode) on request. It is intended to be used as a secure
mechanism to allow real-time scheduling to be used by normal user
processes.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}
./rtkit-daemon --introspect > org.freedesktop.RealtimeKit1.xml

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -D org.freedesktop.RealtimeKit1.xml $RPM_BUILD_ROOT/%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -f -r rtkit
/usr/bin/id rtkit >/dev/null 2>&1 || \
        /usr/sbin/useradd -r -g rtkit -c 'RealtimeKit' -s /sbin/nologin -d /proc rtkit
exit 0

%post
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :

%files
%defattr(0644,root,root,0755)
%doc README GPL LICENSE rtkit.c rtkit.h
%attr(0755,root,root) %{_sbindir}/rtkitctl
%attr(0755,root,root) %{_libexecdir}/rtkit-daemon
%{_datadir}/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
%{_datadir}/polkit-1/actions/org.freedesktop.RealtimeKit1.policy
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with rtkit 0.5
- Based on CentOS: rtkit-0.5-2.el6_4.src.rpm
