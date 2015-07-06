Name:          gavl
Version:       1.4.0
Release:       1%{?dist}
Summary:       A library for handling uncompressed audio and video data
Group:         System Environment/Libraries
License:       GPLv3+
URL:           http://gmerlin.sourceforge.net/
Source0:       http://downloads.sourceforge.net/gmerlin/gavl-%{version}.tar.gz
Patch1:        gavl-1.1.1-system_libgdither.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libtool
BuildRequires: doxygen
BuildRequires: libpng-devel >= 1.0.8
BuildRequires: libgdither-devel

%description
Gavl is a library for handling and converting uncompressed audio and
video data. It provides datatypes for audio/video formats and standardized
structures to store the data. It supports converting between all formats.
Some conversion functions are available in multiple versions (MMX...),
which are selected by compile time configuration, CPU autodetection and
user options.

%package       devel
Summary:       Development files for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch1 -p1 -b .gdither

sed -i -i 's/LQT_TRY_CFLAGS/dnl LQT_TRY_CFLAGS/g' configure.ac
sed -i -i 's/LQT_OPT_CFLAGS/dnl LQT_OPT_CFLAGS/g' configure.ac

sh autogen.sh

%build
%configure \
  --disable-static \
  --disable-cpu-clip \
  --enable-libgdither

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

touch -r include/gavl/gavl.h $RPM_BUILD_ROOT%{_includedir}/gavl/gavl_version.h

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc %{_docdir}/gavl/apiref/
%{_includedir}/gavl/
%{_libdir}/*.so
%{_libdir}/pkgconfig/gavl.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with gavl 1.4.0
- Based on CentOS: gavl-1.4.0-4.el7.src.rpm
