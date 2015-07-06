Name:              p11-kit
Version:           0.23.1
Release:           1%{?dist}
Summary:           Library for loading and sharing PKCS#11 modules
License:           BSD
URL:               http://p11-glue.freedesktop.org/p11-kit.html
Source0:           http://p11-glue.freedesktop.org/releases/p11-kit-%{version}.tar.gz
Source1:           trust-extract-compat
BuildRequires:     libtasn1-devel >= 2.3
BuildRequires:     nss-softokn-freebl
BuildRequires:     libffi-devel
BuildRequires:     gtk-doc

%description
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that theyre discoverable.

%package devel
Summary:           Development files for %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package trust
Summary:           System trust module from %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires(post):    %{_sbindir}/update-alternatives
Requires(postun):  %{_sbindir}/update-alternatives
Conflicts:         nss < 3.14.3-9

%description trust
The %{name}-trust package contains a system trust PKCS#11 module which
contains certificate anchors and black lists.

%define alt_ckbi  libnssckbi.so.%{_arch}

%prep
%setup -q

%build
%configure --disable-static --enable-doc --with-trust-paths=%{_sysconfdir}/pki/ca-trust/source:%{_datadir}/pki/ca-trust-source --with-hash-impl=freebl --disable-silent-rules
make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pkcs11/modules
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/pkcs11/*.la
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/p11-kit/
rm $RPM_BUILD_ROOT%{_sysconfdir}/pkcs11/pkcs11.conf.example

%check
make check

%post -p /sbin/ldconfig

%post trust
%{_sbindir}/update-alternatives --install %{_libdir}/libnssckbi.so \
        %{alt_ckbi} %{_libdir}/pkcs11/p11-kit-trust.so 30

%postun -p /sbin/ldconfig

%postun trust
if [ $1 -eq 0 ] ; then
        # package removal
        %{_sbindir}/update-alternatives --remove %{alt_ckbi} %{_libdir}/pkcs11/p11-kit-trust.so
fi

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS README
%doc p11-kit/pkcs11.conf.example
%dir %{_sysconfdir}/pkcs11
%dir %{_sysconfdir}/pkcs11/modules
%dir %{_datadir}/p11-kit
%dir %{_datadir}/p11-kit/modules
%dir %{_libdir}/p11-kit
%{_bindir}/p11-kit
%{_libdir}/libp11-kit.so.*
%{_libdir}/p11-kit-proxy.so
%{_libdir}/p11-kit/p11-kit-remote
%{_mandir}/man1/trust.1.gz
%{_mandir}/man8/p11-kit.8.gz
%{_mandir}/man5/pkcs11.conf.5.gz

%files devel
%{_includedir}/p11-kit-1/
%{_libdir}/libp11-kit.so
%{_libdir}/pkgconfig/p11-kit-1.pc
%doc %{_datadir}/gtk-doc/

%files trust
%{_bindir}/trust
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/p11-kit-trust.so
%{_datadir}/p11-kit/modules/p11-kit-trust.module
%{_libdir}/p11-kit/trust-extract-compat

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with p11-kit 0.23.1
- Based on Fedora: p11-kit-0.23.1-3.fc23.src
