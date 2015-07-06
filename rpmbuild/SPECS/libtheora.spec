Name:           libtheora
Epoch:          1
Version:        1.1.1
Release:        1%{?dist}
Summary:        Theora Video Compression Codec
Group:          System Environment/Libraries
License:        BSD
URL:            http://www.theora.org
Source0:        http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.xz
Patch0:         libtheora-1.1.1-fix-pp_sharp_mod-calc.patch
Patch1:         libtheora-png.patch
BuildRequires:  libogg-devel >= 2:1.1
BuildRequires:  libvorbis-devel
BuildRequires:  SDL-devel
BuildRequires:  libpng-devel
BuildRequires:  doxygen
BuildRequires:  tetex-latex
BuildRequires:  transfig
BuildRequires:  libtool

%description
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec; Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.


%package devel
Summary:        Development tools for Theora applications
Group:          Development/Libraries
Requires:       libogg-devel >= 2:1.1
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      theora-exp-devel
Provides:       theora-exp-devel

%description devel
The libtheora-devel package contains the header files needed to develop
applications with libtheora.

%package devel-docs
Summary:        Documentation for developing Theora applications
Group:          Development/Libraries
BuildArch:      noarch

%description devel-docs
The libtheora-devel-docs package contains the documentation needed
to develop applications with libtheora.

%package -n theora-tools
Summary:        Command line tools for Theora videos
Group:          Applications/Multimedia
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description -n theora-tools
The theora-tools package contains simple command line tools for use
with theora bitstreams.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
autoreconf -i -f -I m4
sed -i 's/CFLAGS="$CFLAGS $cflags_save"/CFLAGS="$cflags_save"/g' configure

%build
export LDFLAGS="$LDFLAGS -lm"
%configure --enable-shared --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make
make -C doc/spec

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -r $RPM_BUILD_ROOT/%{_docdir}/*

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 examples/.libs/dump_video $RPM_BUILD_ROOT/%{_bindir}/theora_dump_video
install -m 755 examples/.libs/encoder_example $RPM_BUILD_ROOT/%{_bindir}/theora_encode
install -m 755 examples/.libs/player_example $RPM_BUILD_ROOT/%{_bindir}/theora_player
install -m 755 examples/.libs/png2theora $RPM_BUILD_ROOT/%{_bindir}/png2theora

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/theora
%{_libdir}/*.so
%{_libdir}/pkgconfig/theora*.pc

%files devel-docs
%doc doc/libtheora/html doc/vp3-format.txt doc/spec/Theora.pdf
%doc doc/color.html doc/draft-ietf-avt-rtp-theora-00.txt

%files -n theora-tools
%{_bindir}/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Patched for libpng 1.6.17

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libtheora 1.1.1
- Based on CentOS: libtheora-1.1.1-8.el7.src.rpm
