%global        api 142
%global        gitdate 20141221
%global        gitversion 6a301b6
%global        snapshot %{gitdate}-%{gitversion}
%global        gver .%{gitdate}git%{gitversion}
%global        branch stable

Summary:       H264/AVC video streams encoder
Name:          x264
Version:       0.142
Release:       1%{?dist}
License:       GPLv2+
Group:         System Environment/Libraries
URL:           http://developers.videolan.org/x264.html
Source0:       %{name}-0.%{api}-%{snapshot}.tar.bz2
Source1:       x264-snapshot.sh
Patch0:        x264-nover.patch
Patch10:       x264-gpac.patch
BuildRequires: perl-Digest-MD5
BuildRequires: gpac-devel-static
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: ffmpeg-devel
BuildRequires: yasm >= 1.0.0
Requires:      %{name}-libs = %{version}-%{release}

%description
x264 is a free library for encoding H264/AVC video streams, written from
scratch.

%package libs
Summary:       Library for encoding H264/AVC video streams
Group:         Development/Libraries

%description libs
x264 is a free library for encoding H264/AVC video streams, written from
scratch.

%package devel
Summary:       Development files for the x264 library
Group:         Development/Libraries
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      pkgconfig

%description devel
x264 is a free library for encoding H264/AVC video streams, written from
scratch.

%global x_configure \
./configure \\\
	--prefix=%{_prefix} \\\
	--exec-prefix=%{_exec_prefix} \\\
	--bindir=%{_bindir} \\\
	--includedir=%{_includedir} \\\
	--extra-cflags="$RPM_OPT_FLAGS" \\\
	--disable-ffms \\\
	--enable-debug \\\
	--enable-shared \\\
	--system-libx264 \\\
	--enable-pic \\\
	--disable-avs

%prep
%setup -q -c -n %{name}-0.%{api}-%{snapshot}
pushd %{name}-0.%{api}-%{snapshot}
%patch0 -p1 -b .nover
%patch10 -p1 -b .gpac
popd

variants="generic generic10"
for variant in $variants ; do
  rm -rf ${variant}
  cp -pr %{name}-0.%{api}-%{snapshot} ${variant}
done

%build
pushd generic
%{x_configure} \
 --host=%{_target_platform} \
 --libdir=%{_libdir}
 %{__make} \
 %{?_smp_mflags}
popd

pushd generic10
%{x_configure} \
 --host=%{_target_platform} \
 --libdir=%{_libdir} \
 --bit-depth=10

sed -i -e "s/SONAME=libx264.so./SONAME=libx26410b.so./" config.mak

%{__make} %{?_smp_mflags}
popd

%install
pushd generic
%{__make} DESTDIR=%{buildroot} install
popd

pushd generic10
SONAME=`grep "^SONAME=" config.mak`
export $SONAME
install -m 755 ${SONAME} %{buildroot}%{_libdir}
ln -fs ${SONAME} %{buildroot}%{_libdir}/libx26410b.so
popd

touch -r generic/version.h %{buildroot}%{_includedir}/x264.h %{buildroot}%{_includedir}/x264_config.h

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(644, root, root, 0755)
%doc generic/AUTHORS generic/COPYING
%attr(755,root,root) %{_bindir}/x264

%files libs
%defattr(644, root, root, 0755)
%{_libdir}/libx264.so.142
%{_libdir}/libx26410b.so.142

%files devel
%defattr(644, root, root, 0755)
%doc generic/doc/*
%{_includedir}/x264.h
%{_includedir}/x264_config.h
%{_libdir}/libx264.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libx26410b.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with x264 2015-06-17 
- Based on Fedora: x264-0.142-12.20141221git6a301b6.fc22.src
