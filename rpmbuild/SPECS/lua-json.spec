%define luaver 5.1
%define luapkgdir %{_datadir}/lua/%{luaver}
%global commit 7a86bc22066858afeb23845a191a6ab680b46233
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          lua-json
Version:       1.3.2
Release:       1%{?dist}
Summary:       JSON Parser/Constructor for Lua
Group:         Development/Libraries
License:       MIT
URL:           http://luaforge.net/projects/luajson/
Source0:       https://github.com/harningt/luajson/archive/%{commit}/luajson-%{version}-%{shortcommit}.tar.gz
BuildRequires: lua >= %{luaver}, lua-lpeg >= 0.8.1
BuildRequires: lua-filesystem >= 1.4.1, lua-lunit >= 0.4
Requires:      lua >= %{luaver}, lua-lpeg >= 0.8.1
BuildArch:     noarch

%description
LuaJSON is a customizable JSON decoder/encoder, using LPEG for parsing.

%prep
%setup -q -n luajson-%{commit}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{luapkgdir}
cp -pr lua/* $RPM_BUILD_ROOT%{luapkgdir}

%check
make check-regression
make check-unit | tee testlog.txt
grep -q "0 failed, 0 errors" testlog.txt

%files
%doc LICENSE docs/LuaJSON.txt docs/ReleaseNotes-1.0.txt
%{luapkgdir}/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with lua-json 1.3.2
- Based on CentOS: lua-json-1.3.2-2.el6.src.cpio
