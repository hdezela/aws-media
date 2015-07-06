%global            _hardened_build 1
#%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
#%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary:           Validating, recursive, and caching DNS(SEC) resolver
Name:              unbound
Version:           1.5.1
Release:           1%{?dist}
License:           BSD
Url:               http://www.nlnetlabs.nl/unbound/
Source0:           http://www.unbound.net/downloads/%{name}-%{version}.tar.gz
Source1:           unbound.init
Source2:           unbound.conf
Source3:           unbound.munin
Source4:           unbound_munin_
Source5:           root.key
Source6:           dlv.isc.org.key
Source9:           example.com.key
Source10:          example.com.conf
Source11:          block-example.com.conf
Source12:          icannbundle.pem
Source13:          root.anchor
Source14:          unbound.sysconfig
Source15:          unbound.cron
Source16:          unbound-munin.README
Patch1:            unbound-1.5.1-getauxval.patch
Group:             System Environment/Daemons
BuildRequires:     flex
BuildRequires:     openssl-devel
BuildRequires:     libevent-devel
BuildRequires:     expat-devel
Requires:          %{name}-libs = %{version}-%{release}
BuildRequires:     python27-devel
BuildRequires:     swig
Requires(post):    chkconfig
Requires(preun):   chkconfig
Requires(preun):   initscripts
Requires(postun):  initscripts
Requires(pre):     shadow-utils
Obsoletes:         dnssec-conf < 1.27-2
Provides:          dnssec-conf = 1.27-1

%description
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

The C implementation of Unbound is developed and maintained by NLnet
Labs. It is based on ideas and algorithms taken from a java prototype
developed by Verisign labs, Nominet, Kirei and ep.net.

Unbound is designed as a set of modular components, so that also
DNSSEC (secure DNS) validation and stub-resolvers (that do not run
as a server, but are linked into an application) are easily possible.

%package munin
Summary:           Plugin for the munin / munin-node monitoring package
Group:             System Environment/Daemons
Requires:          munin-node
Requires:          %{name} = %{version}-%{release}
Requires:          bc
BuildArch:         noarch

%description munin
Plugin for the munin / munin-node monitoring package

%package devel
Summary:           Development package that includes the unbound header files
Group:             Development/Libraries
Requires:          %{name}-libs = %{version}-%{release}
Requires:          openssl-devel

%description devel
The devel package contains the unbound library and the include files

%package libs
Summary:           Libraries used by the unbound server and client applications
Group:             Applications/System
Requires(post):    /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
Requires:          openssl
Requires:          crontabs

%description libs
Contains libraries used by the unbound server and client applications

%package python
Summary:           Python modules and extensions for unbound
Group:             Applications/System
Requires:          %{name}-libs = %{version}-%{release}

%description python
Python modules and extensions for unbound

%prep
%setup -q 
%patch1 -p1 

%build
export LDFLAGS="$LDFLAGS -Wl,-z,now,-z,relro -pie"
export CFLAGS="$RPM_OPT_FLAGS -fPIE -pie"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIE -pie"
%configure  \
  --with-libevent \
  --with-pthreads \
  --with-ssl \
  --disable-rpath \
  --disable-static \
  --with-conf-file=%{_sysconfdir}/%{name}/unbound.conf \
  --with-pidfile=%{_localstatedir}/run/%{name}/%{name}.pid \
  --with-pythonmodule \
  --with-pyunbound \
  --enable-sha2 \
  --disable-gost \
  --enable-ecdsa \
  --with-rootkey-file=%{_sharedstatedir}/unbound/root.key

%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} streamtcp

%install
rm -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
install -d 0755 %{buildroot}%{_initrddir} %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/unbound
install -p -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/unbound
install -p -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/unbound
install -p -m 0644 %{SOURCE14}  %{buildroot}%{_sysconfdir}/sysconfig/unbound
install -d 0755 %{buildroot}%{_sysconfdir}/cron.d %{buildroot}%{_sharedstatedir}/unbound
install -p -m 0755 %{SOURCE15}   %{buildroot}%{_sysconfdir}/cron.d/unbound-anchor
install -d 0755 %{buildroot}%{_sysconfdir}/munin/plugin-conf.d
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/unbound
install -d 0755 %{buildroot}%{_datadir}/munin/plugins/
install -p -m 0755 %{SOURCE4} %{buildroot}%{_datadir}/munin/plugins/unbound

for plugin in unbound_munin_hits unbound_munin_queue unbound_munin_memory unbound_munin_by_type unbound_munin_by_class unbound_munin_by_opcode unbound_munin_by_rcode unbound_munin_by_flags unbound_munin_histogram; do
    ln -s unbound %{buildroot}%{_datadir}/munin/plugins/$plugin
done 

install -p -m 0755 streamtcp %{buildroot}%{_sbindir}/unbound-streamtcp
install -p -m 0644 %{SOURCE13} %{buildroot}%{_sharedstatedir}/unbound/root.anchor
install -p -m 0644 %{SOURCE5} %{SOURCE6} %{SOURCE13} %{buildroot}%{_sysconfdir}/unbound/
rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{python_sitearch}/*/*.la

for mpage in ub_ctx ub_result ub_ctx_create ub_ctx_delete ub_ctx_set_option ub_ctx_get_option ub_ctx_config ub_ctx_set_fwd ub_ctx_resolvconf ub_ctx_hosts ub_ctx_add_ta ub_ctx_add_ta_file ub_ctx_trustedkeys ub_ctx_debugout ub_ctx_debuglevel ub_ctx_async ub_poll ub_wait ub_fd ub_process ub_resolve ub_resolve_async ub_cancel ub_resolve_free ub_strerror ub_ctx_print_local_zones ub_ctx_zone_add ub_ctx_zone_remove ub_ctx_data_add ub_ctx_data_remove;
do
  echo ".so man3/libunbound.3" > %{buildroot}%{_mandir}/man3/$mpage ;
done

mkdir -p %{buildroot}%{_localstatedir}/run/unbound

mkdir -p %{buildroot}%{_sysconfdir}/unbound/{keys.d,conf.d,local.d}
install -p %{SOURCE9} %{buildroot}%{_sysconfdir}/unbound/keys.d/
install -p %{SOURCE10} %{buildroot}%{_sysconfdir}/unbound/conf.d/
install -p %{SOURCE11} %{buildroot}%{_sysconfdir}/unbound/local.d/

echo ".so man8/unbound-control.8" > %{buildroot}/%{_mandir}/man8/unbound-control-setup.8

install -p -m 0644 %{SOURCE16}  .

%files 
%doc doc/README doc/CREDITS doc/LICENSE doc/FEATURES
%attr(0755,root,root) %{_initrddir}/%{name}
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%ghost %attr(0755,unbound,unbound) %dir %{_localstatedir}/run/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/unbound.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %attr(0755,root,unbound) %{_sysconfdir}/%{name}/keys.d
%attr(0664,root,unbound) %config(noreplace) %{_sysconfdir}/%{name}/keys.d/*.key
%dir %attr(0755,root,unbound) %{_sysconfdir}/%{name}/conf.d
%attr(0664,root,unbound) %config(noreplace) %{_sysconfdir}/%{name}/conf.d/*.conf
%dir %attr(0755,root,unbound) %{_sysconfdir}/%{name}/local.d
%attr(0664,root,unbound) %config(noreplace) %{_sysconfdir}/%{name}/local.d/*.conf

%{_sbindir}/unbound
%{_sbindir}/unbound-checkconf
%{_sbindir}/unbound-control
%{_sbindir}/unbound-control-setup
%{_sbindir}/unbound-host
%{_sbindir}/unbound-streamtcp

%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files python
%{python_sitearch}/*
%doc libunbound/python/examples/*
%doc pythonmod/examples/*

%files munin
%config(noreplace) %{_sysconfdir}/munin/plugin-conf.d/unbound
%{_datadir}/munin/plugins/unbound*
%doc unbound-munin.README

%files devel
%{_libdir}/libunbound.so
%{_includedir}/unbound.h
%{_mandir}/man3/*
%doc README

%files libs
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%{_sbindir}/unbound-anchor
%{_libdir}/libunbound.so.*
%{_sysconfdir}/%{name}/icannbundle.pem
%attr(0644,root,root) %{_sysconfdir}/cron.d/unbound-anchor
%attr(0755,unbound,unbound) %dir %{_sharedstatedir}/%{name}
%attr(0644,unbound,unbound) %config(noreplace) %{_sharedstatedir}/%{name}/root.anchor
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/root.key
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/dlv.isc.org.key
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/root.anchor
%doc doc/README doc/LICENSE

%pre libs
getent group unbound >/dev/null || groupadd -r unbound
getent passwd unbound >/dev/null || \
useradd -r -g unbound -d %{_sysconfdir}/unbound -s /sbin/nologin \
-c "Unbound DNS resolver" unbound || exit 0

%post
/sbin/chkconfig --add %{name}
sed -i "s:/etc/pki/dnssec-keys[/]*dlv:/etc/unbound:" %{_sysconfdir}/unbound/unbound.conf

%post libs 
/sbin/ldconfig
/sbin/runuser --command="%{_sbindir}/unbound-anchor -a %{_sharedstatedir}/unbound/root.key -c %{_sysconfdir}/unbound/icannbundle.pem"  --shell /bin/sh unbound || exit 0

%preun
if [ "$1" -eq 0 ]; then
        /sbin/service %{name} stop >/dev/null 2>&1
        /sbin/chkconfig --del %{name} 
fi

%postun 
if [ "$1" -ge "1" ]; then
  /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi

%postun libs -p /sbin/ldconfig

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with unbound 1.5.1
- Based on CentOS: unbound-1.5.1-1.el6.src
