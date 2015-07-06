Name:          gsm
Version:       1.0.13
Release:       1%{?dist}
Summary:       Shared libraries for GSM speech compressor
Group:         System Environment/Libraries
License:       MIT
URL:           http://www.quut.com/gsm/
Source:        http://www.quut.com/gsm/%{name}-%{version}.tar.gz
Patch0:        %{name}-makefile.patch
Patch1:        %{name}-warnings.patch
Patch2:        %{name}-64bit.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%global srcver 1.0-pl13
%global soname 1.0.12

%description
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 162 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

%package       tools
Summary:       GSM speech compressor tools
Group:         Applications/Multimedia

%description    tools
Contains command line utilities for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

%package       devel
Summary:       Header files and development libraries for libgsm
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description    devel
Contains header files and development libraries for libgsm, an
implementation of the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP
(residual pulse excitation/long term prediction) coding at 13 kbit/s.

%prep
%setup -n gsm-%{srcver} -q
%patch0 -p1 -b .mk
%patch1 -p1 -b .warn
%patch2 -p1 -b .64bit

%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fPIC";
make %{?_smp_mflags} all

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/gsm
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/{man1,man3}

make install \
  INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix} \
  GSM_INSTALL_INC=$RPM_BUILD_ROOT%{_includedir}/gsm \
  GSM_INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir}

cp -p $RPM_BUILD_DIR/gsm-%{srcver}/lib/libgsm.so.%{soname} $RPM_BUILD_ROOT%{_libdir}
ln -s libgsm.so.%{soname} $RPM_BUILD_ROOT%{_libdir}/libgsm.so.1
ln -s libgsm.so.%{soname} $RPM_BUILD_ROOT%{_libdir}/libgsm.so
ln -s gsm/gsm.h $RPM_BUILD_ROOT%{_includedir}
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.a

%check
# This is to ensure that the patch creates the proper library version.
[ -f $RPM_BUILD_ROOT%{_libdir}/libgsm.so.%{soname} ]
make addtst

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYRIGHT MACHINES README
%{_libdir}/libgsm.so.*

%files tools
%{_bindir}/tcat
%{_bindir}/toast
%{_bindir}/untoast
%{_mandir}/man1/toast.1*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/gsm
%{_includedir}/gsm/gsm.h
%{_includedir}/gsm.h
%{_libdir}/libgsm.so
%{_mandir}/man3/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with gsm 1.0.13
- Based on CentOS: gsm-1.0.13-11.el7.src.rpm
