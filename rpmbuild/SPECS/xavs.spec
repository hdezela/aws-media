Summary:           Audio Video Standard of China
Name:              xavs
Version:           0.1.51
Release:           1%{?dist}
License:           GPL
Group:             System Environment/Libraries
URL:               http://xavs.sourceforge.net/
Source0:           %{name}-trunk.tar.gz
BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-root

%description
AVS is the Audio Video Standard of China.  This project aims to
implement high quality AVS encoder and decoder.

%package libs
Summary:           XAVS library files

%description libs
This package contains the shared library for AVS.

%package devel
Summary:           XAVS development files
Requires:          %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the shared library development files for AVS.

%prep
%setup -q -n trunk

%build
export CFLAGS="%{optflags}"
./configure \
  --bindir=%{_bindir} \
  --libdir=%{_libdir} \
  --includedir=%{_includedir} \
  --enable-pic \
  --enable-shared \
  --disable-static

%install
rm -rf %{buildroot}
make install \
  DESTDIR=%{buildroot}

rm -f $RPM_BUILD_ROOT%{_libdir}/libxavs.a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/*.txt
%{_bindir}/xavs

%files libs
%{_libdir}/libxavs.so.1

%files devel
%doc doc/*
%{_includedir}/xavs.h
%{_libdir}/libxavs.so
%{_libdir}/pkgconfig/xavs.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Added libs and devel packages

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with xavs 0.1.51
- Based on Fedora: xavs-0.1.51-2.src
