Name:              librsvg2
Summary:           An SVG library based on cairo
Version:           2.40.9
Release:           1%{?dist}
License:           LGPLv2+
Group:             System Environment/Libraries
URL:               https://wiki.gnome.org/Projects/LibRsvg
Source0:           http://download.gnome.org/sources/librsvg/2.40/librsvg-%{version}.tar.xz
BuildRequires:     pkgconfig(cairo)
BuildRequires:     pkgconfig(cairo-png)
BuildRequires:     pkgconfig(gdk-pixbuf-2.0)
BuildRequires:     pkgconfig(gio-2.0)
BuildRequires:     pkgconfig(gobject-introspection-1.0)
#BuildRequires:     pkgconfig(gtk+-3.0)
BuildRequires:     pkgconfig(libxml-2.0)
BuildRequires:     pkgconfig(libcroco-0.6)
BuildRequires:     pkgconfig(pangocairo)
Requires(post):    gdk-pixbuf2%{?_isa}
Requires(postun):  gdk-pixbuf2%{?_isa}
Provides:          librsvg3 = %{name}.%{version}-%{release}
Obsoletes:         librsvg3 <= 2.26.3-3.fc14

%description
An SVG library based on cairo.

%package devel
Summary:           Libraries and include files for developing with librsvg
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}
Provides:          librsvg3-devel = %{name}.%{version}-%{release}
Obsoletes:         librsvg3-devel <= 2.26.3-3.fc14

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%package tools
Summary:           Extra tools for librsvg
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description tools
This package provides extra utilities based on the librsvg library.

%prep
%setup -q -n librsvg-%{version}

%build
GDK_PIXBUF_QUERYLOADERS=/usr/bin/gdk-pixbuf-query-loaders-%{__isa_bits}
export GDK_PIXBUF_QUERYLOADERS
enable_pixbuf_loader=yes
export enable_pixbuf_loader
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"
%configure \
  --disable-static \
  --disable-gtk-doc \
  --disable-introspection \
  --without-gtk+

sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

rm -f $RPM_BUILD_ROOT%{_libdir}/mozilla/
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/svg-viewer.svg

%post
/sbin/ldconfig
gdk-pixbuf-query-loaders-%{__isa_bits} --update-cache || :

%postun
/sbin/ldconfig
gdk-pixbuf-query-loaders-%{__isa_bits} --update-cache || :

%files
%doc AUTHORS NEWS README
%license COPYING COPYING.LIB
%{_libdir}/librsvg-2.so.*
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-svg.so

%files devel
%{_libdir}/librsvg-2.so
%{_includedir}/librsvg-2.0
%{_libdir}/pkgconfig/librsvg-2.0.pc
%doc %{_datadir}/gtk-doc/html/rsvg-2.0

%files tools
%{_bindir}/rsvg-convert
%{_mandir}/man1/rsvg-convert.1*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Disabled introspection

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libsrvg2 2.40.9
- Based on Fedora: librsvg2-2.40.9-1.fc23.src.rpm
