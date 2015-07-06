Name:              madplay
Version:           0.15.2b
Release:           1%{?dist}
Summary:           MPEG audio decoder and player
Group:             Applications/Multimedia
License:           GPLv2+
URL:               http://www.underbit.com/products/mad/
Source0:           http://download.sourceforge.net/mad/%{name}-%{version}.tar.gz
Source1:           mp3license
Patch0:            %{name}-0.15.2b-abxtest-tempfile.patch
Patch1:            http://ftp.debian.org/debian/pool/main/m/madplay/madplay_0.15.2b-4.diff.gz
BuildRoot:         %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:     libmad-devel
BuildRequires:     libid3tag-devel
BuildRequires:     gettext
BuildRequires:     alsa-lib-devel
Requires:          %{_sbindir}/update-alternatives
Provides:          mp3-cmdline
Provides:          mad = %{version}-%{release}
Obsoletes:         mad < %{version}-%{release}

%description
madplay is a command-line MPEG audio decoder and player based on the
MAD library (libmad).  For details about MAD, see the separately
distributed libmad package.

%prep
%setup -q
%patch0
%patch1 -p1
%{__patch} -i debian/patches/00_ucs4.diff
sed -i -e 's/[-lz]/[]/' configure.ac ; sed -i -e 's/ -lz / /' configure
touch -r aclocal.m4 configure.ac
/usr/bin/iconv -f iso8859-1 -t utf-8 CREDITS > CREDITS.conv \
    && /bin/mv CREDITS.conv CREDITS

%build
%configure --with-alsa --disable-dependency-tracking
make %{?_smp_mflags}
make %{?_smp_mflags} madtime

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -pm 755 madtime $RPM_BUILD_ROOT%{_bindir}
cp -p %{SOURCE1} .
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/update-alternatives --install %{_bindir}/mp3-cmdline \
  mp3-cmdline %{_bindir}/madplay 30

%postun
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove mp3-cmdline %{_bindir}/madplay
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_bindir}/abxtest
%{_bindir}/madplay
%{_bindir}/madtime
%{_mandir}/man1/abxtest.1*
%{_mandir}/man1/madplay.1*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with madplay 0.15.2b
- Based on Fedora: madplay-0.15.2b-10.fc22.src
