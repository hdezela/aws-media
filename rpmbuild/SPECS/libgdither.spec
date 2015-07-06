Name:          libgdither
Version:       0.6
Release:       1%{?dist}
Summary:       Library for applying dithering to PCM audio sources
Group:         System Environment/Libraries
License:       GPLv2+
URL:           http://plugin.org.uk/libgdither/README
Source0:       http://plugin.org.uk/libgdither/libgdither-%{version}.tar.gz
Patch0:        libgdither-0.6-default.patch
Patch1:        libgdither-0.6-gavl.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: fftw-devel >= 3.0.0

%description
Libgdither is a GPL'd library library for performing audio dithering on 
PCM samples. The dithering process should be carried out before reducing 
the bit width of PCM audio data (eg. float to 16 bit int conversions) to 
preserve audio quality.

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
%patch0 -p1 -b .default
%patch1 -p1 -b .gavl_fix

%build
export INIT_CFLAGS="${RPM_OPT_FLAGS}"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

sed -i -e 's|/usr/local|%{_prefix}|g' \
   $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libgdither.pc
sed -i -e 's|%{_prefix}/lib|%{_libdir}|' \
  $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libgdither.pc

%check
make test CFLAGS="${RPM_OPT_FLAGS} -Werror --std=c99 -I%{_builddir}/%{?buildsubdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libgdither/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgdither.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libgdither 0.6
- Based on Fedora: libgdither-0.6-9.fc22.src.rpm
