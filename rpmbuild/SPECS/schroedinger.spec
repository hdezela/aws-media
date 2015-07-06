Name:          schroedinger
Version:       1.0.11
Release:       1%{?dist}
Summary:       Portable libraries for the high quality Dirac video codec
Group:         System Environment/Libraries
License:       GPL+ or LGPLv2+ or MIT or MPLv1.1
URL:           http://www.diracvideo.org/
Source0:       http://www.diracvideo.org/download/schroedinger/schroedinger-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: orc-devel >= 0.4.16
BuildRequires: glew-devel >= 1.5.1
BuildRequires: gtk-doc


%description
The Schrödinger project will implement portable libraries for the high
quality Dirac video codec created by BBC Research and
Development. Dirac is a free and open source codec producing very high
image quality video.

The Schrödinger project is a project done by BBC R&D and Fluendo in
order to create a set of high quality decoder and encoder libraries
for the Dirac video codec.

%package devel
Group:         Development/Libraries
Summary:       Development files for schroedinger
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig
Requires:      orc-devel >= 0.4.10

%description devel
Development files for schroedinger

%prep
%setup -q

%build
%configure --disable-static --enable-gtk-doc

sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name \*.la -delete

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING* NEWS TODO
%{_libdir}/libschroedinger-1.0.so.*

%files devel
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/schroedinger
%{_includedir}/schroedinger-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/schroedinger-1.0.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with schroedinger 1.0.11 
- Based on Fedora: schroedinger-1.0.11-9.fc23.src
