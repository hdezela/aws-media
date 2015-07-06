Name:          ilmbase
Summary:       Abstraction/convenience libraries
Version:       2.2.0
Release:       1%{?dist}
License:       BSD
URL:           http://www.openexr.com/
Source0:       http://download.savannah.nongnu.org/releases/openexr/ilmbase-%{version}.tar.gz
Patch51:       ilmbase-2.2.0-no_undefined.patch
Patch53:       ilmbase-1.0.3-pkgconfig.patch
BuildRequires: pkgconfig
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)

%description
Half is a class that encapsulates the ilm 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%package devel
Summary:       Headers and libraries for building apps that use %{name} 
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%setup -q
%patch51 -p1 -b .no_undefined
%patch53 -p1 -b .pkgconfig

%build
%configure --disable-static

make %{?_smp_mflags} PTHREAD_LIBS="-pthread -lpthread"

%install
make install DESTDIR=%{buildroot}

rm -fv %{buildroot}%{_libdir}/lib*.la

%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion IlmBase)" = "%{version}"
make %{?_smp_mflags} check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libHalf.so.12*
%{_libdir}/libIex-2_2.so.12*
%{_libdir}/libIexMath-2_2.so.12*
%{_libdir}/libIlmThread-2_2.so.12*
%{_libdir}/libImath-2_2.so.12*

%files devel
%{_includedir}/OpenEXR/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/IlmBase.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with ilmbase 2.2.0
- Based on Fedora: ilmbase-2.2.0-4.fc23.src.rpm
