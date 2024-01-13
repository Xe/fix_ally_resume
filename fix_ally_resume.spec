Name:           fix_ally_resume
Version:        0.0.1
Release:        1%{?dist}
Summary:        Fixes ROG Ally controllers on resume from suspend
BuildArch:      noarch

License:        MIT
URL:            https://github.com/Xe/fix_ally_resume
Source0:        %{expand:%%(pwd)}

Requires:       bash


%description
A simple script to fix ROG ally on resume from suspend.


%prep
# clean out old files
find . -mindepth 1 -delete
cp -af %{SOURCEURL0}/. .


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_presetdir}/
%{__install} -Dm755 %{name}.sh $RPM_BUILD_ROOT/%{_bindir}
%{__install} -Dm644 %{name}.service $RPM_BUILD_ROOT/%{_unitdir}/
%{__install} -Dm644 %{name}.preset %{buildroot}%{_presetdir}/50-%{name}.preset


%files
%license LICENSE
%{_bindir}/%{name}.sh
%{_unitdir}/%{name}.service
%{_presetdir}/50-%{name}.preset


%post
%systemd_post fix_ally_resume.service


%postun
%systemd_postun fix_ally_resume.service


%changelog
* Sat Jan 13 2024 Xe Iaso <me@xeiaso.net>
- Initial release
- 
