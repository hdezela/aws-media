Name:          ilbc
Summary:       Internet Low Bitrate Codec
Version:       1.1.1
Release:       1%{?dist}
License:       BSD
Group:         Development/Libraries
Source0:       dekkers-libilbc-upstream-1.1.1-9-g88cd161.tar.gz
Patch1:        %{name}-0001-Don-t-build-silently.patch
Patch2:        %{name}-0002-No-dist-xz-for-EL5.patch
Patch3:        ilbc-0003-Suppress-warning-about-unused-parameter-s.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow
band speech and results in a payload bit rate of 13.33 kbit/s with an
encoding frame length of 30 ms and 15.20 kbps with an encoding length
of 20 ms. The iLBC codec enables graceful speech quality degradation in
the case of lost frames, which occurs in connection with lost or
delayed IP packets.

%package	devel
Summary:       development files for %{name}
Group:         Development/Libraries
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig

%description devel
Additional header files for development with %{name}.

%prep
%setup -q -n dekkers-libilbc-88cd161
%patch1 -p1 -b .fedora_specific
%patch2 -p1 -b .epel5_specific
%patch3 -p1 -b .epel5_specific

%build
autoreconf -ivf
%{configure} --disable-static --with-pic
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libilbc.la
cd %{buildroot}%{_libdir}/pkgconfig && ln -s libilbc.pc ilbc.pc

cd %{buildroot}%{_includedir}
ln -s ilbc.h iLBC_decode.h
ln -s ilbc.h iLBC_define.h
ln -s ilbc.h iLBC_encode.h

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING README
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/ilbc.h
# Compat symlinks
%{_includedir}/iLBC_decode.h
%{_includedir}/iLBC_define.h
%{_includedir}/iLBC_encode.h
%{_libdir}/pkgconfig/ilbc.pc
%{_libdir}/pkgconfig/libilbc.pc
%{_libdir}/lib%{name}.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with ilbc 1.1.1
- Based on Fedora: ilbc-1.1.1-8.fc23.src.rpm
