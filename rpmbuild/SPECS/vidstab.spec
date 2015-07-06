Summary:       Vid.Stab - video stabilization library
Name:          libvidstab
Version:       0.98b
Release:       1%{?dist}
License:       GPL v2+
Group:         Libraries
Source0:       https://github.com/georgmartius/vid.stab/archive/vid.stab-release-%{version}.tar.gz
URL:           http://public.hronopik.de/vid.stab/
BuildRequires: cmake

%description
Vid.Stab is a library for stabilizing video clips.

%package devel
Summary:       Development files for vid.stab library
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Development files for vid.stab library.

%prep
%setup -q -n vid.stab-release-%{version}

%build
%cmake
%{__make}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog LICENSE README Todo
%{_libdir}/libvidstab.so.0.9

%files devel
%defattr(644,root,root,755)
%{_libdir}/libvidstab.so
%{_includedir}/vid.stab
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with vidstab 0.98b
- New spec file