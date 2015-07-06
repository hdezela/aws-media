Summary:           Extensible Binary Meta Language library
Name:              libebml
Version:           1.3.1
Release:           1%{?dist}
License:           LGPLv2+
Group:             System Environment/Libraries
URL:               http://www.matroska.org/
Source0:           http://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.bz2

%description
Extensible Binary Meta Language access library A library for reading
and writing files with the Extensible Binary Meta Language, a binary
pendant to XML.

%package devel
Summary:           Development files for the Extensible Binary Meta Language library
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description devel
Extensible Binary Meta Language access library A library for reading
and writing files with the Extensible Binary Meta Language, a binary
pendant to XML.

This package contains the files required to rebuild applications which
will use the Extensible Binary Meta Language library.

%prep
%setup -q
sed -i 's/\r//' ChangeLog LICENSE.LGPL
iconv -f ISO-8859-1 -t UTF-8 ChangeLog > ChangeLog.tmp
touch -r ChangeLog ChangeLog.tmp
mv ChangeLog.tmp ChangeLog

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc ChangeLog LICENSE.LGPL
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/ebml/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libebml 1.3.1
- Based on Fedora: libebml-1.3.1-4.fc23.src
