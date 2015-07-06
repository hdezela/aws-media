%define            real_version 9.0.0

Name:              mesa-libGLU
Version:           10.6.0
Release:           1%{?dist}
Summary:           Mesa libGLU library
License:           MIT
URL:               http://mesa3d.org/
Source0:           ftp://ftp.freedesktop.org/pub/mesa/glu/glu-%{real_version}.tar.bz2
Patch1:            0001-glu-initialize-PriorityQ-order-field-to-NULL-in-pqNe.patch
Patch2:            0002-Add-D-N-DEBUG-to-CFLAGS-dependent-on-enable-debug.patch
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     libtool
BuildRequires:     mesa-libGL-devel
Provides:          libGLU
Obsoletes:         libGLU < %{version}-%{release}

%description
Mesa implementation of the standard GLU OpenGL utility API.

%package devel
Summary:           Development files for %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          gl-manpages
Provides:          libGLU-devel
Obsoletes:         libGLU-devel < %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n glu-%{real_version}
%patch1 -p1
%patch2 -p1

%build
autoreconf -v -i -f
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_datadir}/man/man3/gl[A-Z]*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libGLU.so.1
%{_libdir}/libGLU.so.1.3.*

%files devel
%{_includedir}/GL/glu*.h
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libbGLU 9.0.0
- Based on Fedora: mesa-libGLU-9.0.0-7.fc22.src.rpm
- Version changed to 10.6.0 to match Amazon versioning
