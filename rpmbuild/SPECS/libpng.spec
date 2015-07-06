Summary:           A library of functions for manipulating PNG image format files
Name:              libpng
Epoch:             2
Version:           1.6.17
Release:           1%{?dist}
License:           zlib
Group:             System Environment/Libraries
URL:               http://www.libpng.org/pub/png/
Source0:           ftp://ftp.simplesystems.org/pub/libpng/png/src/libpng16/libpng-%{version}.tar.gz
Source1:           pngusr.dfa
Patch0:            libpng-multilib.patch
Patch1:            libpng-fix-arm-neon.patch
BuildRequires:     zlib-devel
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     libtool

%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG
is a bit-mapped graphics format similar to the GIF format.  PNG was
created to replace the GIF format, since GIF uses a patented data
compression algorithm.

Libpng should be installed if you need to manipulate PNG format image
files.

%package devel
Summary:           Development tools for programs to manipulate PNG image format files
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:          zlib-devel%{?_isa} pkgconfig%{?_isa}

%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.

If you want to develop programs which will manipulate PNG image format
files, you should install libpng-devel.  Youll also need to install
the libpng package.

%package static
Summary:           Static PNG image format file library
Group:             Development/Libraries
Requires:          %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description static
The libpng-static package contains the statically linkable version of libpng.
Linking to static libraries is discouraged for most applications, but it is
necessary for some boot packages.

%package tools
Summary:           Tools for PNG image format file library
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description tools
The libpng-tools package contains tools used by the authors of libpng.

%prep
%setup -q
cp -p %{SOURCE1} .

%patch0 -p1
%patch1 -p1 -b .arm

%build
autoreconf -vif
%configure
make %{?_smp_mflags} DFA_XTRA=pngusr.dfa

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir $RPM_BUILD_ROOT%{_includedir}/libpng/
ln -s ../libpng16/png.h $RPM_BUILD_ROOT%{_includedir}/libpng/png.h
ln -s ../libpng16/pngconf.h $RPM_BUILD_ROOT%{_includedir}/libpng/pngconf.h
ln -s ../libpng16/pnglibconf.h $RPM_BUILD_ROOT%{_includedir}/libpng/pnglibconf.h

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libpng16.so.*
%{_mandir}/man5/*

%files devel
%doc libpng-manual.txt example.c TODO CHANGES
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libpng*.so
%{_libdir}/pkgconfig/libpng*.pc
%{_mandir}/man3/*

%files static
%{_libdir}/libpng*.a

%files tools
%{_bindir}/pngfix

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Created unversioned include link

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libpng1 1.6.17
- Based on Fedora: libpng-1.6.17-1.fc23.src.rpm
