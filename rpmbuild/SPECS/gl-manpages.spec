%define            debug_package %{nil}
%global            codate 20140424

Name:              gl-manpages
Version:           1.1
Release:           1%{?dist}
Summary:           OpenGL manpages
License:           MIT and Open Publication
URL:               http://www.opengl.org/wiki/Getting_started/XML_Toolchain_and_Man_Pages
Source0:           gl-manpages-%{version}-%{codate}.tar.xz
Source1:           make-gl-man-snapshot.sh
Source2:           http://www.oasis-open.org/docbook/xml/mathml/1.1CR1/dbmathml.dtd
Source3:           http://www.w3.org/Math/DTD/mathml2.tgz
Source4:           gl-manpages-1.0.1.tar.bz2
Source5:           metainfo.xsl
BuildArch:         noarch
BuildRequires:     docbook-style-xsl
BuildRequires:     libxslt

%description
OpenGL manpages

%prep
%setup -q -n %{name}-%{version}-%{codate}
tar xzf %{SOURCE3}
cp -av %{SOURCE2} mathml2/
tar xjf %{SOURCE4}

%build
export BD=`pwd`
xmlcatalog --create --noout \
	--add public "-//W3C//DTD MathML 2.0//EN" "file://$BD/mathml2/mathml2.dtd" \
	--add system "http://www.w3.org/TR/MathML2/dtd/mathml2.dtd" "file://$BD/mathml2/mathml2.dtd" \
	--add public "-//OASIS//DTD DocBook MathML Module V1.1b1//EN" "file://$BD/mathml2/dbmathml.dtd" \
	--add system "http://www.oasis-open.org/docbook/xml/mathml/1.1CR1/dbmathml.dtd" "file://$BD/mathml2/dbmathml.dtd" \
	mathml2.cat
export XML_CATALOG_FILES="$BD/mathml2.cat /etc/xml/catalog"
for MAN in man4 man3 man2 ; do
	pushd $MAN
	for MANP in gl*.xml ; do
		xsltproc --nonet %{SOURCE5} $MANP | xsltproc --nonet /usr/share/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl -
	done
	popd
done

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3/
cp -n {man4,man3,man2}/*.3G $RPM_BUILD_ROOT%{_mandir}/man3/
for MANP in `find gl-manpages-1.0.1 -name *.3gl` ; do
	FN=${MANP//*\//}
	cp -a -n $MANP $RPM_BUILD_ROOT%{_mandir}/man3/${FN/.3gl/.3G}
done
find $RPM_BUILD_ROOT%{_mandir}/man3/ -type f -size -100b | xargs sed -i -e 's/\.3gl/\.3G/' -e 's,^\.so man3G/,.so man3/,'

%files
%{_mandir}/man3/*

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with gl-manpages 1.1
- Based on Fedora: gl-manpages-1.1-9.20140424.fc21.src.rpm
