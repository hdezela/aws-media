Summary:           Open audio/video container format library
Name:              libmatroska
Version:           1.4.2
Release:           1%{?dist}
License:           LGPLv2+
Group:             System Environment/Libraries
URL:               http://www.matroska.org/
Source0:           http://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:     libebml-devel >= 1.3.1

%description
Matroska is an extensible open standard Audio/Video container.  It
aims to become THE standard of multimedia container formats.  Matroska
is usually found as .mkv files (matroska video) and .mka files
(matroska audio).

%package devel
Summary:           Matroska container format library development files
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}
Requires:          libebml-devel >= 1.3.1

%description devel
Matroska is an extensible open standard Audio/Video container.  It
aims to become THE standard of multimedia container formats.  Matroska
is usually found as .mkv files (matroska video) and .mka files
(matroska audio).

This package contains the files required to rebuild applications which
will use the Matroska container format.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc ChangeLog LICENSE.LGPL
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/matroska/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libmatroska 1.4.2
- Based on Fedora: libmatroska-1.4.2-4.fc23.src
