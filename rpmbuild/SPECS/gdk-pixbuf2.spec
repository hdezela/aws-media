Name:              gdk-pixbuf2
Version:           2.28.2
Release:           1%{?dist}
Summary:           An image loading library
Group:             System Environment/Libraries
License:           LGPLv2+
URL:               http://www.gt.org
Source0:           http://download.gnome.org/sources/gdk-pixbuf/2.28/gdk-pixbuf-%{version}.tar.xz
Patch0:            0001-Make-update-cache-work-better.patch
BuildRequires:     glib2-devel >= 2.34.0
BuildRequires:     libpng-devel
BuildRequires:     libjpeg-devel
BuildRequires:     libtiff-devel
BuildRequires:     jasper-devel
BuildRequires:     libX11-devel
BuildRequires:     gobject-introspection-devel >= 0.9.3
BuildRequires:     shared-mime-info
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     libtool
BuildRequires:     gtk-doc
BuildRequires:     gettext-autopoint
Requires:          glib2 >= 2.34.0
Requires:          shared-mime-info
Conflicts:         gtk2 <= 2.21.2

%description
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
clutter.

%package devel
Summary:           Development files for gdk-pixbuf
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}
Requires:          glib2-devel >= 2.34.0
Conflicts:         gtk2-devel <= 2.21.2

%description devel
This package contains the libraries and header files that are needed
for writing applications that are using gdk-pixbuf.

%prep
%setup -q -n gdk-pixbuf-%{version}
%patch0 -p1

%build
(if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; CONFIGFLAGS=--enable-gtk-doc; fi;
 %configure $CONFIGFLAGS             \
        --with-x11                   \
        --with-libjasper             \
        --with-included-loaders=png  )
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT    \
             RUN_QUERY_LOADER_TEST=false

rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.la

touch $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache

(cd $RPM_BUILD_ROOT%{_bindir}
 mv gdk-pixbuf-query-loaders gdk-pixbuf-query-loaders-%{__isa_bits}
)

%find_lang gdk-pixbuf

%post
/sbin/ldconfig
gdk-pixbuf-query-loaders-%{__isa_bits} --update-cache || :

%postun
/sbin/ldconfig
if [ $1 -gt 0 ]; then
  gdk-pixbuf-query-loaders-%{__isa_bits} --update-cache || :
fi

%files -f gdk-pixbuf.lang
%doc AUTHORS COPYING NEWS
%{_libdir}/libgdk_pixbuf-2.0.so.*
%{_libdir}/libgdk_pixbuf_xlib-2.0.so.*
%{_libdir}/girepository-1.0
%dir %{_libdir}/gdk-pixbuf-2.0
%dir %{_libdir}/gdk-pixbuf-2.0/2.10.0
%dir %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.so
%ghost %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
%{_bindir}/gdk-pixbuf-query-loaders-%{__isa_bits}
%{_mandir}/man1/gdk-pixbuf-query-loaders.1*

%files devel
%{_includedir}/gdk-pixbuf-2.0
%{_libdir}/libgdk_pixbuf-2.0.so
%{_libdir}/libgdk_pixbuf_xlib-2.0.so
%{_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{_libdir}/pkgconfig/gdk-pixbuf-xlib-2.0.pc
%{_bindir}/gdk-pixbuf-csource
%{_bindir}/gdk-pixbuf-pixdata
%{_datadir}/gir-1.0
%{_datadir}/gtk-doc/html/*
%{_mandir}/man1/gdk-pixbuf-csource.1*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with gdk-pixbuf 2.28.2 
- Based on CentOS: gdk-pixbuf2-2.28.2-4.el7.src
