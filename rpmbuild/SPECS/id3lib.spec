Summary:       Library for manipulating ID3v1 and ID3v2 tags
Name:          id3lib
Version:       3.8.3
Release:       1%{?dist}
License:       LGPLv2+
Group:         System Environment/Libraries
URL:           http://id3lib.sourceforge.net/
Source0:       http://downloads.sourceforge.net/id3lib/%{name}-%{version}.tar.gz
Source1:       id3lib-no_date_footer.hml
Patch0:        id3lib-dox.patch
Patch1:        id3lib-3.8.3-autoreconf.patch
Patch2:        id3lib-3.8.3-io_helpers-163101.patch
Patch3:        id3lib-3.8.3-mkstemp.patch
Patch4:        id3lib-3.8.3-includes.patch
Patch5:        id3lib-vbr_buffer_overflow.diff
Patch6:        20-create-manpages.patch
Patch7:        60-fix_make_check.patch
Patch8:        60-id3lib-missing-nullpointer-check.patch
Patch9:        id3lib-3.8.3-fix-utf16-stringlists.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: doxygen
BuildRequires: libtool
BuildRequires: zlib-devel

%description
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities. Additionally, it can
tell mp3 header info, like bitrate etc.

%package devel
Summary:        Development tools for the id3lib library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       zlib-devel

%description devel
This package provides files needed to develop with the id3lib library.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .autoreconf
%patch2 -p1 -b .io_helpers-163101
%patch3 -p1 -b .mkstemp
%patch4 -p1 -b .gcc43
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
chmod -x src/*.h src/*.cpp include/id3/*.h
sed -i -e 's/\r//' doc/id3v2.3.0.*
sed -i -e 's|@DOX_DIR_HTML@|%{_docdir}/%{name}-devel-%{version}/api|' \
  doc/index.html.in
iconv -f ISO-8859-1 -t UTF8 ChangeLog > tmp; mv tmp ChangeLog
iconv -f ISO-8859-1 -t UTF8 THANKS > tmp; mv tmp THANKS
sed -i -e "s,HTML_FOOTER.*$,HTML_FOOTER = id3lib-no_date_footer.hml,g" doc/Doxyfile.in
cp %{SOURCE1} doc

%build
autoreconf --force --install
%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags} libid3_la_LIBADD=-lz

%install
make install DESTDIR=$RPM_BUILD_ROOT
make docs
for i in txt html; do
  iconv -f ISO-8859-1 -t UTF8 doc/id3v2.3.0.$i > tmp; mv tmp doc/id3v2.3.0.$i
done
mkdir -p __doc/doc ; cp -p doc/*.{gif,jpg,png,html,txt,ico,css}  __doc/doc
rm -f $RPM_BUILD_ROOT%{_libdir}/libid3.la
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog HISTORY NEWS README THANKS TODO __doc/doc/
%{_libdir}/libid3-3.8.so.*
%{_bindir}/id3convert
%{_bindir}/id3cp
%{_bindir}/id3info
%{_bindir}/id3tag
%{_mandir}/man1/*

%files devel
%doc doc/id3lib.css doc/api/
%{_includedir}/id3.h
%{_includedir}/id3/
%{_libdir}/libid3.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with id3lib 3.8.3
- Based on Epel 6: id3lib-3.8.3-28.el6.src.rpm
