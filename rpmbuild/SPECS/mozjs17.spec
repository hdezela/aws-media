Summary:           JavaScript interpreter and libraries
Name:              mozjs17
Version:           17.0.0
Release:           1%{?dist}
License:           GPLv2+ or LGPLv2+ or MPLv1.1
Group:             Development/Languages
URL:               http://www.mozilla.org/js/
Source0:           http://ftp.mozilla.org/pub/mozilla.org/js/mozjs%{version}.tar.gz
Patch0:		    js17-build-fixes.patch
Patch1:		    js17-jsval.patch
Patch2:            mozbug746112-no-decommit-on-large-pages.patch
Patch3:            js17-bugzilla-887645.patch
BuildRequires:     pkgconfig(nspr)
BuildRequires:     readline-devel
BuildRequires:     clang
BuildRequires:     /usr/bin/zip
BuildRequires:     python27
BuildRequires:     /usr/bin/autoconf-2.13

%description
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscapes JavaScript is a
superset of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

%package devel
Summary:           Header files, libraries and development documentation for %{name}
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n mozjs%{version}
rm js/src/editline -rf
rm js/src/ctypes/libffi -rf
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
chmod a+x configure
(cd js/src && autoconf-2.13)

%build
CC=clang CXX=clang++ ./configure --disable-static --with-system-nspr --enable-threadsafe --enable-readline --prefix=%{_prefix} --libdir=%{_libdir}
make %{?_smp_mflags}

%check
cat > js/src/config/find_vanilla_new_calls << EOF
#!/bin/bash
exit 0
EOF
make -C js/src check

%install
make install DESTDIR=%{buildroot}
find %{buildroot}/usr/include -type f -exec chmod a-x {} \;
chmod a-x  %{buildroot}/usr/lib64/pkgconfig/*.pc
rm -f %{buildroot}/usr/lib64/*.a
rm -f %{buildroot}/usr/bin/js17
rm -f %{buildroot}/usr/bin/js17-config

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE README
%{_libdir}/*.so

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/js-17.0

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with mozjs17 17.0
- Based on Fedora: mozjs17-17.0.0-8.fc20.src.rpm
- Using clang as C compiler (gcc doesn't seem to work)
- Added patch for https://bugzilla.mozilla.org/show_bug.cgi?id=887645
- Added prefix and libdir, modified paths for install and files
