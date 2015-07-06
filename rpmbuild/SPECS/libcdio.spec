Name:            libcdio
Version:         0.93
Release:         1%{?dist}
Summary:         CD-ROM input and control library
Group:           System Environment/Libraries
License:         GPLv3+
URL:             http://www.gnu.org/software/libcdio/
Source0:         http://ftp.gnu.org/gnu/libcdio/libcdio-0.93.tar.gz
Source1:         http://ftp.gnu.org/gnu/libcdio/libcdio-0.93.tar.gz.sig
Source2:         libcdio-no_date_footer.hml
Source3:         cdio_config.h
Patch0:          libcdio-0.93-udf-bigendian.patch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:   pkgconfig
BuildRequires:   doxygen
BuildRequires:   ncurses-devel
BuildRequires:   help2man
BuildRequires:   gettext-devel
BuildRequires:   chrpath
Requires(post):  /sbin/ldconfig
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info

%if 0%{?fedora} >= 23
# ABI compatibility package dropped in F23
Obsoletes: compat-libcdio15 < 0.93
%endif

%description
This library provides an interface for CD-ROM access. It can be used
by applications that need OS- and device-independent access to CD-ROM
devices.

%package devel
Summary:         Header files and libraries for %{name}
Group:           Development/Libraries
Requires:        %{name} = %{version}-%{release}

%description devel
This package contains header files and libraries for %{name}.

%prep
%setup -q
%patch0 -p1 -b .udf-bigendian

iconv -f ISO88591 -t utf-8 -o THANKS.utf8 THANKS && mv THANKS.utf8 THANKS

%build
%configure \
  --disable-vcd-info \
  --disable-dependency-tracking \
  --disable-cddb \
  --disable-static \
  --disable-rpath
make %{?_smp_mflags}

sed -i -e "s,%{version}.*$,%{version}\\\",g" include/cdio/version.h

cd doc/doxygen
sed -i -e "s,HTML_FOOTER.*$,HTML_FOOTER = libcdio-no_date_footer.hml,g; \
		s,EXCLUDE .*$,EXCLUDE = ../../include/cdio/cdio_config.h,g;" Doxyfile
cp %{SOURCE2} .
./run_doxygen

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

case `uname -i` in
	i386 | x86_64 | ppc | ppc64 | s390 | s390x | sparc | sparc64 )
		mv $RPM_BUILD_ROOT%{_includedir}/cdio/cdio_config.h $RPM_BUILD_ROOT%{_includedir}/cdio/cdio_config_`uname -i`.h
		install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_includedir}/cdio
		;;
	*)
		;;
esac

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

rm -rf examples
mkdir -p examples/C++
cp -a example/{*.c,README} examples
cp -a example/C++/{*.cpp,README} examples/C++

for i in cd-info iso-read iso-info cd-read cd-drive; do 
	sed -i -e 's, version.*linux-gnu,,g' $RPM_BUILD_ROOT%{_mandir}/man1/$i.1
	sed -i -e 's,lt-,,g;s,LT-,,g' $RPM_BUILD_ROOT%{_mandir}/man1/$i.1
	touch -r src/$i.help2man $RPM_BUILD_ROOT%{_mandir}/man1/$i.1
done

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/*.so.*

%check
# disable test using local CDROM
%{__sed} -i -e "s,testiso9660\$(EXEEXT),,g" \
	    -e "s,testisocd\$(EXEEXT),,g" \
	    -e "s,check_paranoia.sh check_opts.sh, check_opts.sh,g" \
	    test/Makefile
make check

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete %{_infodir}/%{name}.info \
		%{_infodir}/dir 2>/dev/null || :
fi

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README README.libcdio THANKS TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_infodir}/*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
%doc doc/doxygen/html examples
%{_includedir}/cdio
%{_includedir}/cdio++
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libcdio 0.93
- Based on Fedora: libcdio-0.93-6.fc23.src.rpm
