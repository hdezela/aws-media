Name:              libzen
Version:           0.4.31
Release:           1%{?dist}
Summary:           Shared library for libmediainfo and medianfo*
License:           zlib
URL:               http://sourceforge.net/projects/zenlib
Group:             System Environment/Libraries
Source0:           http://downloads.sourceforge.net/zenlib/%{name}_%{version}.tar.bz2
BuildRequires:     doxygen
BuildRequires:     cmake
BuildRequires:     pkgconfig(zlib)

%description
Files shared library for libmediainfo and medianfo-*.

%package doc
Summary:           Documentation for %{name}
Requires:          %{name} = %{version}-%{release}
BuildArch:         noarch

%description doc
Documentation files.

%package devel
Summary:           Include files and mandatory libraries for development
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description devel
Include files and mandatory libraries for development.

%prep
%setup -q -n ZenLib

sed -i 's/ZenLib_PATCH_VERSION "30/ZenLib_PATCH_VERSION "31/' Project/CMake/CMakeLists.txt

sed -i 's/.$//' *.txt
chmod 644 *.txt Source/Doc/Documentation.html

chmod 644 Source/ZenLib/*.h Source/ZenLib/*.cpp \
    Source/ZenLib/Format/Html/*.h Source/ZenLib/Format/Html/*.cpp \
    Source/ZenLib/Format/Http/*.h Source/ZenLib/Format/Http/*.cpp

%build
pushd Source/Doc/
    doxygen -u Doxyfile
    doxygen Doxyfile
popd
cp Source/Doc/*.html ./

mkdir Project/CMake/build
pushd Project/CMake/build
    %cmake ..
    make %{?_smp_mflags}
popd

%install
pushd Project/CMake/build
    %make_install
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc History.txt ReadMe.txt
%license License.txt
%{_libdir}/%{name}.so.*

%files doc
%doc Documentation.html
%doc Doc

%files devel
%{_includedir}/ZenLib
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/zenlib/

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun 9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with libzen 0.4.31
- Based on Fedora: libzen-0.4.31-3.fc23.src.cpio
