%define luaver 5.1
%define luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-lunit
Version:        0.5
Release:        1%{?dist}
Summary:        Unit testing framework for Lua
Group:          Development/Libraries
License:        MIT
URL:            http://nessie.de/mroth/lunit/index.html
Source0:        http://nessie.de/mroth/lunit/lunit-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  lua >= %{luaver}
Requires:       lua >= %{luaver}
BuildArch:      noarch

%description
Lunit is a unit testing framework for lua, written in lua.

Lunit provides 26 assert functions, and a few misc functions for usage
in an easy unit testing framework.

Lunit comes with a test suite to test itself. The testsuite consists
of approximately 710 assertions.

%prep
%setup -q -n lunit-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p lunit $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{luapkgdir}
cp -pr lunit{,-console}.lua $RPM_BUILD_ROOT%{luapkgdir}

%check
./lunit lunit-tests.lua | tee testlog.txt
grep -q "0 failed, 0 errors" testlog.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE ANNOUNCE CHANGES DOCUMENTATION README* example.lua
%{_bindir}/lunit
%{luapkgdir}/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with lua-unit 0.5
- Based on CentOS: lua-lunit-0.5-1.el6.src.cpio
