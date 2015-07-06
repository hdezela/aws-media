%global niarch x64

Name:           openni
Version:        1.5.7.10
Release:        1%{?dist}
Summary:        Library for human-machine Natural Interaction
Group:          System Environment/Libraries
License:        ASL 2.0 and BSD
URL:            http://www.openni.org
Source0:        OpenNI-%{version}.tar.gz
Source1:        libopenni.pc
Patch0:         openni-1.5.7.10-willow.patch
Patch1:         openni-1.5.7.10-fedora.patch
Patch2:         openni-1.5.2.23-disable-sse.patch
Patch3:         openni-1.3.2.1-silence-assert.patch
Patch4:         openni-1.3.2.1-fedora-java.patch
Patch5:         openni-1.5.2.23-disable-softfloat.patch
Patch6:         openni-1.5.2.23-armsamples.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch:  %{ix86} x86_64 %{arm}
BuildRequires:  freeglut-devel
BuildRequires:  tinyxml-devel
BuildRequires:  libjpeg-devel
BuildRequires:  dos2unix
BuildRequires:  libusb1-devel
BuildRequires:  python27
BuildRequires:  doxygen
BuildRequires:  graphviz

%description
OpenNI (Open Natural Interaction) is a multi-language, cross-platform
framework that defines APIs for writing applications utilizing Natural
Interaction. OpenNI APIs are composed of a set of interfaces for writing NI
applications. The main purpose of OpenNI is to form a standard API that
enables communication with both:
 * Vision and audio sensors
 * Vision and audio perception middleware

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        java
Summary:        %{name} Java library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
Requires:       java-headless
Requires:       jpackage-utils

%description    java
The %{name}-java package contains a Java JNI library for
developing applications that use %{name} in Java.

%package        doc
Summary:        API documentation for %{name}
Group:          Documentation
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the automatically generated API documentation
for OpenNI.

%package        examples
Summary:        Sample programs for %{name}
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}

%description    examples
The %{name}-examples package contains example programs for OpenNI.

%prep
%setup -q -n OpenNI-%{version}
%patch0 -p1 -b .willow
%patch1 -p1 -b .fedora
%patch2 -p1 -b .disable-sse
%patch3 -p1 -b .silence-assert
%patch4 -p1 -b .fedora-java
%patch5 -p1 -b .disable-softfloat
%patch6 -p1 -b .armsamples
rm -rf Source/External
rm -rf Platform/Linux/Build/Prerequisites/*
find Samples -name GL -prune -exec rm -rf {} \;
find Samples -name Libs -prune -exec rm -rf {} \;

for ext in c cpp; do
  find Samples -name "*.$ext" -exec \
    sed -i -e 's|#define SAMPLE_XML_PATH "../../../../Data/SamplesConfig.xml"|#define SAMPLE_XML_PATH "%{_sysconfdir}/%{name}/SamplesConfig.xml"|' {} \;
done

sed -i 's|if (os.path.exists("/usr/bin/gmcs"))|if (0)|' Platform/Linux/CreateRedist/Redist_OpenNi.py

dos2unix README
dos2unix LICENSE

%build
cd Platform/Linux/CreateRedist
chmod +x RedistMaker RedistMaker.Arm

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" DEBUG=1 \
./RedistMaker
cat Output/BuildOpenNI.txt


%install
rm -rf $RPM_BUILD_ROOT
pushd Platform/Linux/Redist/OpenNI-Bin-Dev-Linux-%{niarch}-v%{version}
INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir} \
INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir} \
INSTALL_INC=$RPM_BUILD_ROOT%{_includedir}/ni \
INSTALL_VAR=$RPM_BUILD_ROOT%{_var}/lib/ni \
INSTALL_JAR=$RPM_BUILD_ROOT%{_libdir}/%{name} \
./install.sh -n

install -m 0755 Samples/Bin/%{niarch}-Release/libSample-NiSampleModule.so $RPM_BUILD_ROOT%{_libdir}/libNiSampleModule.so
install -m 0755 Samples/Bin/%{niarch}-Release/NiViewer $RPM_BUILD_ROOT%{_bindir}
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiAudioSample $RPM_BUILD_ROOT%{_bindir}/NiAudioSample
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiBackRecorder $RPM_BUILD_ROOT%{_bindir}/NiBackRecorder
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiConvertXToONI $RPM_BUILD_ROOT%{_bindir}/NiConvertXToONI
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiCRead $RPM_BUILD_ROOT%{_bindir}/NiCRead
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiRecordSynthetic $RPM_BUILD_ROOT%{_bindir}/NiRecordSynthetic
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleCreate $RPM_BUILD_ROOT%{_bindir}/NiSimpleCreate
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleRead $RPM_BUILD_ROOT%{_bindir}/NiSimpleRead
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleViewer $RPM_BUILD_ROOT%{_bindir}/NiSimpleViewer
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiUserTracker $RPM_BUILD_ROOT%{_bindir}/NiUserTracker

popd

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 0644 Data/SamplesConfig.xml $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_var}/lib/ni
touch $RPM_BUILD_ROOT%{_var}/lib/ni/modules.xml

mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -e 's![@]prefix[@]!%{_prefix}!g' \
    -e 's![@]exec_prefix[@]!%{_exec_prefix}!g' \
    -e 's![@]libdir[@]!%{_libdir}!g' \
    -e 's![@]includedir[@]!%{_includedir}!g' \
    -e 's![@]version[@]!%{version}!g' \
    %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/libopenni.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
if [ $1 == 1 ]; then
  niReg -r %{_libdir}/libnimMockNodes.so
  niReg -r %{_libdir}/libnimCodecs.so
  niReg -r %{_libdir}/libnimRecorder.so
fi

%preun
if [ $1 == 0 ]; then
  niReg -u %{_libdir}/libnimMockNodes.so
  niReg -u %{_libdir}/libnimCodecs.so
  niReg -u %{_libdir}/libnimRecorder.so
fi

%postun -p /sbin/ldconfig

%files
%doc LICENSE README NOTICE CHANGES
%dir %{_sysconfdir}/%{name}
%dir %{_var}/lib/ni
%ghost %{_var}/lib/ni/modules.xml
%{_libdir}/*.so
%{_bindir}/ni*

%files devel
%doc Documentation/OpenNI_UserGuide.pdf
%{_includedir}/*
%{_libdir}/pkgconfig/libopenni.pc

%files java
%{_libdir}/%{name}

%files examples
%config(noreplace) %{_sysconfdir}/%{name}/SamplesConfig.xml
%{_bindir}/Ni*
# not packaging any .desktop files for the sample applications. The
# applications will print relevant to the console and hence they are
# intended to be run on the console, not from the menu

%files doc
%doc Source/DoxyGen/html

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with openni 1.5.7.10
- Based on Fedora: openni-1.5.7.10-6.fc23.src.rpm
