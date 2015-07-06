Name:          libvdpau
Version:       1.1
Release:       1%{?dist}
Summary:       Wrapper library for the Video Decode and Presentation API
License:       MIT
URL:           http://freedesktop.org/wiki/Software/VDPAU
Source0:       http://cgit.freedesktop.org/~aplattner/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libtool
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: tetex-latex
BuildRequires: xorg-x11-proto-devel

%description
VDPAU is the Video Decode and Presentation API for UNIX. It provides an
interface to video decode acceleration and presentation hardware present in
modern GPUs.

%package docs
Summary:       Documentation for %{name}
BuildArch:     noarch
Provides:      libvdpau-docs = %{version}-%{release}
Obsoletes:     libvdpau-docs < 0.6-2

%description docs
The %{name}-docs package contains documentation for %{name}.

%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      libX11-devel
Requires:      pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%setup -q

%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -delete
rm -fr %{buildroot}%{_docdir}
mv doc/html-out html

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING
%config(noreplace) %{_sysconfdir}/vdpau_wrapper.cfg
%{_libdir}/*.so.*
%dir %{_libdir}/vdpau
%{_libdir}/vdpau/%{name}_trace.so*

%files docs
%doc html

%files devel
%{_includedir}/vdpau/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/vdpau.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libvdpau 1.1
- Based on Fedora: libvdpau-1.1-3.fc23.src
