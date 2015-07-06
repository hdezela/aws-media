Name:           OpenEXR
Summary:        A high dynamic-range (HDR) image file format
Version:        2.2.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.openexr.com/
Source0:        http://download.savannah.nongnu.org/releases/openexr/openexr-%{version}.tar.gz
Patch0:         openexr-2.1.0-bigendian.patch
Obsoletes:      openexr < %{version}-%{release}
Provides:       openexr = %{version}-%{release}
BuildConflicts: OpenEXR-devel < 2.2.0
BuildRequires:  ilmbase-devel >= %{version}
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
OpenEXR is a high dynamic-range (HDR) image file format developed by Industrial
Light & Magic for use in computer imaging applications. This package contains
libraries and sample applications for handling the format.

%package devel
Summary:        Headers and libraries for building apps that use %{name} 
Obsoletes:      openexr-devel < %{version}-%{release}
Provides:       openexr-devel = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       ilmbase-devel
%description devel
%{summary}.

%package libs
Summary: %{name} runtime libraries
%description libs
%{summary}.

%prep
%setup -q -n openexr-%{version}
%patch0 -p1 -b .bigendian

%build
%configure --disable-static

#sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

rm -fv %{buildroot}%{_libdir}/lib*.la
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion OpenEXR)" = "%{version}"
make %{?_smp_mflags} check ||:

%files
%{_bindir}/exr*

%post libs -p /sbin/ldconfig
%postun libs  -p /sbin/ldconfig

%files libs
%doc AUTHORS ChangeLog LICENSE NEWS README
%{_libdir}/libIlmImf-2_2.so.22*
%{_libdir}/libIlmImfUtil-2_2.so.22*

%files devel
%{_datadir}/aclocal/openexr.m4
%{_includedir}/OpenEXR/*
%{_libdir}/libIlmImf*.so
%{_libdir}/pkgconfig/OpenEXR.pc


%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with openEXR 2.2.0
- Based on Fedora: OpenEXR-2.2.0-4.fc23.src.rpm
