Name:            v4l-utils
Version:         1.6.2
Release:         1%{?dist}
Summary:         Utilities for video4linux and DVB devices
Group:           Applications/System
License:         GPLv2+ and GPLv2
URL:             http://www.linuxtv.org/downloads/v4l-utils/
Source0:         http://linuxtv.org/downloads/v4l-utils/v4l-utils-%{version}.tar.bz2
BuildRequires:   libjpeg-devel
BuildRequires:   kernel-headers
BuildRequires:   alsa-lib-devel
BuildRequires:   doxygen
Requires:        udev
Requires:        libv4l%{?_isa} = %{version}-%{release}

%description
v4l-utils is a collection of various video4linux (V4L) and DVB utilities. The
main v4l-utils package contains cx18-ctl, ir-keytable, ivtv-ctl, v4l2-ctl and
v4l2-sysfs-path.

%package devel-tools
Summary:         Utilities for v4l2 / DVB driver development and debugging
License:         GPLv2+ and GPLv2
Requires:        libv4l%{?_isa} = %{version}-%{release}

%description    devel-tools
Utilities for v4l2 / DVB driver authors: decode_tm6000, v4l2-compliance and
v4l2-dbg.

%package -n libv4l
Summary:         Collection of video4linux support libraries 
Group:           System Environment/Libraries
License:         LGPLv2+ and GPLv2
URL:             http://hansdegoede.livejournal.com/3636.html

%description -n libv4l
libv4l is a collection of libraries which adds a thin abstraction layer on
top of video4linux2 devices. The purpose of this (thin) layer is to make it
easy for application writers to support a wide variety of devices without
having to write separate code for different devices in the same class. libv4l
consists of 3 different libraries: libv4lconvert, libv4l1 and libv4l2.

libv4lconvert offers functions to convert from any (known) pixel-format
to V4l2_PIX_FMT_BGR24 or V4l2_PIX_FMT_YUV420.

libv4l1 offers the (deprecated) v4l1 API on top of v4l2 devices, independent
of the drivers for those devices supporting v4l1 compatibility (which many
v4l2 drivers do not).

libv4l2 offers the v4l2 API on top of v4l2 devices, while adding for the
application transparent libv4lconvert conversion where necessary.

%package -n libdvbv5
Summary:         Libraries to control, scan and zap on Digital TV channels
Group:           Development/Libraries
License:         GPLv2

%description -n libdvbv5
Libraries to control, scan and zap on Digital TV channels

%package -n libv4l-devel
Summary:         Development files for libv4l
Group:           Development/Libraries
License:         LGPLv2+
URL:             http://hansdegoede.livejournal.com/3636.html
Requires:        libv4l%{?_isa} = %{version}-%{release}

%description -n libv4l-devel
The libv4l-devel package contains libraries and header files for
developing applications that use libv4l.

%package -n libdvbv5-devel
Summary:         Development files for libdvbv5
Group:           Development/Libraries
License:         GPLv2
Requires:        libdvbv5%{?_isa} = %{version}-%{release}

%description -n libdvbv5-devel
The libdvbv5-devel package contains libraries and header
files for developing applications that use libdvbv5.

%prep
%setup -q

%build
%configure --disable-static --enable-libdvbv5 --enable-doxygen-man --disable-qv4l2
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
make doxygen-run

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm $RPM_BUILD_ROOT%{_libdir}/{v4l1compat.so,v4l2convert.so}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3/
cp -arv %{_builddir}/%{name}-%{version}/doxygen-doc/man/man3 $RPM_BUILD_ROOT%{_mandir}/
rm $RPM_BUILD_ROOT%{_mandir}/man3/_*3

%post -n libv4l -p /sbin/ldconfig

%postun -n libv4l -p /sbin/ldconfig

%post -n libdvbv5 -p /sbin/ldconfig

%postun -n libdvbv5 -p /sbin/ldconfig

%files
%doc README
%dir %{_sysconfdir}/rc_keymaps
%config(noreplace) %{_sysconfdir}/rc_maps.cfg
/lib/udev/rules.d/70-infrared.rules
/lib/udev/rc_keymaps/*
%{_bindir}/cx18-ctl
%{_bindir}/dvb*
%{_bindir}/ir-keytable
%{_bindir}/ivtv-ctl
%{_bindir}/media-ctl
%{_bindir}/rds-ctl
%{_bindir}/v4l2-ctl
%{_bindir}/v4l2-sysfs-path
%{_mandir}/man1/*.1*

%files devel-tools
%doc README
%{_bindir}/decode_tm6000
%{_bindir}/v4l2-compliance
%{_sbindir}/v4l2-dbg

%files -n libv4l
%doc COPYING.libv4l COPYING ChangeLog README.libv4l TODO
%{_libdir}/libv4l
%{_libdir}/libv4l*.so.*

%files -n libv4l-devel
%doc README.lib-multi-threading
%{_includedir}/libv4l*.h
%{_libdir}/libv4l*.so
%{_libdir}/pkgconfig/libv4l*.pc

%files -n libdvbv5
%doc COPYING ChangeLog lib/libdvbv5/README
%{_libdir}/libdvbv5*.so.*

%files -n libdvbv5-devel
%{_includedir}/libdvbv5/*.h
%{_libdir}/libdvbv5*.so
%{_libdir}/pkgconfig/libdvbv5*.pc
%{_mandir}/man3/*.3*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Disabled qv412

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with v4l 1.6.2
- Based on Fedora: v4l-utils-1.6.2-3.fc23.src.rpm
