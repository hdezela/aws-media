%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}

Name:          lua-lpeg
Version:       0.9
Release:       1%{?dist}
Summary:       Parsing Expression Grammars for Lua
Group:         Development/Libraries
License:       MIT
URL:           http://www.inf.puc-rio.br/~roberto/lpeg.html
Source0:       http://www.inf.puc-rio.br/~roberto/lpeg/lpeg-0.9.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: lua >= %{luaver}
BuildRequires: lua-devel >= %{luaver}
Requires:      lua >= %{luaver}

%description
LPeg is a new pattern-matching library for Lua, based on Parsing Expression
Grammars (PEGs).

%prep
%setup -q -n lpeg-%{version}
%{__sed} -i -e "s|/usr/local/bin/lua5.1|%{_bindir}/lua|" test.lua
%{__chmod} -x test.lua

%build
%{__cc} %{optflags} -fPIC -c -o lpeg.o lpeg.c
%{__cc} %{optflags} -fPIC -shared -o lpeg.so.%{version} lpeg.o
%{__ln_s} lpeg.so.%{version} lpeg.so

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{lualibdir}
%{__mkdir_p} %{buildroot}%{luapkgdir}
%{__install} -p lpeg.so.%{version} %{buildroot}%{lualibdir}
%{__ln_s} lpeg.so.%{version} %{buildroot}%{lualibdir}/lpeg.so
%{__install} -p -m 0644 re.lua %{buildroot}%{luapkgdir}

%check
lua test.lua

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc lpeg.html re.html lpeg-128.gif test.lua
%{lualibdir}/*
%{luapkgdir}/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with lua-lpeg 0.9
- Based on CentOS: lua-lpeg-0.9-3.el6.src.cpio
