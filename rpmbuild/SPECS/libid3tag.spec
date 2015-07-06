Name:          libid3tag
Version:       0.15.1b
Release:       1%{?dist}
Summary:       ID3 tag manipulation library
Group:         System Environment/Libraries
License:       GPLv2+
URL:           http://www.underbit.com/products/mad/
Source0:       http://downloads.sourceforge.net/mad/%{name}-%{version}.tar.gz
Patch0:         libid3tag-0.15.1b-fix_overflow.patch
BuildRequires: zlib-devel >= 1.1.4
BuildRequires: libtool

%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.

%package       devel
Summary:       Development files for %{name}
Group:         Development/Libraries
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description    devel
ID3 tag library development files.

%prep
%setup -q
%patch0 -p0 -b .CVE-2008-2109
touch NEWS AUTHORS ChangeLog
autoreconf -i -f

cat << \EOF > %{name}.pc
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name:          id3tag
Description:   ID3 tag manipulation library
Requires:
Version:       %{version}
Libs:          -lid3tag
Cflags:
EOF

%build
%configure --disable-static
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
install -Dpm 644 %{name}.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/id3tag.pc

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/libid3tag.so.*

%files devel
%{_includedir}/id3tag.h
%{_libdir}/libid3tag.so
%{_libdir}/pkgconfig/id3tag.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libid3tag 0.15.1b
- Based on CentOS: libid3tag-0.15.1b-17.el7.src.rpm
