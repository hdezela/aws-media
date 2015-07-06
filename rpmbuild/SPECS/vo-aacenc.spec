Name:          vo-aacenc
Version:       0.1.3
Release:       1%{?dist}
Summary:       VisualOn AAC encoder library
Group:         System Environment/Libraries
License:       ASL 2.0
URL:           http://opencore-amr.sourceforge.net/
Source0:       http://sourceforge.net/projects/opencore-amr/files/%{name}/%{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake

%description
This library contains an encoder implementation of the Advanced Audio
Coding (AAC) audio codec. The library is based on a codec implementation
by VisualOn as part of the Stagefright framework from the Google
Android project.

%package devel
Summary:       Development files for %{name}
Group:         Development/Libraries
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
autoreconf -fv --install

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT 
rm $RPM_BUILD_ROOT%{_libdir}/libvo-aacenc.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING README NOTICE
%{_libdir}/libvo-aacenc.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libvo-aacenc.so
%{_libdir}/pkgconfig/vo-aacenc.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with vo-aacenc 0.1.3 
- New spec file
