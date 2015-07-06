Summary:           A 2D graphics library
Name:              cairo
Version:           1.14.2
Release:           1%{?dist}
License:           LGPLv2 or MPLv1.1
Group:		    System Environment/Libraries
URL:               http://cairographics.org
Source0:           http://cairographics.org/releases/%{name}-%{version}.tar.xz
Patch3:            cairo-multilib.patch
BuildRequires:     pkgconfig
BuildRequires:     libpng-devel
BuildRequires:     libxml2-devel
BuildRequires:     pixman-devel >= 0.30.0
BuildRequires:     freetype-devel >= 2.1.9
BuildRequires:     fontconfig-devel >= 2.2.95
BuildRequires:     glib2-devel
BuildRequires:     mesa-libGL-devel
BuildRequires:     mesa-libEGL-devel
Obsoletes:         %{name} < %{version}-%{release}

%description
Cairo is a 2D graphics library designed to provide high-quality display
and print output. Currently supported output targets include the X Window
System, OpenGL (via glitz), in-memory image buffers, and image files (PDF,
PostScript, and SVG).

Cairo is designed to produce consistent output on all output media while
taking advantage of display hardware acceleration when available (e.g.
through the X Render Extension or OpenGL).

%package devel
Summary:           Development files for cairo
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}
Obsoletes:         %{name}-devel < %{version}-%{release}

%description devel
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains libraries, header files and developer documentation
needed for developing software which uses the cairo graphics library.

%package gobject
Summary:           GObject bindings for cairo
Group:             System Environment/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}
Obsoletes:         %{name}-gobject < %{version}-%{release}

%description gobject
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains functionality to make cairo graphics library
integrate well with the GObject object system used by GNOME.

%package gobject-devel
Summary:           Development files for cairo-gobject
Group:             Development/Libraries
Requires:          %{name}-devel%{?_isa} = %{version}-%{release}
Requires:          %{name}-gobject%{?_isa} = %{version}-%{release}
Obsoletes:         %{name}-gobject-devel < %{version}-%{release}

%description gobject-devel
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains libraries, header files and developer documentation
needed for developing software which uses the cairo Gobject library.

%package tools
Summary:           Development tools for cairo
Group:             Development/Tools
Obsoletes:         %{name}-tools < %{version}-%{release}

%description tools
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains tools for working with the cairo graphics library.
 * cairo-trace: Record cairo library calls for later playback

%prep
%setup -q
%patch3 -p1 -b .multilib

%build
export LDFLAGS='-lX11'
%configure --disable-static \
  --disable-xlib \
  --enable-ft \
  --enable-fc \
  --enable-ps \
  --enable-pdf \
  --enable-svg \
  --enable-gl \
  --enable-gobject \
  --disable-gtk-doc \
  --disable-silent-rules
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make V=1 %{?_smp_mflags}

%install
make install V=1 DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post gobject -p /sbin/ldconfig
%postun gobject -p /sbin/ldconfig

%files
%doc AUTHORS BIBLIOGRAPHY BUGS COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1 NEWS README
%{_libdir}/libcairo.so.*
%{_libdir}/libcairo-script-interpreter.so.*

%files devel
%doc ChangeLog PORTING_GUIDE
%dir %{_includedir}/cairo/
%{_includedir}/cairo/cairo-deprecated.h
%{_includedir}/cairo/cairo-features.h
%{_includedir}/cairo/cairo-gl.h
%{_includedir}/cairo/cairo-ft.h
%{_includedir}/cairo/cairo.h
%{_includedir}/cairo/cairo-pdf.h
%{_includedir}/cairo/cairo-ps.h
%{_includedir}/cairo/cairo-script-interpreter.h
%{_includedir}/cairo/cairo-svg.h
%{_includedir}/cairo/cairo-version.h
%{_includedir}/cairo/cairo-script.h
%{_includedir}/cairo/cairo-xcb.h
%{_libdir}/libcairo.so
%{_libdir}/libcairo-script-interpreter.so
%{_libdir}/pkgconfig/cairo-fc.pc
%{_libdir}/pkgconfig/cairo-ft.pc
%{_libdir}/pkgconfig/cairo-egl.pc
%{_libdir}/pkgconfig/cairo-gl.pc
%{_libdir}/pkgconfig/cairo-glx.pc
%{_libdir}/pkgconfig/cairo.pc
%{_libdir}/pkgconfig/cairo-pdf.pc
%{_libdir}/pkgconfig/cairo-png.pc
%{_libdir}/pkgconfig/cairo-ps.pc
%{_libdir}/pkgconfig/cairo-svg.pc
%{_libdir}/pkgconfig/cairo-script.pc
%{_libdir}/pkgconfig/cairo-xcb-shm.pc
%{_libdir}/pkgconfig/cairo-xcb.pc
%{_datadir}/gtk-doc/html/cairo

%files gobject
%{_libdir}/libcairo-gobject.so.*

%files gobject-devel
%{_includedir}/cairo/cairo-gobject.h
%{_libdir}/libcairo-gobject.so
%{_libdir}/pkgconfig/cairo-gobject.pc

%files tools
%{_bindir}/cairo-trace
%{_libdir}/cairo/

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with cairo 1.14.2
- Based on Fedora: cairo-1.14.2-1.fc23.src.rpm
