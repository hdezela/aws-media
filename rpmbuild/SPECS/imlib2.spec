Summary:       Image loading, saving, rendering, and manipulation library
Name:          imlib2
Version:       1.4.6
Release:       1%{?dist}
License:       Imlib2
Group:         System Environment/Libraries
URL:           http://docs.enlightenment.org/api/imlib2/html/
Source0:       http://downloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.bz2
Patch0:        imlib2-1.4.6-multilib.patch
Patch1:        imlib2-giflib5.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: giflib-devel
BuildRequires: freetype-devel >= 2.1.9-4
BuildRequires: libtool
BuildRequires: bzip2-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libid3tag-devel
BuildRequires: pkgconfig

%description
Imlib 2 is a library that does image file loading and saving as well
as rendering, manipulation, arbitrary polygon support, etc.  It does
ALL of these operations FAST. Imlib2 also tries to be highly
intelligent about doing them, so writing naive programs can be done
easily, without sacrificing speed.  This is a complete rewrite over
the Imlib 1.x series. The architecture is more modular, simple, and
flexible.

%package devel
Summary:       Development package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      libX11-devel libXext-devel freetype-devel >= 2.1.9-4 pkgconfig

%description devel
This package contains development files for %{name}.

Imlib 2 is a library that does image file loading and saving as well
as rendering, manipulation, arbitrary polygon support, etc.  It does
ALL of these operations FAST. Imlib2 also tries to be highly
intelligent about doing them, so writing naive programs can be done
easily, without sacrificing speed.  This is a complete rewrite over
the Imlib 1.x series. The architecture is more modular, simple, and
flexible.

%package id3tag-loader
Summary:       Imlib2 id3tag-loader
License:       GPLv2+
Group:         System Environment/Libraries
Requires:      %{name} = %{version}-%{release}

%description id3tag-loader
This package contains a plugin which makes imlib2 capable of parsing id3 tags
of mp3 files. This plugin is packaged separately because it links with
libid3tag which is GPLv2+, thus making imlib2 and apps using it subject to the
conditions of the GPL version 2 (or at your option) any later version.

%prep
%setup -q
%patch0 -p1 -b .multilib
%patch1 -p1 -b .giflib

%build
asmopts="--disable-mmx --enable-amd64"

autoreconf -ifv

export x_libs=" "
%configure --disable-static --with-pic $asmopts
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_bindir}/imlib2_*
rm -rf $RPM_BUILD_ROOT%{_datadir}/imlib2/data/
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f \{\} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README TODO
%{_libdir}/libImlib2.so.*
%dir %{_libdir}/imlib2/
%dir %{_libdir}/imlib2/filters/
%{_libdir}/imlib2/filters/*.so
%dir %{_libdir}/imlib2/loaders/
%{_libdir}/imlib2/loaders/*.so
%exclude %{_libdir}/imlib2/loaders/id3.*

%files devel
%defattr(-,root,root,-)
%doc doc/*.gif doc/*.html
%{_bindir}/imlib2-config
%{_includedir}/Imlib2.h
%{_libdir}/libImlib2.so
%{_libdir}/pkgconfig/imlib2.pc

%files id3tag-loader
%{_libdir}/imlib2/loaders/id3.*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Added giflib5 patch

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with imlib2 1.4.6
- Based on Fedora: imlib2-1.4.6-4.fc23.src.rpm
