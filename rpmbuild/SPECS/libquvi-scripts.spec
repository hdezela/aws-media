%global debug_package %{nil}

Name:      libquvi-scripts
Version:   0.9.20131130
Release:   1%{?dist}
Summary:   Embedded lua scripts for parsing the media details
License:   AGPLv3+
URL:       http://quvi.sourceforge.net
Source0:   http://downloads.sourceforge.net/project/quvi/0.9/%{name}/%{name}-%{version}.tar.xz
BuildArch: noarch
Requires:  lua-expat
Requires:  lua-socket
Requires:  lua-json
Patch0:    0001-guardian.lua-Update-for-website-changes.patch

%description
libquvi-scripts contains the embedded lua scripts that libquvi
uses for parsing the media details. Some additional utility
scripts are also included.

%prep
%setup -q
%patch0 -p1

%build
%configure --with-nsfw

%install
make install DESTDIR=%{buildroot} pkgconfigdir=%{_datadir}/pkgconfig/

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_datadir}/%{name}
%{_datadir}/pkgconfig/%{name}*.pc
%{_mandir}/man7/%{name}.7*
%{_mandir}/man7/quvi-modules*.7*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libquvi-scripts 0.9
- Based on Fedora: libquvi-scripts-0.9.20131130-5.fc23.src.rpm
