Name:          enca
Summary:       Character set analyzer and detector
Version:       1.16
Release:       1%{?dist}
License:       GPLv2
Group:         Applications/Text
Source:        http://dl.cihar.com/enca/enca-%{version}.tar.xz
URL:           http://cihar.com/software/enca

%description
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings using
either a built-in converter or external libraries and tools like libiconv,
librecode, or cstocs.

Currently, it has support for Belarussian, Bulgarian, Croatian, Czech,
Estonian, Latvian, Lithuanian, Polish, Russian, Slovak, Slovene, Ukrainian,
Chinese and some multibyte encodings (mostly variants of Unicode)
independent on the language.

This package also contains shared Enca library other programs can make use of.

Install %{name} if you need to cope with text files of dubious origin
and unknown encoding and convert them to some reasonable encoding.

%package devel
Summary:       Header files and libraries for %{name} charset analyzer
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig

%description devel
The %{name}-devel package contains the static libraries and header files
for writing programs using the Extremely Naive Charset Analyser library,
and its API documentation.

Install %{name}-devel if you are going to create applications using the Enca
library.

%prep
%setup -q

%build

%configure \
  --disable-dependency-tracking \
  --without-librecode \
  --disable-external \
  --disable-static \
  --enable-shared \
  --disable-gtk-doc \
  --disable-rpath

sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT HTML_DIR=/tmp/html

rm -rf $RPM_BUILD_ROOT/tmp/html
rm -rf $RPM_BUILD_ROOT/%{_libexecdir}
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%check
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:$LD_LIBARY_PATH
export LD_LIBRARY_PATH
make check
unset LD_LIBRARY_PATH

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/*
%{_libdir}/libenca.so.*
%{_mandir}/*/*
%doc AUTHORS COPYING FAQ README THANKS TODO

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{?_with_static: %{_libdir}/*.a}
%{_libdir}/*.so
%doc README.devel

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with enca 1.16
- Based on Fedora: enca-1.15-4.fc23.src.rpm
