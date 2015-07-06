Name:              fftw
Version:           3.3.4
Release:           1%{?dist}
Summary:           A Fast Fourier Transform library
Group:             System Environment/Libraries
License:           GPLv2+
URL:               http://www.fftw.org
Source0:           http://www.fftw.org/fftw-%{version}.tar.gz
BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:     gcc-gfortran
BuildRequires:     time
BuildRequires:     perl
Requires(post):    info 
Requires(preun):   info

%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package libs
Summary:           FFTW run-time library
Group:             System Environment/Libraries
Provides:          fftw3 = %{version}-%{release}
Obsoletes:         fftw-libs-threads < %{version}-%{release}
Obsoletes:         fftw-libs-openmp < %{version}-%{release}
Requires:          %{name}-libs-single%{?_isa} = %{version}-%{release}
Requires:          %{name}-libs-double%{?_isa} = %{version}-%{release}
Requires:          %{name}-libs-long%{?_isa} = %{version}-%{release}
Requires:          %{name}-libs-quad%{?_isa} = %{version}-%{release}

%description libs
This is a dummy package package, pulling in the individual FFTW
run-time libraries.

%package devel
Summary:           Headers, libraries and docs for the FFTW library
Group:             Development/Libraries
Requires:          pkgconfig
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          %{name}-libs%{?_isa} = %{version}-%{release}
Provides:          fftw3-devel%{?_isa} = %{version}-%{release}
Provides:          fftw3-devel = %{version}-%{release}

%description devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains header files and development libraries needed to
develop programs using the FFTW fast Fourier transform library.

%package libs-double
Summary:           FFTW library, double precision
Group:             Development/Libraries

%description libs-double
This package contains the FFTW library compiled in double precision.

%package libs-single
Summary:           FFTW library, single precision
Group:             Development/Libraries

%description libs-single
This package contains the FFTW library compiled in single precision.

%package libs-long
Summary:           FFTW library, long double precision 
Group:             Development/Libraries

%description libs-long
This package contains the FFTW library compiled in long double
precision.

%package libs-quad
Summary:           FFTW library, quadruple
Group:             Development/Libraries

%description libs-quad
This package contains the FFTW library compiled in quadruple
precision.

%package static
Summary:           Static versions of the FFTW libraries
Group:             Development/Libraries
Requires:          %{name}-devel%{?_isa} = %{version}-%{release}
Provides:          fftw3-static%{?_isa} = %{version}-%{release}
Provides:          fftw3-static = %{version}-%{release}

%description static
The fftw-static package contains the statically linkable version of
the FFTW fast Fourier transform library.

%package doc
Summary:           FFTW library manual
Group:             Documentation
BuildArch:         noarch

%description doc
This package contains the manual for the FFTW fast Fourier transform
library.

%prep
%setup -q

%build
export F77=gfortran

BASEFLAGS="--enable-shared --disable-dependency-tracking --enable-threads --enable-openmp"

prec_name[0]=single
prec_name[1]=double
prec_name[2]=long
prec_name[3]=quad

prec_flags[0]=--enable-single
prec_flags[1]=--enable-double
prec_flags[2]=--enable-long-double
prec_flags[3]=--enable-quad-precision

for((i=0;i<2;i++)); do
 prec_flags[i]+=" --enable-sse2 --enable-avx"
done

for((iprec=0;iprec<4;iprec++))
do
 mkdir ${prec_name[iprec]}${ver_name[iver]}
 cd ${prec_name[iprec]}${ver_name[iver]}
 ln -s ../configure .
 %{configure} ${BASEFLAGS} ${prec_flags[iprec]}
 sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
 sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
 make %{?_smp_mflags}
 cd ..
done

%install
rm -rf %{buildroot}
for ver in single double long quad
do
 make -C $ver install DESTDIR=%{buildroot}
done
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/*.la

%check
bdir=`pwd`
for ver in single double long quad
do 
 export LD_LIBRARY_PATH=$bdir/$ver/.libs:$bdir/$ver/threads/.libs
 make -C $ver check
done

%clean
rm -rf %{buildroot}

%post libs-single -p /sbin/ldconfig
%postun libs-single -p /sbin/ldconfig
%post libs-double -p /sbin/ldconfig
%postun libs-double -p /sbin/ldconfig
%post libs-long -p /sbin/ldconfig
%postun libs-long -p /sbin/ldconfig
%post libs-quad -p /sbin/ldconfig
%postun libs-quad -p /sbin/ldconfig

%post devel
/sbin/install-info --section="Math" %{_infodir}/%{name}.info.gz %{_infodir}/dir  2>/dev/null || :

%preun devel
if [ "$1" = 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir 2>/dev/null || :
fi

%files
%defattr(-,root,root,-)
%doc %{_mandir}/man1/fftw*.1.*
%{_bindir}/fftw*-wisdom*

%files libs
%defattr(-,root,root,-)

%files libs-single
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{_libdir}/libfftw3f.so.*
%{_libdir}/libfftw3f_threads.so.*
%{_libdir}/libfftw3f_omp.so.*

%files libs-double
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{_libdir}/libfftw3.so.*
%{_libdir}/libfftw3_threads.so.*
%{_libdir}/libfftw3_omp.so.*

%files libs-long
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{_libdir}/libfftw3l.so.*
%{_libdir}/libfftw3l_threads.so.*
%{_libdir}/libfftw3l_omp.so.*

%files libs-quad
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{_libdir}/libfftw3q.so.*
%{_libdir}/libfftw3q_threads.so.*
%{_libdir}/libfftw3q_omp.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/FAQ/fftw-faq.html/
%doc %{_infodir}/fftw3.info*
%{_includedir}/fftw3*
%{_libdir}/pkgconfig/fftw3*.pc
%{_libdir}/libfftw3*.so

%files doc
%defattr(-,root,root,-)
%doc doc/*.pdf doc/html/

%files static
%defattr(-,root,root,-)
%{_libdir}/libfftw3*.a

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with fftw 3.3.4
- Based on Fedora: fftw-3.3.4-5.fc22.src.rpm
