%define luaver 5.1
%define luacompatver 5.1
%define luacompatlibdir %{_libdir}/lua/%{luacompatver}
%define luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%define lua51dir %{_builddir}/lua51-%{name}-%{version}-%{release}
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%global baseversion 3.0-rc1
%global upstreamname luasocket

Name:          lua-socket
Version:       3.0
Release:       1%{?dist}
Summary:       Network support for the Lua language
Group:         Development/Libraries
License:       MIT
URL:           http://www.tecgraf.puc-rio.br/~diego/professional/luasocket/
Source0:       https://github.com/diegonehab/%{upstreamname}/archive/v%{baseversion}.tar.gz
Patch0:        luasocket-optflags.patch
Patch1:        luasocket-no-global-vars.patch
Patch2:        luasocket-3.0-settimeout.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: lua >= %{luaver}, lua-devel >= %{luaver}
BuildRequires: /usr/bin/iconv
Requires:      lua >= %{luaver}

%package devel
Summary:       Development files for %{name}
Group:         Development/Languages
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description
LuaSocket is a Lua extension library that is composed by two parts: a C core
that provides support for the TCP and UDP transport layers, and a set of Lua
modules that add support for functionality commonly needed by applications
that deal with the Internet.

Among the support modules, the most commonly used implement the SMTP, HTTP
and FTP. In addition there are modules for MIME, URL handling and LTN12.

%description devel
Header files and libraries for building an extension library for the
Lua using %{name}

%prep
%setup -q -n %{upstreamname}-%{baseversion}
%patch0 -p1 -b .optflags
%patch1 -p1 -b .noglobal
%patch2 -p1 -b .settimeout

%build
make %{?_smp_mflags} LUAV=%{luaver} OPTFLAGS="%{optflags} -fPIC" linux
/usr/bin/iconv -f ISO8859-1 -t UTF8 LICENSE >LICENSE.UTF8
mv -f LICENSE.UTF8 LICENSE

%install
rm -rf $RPM_BUILD_ROOT
make install-unix OPTFLAGS="%{optflags}" INSTALL_TOP=$RPM_BUILD_ROOT \
    INSTALL_TOP_CDIR=$RPM_BUILD_ROOT%{lualibdir} \
    INSTALL_TOP_LDIR=$RPM_BUILD_ROOT%{luapkgdir}

install -d $RPM_BUILD_ROOT%{_includedir}/%{upstreamname}
install -p src/*.h $RPM_BUILD_ROOT%{_includedir}/%{upstreamname}

%clean

%files
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README doc/*
%{lualibdir}/*
%{luapkgdir}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{upstreamname}

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with lua-socket 3.0
- Based on CentOS: lua-socket-3.0-0.10.rc1.el6.src.cpio
