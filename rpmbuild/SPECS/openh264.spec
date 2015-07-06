Name:          openh264
Summary:       Open Source H.264 Codec
URL:           http://www.openh264.org/
Group:         System/Libraries
License:       BSD
Version:       1.4.0
Release:       1%{?dist}
Source0:       %{name}-%{version}.tar.gz
BuildRequires: nasm

%description
OpenH264 is a codec library which supports H.264 encoding and decoding.
It is suitable for use in real time applications such as WebRTC.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q
sed -i -e 's| $(PREFIX)| $(DESTDIR)$(PREFIX)|' -e 's| $(SHAREDLIB_DIR)| $(DESTDIR)$(SHAREDLIB_DIR)|' Makefile

%build
make %{_smp_mflags} PREFIX=/usr

%install
%make_install PREFIX=/usr
%ifarch x86_64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%doc README.md LICENSE CONTRIBUTORS
%{_libdir}/lib*

%files devel
%{_includedir}/wels
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with openh264 1.4.0 
- Based on Fedora: openh264-1.3.1-8.1.src
