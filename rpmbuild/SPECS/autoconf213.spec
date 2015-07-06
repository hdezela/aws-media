Summary:           A GNU tool for automatically configuring source code
Name:              autoconf213
Version:           2.13
Release:           1%{?dist}
License:           GPLv2+
Group:             Development/Tools
URL:               http://www.gnu.org/software/autoconf/
Source0:           ftp://prep.ai.mit.edu/pub/gnu/autoconf/autoconf-%{version}.tar.gz
Patch0:            autoconf-2.12-race.patch
Patch1:            autoconf-2.13-mawk.patch
Patch2:            autoconf-2.13-notmp.patch
Patch3:            autoconf-2.13-c++exit.patch
Patch4:            autoconf-2.13-headers.patch
Patch6:            autoconf-2.13-exit.patch
Patch7:            autoconf-2.13-wait3test.patch
Patch8:            autoconf-2.13-make-defs-62361.patch
Patch9:            autoconf-2.13-versioning.patch
Patch10:           autoconf213-destdir.patch
Patch11:           autoconf213-info.patch
Patch12:           autoconf213-testsuite.patch
Buildrequires:     texinfo
Buildrequires:     m4 >= 1.1
Buildrequires:     perl
Buildrequires:     gawk
Buildrequires:     dejagnu
Buildrequires:     flex
Requires:          gawk
Requires:          m4 >= 1.1
Requires:          coreutils
Requires(post):    /sbin/install-info
Requires(preun):   /sbin/install-info
BuildArch:         noarch
BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
GNUs Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to specify
various configuration options.

You should install Autoconf if you are developing software and you
would like to use it to create shell scripts that will configure your
source code packages. If you are installing Autoconf, you will also
need to install the GNU m4 package.

Note that the Autoconf package is not required for the end-user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not their
use.

%prep
%setup -q -n autoconf-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
mv autoconf.texi autoconf213.texi
rm -f autoconf.info

%build
%configure --program-suffix=-%{version}
make

%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=$RPM_BUILD_ROOT

rm ${RPM_BUILD_ROOT}/%{_bindir}/autoscan-%{version}

%check
make check

rm -f ${RPM_BUILD_ROOT}%{_infodir}/standards*

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_infodir}/*.info*
%{_datadir}/autoconf-%{version}/
%doc AUTHORS COPYING NEWS README TODO

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with autoconf213 2.13
- Based on Fedora: autoconf213-2.13-34.fc23.src.rpm
