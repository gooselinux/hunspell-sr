Name: hunspell-sr
Summary: Serbian hunspell dictionaries
%define upstreamid 20090511
Version: 0.%{upstreamid}
Release: 2.1%{?dist}
Source: http://extensions.services.openoffice.org/files/1572/4/dict-sr.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/project/dict-sr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch
Requires: hunspell
Provides: hunspell-bs = %{version}-%{release}

%description
Serbian hunspell dictionaries.

%package -n hyphen-sr
Requires: hyphen
Summary: Serbian hyphenation rules
Group: Applications/Text
Provides: hyphen-bs = %{version}-%{release}

%description -n hyphen-sr
Serbian hyphenation rules.

%prep
%setup -q -c

%build
cp -p README_sh.txt README_hyph.txt

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p sr.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/sr_YU.dic
cp -p sr.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/sr_YU.aff
cp -p sh.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/sh_YU.dic
cp -p sh.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/sh_YU.aff

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_sr_YU.dic
cp -p hyph_sh.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_sh_YU.dic

sr_YU_aliases="sr_ME sr_RS"
sh_YU_aliases="sh_ME sh_RS bs_BA"

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
for lang in $sr_YU_aliases; do
	ln -s sr_YU.aff $lang.aff
	ln -s sr_YU.dic $lang.dic
done
for lang in $sh_YU_aliases; do
	ln -s sh_YU.aff $lang.aff
	ln -s sh_YU.dic $lang.dic
done
popd

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
for lang in $sr_YU_aliases; do
	ln -s hyph_sr_YU.dic "hyph_"$lang".dic"
done
for lang in $sh_YU_aliases; do
	ln -s hyph_sh_YU.dic "hyph_"$lang".dic"
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_sh.txt README_sr.txt registration/license*.txt
%{_datadir}/myspell/*

%files -n hyphen-sr
%doc README_hyph.txt
%defattr(-,root,root,-)
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090511-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090511-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090511-1
- latest version

* Tue May 05 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090213-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080711-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 11 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080711-1
- initial version
