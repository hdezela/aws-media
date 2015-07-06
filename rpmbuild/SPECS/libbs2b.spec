Name:          libbs2b
Version:       3.1.0
Release:       1%{?dist}
Summary:       Bauer stereophonic-to-binaural DSP library
Group:         Applications/Multimedia
License:       Copyright only
URL:           http://bs2b.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/bs2b/bs2b/%{version}/%{name}-%{version}.tar.lzma
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: libsndfile-devel
Requires:      libsndfile

%package devel
Summary:       Development files for libbs2b
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig

%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is designed
to improve headphone listening of stereo audio records. Recommended for
headphone prolonged listening to disable superstereo fatigue without essential
distortions.

%description devel
This package contains the development files for the Bauer
stereophonic-to-binaural (bs2b) DSP effect library.

%prep
%setup -q

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm %{buildroot}/%{_libdir}/%{name}.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libbs2b 3.1.0
- Based on CentOS: libbs2b-3.1.0-2.el6.src.rpm
