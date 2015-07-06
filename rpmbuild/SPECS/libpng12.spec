Summary:           Old version of libpng, needed to run old binaries
Name:              libpng12
Version:           1.2.50
Release:           1%{?dist}
License:           zlib
Group:             System Environment/Libraries
URL:               http://www.libpng.org/pub/png/
Source0:           ftp://ftp.simplesystems.org/pub/png/src/libpng-%{version}.tar.bz2
Patch0:            libpng12-multilib.patch
Patch1:            libpng12-pngconf.patch
Patch2:            libpng12-CVE-2013-6954.patch
BuildRequires:     zlib-devel
BuildRequires:     pkgconfig
Obsoletes:         libpng-compat <= 2:1.5.10
Obsoletes:         libpng <= 2:1.2.49

%description
The libpng12 package provides libpng 1.2, an older version of the libpng
library for manipulating PNG (Portable Network Graphics) image format files.
This version should be used only if you are unable to use the current
version of libpng.

%package devel
Summary:           Development files for libpng 1.2
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          zlib-devel%{?_isa}
Requires:          pkgconfig%{?_isa}

%description devel
The libpng12-devel package contains header files and documentation necessary
for developing programs using libpng12.

%prep
%setup -q -n libpng-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure \
  --disable-static \
  --without-libpng-compat

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm -fv $RPM_BUILD_ROOT%{_libdir}/libpng*.la
rm -fv $RPM_BUILD_ROOT%{_mandir}/man5/*
rm -fv $RPM_BUILD_ROOT%{_bindir}/libpng-config
rm -fv $RPM_BUILD_ROOT%{_includedir}/{png,pngconf}.h
rm -fv $RPM_BUILD_ROOT%{_libdir}/libpng.so
rm -fv $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libpng.pc
rm -fv $RPM_BUILD_ROOT%{_mandir}/man3/{libpng,libpngpf}.3*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE
%doc libpng-%{version}.txt README TODO CHANGES
%{_libdir}/libpng12.so.0*

%files devel
#doc example.c
%{_bindir}/libpng12-config
%{_includedir}/libpng12/
%{_libdir}/libpng12.so
%{_libdir}/pkgconfig/libpng12.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libpng12 1.2
- Based on Fedora: libpng12-1.2.50-8.fc22.src.rpm
- Required for compatibility with EC2 tools and Java
