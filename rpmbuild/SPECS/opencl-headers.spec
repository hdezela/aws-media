Summary:           Khronos OpenCL development headers
Name:              opencl-headers
Version:           1.2
Release:           1%{?dist}
License:           MIT
URL:               http://www.khronos.org/registry/cl/
BuildArch:         noarch
Source0:           http://www.khronos.org/registry/cl/api/1.2/opencl.h
Source1:           http://www.khronos.org/registry/cl/api/1.2/cl_platform.h
Source2:           http://www.khronos.org/registry/cl/api/1.2/cl.h
Source3:           http://www.khronos.org/registry/cl/api/1.2/cl_ext.h
Source4:           http://www.khronos.org/registry/cl/api/1.2/cl_dx9_media_sharing.h
Source5:           http://www.khronos.org/registry/cl/api/1.2/cl_d3d10.h
Source6:           http://www.khronos.org/registry/cl/api/1.2/cl_d3d11.h
Source7:           http://www.khronos.org/registry/cl/api/1.2/cl_gl.h
Source8:           http://www.khronos.org/registry/cl/api/1.2/cl_gl_ext.h
Source9:           http://www.khronos.org/registry/cl/api/1.2/cl.hpp
Patch0:            arm-nosse2.patch

%description
Khronos OpenCL development headers

%prep
%setup -T -c

cp %{SOURCE9} .
%patch0 -b .nosse2

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_includedir}/CL/
cp \
	%{SOURCE0} \
	%{SOURCE1} \
	%{SOURCE2} \
	%{SOURCE3} \
	%{SOURCE4} \
	%{SOURCE5} \
	%{SOURCE6} \
	%{SOURCE7} \
	%{SOURCE8} \
	cl.hpp \
	$RPM_BUILD_ROOT%{_includedir}/CL/

%files
%dir %{_includedir}/CL
%{_includedir}/CL/opencl.h
%{_includedir}/CL/cl.h
%{_includedir}/CL/cl_ext.h
%{_includedir}/CL/cl_d3d10.h
%{_includedir}/CL/cl_d3d11.h
%{_includedir}/CL/cl_gl.h
%{_includedir}/CL/cl_gl_ext.h
%{_includedir}/CL/cl_platform.h
%{_includedir}/CL/cl_dx9_media_sharing.h
%{_includedir}/CL/cl.hpp

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with opencl-headers 1.2
- Based on Fedora: opencl-headers-1.2-7.fc23.src.rpm
