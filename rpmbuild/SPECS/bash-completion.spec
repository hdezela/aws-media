Name:              bash-completion
Version:           2.1
Release:           1%{?dist}
Epoch:             1
Summary:           Programmable completion for Bash
License:           GPLv2+
URL:               http://bash-completion.alioth.debian.org/
Source0:           http://bash-completion.alioth.debian.org/files/%{name}-%{version}.tar.bz2
Source2:           CHANGES.package.old
Source3:           %{name}-2.0-redefine_filedir.bash
Source4:           script_list
Patch0:            %{name}-1.99-noblacklist.patch
Patch1:            %{name}-2.1-util-linux-223.patch
BuildArch:         noarch
Requires:          bash >= 4.1

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
install -pm 644 %{SOURCE2} .

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/{cowsay,cowthink}
install -pm 644 completions/_udevadm $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/udevadm
for script in $(cat %{SOURCE4}); do
 rm -f $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/$script
done
install -Dpm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/redefine_filedir

%files
%doc AUTHORS CHANGES CHANGES.package.old COPYING README
%config %{_sysconfdir}/profile.d/bash_completion.sh
%{_sysconfdir}/bash_completion.d/
%{_datadir}/bash-completion/
%{_datadir}/pkgconfig/bash-completion.pc

%changelog
* Thu Jun 18 2015 Hugo De Zela <hugodz@winet.com.pe>
- First release
- Spec and sources cleaned up

* Tue Jun  9 2015 Hugo De Zela <hugodz@winet.com.pe>
- First test with bash-completion 2.1
- Based on CentOS: bash-completion-2.1-6.el7.src.rpm
