Name:              xvidcore
Version:           1.3.4
Release:           1%{?dist}
Summary:           MPEG-4 Simple and Advanced Simple Profile codec
Group:             System Environment/Libraries
License:           GPLv2+
URL:               http://www.xvid.org/
Source0:           http://downloads.xvid.org/downloads/xvidcore-%{version}.tar.gz
BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:     nasm >= 2.0

%description
The Xvid video codec implements MPEG-4 Simple Profile and Advanced Simple
Profile standards. It permits compressing and decompressing digital video
in order to reduce the required bandwidth of video data for transmission
over computer networks or efficient storage on CDs or DVDs. Due to its
unrivalled quality Xvid has gained great popularity and is used in many
other GPLed applications, like e.g. Transcode, MEncoder, MPlayer, Xine and
many more.

%package devel
Summary:           Development files for the Xvid video codec
Group:             Development/Libraries
Requires:          %{name} = %{version}-%{release}

%description devel
This package contains header files, static library and API
documentation for the Xvid video codec.

%prep
%setup -q -n %{name}
chmod -x examples/*.pl
f=AUTHORS ; iconv -f iso-8859-1 -t utf-8 -o $f.utf8 $f && touch -r $f $f.utf8 && mv $f.utf8 $f
%{__perl} -pi -e 's/^\t@(?!echo\b)/\t/' build/generic/Makefile

%build
cd build/generic
export CFLAGS="$RPM_OPT_FLAGS -ffast-math"
%configure
make %{?_smp_mflags} 
cd -

%install
rm -rf $RPM_BUILD_ROOT
make -C build/generic install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libxvidcore.a
cd $RPM_BUILD_ROOT%{_libdir}
chmod 755 libxvidcore.so*
/sbin/ldconfig -n .
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README AUTHORS ChangeLog
%{_libdir}/libxvidcore.so.*

%files devel
%defattr(-,root,root,-)
%doc CodingStyle TODO examples/
%{_includedir}/xvid.h
%{_libdir}/libxvidcore.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with xvidcore 1.3.4
- Based on Fedora: xvidcore-1.3.2-6.fc22.src
