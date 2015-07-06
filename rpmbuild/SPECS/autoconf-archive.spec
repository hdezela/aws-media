Name:              autoconf-archive
Version:           2015.02.24
Release:           1%{?dist}
Summary:           The Autoconf Macro Archive
License:           GPLv3+ with exceptions
URL:               http://www.gnu.org/software/autoconf-archive/
Source0:           http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
BuildArch:         noarch
Requires:          autoconf
Requires(post):    info
Requires(preun):   info

%description
The GNU Autoconf Archive is a collection of more than 450 macros for
GNU Autoconf that have been contributed as free software by friendly
supporters of the cause from all over the Internet.

%prep
%setup -q
autoreconf -i -f

%build
%configure
make

%install
%make_install INSTALL="install -p"
rm -frv %{buildroot}%{_infodir}/dir
rm -frv %{buildroot}%{_datadir}/%{name}

%post
install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%preun
if [ $1 = 0 ]; then
  install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi

%files
%doc AUTHORS NEWS README TODO COPYING*
%{_datadir}/aclocal/*.m4
%{_infodir}/autoconf-archive.info*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with autoconf-archive 2015.02.24
- Based on Fedora: autoconf-archive-2015.02.24-2.fc23.src
