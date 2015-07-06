Name:              libmpeg2
Version:           0.5.1
Release:           1%{?dist}
Summary:           MPEG-2 decoder libraries
Group:             System Environment/Libraries
License:           GPLv2+
URL:               http://libmpeg2.sourceforge.net/
Source0:           http://libmpeg2.sourceforge.net/files/libmpeg2-%{version}.tar.gz
BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:     SDL-devel
BuildRequires:     libXt-devel
BuildRequires:     libXv-devel

%description
libmpeg2 is a free library for decoding mpeg-2 and mpeg-1 video
streams. It is released under the terms of the GPL license.

%package -n mpeg2dec
Summary:           MPEG-2 decoder program
Group:             Applications/Multimedia
Requires:          %{name} = %{version}-%{release}

%description -n mpeg2dec
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package devel
Summary:           Development files for %{name}
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}
Requires:          pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
iconv -f ISO-8859-1 -t UTF-8 AUTHORS > AUTHORS.tmp
touch -r AUTHORS AUTHORS.tmp 
cp -p -f AUTHORS.tmp AUTHORS
rm AUTHORS.tmp

sed -i -e 's/ppc-/noppc64-/' configure.ac configure
sed -i -e 's/powerpc-/nopowerpc64-/' configure.ac configure

%build
%configure --disable-static \

sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} \
  OPT_CFLAGS="-fPIC -DPIC" \

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

install -pm 0644 libmpeg2/mpeg2_internal.h \
  $RPM_BUILD_ROOT%{_includedir}/mpeg2dec/

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files -n mpeg2dec
%defattr(-,root,root,-)
%{_bindir}/corrupt_mpeg2
%{_bindir}/extract_mpeg2
%{_bindir}/mpeg2dec
%{_mandir}/man1/*.1*

%files devel
%defattr(-,root,root,-)
%doc CodingStyle doc/libmpeg2.txt doc/sample*.c
%{_includedir}/mpeg2dec/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmpeg2.pc
%{_libdir}/pkgconfig/libmpeg2convert.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with  libmpeg2 0.5.1
- Based on Fedora: libmpeg2-0.5.1-11.fc22.src
