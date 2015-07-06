Name:              opencl-filesystem
Version:           1.0
Release:           1%{?dist}
Summary:           OpenCL filesystem layout
Group:             System Environment/Libraries
License:           Public Domain
URL:               http://www.khronos.org/registry/cl/
BuildArch:         noarch

%description
This package provides some directories required by packages which use OpenCL.

%prep

%install
mkdir -p %{buildroot}/%{_sysconfdir}/OpenCL/vendors/

%files
%{_sysconfdir}/OpenCL/

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with opencl-filesystem 1.0
- Based on Fedora: opencl-filesystem-1.0-3.fc23.src
