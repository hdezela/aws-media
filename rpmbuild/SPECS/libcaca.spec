%define beta beta19

Summary:       Library for Colour AsCii Art, text mode graphics
Name:          libcaca
Version:       0.99
Release:       1%{?dist}
License:       WTFPL
Group:         System Environment/Libraries
URL:           http://caca.zoy.org/wiki/libcaca
Source:        http://caca.zoy.org/files/libcaca/libcaca-%{version}.%{beta}.tar.gz
Patch0:        libcaca-0.99.beta16-multilib.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: slang-devel
BuildRequires: ncurses-devel
BuildRequires: glut-devel
BuildRequires: libGLU-devel
BuildRequires: imlib2-devel
BuildRequires: pango-devel
Buildrequires: doxygen
Buildrequires: tetex-latex
Buildrequires: tetex-dvips

%description
libcaca is the Colour AsCii Art library. It provides high level functions
for color text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.


%package devel
Summary: Development files for libcaca, the library for Colour AsCii Art
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: slang-devel
Requires: ncurses-devel
Requires: glut-devel
Requires: libGLU-devel
Requires: imlib2-devel
Requires: pango-devel

%description devel
libcaca is the Colour AsCii Art library. It provides high level functions
for color text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.

This package contains the header files and static libraries needed to
compile applications or shared objects that use libcaca.


%package -n caca-utils
Summary: Colour AsCii Art Text mode graphics utilities based on libcaca
Group: Amusements/Graphics

%description -n caca-utils
This package contains utilities and demonstration programs for libcaca, the
Colour AsCii Art library.

cacaview is a simple image viewer for the terminal. It opens most image
formats such as JPEG, PNG, GIF etc. and renders them on the terminal using
ASCII art. The user can zoom and scroll the image, set the dithering method
or enable anti-aliasing.

cacaball is a tiny graphic program that renders animated ASCII metaballs on
the screen, cacafire is a port of AALib aafire and displays burning ASCII
art flames, and cacademo is a simple application that shows the libcaca
rendering features such as line and ellipses drawing, triangle filling and
sprite blitting.


%package -n python-caca
Summary: Python bindings for libcaca
Group: Development/Libraries
BuildRequires: python27-devel

%description -n python-caca
This package contains the python bindings for using libcaca from python.

%prep
%setup -q -n libcaca-%{version}.%{beta}
%patch0 -p1 -b .multilib

%build
sed -i -e 's|Config::CONFIG\["sitearchdir"\]|Config::CONFIG["vendorarchdir"]|' \
       -e 's|Config::CONFIG\["sitelibdir"\]|Config::CONFIG["vendorlibdir"]|' \
       -e "s|rbconfig -e 'print Config|rbconfig -e 'print RbConfig|g" \
  configure
%configure \
  --disable-static \
  --disable-csharp \
  --disable-java \
  --disable-ruby \
  --disable-x11
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf %{buildroot} libcaca-dev-docs
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_docdir}/libcaca-dev libcaca-dev-docs
rm -f %{buildroot}%{_docdir}/libcucul-dev

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc ChangeLog libcaca-dev-docs/html/
%{_bindir}/caca-config
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man1/caca-config.1*
%{_mandir}/man3/*

%files -n caca-utils
%defattr(-,root,root,-)
%doc AUTHORS COPYING* NEWS NOTES README THANKS
%{_bindir}/cacademo
%{_bindir}/cacafire
%{_bindir}/cacaclock
%{_bindir}/cacaplay
%{_bindir}/cacaserver
%{_bindir}/cacaview
%{_bindir}/img2txt
%{_datadir}/libcaca/
%{_mandir}/man1/cacademo.1*
%{_mandir}/man1/cacafire.1*
%{_mandir}/man1/cacaplay.1*
%{_mandir}/man1/cacaserver.1*
%{_mandir}/man1/cacaview.1*
%{_mandir}/man1/img2txt.1*

%files -n python-caca
%defattr(-,root,root,-)
%doc python/examples
%{python_sitelib}/caca/

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Ruby disabled
- X11 disabled

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libcaca 0.99
- Based on Fedora: libcaca-0.99-0.25.beta18.fc23.src.rpm
