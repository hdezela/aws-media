Summary:       Fixed-point MP3 encoding library
Name:          shine
Version:       3.1.0
Release:       1%{?dist}
License:       None
Group:         Libraries
Source0:       https://github.com/savonet/shine/archive/%{version}/%{name}-%{version}.tar.gz
URL:           https://github.com/savonet/shine/
BuildRequires: autoconf >= 2.50
BuildRequires: automake
BuildRequires: libtool >= 2
BuildRoot:     %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fixed-point MP3 encoding library.

%package devel
Summary:       Header files for shine library
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Header files for shine library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

find $RPM_BUILD_ROOT -type f -name "*.a" -delete
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libshine.so.*.*.*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libshine.so.3
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libshine.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md README.old
%attr(755,root,root) %{_bindir}/shineenc
%{_libdir}/libshine.so.*.*.*
%{_libdir}/libshine.so.3

%files devel
%defattr(644,root,root,755)
%{_libdir}/libshine.so
%{_includedir}/shine
%{_libdir}/pkgconfig/shine.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libshine 3.1.0
- New spec file