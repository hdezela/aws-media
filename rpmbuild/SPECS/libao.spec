Name:              libao
Version:           1.2.0
Release:           1%{?dist}
Summary:           Cross Platform Audio Output Library
Group:             System Environment/Libraries
License:           GPLv2+
URL:               http://xiph.org/ao/
Source0:           http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.gz
Patch1:            0001-ao_pulse.c-fix-latency-calculation.patch
BuildRequires:     alsa-lib-devel
BuildRequires:     pkgconfig(libpulse)

%description
Libao is a cross platform audio output library. It currently supports
ESD, OSS, Solaris, and IRIX.

%package devel
Summary:           Development files for %{name}
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch1 -p1
sed -i "s/-O20 -ffast-math//" configure

%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
%make_install INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -rf {} \;
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS CHANGES COPYING README
%{_libdir}/libao.so.*
%{_libdir}/ao
%{_mandir}/man5/*

%files devel
%doc doc/*.html doc/*.c doc/*.css
%{_includedir}/ao
%{_libdir}/ckport
%{_libdir}/libao.so
%{_libdir}/pkgconfig/ao.pc
%{_datadir}/aclocal/ao.m4

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libao 1.2.0
- Based on Fedora: libao-1.2.0-5.fc23.src
