Summary:       HE-AAC+ codec
Name:          libaacplus
Version:       2.0.2
Release:       1%{?dist}
License:       3GPP
Group:         Applications/Multimedia
URL:           http://tipok.org.ua/node/17
Source0:       http://tipok.org.ua/downloads/media/aac+/libaacplus/%{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: fftw-devel
BuildRequires: wget

%description
HE-AAC+ v2 library.

%package devel
Summary:       The %{name} development files
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig

%description devel
This package contains development files for %{name}.

%prep
%setup -q

sed -i "s|AM_CONFIG_HEADER|AC_CONFIG_HEADERS|" configure.ac

%build
export LDFLAGS="$LDFLAGS -Wl,-z,now,-z,relro -pie"
export CFLAGS="$RPM_OPT_FLAGS -fPIE -pie"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIE -pie"
./autogen.sh \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir} \
  --enable-shared \
  --disable-static \
  --with-fftw3
./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir} \
  --enable-shared \
  --disable-static \
  --with-fftw3

sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/aacplusenc
%{_libdir}/libaacplus.so.*
%{_mandir}/man1/aacplusenc.1.gz

%files devel
%defattr(-,root,root,-)
%{_libdir}/libaacplus.so
%exclude %{_libdir}/libaacplus.a
%{_libdir}/libaacplus.la
%{_includedir}/aacplus.h
%{_libdir}/pkgconfig/aacplus.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Have to pass prefix/libdir/mandir twice or it defaults to /usr/local

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libaacplus 2.0.2
- New spec file
