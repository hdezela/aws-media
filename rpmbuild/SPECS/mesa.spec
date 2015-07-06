%define            debug_package %{nil}
%define            _default_patch_fuzz 2
%define            githash 5a55f68
%define            git %{?githash:%{githash}}%{!?githash:%{gitdate}}

Summary:           Mesa graphics libraries
Name:              mesa
Version:           10.6.0
Release:           1%{?dist}
License:           MIT
Group:             System Environment/Libraries
URL:               http://www.mesa3d.org
Source0:           %{name}-%{git}.tar.xz
Source1:           Makefile
Source2:           vl_decoder.c
Source3:           vl_mpeg12_decoder.c
Source4:           Mesa-MLAA-License-Clarification-Email.txt
Patch1:            mesa-10.0-nv50-fix-build.patch
Patch2:            mesa-9.2-hardware-float.patch
Patch3:            mesa-10.2-evergreen-big-endian.patch
Patch4:            mesa-10.3-bigendian-assert.patch
Patch5:            mesa-10.6-nir-linker.patch
Patch6:            0001-opencl-use-versioned-.so-in-mesa.icd.patch
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     bison
BuildRequires:     elfutils
BuildRequires:     elfutils-libelf-devel
BuildRequires:     expat-devel
BuildRequires:     flex
BuildRequires:     gettext
BuildRequires:     git
BuildRequires:     libdrm-devel >= 2.4.42
BuildRequires:     libselinux-devel
BuildRequires:     libtool
BuildRequires:     libudev-devel
BuildRequires:     libXdamage-devel
BuildRequires:     libXext-devel
BuildRequires:     libXfixes-devel
BuildRequires:     libXi-devel
BuildRequires:     libxml2-python27
BuildRequires:     libXmu-devel
BuildRequires:     libxshmfence-devel
BuildRequires:     libXxf86vm-devel
BuildRequires:     makedepend
BuildRequires:     pkgconfig
BuildRequires:     python27
BuildRequires:     python27-mako
BuildRequires:     xorg-x11-proto-devel
BuildRequires:     zlib-devel
BuildRequires:     gl-manpages

%description
Mesa

%package libGL
Summary:           Mesa libGL runtime libraries and DRI drivers
Group:             System Environment/Libraries
Provides:          libGL
Obsoletes:         mesa-libGL < %{version}-%{release}

%description libGL
Mesa libGL runtime library.

%package libEGL
Summary:           Mesa libEGL runtime libraries
Group:             System Environment/Libraries
Obsoletes:         mesa-libEGL < %{version}-%{release}

%description libEGL
Mesa libEGL runtime libraries

%package libGLES
Summary:           Mesa libGLES runtime libraries
Group:             System Environment/Libraries
Obsoletes:         mesa-libGLES < %{version}-%{release}

%description libGLES
Mesa GLES runtime libraries

%package filesystem
Summary:           Mesa driver filesystem
Group:             User Interface/X Hardware Support
Provides:          mesa-dri-filesystem = %{version}-%{release}
Obsoletes:         mesa-dri-filesystem < %{version}-%{release}

%description filesystem
Mesa driver filesystem

%package dri-drivers
Summary:           Mesa-based DRI drivers
Group:             User Interface/X Hardware Support
Requires:          mesa-filesystem%{?_isa}
Obsoletes:         mesa-dri1-drivers < 7.12
Obsoletes:         mesa-dri-llvmcore <= 7.12
Obsoletes:         mesa-dri-drivers < %{version}-%{release}

%description dri-drivers
Mesa-based DRI drivers.

%package libGL-devel
Summary:           Mesa libGL development package
Group:             Development/Libraries
Requires:          mesa-libGL = %{version}-%{release}
Requires:          gl-manpages
Provides:          libGL-devel
Obsoletes:         mesa-libGL-devel < %{version}-%{release}

%description libGL-devel
Mesa libGL development package

%package libEGL-devel
Summary:           Mesa libEGL development package
Group:             Development/Libraries
Requires:          mesa-libEGL = %{version}-%{release}
Provides:          khrplatform-devel = %{version}-%{release}
Obsoletes:         khrplatform-devel < %{version}-%{release}
Obsoletes:         mesa-libEGL-devel < %{version}-%{release}

%description libEGL-devel
Mesa libEGL development package

%package libGLES-devel
Summary:           Mesa libGLES development package
Group:             Development/Libraries
Requires:          mesa-libGLES = %{version}-%{release}
Obsoletes:         mesa-libGLES-devel < %{version}-%{release}

%description libGLES-devel
Mesa libGLES development package

%package libOSMesa
Summary:           Mesa offscreen rendering libraries
Group:             System Environment/Libraries
Provides:          libOSMesa
Obsoletes:         libOSMesa < %{version}-%{release}

%description libOSMesa
Mesa offscreen rendering libraries

%package libOSMesa-devel
Summary:           Mesa offscreen rendering development package
Group:             Development/Libraries
Requires:          mesa-libOSMesa = %{version}-%{release}
Obsoletes:         mesa-libOSMesa-devel < %{version}-%{release}

%description libOSMesa-devel
Mesa offscreen rendering development package

%package libgbm
Summary:           Mesa gbm library
Group:             System Environment/Libraries
Provides:          libgbm

%description libgbm
Mesa gbm runtime library.

%package libgbm-devel
Summary:           Mesa libgbm development package
Group:             Development/Libraries
Requires:          mesa-libgbm%{?_isa} = %{version}-%{release}
Provides:          libgbm-devel

%description libgbm-devel
Mesa libgbm development package

%package libglapi
Summary:           Mesa shared glapi
Group:             System Environment/Libraries

%description libglapi
Mesa shared glapi

%prep
%setup -q -n mesa-%{git}
grep -q ^/ src/gallium/auxiliary/vl/vl_decoder.c && exit 1

%patch1 -p1 -b .nv50rtti
%patch2 -p1 -b .hwfloat
%patch3 -p1 -b .egbe
%patch4 -p1 -b .beassert
%patch5 -p1 -b .nir
%patch6 -p1 -b .icd

sed -i 's/llvm-config/mesa-private-llvm-config-%{__isa_bits}/g' configure.ac
sed -i 's/`$LLVM_CONFIG --version`/&-mesa/' configure.ac

cp %{SOURCE4} docs/

%build

autoreconf --install

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
%define asm_flags --disable-asm

%configure \
  %{?asm_flags} \
  --enable-selinux \
  --enable-osmesa \
  --with-dri-driverdir=%{_libdir}/dri \
  --enable-egl \
  --disable-gles1 \
  --enable-gles2 \
  --disable-xvmc \
  --with-egl-platforms=x11,drm \
  --enable-shared-glapi \
  --enable-gbm \
  --disable-opencl \
  --enable-glx-tls \
  --enable-texture-float=yes \
  --enable-dri \
  --disable-dri3 \
  --with-dri-drivers=swrast \
  --with-gallium-drivers=swrast

make -C src/mesa/drivers/dri/common/xmlpool/

make %{?_smp_mflags} MKDEP=/bin/true

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/dri/{radeon,r200,nouveau_vieux}_dri.*

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/drirc

rm -f $RPM_BUILD_ROOT%{_libdir}/vdpau/*.so

rm -f $RPM_BUILD_ROOT%{_includedir}/GL/w*.h

find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

pushd $RPM_BUILD_ROOT%{_libdir}
for i in libOSMesa*.so libGL.so ; do
    eu-findtextrel $i && exit 1
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%check

%post libGL -p /sbin/ldconfig
%postun libGL -p /sbin/ldconfig
%post libOSMesa -p /sbin/ldconfig
%postun libOSMesa -p /sbin/ldconfig
%post libEGL -p /sbin/ldconfig
%postun libEGL -p /sbin/ldconfig
%post libGLES -p /sbin/ldconfig
%postun libGLES -p /sbin/ldconfig
%post libglapi -p /sbin/ldconfig
%postun libglapi -p /sbin/ldconfig
%post libgbm -p /sbin/ldconfig
%postun libgbm -p /sbin/ldconfig

%files libGL
%defattr(-,root,root,-)
%doc docs/COPYING
%{_libdir}/libGL.so.1
%{_libdir}/libGL.so.1.*

%files libEGL
%defattr(-,root,root,-)
%doc docs/COPYING
%{_libdir}/libEGL.so.1
%{_libdir}/libEGL.so.1.*

%files libGLES
%defattr(-,root,root,-)
%doc docs/COPYING
%{_libdir}/libGLESv2.so.2
%{_libdir}/libGLESv2.so.2.*

%files filesystem
%defattr(-,root,root,-)
%doc docs/COPYING docs/Mesa-MLAA-License-Clarification-Email.txt
%dir %{_libdir}/dri

%files libglapi
%{_libdir}/libglapi.so.0
%{_libdir}/libglapi.so.0.*

%files dri-drivers
%defattr(-,root,root,-)
%{_libdir}/dri/swrast_dri.so
%{_libdir}/dri/kms_swrast_dri.so

%files libGL-devel
%defattr(-,root,root,-)
%{_includedir}/GL/gl.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glx_mangle.h
%{_includedir}/GL/glxext.h
%{_includedir}/GL/glcorearb.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h
%{_libdir}/pkgconfig/dri.pc
%{_libdir}/libGL.so
%{_libdir}/libglapi.so
%{_libdir}/pkgconfig/gl.pc

%files libEGL-devel
%defattr(-,root,root,-)
%dir %{_includedir}/EGL
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglmesaext.h
%{_includedir}/EGL/eglplatform.h
%{_includedir}/EGL/eglextchromium.h
%dir %{_includedir}/KHR
%{_includedir}/KHR/khrplatform.h
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/libEGL.so

%files libGLES-devel
%defattr(-,root,root,-)
%dir %{_includedir}/GLES2
%{_includedir}/GLES2/gl2platform.h
%{_includedir}/GLES2/gl2.h
%{_includedir}/GLES2/gl2ext.h
%{_includedir}/GLES3/gl3platform.h
%{_includedir}/GLES3/gl3.h
%{_includedir}/GLES3/gl3ext.h
%{_includedir}/GLES3/gl31.h
%{_libdir}/pkgconfig/glesv2.pc
%{_libdir}/libGLESv2.so

%files libOSMesa
%defattr(-,root,root,-)
%doc docs/COPYING
%{_libdir}/libOSMesa.so.8*

%files libOSMesa-devel
%defattr(-,root,root,-)
%dir %{_includedir}/GL
%{_includedir}/GL/osmesa.h
%{_libdir}/libOSMesa.so
%{_libdir}/pkgconfig/osmesa.pc

%files libgbm
%defattr(-,root,root,-)
%doc docs/COPYING
%{_libdir}/libgbm.so.1
%{_libdir}/libgbm.so.1.*

%files libgbm-devel
%defattr(-,root,root,-)
%{_libdir}/libgbm.so
%{_includedir}/gbm.h
%{_libdir}/pkgconfig/gbm.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Removed architecture conditionals
- Added obsoletes to packages
- Removed mesa-libGL-devel dependency

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with mesa 10.6.0
- Based on Fedora: mesa-10.6.0-0.devel.6.5a55f68.fc23.src.rpm
