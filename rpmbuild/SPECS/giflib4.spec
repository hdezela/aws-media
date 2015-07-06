Summary:       Old version library for manipulating GIF format image files
Name:          giflib4
Version:       4.1.6
Release:       1%{?dist}
License:       MIT
Group:         System Environment/Libraries
URL:           http://www.sourceforge.net/projects/giflib/
Source:        http://downloads.sourceforge.net/giflib/giflib-%{version}.tar.bz2
BuildRequires: libX11-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libXt-devel
Provides:      libungif = %{version}-%{release}
Obsoletes:     libungif <= %{version}-%{release}
Obsoletes:     giflib < 5.1.1
BuildRoot:     %{_tmppath}/giflib-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The giflib package contains a shared library of functions for loading and
saving GIF format image files. It is API and ABI compatible with libungif,
the library which supported uncompressed GIFs while the Unisys LZW patent
was in effect.

%package devel
Summary:       Development tools for programs using the giflib library
Group:         Development/Libraries
Requires:      giflib4 = %{version}-%{release}
Provides:      libungif-devel = %{version}-%{release}
Obsoletes:     libungif-devel <= %{version}-%{release}
Obsoletes:     giflib-devel < 5.1.1

%description devel
The giflib-devel package includes header files, libraries necessary for
developing programs which use the giflib library to load and save GIF format
image files. It contains the documentation of the giflib library, too.

%prep
%setup -q -n giflib-%{version}

%build
%configure
make %{?_smp_mflags} all

MAJOR=`echo '%{version}' | sed -e 's/\([0-9]\+\)\..*/\1/'`
%{__cc} $RPM_OPT_FLAGS -shared -Wl,-soname,libungif.so.$MAJOR -Llib/.libs -lgif -o libungif.so.%{version}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install

rm -fv $RPM_BUILD_ROOT%{_libdir}/libgif*.la
rm -fv $RPM_BUILD_ROOT%{_mandir}/man5/*
rm -fv $RPM_BUILD_ROOT%{_bindir}/gif*
rm -fv $RPM_BUILD_ROOT%{_bindir}/icon2gif
rm -fv $RPM_BUILD_ROOT%{_bindir}/raw2gif
rm -fv $RPM_BUILD_ROOT%{_bindir}/rgb2gif
rm -fv $RPM_BUILD_ROOT%{_bindir}/text2gif
rm -fv $RPM_BUILD_ROOT%{_libdir}/libgif.so
rm -fv $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libgif.pc
rm -fv $RPM_BUILD_ROOT%{_mandir}/man3/{libgif}.3*
rm -fv $RPM_BUILD_ROOT%{_libdir}/libungif.so.4
rm -fv $RPM_BUILD_ROOT%{_libdir}/libungif.so

rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

rm -f doc/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libgif.so.4
%{_libdir}/libgif.so.4.1.6

%files devel
%defattr(-,root,root,-)
%doc doc/* util/giffiltr.c util/gifspnge.c
%{_libdir}/libgif.so.4
%{_libdir}/libgif.so.4.1.6
%{_includedir}/*.h

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with giflib 4.1.6
- Based on Amazon: giflib-4.1.6-3.1.6.amzn1.src.rpm
- Required for compatibility with EC2 tools and Java
