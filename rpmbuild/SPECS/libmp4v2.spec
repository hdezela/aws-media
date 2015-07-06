Summary:       Library for working with files using the mp4 container format
Name:          libmp4v2
Version:       2.0.0
Release:       1%{?dist}
License:       MPLv1.1
Group:         System Environment/Libraries
URL:           http://code.google.com/p/mp4v2
Source0:       http://mp4v2.googlecode.com/files/mp4v2-%{version}.tar.bz2
Patch0:        libmp4v2-help2man.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: libtool
BuildRequires: texinfo

%description
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.

%package devel
Summary:       Development files for the mp4v2 library
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Development files and documentation needed to develop and compile programs
using the libmp4v2 library.

%prep
%setup -q -n mp4v2-%{version}
%patch0 -p1

%build
%configure \
  --disable-static \
  --disable-dependency-tracking

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README COPYING doc/Documentation.txt doc/Authors.txt doc/ReleaseNotes.txt doc/BuildSource.txt doc/ToolGuide.txt
%{_bindir}/*
%{_libdir}/libmp4v2.so.2*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/mp4v2/
%{_libdir}/libmp4v2.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libmp4v2 2.0.0
- Based on EPEL: libmp4v2-2.0.0-2.el7.src.rpm
