Name:        libmodplug
Version:     0.8.8.5
Release:     1%{?dist}
Epoch:       1
Summary:     Modplug mod music file format library
Group:       System Environment/Libraries
License:     Public Domain
URL:         http://modplug-xmms.sourceforge.net/
Source0:     http://downloads.sourceforge.net/modplug-xmms/%{name}-%{version}.tar.gz
Patch0:     %{name}-0.8.4-timiditypaths.patch
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
%{summary}.

%package devel
Summary:     Development files for the Modplug mod music file format library
Group:       Development/Libraries
Requires:    %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
%{summary}.

%prep
%setup -q
%patch0 -p1
sed -i -e 's/\r//g' ChangeLog

%build
%configure
make %{?_smp_mflags} V=1

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make check

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_libdir}/libmodplug.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libmodplug/
%{_libdir}/libmodplug.so
%{_libdir}/pkgconfig/libmodplug.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libmodplug 0.8.8.5
- Based on Fedora: libmodplug-0.8.8.5-6.fc23.src
