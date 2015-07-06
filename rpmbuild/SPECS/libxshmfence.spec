%define            debug_package %{nil}

Name:              libxshmfence
Version:           1.2
Release:           1%{?dist}
Summary:           X11 shared memory fences
License:           MIT
URL:               http://www.x.org/
Source0:           http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     libtool
BuildRequires:     pkgconfig(xproto)
BuildRequires:     xorg-x11-util-macros

%description
Shared memory fences for X11, as used in DRI3.

%package devel
Summary:           Development files for %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
autoreconf -v -i -f
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc
%{_libdir}/libxshmfence.so.1*

%files devel
%doc
%{_includedir}/*
%{_libdir}/pkgconfig/xshmfence.pc
%{_libdir}/*.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libxshmfence 1.2
- Based on Fedora: libxshmfence-1.2-1.fc23.src.rpm
