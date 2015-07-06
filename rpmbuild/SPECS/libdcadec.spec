Summary:     Free DTS Coherent Acoustics decoder with support for HD extensions
Name:        libdcadec
Version:	   0.0.0
%define	   snap 20150606
%define	   git 2a9186e34ce557d3af1a20f5b558d1e6687708b9
Release:     1%{?dist}
License:     LGPL v2.1+
Group:       Applications/Sound
Source0:     https://github.com/foo86/dcadec/archive/2a9186e34ce557d3af1a20f5b558d1e6687708b9/%{name}-%{snap}.tar.gz
URL:         https://github.com/foo86/dcadec
Provides:    libdcadec.so()(64bit)

%description
dcadec is a free DTS Coherent Acoustics decoder with support for HD
extensions.

%package devel
Summary:     Development files for %{name}
Group:       Development/Libraries

%description devel
Development files for %{name}

%prep
%setup -q -n %{name}-%{git}

%build
export LDFLAGS="$LDFLAGS -Wl,-z,now,-z,relro -pie"
export CFLAGS="$RPM_OPT_FLAGS -fPIE -pie"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIE -pie"
%{__make} all \
  CC="%{__cc}" \
  CONFIG_SHARED=1 \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir}

%install
%{__make} install \
  CONFIG_SHARED=1 \
  DESTDIR=$RPM_BUILD_ROOT \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir}

ln -s dcadec.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libdcadec.pc
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libdcadec.so

%clean

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%{_bindir}/dcadec
%{_libdir}/libdcadec.so

%files devel
%{_includedir}/libdcadec
%{_libdir}/libdcadec.so
%{_libdir}/pkgconfig/dcadec.pc
%{_libdir}/pkgconfig/libdcadec.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libdcadec no-version
- New spec file