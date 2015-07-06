Name:              glew
Version:           1.10.0
Release:           1%{?dist}
Summary:           The OpenGL Extension Wrangler Library
Group:             System Environment/Libraries
License:           BSD and MIT
URL:               http://glew.sourceforge.net
Source0:           http://downloads.sourceforge.net/project/glew/glew/%{version}/glew-%{version}.tgz
Patch0:            0001-BUILD-respect-DESTDIR-variable.patch
Patch1:            glew-1.9.0-makefile.patch
BuildRequires:     libGLU-devel

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library. GLEW provides efficient run-time mechanisms for
determining which OpenGL extensions are supported on the target platform.
OpenGL core and extension functionality is exposed in a single header file.
GLEW is available for a variety of operating systems, including Windows, Linux,
Mac OS X, FreeBSD, Irix, and Solaris.

This package contains the demo GLEW utilities.  The libraries themselves
are in libGLEW and libGLEWmx.

%package devel
Summary:           Development files for glew
Group:             Development/Libraries
Requires:          libGLEW = %{version}-%{release}
Requires:          libGLEWmx = %{version}-%{release}
Requires:          libGLU-devel

%description devel
Development files for glew

%package -n libGLEW
Summary:           libGLEW
Group:             System Environment/Libraries

%description -n libGLEW
libGLEW

%package -n libGLEWmx
Summary:           libGLEWmx
Group:             System Environment/Libraries

%description -n libGLEWmx
libGLEWmx

%prep
%setup -q
%patch0 -p1 -b .bld
%patch1 -p1 -b .make

cp /usr/lib/rpm/amazon/config.guess config/

%build
make %{?_smp_mflags} CFLAGS.EXTRA="$RPM_OPT_FLAGS -fPIC" includedir=%{_includedir} STRIP= libdir=%{_libdir} bindir=%{_bindir} GLEW_DEST=

%install
make install.all GLEW_DEST= DESTDIR="$RPM_BUILD_ROOT" libdir=%{_libdir} bindir=%{_bindir} includedir=%{_includedir}
find $RPM_BUILD_ROOT -type f -name "*.a" -delete
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/*.so*

%post -n libGLEW -p /sbin/ldconfig

%postun -n libGLEW -p /sbin/ldconfig

%post -n libGLEWmx -p /sbin/ldconfig

%postun -n libGLEWmx -p /sbin/ldconfig

%files
%doc LICENSE.txt
%{_bindir}/*

%files -n libGLEW
%doc LICENSE.txt
%{_libdir}/libGLEW.so.*

%files -n libGLEWmx
%doc LICENSE.txt
%{_libdir}/libGLEWmx.so.*

%files devel
%{_libdir}/libGLEW.so
%{_libdir}/libGLEWmx.so
%{_libdir}/pkgconfig/glew.pc
%{_libdir}/pkgconfig/glewmx.pc
%{_includedir}/GL/*.h
%doc doc/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with glew 1.10.0
- Based on Fedora: glew-1.10.0-5.fc22.src.rpm
