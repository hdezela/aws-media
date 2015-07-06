%global            tarball mesa-demos
%global            xdriinfo xdriinfo-1.0.4
%global            demodir %{_libdir}/mesa
%define            real_version 8.2.0

Summary:           Mesa demos
Name:              mesa-demos
Version:           10.6.0
Release:           1%{?dist}
License:           MIT
Group:             Development/Libraries
URL:               http://www.mesa3d.org
Source0:           ftp://ftp.freedesktop.org/pub/mesa/demos/8.2.0/%{tarball}-%{real_version}.tar.bz2
Source1:           http://www.x.org/pub/individual/app/%{xdriinfo}.tar.bz2
Source2:           mesad-git-snapshot.sh
Patch0:            mesa-demos-8.0.1-legal.patch
Patch1:            mesa-demos-as-needed.patch
BuildRequires:     pkgconfig
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     libtool
BuildRequires:     freeglut-devel
BuildRequires:     libGL-devel
BuildRequires:     libGLU-devel
BuildRequires:     glew-devel
Obsoletes:         mesa-demos < %{version}-%{release}

%description
This package provides some demo applications for testing Mesa.

%package -n glx-utils
Summary:           GLX utilities
Group:             Development/Libraries
Provides:          glxinfo glxinfo%{?__isa_bits}

%description -n glx-utils
The glx-utils package provides the glxinfo and glxgears utilities.

%prep
%setup -q -n %{tarball}-%{real_version} -b1
%patch0 -p1 -b .legal
%patch1 -p1 -b .asneeded

rm -rf src/demos/pointblast.c
rm -rf src/demos/spriteblast.c

%build
autoreconf -i
%configure --bindir=%{demodir} --with-system-data-files \
  --disable-egl \
  --disable-static
make %{?_smp_mflags}

pushd ../%{xdriinfo}
%configure
make %{?_smp_mflags}
popd

%install
make install DESTDIR=%{buildroot}

pushd ../%{xdriinfo}
make %{?_smp_mflags} install DESTDIR=%{buildroot}
popd

install -m 0755 src/xdemos/glxgears %{buildroot}%{_bindir}
install -m 0755 src/xdemos/glxinfo %{buildroot}%{_bindir}
%if 0%{?__isa_bits} != 0
install -m 0755 src/xdemos/glxinfo %{buildroot}%{_bindir}/glxinfo%{?__isa_bits}
%endif

%check

%files
%{demodir}
%{_datadir}/%{name}/

%files -n glx-utils
%{_bindir}/glxinfo*
%{_bindir}/glxgears
%{_bindir}/xdriinfo
%{_datadir}/man/man1/xdriinfo.1*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with mesa-demos 8.2.0
- Based on Fedora: mesa-demos-8.2.0-2.fc22.src.rpm
- Version changed to 10.6.0 to match Amazon versioning
