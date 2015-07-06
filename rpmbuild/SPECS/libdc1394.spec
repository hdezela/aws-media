Summary:       1394-based digital camera control library
Name:          libdc1394
Version:       2.2.2
Release:       1%{?svn_snapshot}%{?dist}
License:       LGPLv2+
Group:         System Environment/Libraries
URL:           http://sourceforge.net/projects/libdc1394/
Source:        http://downloads.sourceforge.net/project/libdc1394/libdc1394-2/%{version}/libdc1394-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
ExcludeArch:   s390 s390x
BuildRequires: kernel-headers
BuildRequires: libraw1394-devel
BuildRequires: libusb1-devel
BuildRequires: doxygen
BuildRequires: libX11-devel
BuildRequires: libXv-devel

%description
Libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification.

%package devel
Summary:       Header files and libraries for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}, libraw1394-devel
Requires:      pkgconfig

%description devel
This package contains the header files and libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package docs
Summary:       Development documentation for %{name}
Group:         Documentation

%description docs
This package contains the development documentation for %{name}.

%package tools
Summary:       Tools for use with %{name}
Group:         Applications/System
Requires:      %{name} = %{version}-%{release}

%description tools
This package contains tools that are useful when working and
developing with %{name}.

%prep
%setup -q -n libdc1394-%{version}

%build
%configure --disable-static --enable-doxygen-html --enable-doxygen-dot
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
make doc

%install
%{__rm} -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
for p in grab_color_image grab_gray_image grab_partial_image ladybug grab_partial_pvn; do
	%{__install} -p -m 0644 -s examples/.libs/$p %{buildroot}%{_bindir}/dc1394_$p
done
%{__install} -p -m 0644 examples/dc1394_multiview %{buildroot}%{_bindir}/dc1394_multiview
for f in grab_color_image grab_gray_image grab_partial_image; do
	mv %{buildroot}%{_mandir}/man1/$f.1 %{buildroot}%{_mandir}/man1/dc1394_$f.1
done

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libdc1394*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc examples/*.h examples/*.c
%{_includedir}/dc1394/
%{_libdir}/libdc1394*.so
%{_libdir}/pkgconfig/%{name}-2.pc
%exclude %{_libdir}/*.la

%files docs
%defattr(-, root, root, 0755)
%doc doc/html/*

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/dc1394_*
%{_mandir}/man1/dc1394_*.1.gz

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libdc1394 2.2.2
- Based on EPEL: libdc1394-2.2.2-3.el7.src.rpm
