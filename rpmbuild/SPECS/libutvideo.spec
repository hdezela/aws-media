Summary:       Ut Video codec
Name:          libutvideo
Version:       15.1.0
Release:       1%{?dist}
Summary:       Fast compression and decompression library
Group:         System Environment/Libraries
License:       GPL v2+
URL:           https://github.com/qyot27/libutvideo/
Source0:       https://github.com/qyot27/libutvideo/archive/libutvideo-15.1.0.zip
BuildRequires: libstdc++-devel
BuildRequires: libtool
BuildRequires: nasm

%description
Ut Video codec

%package devel
Summary:       Development files for %{name}
Group:         Development/Libraries
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      libstdc++-devel

%description devel
Header files for Ut Video codec.

%prep
%setup -q -n %{name}-%{version}

%build
./configure \
  --enable-pic \
  --enable-shared \
  --disable-static
make

%install
make install \
 DESTDIR=$RPM_BUILD_ROOT \
 prefix=%{_prefix} \
 libdir=%{_libdir}

ln -s libutvideo.so.15.1.0 $RPM_BUILD_ROOT%{_libdir}/libutvideo.so.0

%clean

%check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc readme.en.html
%{_libdir}/libutvideo.so.*.*.*
%{_libdir}/libutvideo.so.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/libutvideo.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/utvideo

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libutvideo 15.1.0
- New spec file
