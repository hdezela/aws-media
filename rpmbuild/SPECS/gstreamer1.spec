%global         majorminor              1.0
%global         _glib2                  2.32.0
%global         _libxml2                2.4.0
%global         _gobject_introspection  1.31.1

Name:           gstreamer1
Version:        1.5.2
Release:        1%{?dist}
Summary:        GStreamer streaming media framework runtime
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz
Patch0:         gstreamer-inspect-rpm-format.patch
Source1:        gstreamer1.prov
Source2:        gstreamer1.attr
BuildRequires:  glib2-devel >= %{_glib2}
BuildRequires:  libxml2-devel >= %{_libxml2}
BuildRequires:  gobject-introspection-devel >= %{_gobject_introspection}
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  m4
BuildRequires:  check-devel
BuildRequires:  gtk-doc >= 1.3
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  chrpath
BuildRequires:  python27
BuildRequires:  openjade
BuildRequires:  jadetex
BuildRequires:  libxslt
BuildRequires:  docbook-style-dsssl
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:  transfig
BuildRequires:  netpbm-progs
BuildRequires:  tetex-dvips
BuildRequires:  ghostscript

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package devel
Summary:        Libraries/include files for GStreamer streaming media framework
Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel >= %{_glib2}
Requires:       libxml2-devel >= %{_libxml2}
Requires:       check-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package devel-docs
Summary:        Developer documentation for GStreamer streaming media framework
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description devel-docs
This %{name}-devel-docs contains developer documentation for the
GStreamer streaming media framework.

%prep
%setup -q -n gstreamer-%{version}
%patch0 -p1 -b .rpm-provides

%build
%configure \
  --with-package-name='Amazon GStreamer package' \
  --enable-gtk-doc \
  --enable-debug \
  --disable-tests --disable-examples
make %{?_smp_mflags} V=1

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libgstbase-1.0.so.*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libgstcheck-1.0.so.*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libgstcontroller-1.0.so.* 
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libgstnet-1.0.so.*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstcoreelements.so
chrpath --delete $RPM_BUILD_ROOT%{_libexecdir}/gstreamer-%{majorminor}/gst-plugin-scanner
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/gst-inspect-1.0
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/gst-launch-1.0
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/gst-typefind-1.0

%find_lang gstreamer-%{majorminor}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
install -m0755 -D %{SOURCE1} $RPM_BUILD_ROOT%{_rpmconfigdir}/gstreamer1.prov
install -m0644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/gstreamer1.attr

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f gstreamer-%{majorminor}.lang
%doc AUTHORS COPYING NEWS README RELEASE
%{_libdir}/libgstreamer-%{majorminor}.so.*
%{_libdir}/libgstbase-%{majorminor}.so.*
%{_libdir}/libgstcheck-%{majorminor}.so.*
%{_libdir}/libgstcontroller-%{majorminor}.so.*
%{_libdir}/libgstnet-%{majorminor}.so.*

%{_libexecdir}/gstreamer-%{majorminor}/

%dir %{_libdir}/gstreamer-%{majorminor}
%{_libdir}/gstreamer-%{majorminor}/libgstcoreelements.so

%{_libdir}/girepository-1.0/Gst-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstBase-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstCheck-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstController-%{majorminor}.typelib
%{_libdir}/girepository-1.0/GstNet-%{majorminor}.typelib

%{_bindir}/gst-inspect-%{majorminor}
%{_bindir}/gst-launch-%{majorminor}
%{_bindir}/gst-typefind-%{majorminor}

%{_rpmconfigdir}/gstreamer1.prov
%{_rpmconfigdir}/fileattrs/gstreamer1.attr

%doc %{_mandir}/man1/gst-inspect-%{majorminor}.*
%doc %{_mandir}/man1/gst-launch-%{majorminor}.*
%doc %{_mandir}/man1/gst-typefind-%{majorminor}.*

%{_datadir}/bash-completion/completions/gst-inspect-1.0
%{_datadir}/bash-completion/completions/gst-launch-1.0
%{_datadir}/bash-completion/helpers/gst
%{_datadir}/bash-completion/helpers/gst-completion-helper-1.0

%files devel
%dir %{_includedir}/gstreamer-%{majorminor}
%dir %{_includedir}/gstreamer-%{majorminor}/gst
%dir %{_includedir}/gstreamer-%{majorminor}/gst/base
%dir %{_includedir}/gstreamer-%{majorminor}/gst/check
%dir %{_includedir}/gstreamer-%{majorminor}/gst/controller
%dir %{_includedir}/gstreamer-%{majorminor}/gst/net
%{_includedir}/gstreamer-%{majorminor}/gst/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/base/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/check/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/controller/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/net/*.h

%{_libdir}/gstreamer-%{majorminor}/include/gst/*.h

%{_libdir}/libgstreamer-%{majorminor}.so
%{_libdir}/libgstbase-%{majorminor}.so
%{_libdir}/libgstcheck-%{majorminor}.so
%{_libdir}/libgstcontroller-%{majorminor}.so
%{_libdir}/libgstnet-%{majorminor}.so

%{_datadir}/gir-1.0/Gst-%{majorminor}.gir
%{_datadir}/gir-1.0/GstBase-%{majorminor}.gir
%{_datadir}/gir-1.0/GstCheck-%{majorminor}.gir
%{_datadir}/gir-1.0/GstController-%{majorminor}.gir
%{_datadir}/gir-1.0/GstNet-%{majorminor}.gir

%{_datadir}/aclocal/gst-element-check-%{majorminor}.m4

%{_libdir}/pkgconfig/gstreamer-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-base-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-controller-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-check-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-net-%{majorminor}.pc

%files devel-docs
%doc %{_datadir}/gtk-doc/html/gstreamer-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gstreamer-libs-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gstreamer-plugins-%{majorminor}

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with gstreamer 1.5.2
- Based on Fedora: gstreamer1-1.5.2-1.fc23.src.rpm

