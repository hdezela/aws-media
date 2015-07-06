Name:              taglib
Summary:           Audio Meta-Data Library
Version:           1.9.1
Release:           1%{?dist}
License:           LGPLv2 or MPLv1.1
URL:               http://taglib.github.com/
Source0:           http://taglib.github.io/releases/taglib-%{version}.tar.gz
Source1:           taglib-snapshot.sh
Patch2:            taglib-1.5rc1-multilib.patch
Patch1002:         0002-Fixed-ABI-breakage-in-TagLib-String.patch
Patch1003:         0003-Rewrote-ByteVector-replace-simpler.patch
Patch1004:         0001-Fixed-a-wrong-byte-order-handling-on-big-endian-mach.patch
Patch1005:         0001-Added-some-missing-deletes-to-test_flac.cpp.patch
BuildRequires:     cmake
BuildRequires:     pkgconfig
BuildRequires:     zlib-devel
BuildRequires:     doxygen
BuildRequires:     graphviz

%description
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3
files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC,
Speex, WavPack, TrueAudio files, as well as APE Tags.

%package doc
Summary:           API Documentation for %{name}
BuildArch:         noarch

%description doc
This is API documentation generated from the TagLib source code.

%package devel
Summary:           Development files for %{name} 
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description devel
Files needed when building software with %{name}.

%prep
%setup -q -n taglib-%{version}%{?pre}

%patch2 -p1 -b .multilib
%patch1002 -p1 -b .0002
%patch1003 -p1 -b .0003
%patch1004 -p1 -b .bigendian
%patch1005 -p1 -b .delete

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
  %{?with_tests:-DBUILD_TESTS:BOOL=ON} \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}

make docs -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

rm -fr %{apidocdir} ; mkdir %{apidocdir}
cp -a %{_target_platform}/doc/html/ %{apidocdir}/
ln -s html/index.html %{apidocdir}
find %{apidocdir} -name '*.md5' | xargs rm -fv

%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion taglib)" = "%{version}"
test "$(pkg-config --modversion taglib_c)" = "%{version}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS NEWS
%doc COPYING.LGPL COPYING.MPL
%{_libdir}/libtag.so.1*
%{_libdir}/libtag_c.so.0*

%files devel
%doc examples
%{_bindir}/taglib-config
%{_includedir}/taglib/
%{_libdir}/libtag.so
%{_libdir}/libtag_c.so
%{_libdir}/pkgconfig/taglib.pc
%{_libdir}/pkgconfig/taglib_c.pc

%files doc
%doc %{apidocdir}/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with taglib 1.9.1
- Based on Fedora: taglib-1.9.1-10.fc23.src
