Name:              zeromq
Version:           4.1.2
Release:           1%{?dist}
Summary:           Software library for fast, message-based applications
Group:             System Environment/Libraries
License:           LGPLv3+
URL:               http://www.zeromq.org
Source0:           http://download.zeromq.org/zeromq-%{version}.tar.gz
Patch0:            zeromq-4.1.2-ipv6.patch
Source1:           https://raw.githubusercontent.com/zeromq/cppzmq/master/zmq.hpp
Source2:           https://raw.githubusercontent.com/zeromq/cppzmq/master/LICENSE
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     libtool
BuildRequires:     libsodium-devel
BuildRequires:     glib2-devel
BuildRequires:     libuuid-devel

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the ZeroMQ shared library.

%package devel
Summary:           Development files for %{name}
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n cppzmq-devel
Summary:           Development files for cppzmq
Group:             Development/Libraries
License:           MIT
Requires:          %{name}-devel%{?_isa} = %{version}-%{release}

%description -n cppzmq-devel
The cppzmq-devel package contains libraries and header files for
developing applications that use the C++ header files of %{name}.

%prep
%setup -q
%patch0 -p1
cp -a %{SOURCE2} .

iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

sed -i "s/libzmq_werror=\"yes\"/libzmq_werror=\"no\"/g" \
    configure

%global openpgm_pc $(basename %{_libdir}/pkgconfig/openpgm*.pc .pc)
sed -i "s/openpgm-[0-9].[0-9]/%{openpgm_pc}/g" \
    configure*

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags} V=1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -m 644 -p %{SOURCE1} %{buildroot}%{_includedir}/

rm %{buildroot}%{_libdir}/libzmq.la

%check
make check V=1

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog MAINTAINERS NEWS
%license COPYING COPYING.LESSER
%{_bindir}/curve_keygen
%{_libdir}/libzmq.so.*

%files devel
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/zmq*.h
%{_mandir}/man3/zmq*
%{_mandir}/man7/zmq*

%files -n cppzmq-devel
%license LICENSE
%{_includedir}/zmq.hpp

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with zeromq 4.1.2
- Based on Fedora: zeromq-4.1.2-1.fc23.src
