%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-expat
Version:        1.3.0
Release:        1%{?dist}
Summary:        SAX XML parser based on the Expat library
Group:          Development/Libraries
License:        MIT
URL:            http://www.keplerproject.org/luaexpat/
Source0:        http://matthewwild.co.uk/projects/luaexpat/luaexpat-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  lua >= %{luaver}, lua-devel >= %{luaver}
BuildRequires:  expat-devel
Requires:       lua >= %{luaver}

%description
LuaExpat is a SAX XML parser based on the Expat library.

%prep
%setup -q -n luaexpat-%{version}

%build
make %{?_smp_mflags} LUA_CDIR=%{lualibdir} LUA_LDIR=%{luapkgdir} LUA_INC=-I%{_includedir} EXPAT_INC=-I%{_includedir} CFLAGS="%{optflags} -fPIC"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} LUA_CDIR=%{lualibdir} LUA_LDIR=%{luapkgdir} INSTALL='install -p'

%check
lua -e 'package.cpath="./src/?.so;"..package.cpath; dofile("tests/test.lua");'
lua -e 'package.cpath="./src/?.so;" .. package.cpath; package.path="./src/?.lua;" .. package.path; dofile("tests/test-lom.lua");'

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README doc/us/*
%{lualibdir}/*
%{luapkgdir}/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with lua-expat 1.3.0
- Based on CentOS: lua-expat-1.3.0-1.el6.src.cpio
