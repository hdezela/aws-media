Name:           opencv
Version:        2.4.11
Release:        1%{?dist}
Summary:        Collection of algorithms for computer vision
Group:          Development/Libraries
License:        BSD
URL:            http://opencv.org
Source0:        https://github.com/Itseez/opencv/archive/%{name}-%{version}.tar.gz
Source1:        opencv-samples-Makefile
Patch2:         OpenCV-2.4.4-pillow.patch
Patch3:         opencv-2.4.9-ts_static.patch
Patch4:         opencv-2.4.7-cmake_paths.patch
BuildRequires:  libtool
BuildRequires:  cmake >= 2.6.3
BuildRequires:  chrpath
BuildRequires:  eigen3-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libdc1394-devel
BuildRequires:  jasper-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libv4l-devel
BuildRequires:  libGL-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  openni-devel
BuildRequires:  tbb-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig
BuildRequires:  python27-devel
BuildRequires:  python27-numpy
BuildRequires:  swig >= 1.3.24
BuildRequires:  python27-sphinx
BuildRequires:  ffmpeg-devel >= 0.4.9
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  opencl-headers
Requires:       opencv-core%{_isa} = %{version}-%{release}


%description
OpenCV means Intel® Open Source Computer Vision Library. It is a collection of
C functions and a few C++ classes that implement some popular Image Processing
and Computer Vision algorithms.

%package        core
Summary:        OpenCV core libraries
Group:          Development/Libraries

%description    core
This package contains the OpenCV C/C++ core libraries.

%package        devel
Summary:        Development files for using the OpenCV library
Group:          Development/Libraries
Requires:       opencv%{_isa} = %{version}-%{release}

%description    devel
This package contains the OpenCV C/C++ library and header files, as well as
documentation. It should be installed if you want to develop programs that
will use the OpenCV library. You should consider installing opencv-devel-docs
package.

%package        devel-docs
Summary:        Development files for using the OpenCV library
Group:          Development/Libraries
Requires:       opencv-devel = %{version}-%{release}
BuildArch:      noarch

%description    devel-docs
This package contains the OpenCV documentation and examples programs.

%package        python
Summary:        Python bindings for apps which use OpenCV
Group:          Development/Libraries
Requires:       opencv%{_isa} = %{version}-%{release}
Requires:       numpy

%description    python
This package contains Python bindings for the OpenCV library.

%prep
%setup -q
%patch2 -p1 -b .pillow
%patch3 -p1 -b .ts_static
%patch4 -p1 -b .cmake_paths

sed -i 's|\r||g'  samples/c/adaptiveskindetector.cpp

%build
mkdir -p build
pushd build
%cmake CMAKE_VERBOSE=1 \
  -DPYTHON_PACKAGES_PATH=%{python_sitearch} \
  -DCMAKE_SKIP_RPATH=1 \
  -DENABLE_PRECOMPILED_HEADERS:BOOL=OFF \
  -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo \
  -DBUILD_TEST=1 \
  -DBUILD_opencv_java=0 \
  -DWITH_TBB=1 \
  -DTBB_LIB_DIR=%{_libdir} \
  -DWITH_GSTREAMER=1 \
  -DWITH_GTK=0 \
  -DWITH_GTK_2_X=0 \
  -DWITH_XINE=0 \
  -DWITH_CUDA=0 \
  -DWITH_CUFFT=0 \
  -DWITH_CUBLAS=0 \
  -DWITH_NVCUVID=0 \
  -DWITH_PVAPI=0 \
  -DWITH_GIGEAPI=0 \
  -DWITH_GPHOTO2=0 \
  -DWITH_FFMPEG=1 \
  -DBUILD_opencv_nonfree=1 \
  -DBUILD_opencv_gpu=0 \
  -DBUILD_opencv_python=1 \
  -DWITH_OPENNI=ON \
  -DWITH_VTK=0 \
  -DINSTALL_C_EXAMPLES=1 \
  -DINSTALL_PYTHON_EXAMPLES=1 \
  -DOPENCL_INCLUDE_DIR=${_includedir}/CL \
 ..

make VERBOSE=1 %{?_smp_mflags}

popd

%install
rm -rf __devel-doc
pushd build
make install DESTDIR=%{buildroot} INSTALL="install -p" CPPROG="cp -p"
find %{buildroot} -name '*.la' -delete

install -pm644 %{SOURCE1} %{buildroot}%{_datadir}/OpenCV/samples/GNUmakefile

rm -rf %{buildroot}%{_datadir}/OpenCV/doc

popd

%check
%if 0
pushd build
    LD_LIBRARY_PATH=%{_builddir}/%{tar_name}-%{version}/lib:$LD_LIBARY_PATH make test ARGS=-V || :
popd
%endif

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc LICENSE
%{_bindir}/opencv_*
%{_libdir}/libopencv_calib3d.so.2.4*
%{_libdir}/libopencv_contrib.so.2.4*
%{_libdir}/libopencv_features2d.so.2.4*
%{_libdir}/libopencv_highgui.so.2.4*
%{_libdir}/libopencv_legacy.so.2.4*
%{_libdir}/libopencv_objdetect.so.2.4*
%{_libdir}/libopencv_ocl.so.2.4*
%{_libdir}/libopencv_stitching.so.2.4*
%{_libdir}/libopencv_superres.so.2.4*
%{_libdir}/libopencv_ts.so.2.4*
%{_libdir}/libopencv_videostab.so.2.4*
%dir %{_datadir}/OpenCV
%{_datadir}/OpenCV/haarcascades
%{_datadir}/OpenCV/lbpcascades

%files core
%{_libdir}/libopencv_core.so.2.4*
%{_libdir}/libopencv_flann.so.2.4*
%{_libdir}/libopencv_imgproc.so.2.4*
%{_libdir}/libopencv_ml.so.2.4*
%{_libdir}/libopencv_photo.so.2.4*
%{_libdir}/libopencv_video.so.2.4*
%{_libdir}/libopencv_nonfree.so.2.4*

%files devel
%{_includedir}/opencv
%{_includedir}/opencv2
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/opencv.pc
%dir %{_libdir}/OpenCV/
%{_libdir}/OpenCV/*.cmake

%files devel-docs
%doc doc/*.{htm,png,jpg}
%doc %{_datadir}/OpenCV/samples

%files python
%{python_sitearch}/cv.py*
%{python_sitearch}/cv2.so

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up
- Disabled gtk
- Enabled gstreamer

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with opencv 2.4.11
- Based on Fedora: opencv-2.4.11-1.fc23.src.rpm
