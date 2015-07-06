%global cups_serverbin %{_exec_prefix}/lib/cups
%global _tmpfilesdir /etc/tmpfiles.d

Summary:        CUPS printing system
Name:           cups
Epoch:          1
Version:        2.0.3
Release:        1%{?dist}
License:        GPLv2
Url:            http://www.cups.org/
Source0:        http://www.cups.org/software/%{version}/cups-%{version}-source.tar.bz2
Source2:        cupsprinter.png
Source6:        cups.logrotate
Source7:        ncp.backend
Source8:        macros.cups
Patch1:         cups-no-gzip-man.patch
Patch2:         cups-system-auth.patch
Patch3:         cups-multilib.patch
Patch4:         cups-str4538.patch
Patch5:         cups-banners.patch
Patch6:         cups-serverbin-compat.patch
Patch7:         cups-no-export-ssllibs.patch
Patch8:         cups-direct-usb.patch
Patch9:         cups-lpr-help.patch
Patch10:        cups-peercred.patch
Patch11:        cups-pid.patch
Patch12:        cups-eggcups.patch
Patch13:        cups-driverd-timeout.patch
Patch14:        cups-strict-ppd-line-length.patch
Patch15:        cups-logrotate.patch
Patch16:        cups-usb-paperout.patch
Patch17:        cups-res_init.patch
Patch18:        cups-filter-debug.patch
Patch19:        cups-uri-compat.patch
Patch20:        cups-str3382.patch
Patch21:        cups-0755.patch
Patch22:        cups-hp-deviceid-oid.patch
Patch23:        cups-dnssd-deviceid.patch
Patch24:        cups-ricoh-deviceid-oid.patch
Patch26:        cups-str4646.patch
Patch27:        cups-avahi-address.patch
Patch28:        cups-enum-all.patch
Patch29:        cups-dymo-deviceid.patch
Patch30:        cups-freebind.patch
Patch31:        cups-no-gcry.patch
Patch32:        cups-libusb-quirks.patch
Patch33:        cups-use-ipp1.1.patch
Patch34:        cups-avahi-no-threaded.patch
Patch35:        cups-ipp-multifile.patch
Patch36:        cups-web-devices-timeout.patch
Patch37:        cups-journal.patch
Patch38:        cups-synconclose.patch
Requires:       %{name}-filesystem = %{epoch}:%{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-client%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       cupsddk
Provides:       cupsddk-drivers
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  gnutls-devel
BuildRequires:  libacl-devel
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  krb5-devel
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  automake
Requires:       dbus
Requires(post): grep
Requires(post): sed
Requires:       acl
Requires:       ghostscript-cups
Requires:       cups-filters

%package client
Summary:        CUPS printing system - client programs
License:        GPLv2
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       /usr/bin/lpq /usr/bin/lpr /usr/bin/lp /usr/bin/cancel /usr/bin/lprm /usr/bin/lpstat
Requires:       /usr/sbin/alternatives
Provides:       lpr

%package devel
Summary:        CUPS printing system - development environment
License:        LGPLv2
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnutls-devel
Requires:       krb5-devel
Requires:       zlib-devel
Provides:       cupsddk-devel

%package libs
Summary:        CUPS printing system - libraries
License:        LGPLv2 and zlib

%package filesystem
Summary:        CUPS printing system - directory layout
BuildArch:      noarch

%package lpd
Summary:        CUPS printing system - lpd emulation
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       lpd

%package ipptool
Summary:        CUPS printing system - tool for performing IPP requests
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description
CUPS printing system provides a portable printing layer for
UNIX® operating systems. It has been developed by Apple Inc.
to promote a standard printing solution for all UNIX vendors and users.
CUPS provides the System V and Berkeley command-line interfaces.

%description client
CUPS printing system provides a portable printing layer for
UNIX® operating systems. This package contains command-line client
programs.

%description devel
CUPS printing system provides a portable printing layer for
UNIX® operating systems. This is the development package for creating
additional printer drivers, and other CUPS services.

%description libs
CUPS printing system provides a portable printing layer for
UNIX® operating systems. It has been developed by Apple Inc.
to promote a standard printing solution for all UNIX vendors and users.
CUPS provides the System V and Berkeley command-line interfaces.
The cups-libs package provides libraries used by applications to use CUPS
natively, without needing the lp/lpr commands.

%description filesystem
CUPS printing system provides a portable printing layer for
UNIX® operating systems. This package provides some directories which are
required by other packages that add CUPS drivers (i.e. filters, backends etc.).

%description lpd
CUPS printing system provides a portable printing layer for
UNIX® operating systems. This is the package that provides standard
lpd emulation.

%description ipptool
Sends IPP requests to the specified URI and tests and/or displays the results.

%prep
%setup -q
%patch1 -p1 -b .no-gzip-man
%patch2 -p1 -b .system-auth
%patch3 -p1 -b .multilib
%patch4 -p1 -b .str4538
%patch5 -p1 -b .banners
%patch6 -p1 -b .serverbin-compat
%patch7 -p1 -b .no-export-ssllibs
%patch8 -p1 -b .direct-usb
%patch9 -p1 -b .lpr-help
%patch10 -p1 -b .peercred
%patch11 -p1 -b .pid
%patch12 -p1 -b .eggcups
%patch13 -p1 -b .driverd-timeout
%patch14 -p1 -b .strict-ppd-line-length
%patch15 -p1 -b .logrotate
%patch16 -p1 -b .usb-paperout
%patch17 -p1 -b .res_init
%patch18 -p1 -b .filter-debug
%patch19 -p1 -b .uri-compat
%patch20 -p1 -b .str3382
%patch21 -p1 -b .0755
%patch22 -p1 -b .hp-deviceid-oid
%patch23 -p1 -b .dnssd-deviceid
%patch24 -p1 -b .ricoh-deviceid-oid
%patch26 -p1 -b .str4646
%patch27 -p1 -b .avahi-address
%patch28 -p1 -b .enum-all
%patch29 -p1 -b .dymo-deviceid
%patch30 -p1 -b .freebind
%patch31 -p1 -b .no-gcry
%patch32 -p1 -b .libusb-quirks
%patch33 -p1 -b .use-ipp1.1
%patch34 -p1 -b .avahi-no-threaded
%patch35 -p1 -b .ipp-multifile
%patch36 -p1 -b .web-devices-timeout
%patch37 -p1 -b .journal
%patch38 -p1 -b .synconclose

sed -i -e '1iMaxLogSize 0' conf/cupsd.conf.in
sed -i -e 's,^ErrorLog .*$,ErrorLog journal,' conf/cups-files.conf.in

perl -pi -e "s,^.SILENT:,," Makedefs.in

f=CREDITS.txt
mv "$f" "$f"~
iconv -f MACINTOSH -t UTF-8 "$f"~ > "$f"
rm -f "$f"~

aclocal -I config-scripts
autoconf -I config-scripts

%build
export CFLAGS="$RPM_OPT_FLAGS -fstack-protector-all -DLDAP_DEPRECATED=1"
%configure --with-docdir=%{_datadir}/%{name}/www --enable-debug \
  --with-cupsd-file-perm=0755 \
  --with-log-file-perm=0600 \
  --enable-relro \
  --with-dbusdir=%{_sysconfdir}/dbus-1 \
  --with-php=/usr/bin/php-cgi \
  --enable-avahi \
  --enable-threads \
  --enable-gnutls \
  --enable-webif \
  --with-xinetd=no \
  --disable-systemd \
  localedir=%{_datadir}/locale

make %{?_smp_mflags}

%install
make BUILDROOT=$RPM_BUILD_ROOT install 

find $RPM_BUILD_ROOT%{_datadir}/cups/model -name "*.ppd" |xargs gzip -n9f

pushd $RPM_BUILD_ROOT%{_bindir}
for i in cancel lp lpq lpr lprm lpstat; do
	mv $i $i.cups
done
cd $RPM_BUILD_ROOT%{_sbindir}
mv lpc lpc.cups
cd $RPM_BUILD_ROOT%{_mandir}/man1
for i in cancel lp lpq lpr lprm lpstat; do
	mv $i.1 $i-cups.1
done
cd $RPM_BUILD_ROOT%{_mandir}/man8
mv lpc.8 lpc-cups.8
popd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps $RPM_BUILD_ROOT%{_sysconfdir}/X11/sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/System $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/cups
install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{cups_serverbin}/backend/ncp

mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d
install -m 0644 %{SOURCE8} $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d

touch $RPM_BUILD_ROOT%{_sysconfdir}/cups/printers.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/cups/classes.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/cups/client.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/cups/subscriptions.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/cups/lpoptions

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ppd

rm -rf $RPM_BUILD_ROOT%{_mandir}/cat? $RPM_BUILD_ROOT%{_mandir}/*/cat?
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/cups.desktop
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons
rm -rf $RPM_BUILD_ROOT%{_datadir}/cups/banners
rm -f $RPM_BUILD_ROOT%{_datadir}/cups/data/testprint

mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
cat > ${RPM_BUILD_ROOT}%{_tmpfilesdir}/cups.conf <<EOF

d /run/cups 0755 root lp -
d /run/cups/certs 0511 lp sys -

d /var/spool/cups/tmp - - - 30d
EOF

cat > ${RPM_BUILD_ROOT}%{_tmpfilesdir}/cups-lp.conf <<EOF

c /dev/lp0 0660 root lp - 6:0
c /dev/lp1 0660 root lp - 6:1
c /dev/lp2 0660 root lp - 6:2
c /dev/lp3 0660 root lp - 6:3
EOF

find $RPM_BUILD_ROOT -type f -o -type l | sed '
s:.*\('%{_datadir}'/\)\([^/_]\+\)\(.*\.po$\):%lang(\2) \1\2\3:
/^%lang(C)/d
/^\([^%].*\)/d
' > %{name}.lang

%post
rm -rf %{_sysconfdir}/cups/certs
rm -f %{_localstatedir}/cache/cups/*.ipp %{_localstatedir}/cache/cups/*.cache
FILE=%{_sysconfdir}/cups/cups-files.conf
for keyword in PageLogFormat; do
    /bin/sed -i -e "s,^$keyword,#$keyword,i" "$FILE" || :
done

exit 0

%post client
/usr/sbin/alternatives --install %{_bindir}/lpr print %{_bindir}/lpr.cups 40 \
	 --slave %{_bindir}/lp print-lp %{_bindir}/lp.cups \
	 --slave %{_bindir}/lpq print-lpq %{_bindir}/lpq.cups \
	 --slave %{_bindir}/lprm print-lprm %{_bindir}/lprm.cups \
	 --slave %{_bindir}/lpstat print-lpstat %{_bindir}/lpstat.cups \
	 --slave %{_bindir}/cancel print-cancel %{_bindir}/cancel.cups \
	 --slave %{_sbindir}/lpc print-lpc %{_sbindir}/lpc.cups \
	 --slave %{_mandir}/man1/cancel.1.gz print-cancelman %{_mandir}/man1/cancel-cups.1.gz \
	 --slave %{_mandir}/man1/lp.1.gz print-lpman %{_mandir}/man1/lp-cups.1.gz \
	 --slave %{_mandir}/man8/lpc.8.gz print-lpcman %{_mandir}/man8/lpc-cups.8.gz \
	 --slave %{_mandir}/man1/lpq.1.gz print-lpqman %{_mandir}/man1/lpq-cups.1.gz \
	 --slave %{_mandir}/man1/lpr.1.gz print-lprman %{_mandir}/man1/lpr-cups.1.gz \
	 --slave %{_mandir}/man1/lprm.1.gz print-lprmman %{_mandir}/man1/lprm-cups.1.gz \
	 --slave %{_mandir}/man1/lpstat.1.gz print-lpstatman %{_mandir}/man1/lpstat-cups.1.gz
exit 0

%post lpd

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%preun

%preun client
if [ $1 -eq 0 ] ; then
	/usr/sbin/alternatives --remove print %{_bindir}/lpr.cups
fi
exit 0

%preun lpd

%postun

%postun lpd

%triggerin -- samba-client
ln -sf ../../../bin/smbspool %{cups_serverbin}/backend/smb || :
exit 0

%triggerun -- samba-client
[ $2 = 0 ] || exit 0
rm -f %{cups_serverbin}/backend/smb

%triggerin -- samba4-client
ln -sf %{_bindir}/smbspool %{cups_serverbin}/backend/smb || :
exit 0

%triggerun -- samba4-client
[ $2 = 0 ] || exit 0
rm -f %{cups_serverbin}/backend/smb

%files -f %{name}.lang
%doc README.txt CREDITS.txt CHANGES.txt
%dir %attr(0755,root,lp) %{_sysconfdir}/cups
%dir %attr(0755,root,lp) %{_localstatedir}/run/cups
%dir %attr(0511,lp,sys) %{_localstatedir}/run/cups/certs
%{_tmpfilesdir}/cups.conf
%{_tmpfilesdir}/cups-lp.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0640,root,lp) %{_sysconfdir}/cups/cupsd.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0640,root,lp) %{_sysconfdir}/cups/cups-files.conf
%attr(0640,root,lp) %{_sysconfdir}/cups/cupsd.conf.default
%verify(not md5 size mtime) %config(noreplace) %attr(0644,root,lp) %{_sysconfdir}/cups/client.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0600,root,lp) %{_sysconfdir}/cups/classes.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0600,root,lp) %{_sysconfdir}/cups/printers.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0644,root,lp) %{_sysconfdir}/cups/snmp.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0644,root,lp) %{_sysconfdir}/cups/subscriptions.conf
%{_sysconfdir}/cups/interfaces
%verify(not md5 size mtime) %config(noreplace) %attr(0644,root,lp) %{_sysconfdir}/cups/lpoptions
%dir %attr(0755,root,lp) %{_sysconfdir}/cups/ppd
%dir %attr(0700,root,lp) %{_sysconfdir}/cups/ssl
%config(noreplace) %{_sysconfdir}/pam.d/cups
%config(noreplace) %{_sysconfdir}/logrotate.d/cups
%dir %{_datadir}/%{name}/www
%dir %{_datadir}/%{name}/www/de
%dir %{_datadir}/%{name}/www/es
%dir %{_datadir}/%{name}/www/ja
%dir %{_datadir}/%{name}/www/ru
%{_datadir}/%{name}/www/images
%{_datadir}/%{name}/www/*.css
%doc %{_datadir}/%{name}/www/index.html
%doc %{_datadir}/%{name}/www/help
%doc %{_datadir}/%{name}/www/robots.txt
%doc %{_datadir}/%{name}/www/de/index.html
%doc %{_datadir}/%{name}/www/es/index.html
%doc %{_datadir}/%{name}/www/ja/index.html
%doc %{_datadir}/%{name}/www/ru/index.html
%doc %{_datadir}/%{name}/www/apple-touch-icon.png
%dir %{_datadir}/%{name}/usb
%{_datadir}/%{name}/usb/org.cups.usb-quirks
%{_bindir}/cupstestppd
%{_bindir}/cupstestdsc
%{_bindir}/ppd*
%{cups_serverbin}/backend/*
%{cups_serverbin}/cgi-bin
%dir %{cups_serverbin}/daemon
%{cups_serverbin}/daemon/cups-deviced
%{cups_serverbin}/daemon/cups-driverd
%{cups_serverbin}/daemon/cups-exec
%{cups_serverbin}/notifier
%{cups_serverbin}/filter/*
%{cups_serverbin}/monitor
%{_mandir}/man[1578]/*
%exclude %{_mandir}/man1/lp*.1.gz
%exclude %{_mandir}/man1/cancel-cups.1.gz
%exclude %{_mandir}/man8/lpc-cups.8.gz
%exclude %{_mandir}/man1/cups-config.1.gz
%exclude %{_mandir}/man1/ipptool.1.gz
%exclude %{_mandir}/man5/ipptoolfile.5.gz
%exclude %{_mandir}/man8/cups-lpd.8.gz
%{_sbindir}/*
%exclude %{_sbindir}/lpc.cups
%dir %{_datadir}/cups/templates
%dir %{_datadir}/cups/templates/de
%dir %{_datadir}/cups/templates/es
%dir %{_datadir}/cups/templates/ja
%dir %{_datadir}/cups/templates/ru
%{_datadir}/cups/templates/*.tmpl
%{_datadir}/cups/templates/de/*.tmpl
%{_datadir}/cups/templates/es/*.tmpl
%{_datadir}/cups/templates/ja/*.tmpl
%{_datadir}/cups/templates/ru/*.tmpl
%dir %attr(1770,root,lp) %{_localstatedir}/spool/cups/tmp
%dir %attr(0710,root,lp) %{_localstatedir}/spool/cups
%dir %attr(0755,lp,sys) %{_localstatedir}/log/cups
%{_datadir}/pixmaps/cupsprinter.png
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/cups.conf
%{_datadir}/cups/drv/sample.drv
%{_datadir}/cups/examples
%{_datadir}/cups/mime/mime.types
%{_datadir}/cups/mime/mime.convs
%{_datadir}/cups/ppdc/*.defs
%{_datadir}/cups/ppdc/*.h
%{_sysconfdir}/init.d
%{_sysconfdir}/rc?.d

%files client
%{_sbindir}/lpc.cups
%{_bindir}/cancel*
%{_bindir}/lp*
%{_mandir}/man1/lp*.1.gz
%{_mandir}/man1/cancel-cups.1.gz
%{_mandir}/man8/lpc-cups.8.gz

%files libs
%doc LICENSE.txt
%{_libdir}/*.so.*

%files filesystem
%dir %{cups_serverbin}
%dir %{cups_serverbin}/backend
%dir %{cups_serverbin}/driver
%dir %{cups_serverbin}/filter
%dir %{_datadir}/cups
%dir %{_datadir}/cups/data
%dir %{_datadir}/cups/drv
%dir %{_datadir}/cups/mime
%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/ppdc
%dir %{_datadir}/ppd

%files devel
%{_bindir}/cups-config
%{_libdir}/*.so
%{_includedir}/cups
%{_mandir}/man1/cups-config.1.gz
%{_rpmconfigdir}/macros.d/macros.cups

%files lpd
%{cups_serverbin}/daemon/cups-lpd
%{_mandir}/man8/cups-lpd.8.gz

%files ipptool
%{_bindir}/ipptool
%{_bindir}/ippfind
%dir %{_datadir}/cups/ipptool
%{_datadir}/cups/ipptool/*
%{_mandir}/man1/ipptool.1.gz
%{_mandir}/man5/ipptoolfile.5.gz

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Systemd support disabled
- Lspp disabled

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with cups 2.0.3
- Based on Fedora: cups-2.0.3-3.fc23.src.rpm
