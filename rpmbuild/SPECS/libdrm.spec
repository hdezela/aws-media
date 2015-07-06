%define            debug_package %{nil}

Summary:           Direct Rendering Manager runtime library
Name:              libdrm
Version:           2.4.61
Release:           1%{?dist}
License:           MIT
Group:             System Environment/Libraries
URL:               http://dri.sourceforge.net
Source0:           http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
Source1:           91-drm-modeset.rules
Patch1:            libdrm-make-dri-perms-okay.patch
Patch2:            libdrm-2.4.0-no-bc.patch
Patch3:            libdrm-2.4.25-check-programs.patch
Requires:          udev
Obsoletes:         %{name} < %{version}-%{release}
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     docbook-style-xsl
BuildRequires:     kernel-headers
BuildRequires:     libtool
BuildRequires:     libatomic_ops-devel
BuildRequires:     libpciaccess-devel
BuildRequires:     libudev-devel
BuildRequires:     libxcb-devel
BuildRequires:     libxslt
BuildRequires:     pkgconfig
BuildRequires:     valgrind-devel
BuildRequires:     xorg-x11-util-macros

%description
Direct Rendering Manager runtime library

%package devel
Summary:           Direct Rendering Manager development package
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}
Requires:          kernel-headers >= 2.6.27-0.144.rc0.git2.fc10
Requires:          pkgconfig
Obsoletes:         %{name}-devel < %{version}-%{release}

%description devel
Direct Rendering Manager development package

%package -n drm-utils
Summary:           Direct Rendering Manager utilities
Group:             Development/Tools

%description -n drm-utils
Utility programs for the kernel DRM interface.  Will void your warranty.

%prep
%setup -q
%patch1 -p1 -b .forceperms
%patch2 -p1 -b .no-bc
%patch3 -p1 -b .check

%build
autoreconf -v --install || exit 1
%configure \
  --enable-install-test-programs \
  --enable-udev
make %{?_smp_mflags}
pushd tests
make %{?smp_mflags} `make check-programs`
popd

%install
make install DESTDIR=$RPM_BUILD_ROOT
pushd tests
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for foo in $(make check-programs) ; do
 install -m 0755 .libs/$foo $RPM_BUILD_ROOT%{_bindir}
done
popd
mkdir -p $RPM_BUILD_ROOT/lib/udev/rules.d/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/lib/udev/rules.d/

find $RPM_BUILD_ROOT -type f -name '*.la' | xargs rm -f -- || :
for i in r300_reg.h via_3d_reg.h
do
rm -f $RPM_BUILD_ROOT/usr/include/libdrm/$i
done

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/libdrm.so.2
%{_libdir}/libdrm.so.2.4.0
%{_libdir}/libdrm_intel.so.1
%{_libdir}/libdrm_intel.so.1.0.0
%{_libdir}/libdrm_radeon.so.1
%{_libdir}/libdrm_radeon.so.1.0.1
%{_libdir}/libdrm_nouveau.so.2
%{_libdir}/libdrm_nouveau.so.2.0.0
%{_libdir}/libkms.so.1
%{_libdir}/libkms.so.1.0.0
/lib/udev/rules.d/91-drm-modeset.rules

%files -n drm-utils
%defattr(-,root,root,-)
%{_bindir}/dristat
%{_bindir}/drmstat
%{_bindir}/getclient
%{_bindir}/getstats
%{_bindir}/getversion
%{_bindir}/name_from_fd
%{_bindir}/openclose
%{_bindir}/setversion
%{_bindir}/updatedraw
%{_bindir}/modetest
%{_bindir}/modeprint
%{_bindir}/vbltest
%{_bindir}/kmstest
%exclude %{_bindir}/exynos*
%exclude %{_bindir}/drmsl
%exclude %{_bindir}/hash
%exclude %{_bindir}/proptest
%exclude %{_bindir}/random

%files devel
%defattr(-,root,root,-)
%{_includedir}/xf86drm.h
%{_includedir}/xf86drmMode.h
%dir %{_includedir}/libdrm
%{_includedir}/libdrm/drm.h
%{_includedir}/libdrm/drm_fourcc.h
%{_includedir}/libdrm/drm_mode.h
%{_includedir}/libdrm/drm_sarea.h
%{_includedir}/libdrm/intel_aub.h
%{_includedir}/libdrm/intel_bufmgr.h
%{_includedir}/libdrm/intel_debug.h
%{_includedir}/libdrm/radeon_bo.h
%{_includedir}/libdrm/radeon_bo_gem.h
%{_includedir}/libdrm/radeon_bo_int.h
%{_includedir}/libdrm/radeon_cs.h
%{_includedir}/libdrm/radeon_cs_gem.h
%{_includedir}/libdrm/radeon_cs_int.h
%{_includedir}/libdrm/radeon_surface.h
%{_includedir}/libdrm/r600_pci_ids.h
%{_includedir}/libdrm/nouveau.h
%{_includedir}/libdrm/*_drm.h
%{_includedir}/libkms
%{_libdir}/libdrm.so
%{_libdir}/libdrm_intel.so
%{_libdir}/libdrm_radeon.so
%{_libdir}/libdrm_nouveau.so
%{_libdir}/libkms.so
%{_libdir}/pkgconfig/libdrm.pc
%{_libdir}/pkgconfig/libdrm_intel.pc
%{_libdir}/pkgconfig/libdrm_radeon.pc
%{_libdir}/pkgconfig/libdrm_nouveau.pc
%{_libdir}/pkgconfig/libkms.pc
%{_mandir}/man3/drm*.3*
%{_mandir}/man7/drm*.7*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Removed obsolete git conditionals
- Restarted patch numbering
- Removed architecture conditionals

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libdrm 2.4.61
- Based on Fedora: libdrm-2.4.61-3.fc23.src.rpm
