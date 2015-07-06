Name:           lame
Version:        3.99.5
Release:        1%{?dist}
Summary:        Free MP3 audio compressor
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://lame.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/lame/%{name}-%{version}.tar.gz
Patch1:         %{name}-noexecstack.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  nasm
Requires:       %{name}-libs = %{version}-%{release}

%description
LAME is an open source MP3 encoder whose quality and speed matches
commercial encoders. LAME handles MPEG1,2 and 2.5 layer III encoding
with both constant and variable bitrates.

%package libs
Summary:        LAME MP3 encoding library
Group:          System Environment/Libraries

%description libs
LAME MP3 encoding library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}

%description devel
This package development files for %{name}.

%prep
%setup -q
%patch1 -p1 -b .noexec

%build
sed -i -e 's/^\(\s*hardcode_libdir_flag_spec\s*=\).*/\1/' configure
%configure \
  --disable-dependency-tracking \
  --disable-static \
  --enable-nasm \
  --enable-mp3rtp \
  --disable-rpath \
  --disable-gtktest

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
ln -sf lame/lame.h $RPM_BUILD_ROOT%{_includedir}/lame.h
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%check
make test

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root,-)
%doc README TODO USAGE doc/html/*.html
%{_bindir}/lame
%{_bindir}/mp3rtp
%{_mandir}/man1/lame.1*

%files libs
%defattr(-,root,root,-)
%doc ChangeLog COPYING LICENSE
%{_libdir}/libmp3lame.so.*

%files devel
%defattr (-,root,root,-)
%doc API HACKING STYLEGUIDE
%{_libdir}/libmp3lame.so
%{_includedir}/lame/
%{_includedir}/lame.h

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Disabled mp3x

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with lame 3.99.5
- Based on Fedora: lame-3.99.5-5.fc22.src.rpm
