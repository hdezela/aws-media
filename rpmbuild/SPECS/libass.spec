Name:          libass
Version:       0.12.2
Release:       1%{?dist}
Summary:       Portable library for SSA/ASS subtitles rendering
Group:         System Environment/Libraries
License:       ISC
URL:           https://github.com/libass
Source0:       https://github.com/libass/libass/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires: enca-devel
BuildRequires: fontconfig-devel
BuildRequires: fribidi-devel
BuildRequires: harfbuzz-devel >= 0.9.5
BuildRequires: libpng-devel

%description
Libass is a portable library for SSA/ASS subtitles rendering.

%package devel
Summary:       Development files for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure \
  --disable-static \
  --enable-shared
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc Changelog COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libass.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libass 0.12.2
- Based on Fedora: libass-0.12.1-2.fc23.src.rpm
