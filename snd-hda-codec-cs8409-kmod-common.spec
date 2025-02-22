%global debug_package %{nil}

%global short snd-hda-codec-cs8409
%global module_names snd_hda_codec snd_hda_codec_generic

Name:     %{short}-kmod-common
Version:  1.0.0
Release:  1%{?dist}
Summary:  Linux Kernel Sound Driver for Cirrus Logic CS8409 kmod common files
License:  GPL-2.0-or-later
URL:      https://github.com/egorenar/snd-hda-codec-cs8409

Requires: %{short}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Linux Kernel Sound Driver for Cirrus Logic CS8409 kmod common files

%prep

%build

for module in %{module_names}; do
  echo "$module" > ${module}.conf
  install -D -m 0644 ${module}.conf %{buildroot}%{_modulesloaddir}/${module}.conf
done

%install
mkdir -p %{buildroot}%{_modulesloaddir}
for module in %{module_names}; do
    echo "$module" > ${module}.conf
    install -D -m 0644 ${module}.conf %{buildroot}%{_modulesloaddir}/${module}.conf
done

%files
%{_modulesloaddir}/*.conf

%changelog
* Sat Feb 22 2025 Alexander Egorenkov <egorenar-dev@posteo.net> - 1.0.0-1
- Initial version of the package
