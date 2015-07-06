%global            commit e822ae33c3547e0dcc8a32da97f987427b8bfe1d
%global            commitdate 20140901
%global            checkout %{commitdate}git%{shortcommit}
%global            shortcommit %(c=%{commit}; echo ${c:0:7})
%global            shortname clc

Name:              libclc
Version:           0.0.1
Release:           1%{?dist}
Summary:           An open source implementation of the OpenCL 1.1 library requirements
License:           BSD
URL:               http://libclc.llvm.org/
Source0:           https://github.com/llvm-mirror/%{name}/archive/%{commit}/%{name}-%{checkout}.tar.xz
ExclusiveArch:     %{ix86} x86_64
BuildRequires:     clang-devel
BuildRequires:     libedit-devel
BuildRequires:     llvm-devel
BuildRequires:     llvm-static
BuildRequires:     python27
BuildRequires:     zlib-devel

%description
libclc is an open source, BSD licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification. The following sections of the specification
impose library requirements:

  * 6.1: Supported Data Types
  * 6.2.3: Explicit Conversions
  * 6.2.4.2: Reinterpreting Types Using as_type() and as_typen()
  * 6.9: Preprocessor Directives and Macros
  * 6.11: Built-in Functions
  * 9.3: Double Precision Floating-Point
  * 9.4: 64-bit Atomics
  * 9.5: Writing to 3D image memory objects
  * 9.6: Half Precision Floating-Point

libclc is intended to be used with the Clang compilers OpenCL frontend.

libclc is designed to be portable and extensible. To this end, it provides
generic implementations of most library requirements, allowing the target
to override the generic implementation at the granularity of individual
functions.

libclc currently only supports the PTX target, but support for more
targets is welcome.

%package devel
Summary:           Development files for %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n "%{name}-%{commitdate}git%{shortcommit}"

%build
CFLAGS="%{optflags} -D__extern_always_inline=inline"
./configure.py --prefix=%{_prefix} --libexecdir=%{_libdir}/%{shortname}/ --pkgconfigdir=%{_libdir}/pkgconfig/

sed -i "s/fstack-protector-strong/fstack-protector/" Makefile

make %{?_smp_mflags}

%install
%make_install

%files
%doc LICENSE.TXT README.TXT CREDITS.TXT
%{_libdir}/%{shortname}/*.bc
%{_includedir}/%{shortname}

%files devel
%doc
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libclc 0.0.1 
- Based on Fedora: libclc-0.0.1-10.20140901gite822ae3.fc23.src
