Summary:       Sample rate conversion library for audio data
Name:          libsamplerate
Version:       0.1.8
Release:       1%{?dist}
License:       GPLv2+
Group:         System Environment/Libraries
URL:           http://www.mega-nerd.com/SRC/
Source0:       http://www.mega-nerd.com/SRC/%{name}-%{version}.tar.gz
BuildRequires: fftw-devel
BuildRequires: libsndfile-devel >= 1.0.6
BuildRequires: pkgconfig

%description
Secret Rabbit Code is a sample rate converter for audio. It is capable
of arbitrary and time varying conversions. It can downsample by a
factor of 12 and upsample by the same factor. The ratio of input and
output sample rates can be a real number. The conversion ratio can
also vary with time for speeding up and slowing down effects.

%package devel
Summary:       Development related files for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}, pkgconfig

%description devel
Secret Rabbit Code is a sample rate converter for audio. It is capable
of arbitrary and time varying conversions. It can downsample by a
factor of 12 and upsample by the same factor. The ratio of input and
output sample rates can be a real number. The conversion ratio can
also vary with time for speeding up and slowing down effects.
This package contains development files for %{name}

%prep
%setup -q

%build
%configure --disable-dependency-tracking --enable-fftw --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/%{name}.la
rm -rf $RPM_BUILD_ROOT%{_docdir}/libsamplerate0-dev _doc
cp -a doc _doc
rm _doc/Makefile*

%check
export LD_LIBRARY_PATH=`pwd`/src/.libs
make check
unset LD_LIBRARY_PATH

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README _doc/*
%{_bindir}/sndfile-resample
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/samplerate.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/samplerate.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libsamplerate 0.1.8
- Based on CentOS: libsamplerate-0.1.8-6.el7.src.rpm
