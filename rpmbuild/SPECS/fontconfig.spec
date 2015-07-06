%global            freetype_version 2.1.4

Summary:           Font configuration and customization library
Name:              fontconfig
Version:           2.11.94
Release:           1%{?dist}
License:           MIT and Public Domain and UCD
Group:             System Environment/Libraries
Source:            http://fontconfig.org/release/%{name}-%{version}.tar.bz2
URL:               http://fontconfig.org
Source1:           25-no-bitmap-fedora.conf
Patch0:            %{name}-sleep-less.patch
BuildRequires:     expat-devel
BuildRequires:     freetype-devel >= %{freetype_version}
BuildRequires:     fontpackages-devel
Requires:          fontpackages-filesystem
Requires(pre):     freetype
Requires(post):    grep
Requires(post):    coreutils
Requires:          font(:lang=en)

%description
Fontconfig is designed to locate fonts within the
system and select them according to requirements specified by 
applications.

%package devel
Summary:           Font configuration and customization library
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          freetype-devel >= %{freetype_version}
Requires:          pkgconfig

%description devel
The fontconfig-devel package includes the header files,
and developer docs for the fontconfig package.

Install fontconfig-devel if you want to develop programs which 
will use fontconfig.

%package devel-doc
Summary:           Development Documentation files for fontconfig library
Group:             Documentation
BuildArch:         noarch
Requires:          %{name}-devel = %{version}-%{release}

%description devel-doc
The fontconfig-devel-doc package contains the documentation files
which is useful for developing applications that uses fontconfig.

%prep
%setup -q
%patch0 -p1 -b .sleep-less

%build
export HASDOCBOOK=no

%configure \
  --with-add-fonts=/usr/share/X11/fonts/Type1,/usr/share/X11/fonts/TTF,/usr/local/share/fonts \
  --disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_fontconfig_templatedir}/25-unhint-nonlatin.conf $RPM_BUILD_ROOT%{_fontconfig_confdir}/

mv $RPM_BUILD_ROOT%{_docdir}/fontconfig/* .
rmdir $RPM_BUILD_ROOT%{_docdir}/fontconfig/

%check
make check

%post
/sbin/ldconfig

umask 0022

mkdir -p %{_localstatedir}/cache/fontconfig

if [ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache --version 2>&1 | grep -q %{version} ; then
  HOME=/root /usr/bin/fc-cache -f
fi

%postun -p /sbin/ldconfig

%files
%doc README AUTHORS COPYING
%doc fontconfig-user.txt fontconfig-user.html
%doc %{_fontconfig_confdir}/README
%{_libdir}/libfontconfig.so.*
%{_bindir}/fc-cache
%{_bindir}/fc-cat
%{_bindir}/fc-list
%{_bindir}/fc-match
%{_bindir}/fc-pattern
%{_bindir}/fc-query
%{_bindir}/fc-scan
%{_bindir}/fc-validate
%{_fontconfig_templatedir}/*.conf
%{_datadir}/xml/fontconfig
%config %{_fontconfig_masterdir}/fonts.conf
%config(noreplace) %{_fontconfig_confdir}/*.conf
%dir %{_localstatedir}/cache/fontconfig
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%{_libdir}/libfontconfig.so
%{_libdir}/pkgconfig/*
%{_includedir}/fontconfig
%{_mandir}/man3/*

%files devel-doc
%doc fontconfig-devel.txt fontconfig-devel

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with fontconfig 2.11.94
- Based on Fedora: fontconfig-2.11.94-2.fc23.src
