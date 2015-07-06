Name:          flite
Version:       2.0.0
Release:       4%{?dist}
Summary:       Small, fast speech synthesis engine (text-to-speech)
Group:         Applications/Multimedia
License:       CMU
URL:           http://www.festvox.org/flite/
Source0:       http://www.festvox.org/flite/packed/%{name}-%{version}/%{name}-%{version}-release.tar.bz2
Source1:       README-ALSA.txt
Source2:       flite.pc.in
Patch0:        flite-pkgconfig-configure.in.patch
Patch1:        flite-pkgconfig-configure.patch
Patch2:        flite-pkgconfig-Makefile.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: texi2html
BuildRequires: ed
BuildRequires: alsa-lib-devel
BuildRequires: autoconf
BuildRequires: chrpath

%description
Flite (festival-lite) is a small, fast run-time speech synthesis engine
developed at CMU and primarily designed for small embedded machines and/or
large servers. Flite is designed as an alternative synthesis engine to
Festival for voices built using the FestVox suite of voice building tools.

%package devel
Summary:       Development files for flite
Group:         Development/Libraries
Requires:      flite = %{version}-%{release}

%description devel
Development files for Flite, a small, fast speech synthesis engine.

%prep
%setup -q -n %{name}-%{version}-release
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
%configure \
  --enable-shared \
  --with-audio=alsa \
  --with-pic \

make

cd doc
make flite.html

%install
rm -rf %{buildroot}
make install INSTALLBINDIR=%{buildroot}%{_bindir} INSTALLLIBDIR=%{buildroot}%{_libdir}  INSTALLINCDIR=%{buildroot}%{_includedir}/flite

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/flite_cmu_time_awb
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/flite_cmu_us_slt
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/flite_cmu_us_rms
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/flite_cmu_us_kal
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/flite_cmu_us_kal16
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/flite_cmu_us_awb
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/flite

#find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;

ln -s flite.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libflite.pc

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ACKNOWLEDGEMENTS README COPYING doc/html README-ALSA.txt
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/flite
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Patched to add pkgconfig

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with flite 2.0.0
- Based on Fedora: flite-1.3-23.fc22.src
