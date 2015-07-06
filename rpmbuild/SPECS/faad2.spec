Summary:       Library and frontend for decoding MPEG2/4 AAC
Name:          faad2
Epoch:         1
Version:       2.7
Release:       1%{?dist}
License:       GPLv2+
Group:         Applications/Multimedia
URL:           http://www.audiocoding.com/faad2.html
Source:        http://downloads.sourceforge.net/sourceforge/faac/%{name}-%{version}.tar.bz2
Patch0:        %{name}-pic.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
BuildRequires: id3lib-devel
BuildRequires: zlib-devel
BuildRequires: libdrm-devel
Requires:      libdrm

%description
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

%package libs
Summary:       Shared libraries of the FAAD 2 AAC decoder
Group:         System Environment/Libraries
Obsoletes:     %{name} < 1:2.6.1-3
Requires:      libdrm

%description libs
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

This package contains libfaad.

%package devel
Summary:       Development libraries of the FAAD 2 AAC decoder
Group:         Development/Libraries
Requires:      %{name}-libs = %{epoch}:%{version}-%{release}
Requires:      libdrm-devel

%description devel
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

This package contains development files and documentation for libfaad.

%prep
%setup -q
%patch0 -p1 -b .pic
find . -name "*.c" -o -name "*.h" | xargs chmod 644

for f in AUTHORS COPYING ChangeLog NEWS README* TODO ; do
    tr -d '\r' <$f >$f.n && touch -r $f $f.n && mv -f $f.n $f
done

%build
%configure \
  --disable-static \
  --with-drm

sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__rm} %{buildroot}%{_libdir}/libfaad.la
%{__rm} %{buildroot}%{_includedir}/mp4ff{,int}.h
%{__rm} %{buildroot}%{_libdir}/libmp4ff.a
install -dm755 %{buildroot}%{_mandir}/man1
%{__mv} %{buildroot}%{_mandir}/{manm/faad.man,man1/faad.1}

%clean
%{__rm} -rf %{buildroot}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING ChangeLog NEWS README*
%{_bindir}/faad
%{_mandir}/man1/faad.1*

%files libs
%defattr(-,root,root,-)
%{_libdir}/libfaad.so.*

%files devel
%defattr(-, root, root, -)
%doc TODO
%{_includedir}/faad.h
%{_includedir}/neaacdec.h
%{_libdir}/libfaad.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Enabled libdrm support

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with faad2 2.7
- Based on CentOS: faad2-2.7-2.el6.3.src.rpm
