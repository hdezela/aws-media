Name:          libva
Version:       1.5.1
Release:       1%{?dist}
Summary:       Video Acceleration (VA) API for Linux
Group:         System Environment/Libraries
License:       MIT
URL:           http://freedesktop.org/wiki/Software/vaapi
Source0:       http://www.freedesktop.org/software/vaapi/releases/libva/libva-%{version}.tar.bz2
BuildRequires: libudev-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libdrm-devel
BuildRequires: libpciaccess-devel
#BuildRequires: mesa-libEGL-devel
#BuildRequires: mesa-libGL-devel
#BuildRequires: mesa-libGLES-devel
# owns the %{_libdir}/dri directory
Requires:      mesa-dri-filesystem

%description
Libva is a library providing the VA API video acceleration API.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	utils
Summary:	Tools for %{name} (including vainfo)
Group:		Development/Libraries
Requires:	%{name}%{_isa} = %{version}-%{release}

%description	utils
The %{name}-utils package contains tools that are provided as part
of %{name}, including the vainfo tool for determining what (if any)
%{name} support is available on a system.

%prep
%setup -q

%build
%configure --disable-static \
  --enable-glx \
  --disable-wayland

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_libdir}/libva*.so.*
# Keep these specific: if any new real drivers start showing up
# in libva, we need to know about it so they can be patent-audited
%{_libdir}/dri/dummy_drv_video.so

%files devel
%{_includedir}/va
%{_libdir}/libva*.so
%{_libdir}/pkgconfig/libva*.pc

%files utils
%{_bindir}/vainfo
%{_bindir}/loadjpeg
%{_bindir}/jpegenc
%{_bindir}/avcenc
%{_bindir}/h264encode
%{_bindir}/mpeg2vldemo
%{_bindir}/mpeg2vaenc
%{_bindir}/putsurface

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libva 1.5.1
- Based on Fedora: libva-1.5.1-1.fc23.src.rpm
