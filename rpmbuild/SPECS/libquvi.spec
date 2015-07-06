Name:          libquvi
Version:       0.9.4
Release:       1%{?dist}
Summary:       A cross-platform library for parsing flash media stream
License:       AGPLv3+
URL:           http://quvi.sourceforge.net
Source0:       http://downloads.sourceforge.net/project/quvi/0.9/%{name}/%{name}-%{version}.tar.xz
BuildRequires: lua-devel
BuildRequires: lua-socket
BuildRequires: glib2-devel
BuildRequires: libcurl-devel
BuildRequires: libgcrypt-devel
BuildRequires: libproxy-devel
BuildRequires: libquvi-scripts
BuildRequires: doxygen
Requires:      libquvi-scripts

%description
Libquvi is a cross-platform library for parsing flash media stream
URLs with C API.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Obsoletes:     quvi-devel <= 0.2.19
Provides:      quvi-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static --disable-rpath
make %{?_smp_mflags} V=1
make doc

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -delete

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING README 
%{_libdir}/%{name}-0.9-%{version}.so
%{_mandir}/man3/%{name}.3*

%files devel
%{_includedir}/quvi-0.9
%{_libdir}/%{name}-0.9.so
%{_libdir}/pkgconfig/%{name}-0.9.pc
%{_mandir}/man7/quvi-object.7*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libquvi 0.9.4
- Based on Fedora: libquvi-0.9.4-7.fc23.src
