Summary:       A free ATSC A/52 stream decoder
Name:          a52dec
Version:       0.7.4
Release:       1%{?dist}
License:       GPLv2
Group:         System Environment/Libraries
URL:           http://liba52.sourceforge.net/
Source0:       http://liba52.sourceforge.net/files/%{name}-%{version}.tar.gz
Patch0:        a52dec-configure-optflags.patch
Patch1:        a52dec-0.7.4-rpath64.patch
Patch2:        liba52-silence.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: %{__perl}

%package devel
Summary:       Development files needed for a52dec
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description
liba52 is a free library for decoding ATSC A/52 streams. The A/52
standard is used in a variety of applications, including digital
television and DVD. It is also known as AC-3. The package also
includes a52dec, a small test program for liba52.

%description devel
liba52 is a free library for decoding ATSC A/52 streams. The A/52
standard is used in a variety of applications, including digital
television and DVD. It is also known as AC-3.
This package contains development files for a52dec.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%{__perl} -pi -e 's/-prefer-non-pic\b/-prefer-pic/' \
  configure liba52/configure.incl

%build
%configure \
  --enable-shared \
  --disable-static

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%exclude %{_libdir}/liba52.la
%doc AUTHORS COPYING ChangeLog HISTORY NEWS TODO
%{_libdir}/liba52.so.*
%{_bindir}/a52dec
%{_bindir}/extract_a52
%{_mandir}/man1/a52dec.1*
%{_mandir}/man1/extract_a52.1*

%files devel
%defattr(-,root,root,-)
%doc doc/liba52.txt
%{_includedir}/a52dec
%{_libdir}/liba52.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with a52dec 0.7.4
- Based on Fedora: a52dec-0.7.4-19.fc22.src.rpm
