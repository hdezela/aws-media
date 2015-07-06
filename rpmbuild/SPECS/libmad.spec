Name:              libmad
Version:           0.15.1b
Release:           1%{?dist}
Summary:           MPEG audio decoder library
Group:             System Environment/Libraries
License:           GPLv2
URL:               http://www.underbit.com/products/mad/
Source0:           http://download.sourceforge.net/mad/%{name}-%{version}.tar.gz
Patch0:            libmad-0.15.1b-multiarch.patch
Patch1:            libmad-0.15.1b-ppc.patch
Patch2:            Provide-Thumb-2-alternative-code-for-MAD_F_MLN.diff
Patch3:            libmad.thumb.diff
BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:     automake
BuildRequires:     autoconf
BuildRequires:     libtool

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

%package devel
Summary:           MPEG audio decoder library development files
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}
Requires:          pkgconfig

%description devel
%{summary}.

%prep
%setup -q
%patch0 -p1 -b .multiarch
%patch1 -p1 -b .ppc
%patch2 -p1 -b .alt_t2
%patch3 -p1 -b .thumb

sed -i -e /-fforce-mem/d configure*
touch -r aclocal.m4 configure.ac NEWS AUTHORS ChangeLog

%{__cat} << EOF > mad.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: mad
Description: MPEG Audio Decoder
Requires:
Version: %{version}
Libs: -L%{_libdir} -lmad -lm
Cflags: -I%{_includedir}
EOF

%build
autoreconf -sfi
%configure \
  --enable-fpm=64bit \
  --disable-dependency-tracking \
  --enable-accuracy \
  --disable-debugging \
  --disable-static

make %{?_smp_mflags} CPPFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%{__install} -D -p -m 0644 mad.pc %{buildroot}%{_libdir}/pkgconfig/mad.pc
touch -r mad.h.sed %{buildroot}/%{_includedir}/mad.h

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/libmad.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libmad.so
%{_libdir}/pkgconfig/mad.pc
%{_includedir}/mad.h

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libmad 0.15.1b
- Based on Fedora: libmad-0.15.1b-17.fc22.src
