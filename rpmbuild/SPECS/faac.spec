Name:           faac
Version:        1.28
Release:        1%{?dist}
Summary:        Encoder and encoding library for MPEG2/4 AAC
Group:          Applications/Multimedia
License:        LGPLv2+
URL:            http://www.audiocoding.com/
Source0:        http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:         %{name}-libmp4v2.patch
BuildRequires:  libtool
BuildRequires:  libmp4v2-devel

%description
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

%package devel
Summary:        Development libraries of the FAAC AAC encoder
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

This package contains development files and documentation for libfaac.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .mp4v2
find . -type f \( -name \*.h -or -name \*.c \) -exec chmod 644 {} \;
chmod 644 AUTHORS COPYING ChangeLog NEWS README TODO docs/*

/usr/bin/iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && touch -r AUTHORS AUTHORS.conv && /bin/mv -f AUTHORS.conv AUTHORS

autoreconf -vif

%build
%configure --disable-static
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%doc AUTHORS COPYING ChangeLog NEWS README TODO docs/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/%{name}*

%files devel
%exclude  %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with faac 1.28
- Based on Fedora: faac-1.28-7.fc22.src.rpm
