%global debug_package %{nil}

%define buildforkernels akmod

%define modname snd-hda-codec-cs8409

Name:    %{modname}-kmod
Version: 1.0.0
Release: 1%{?dist}
Summary: Linux Kernel Sound Driver for Cirrus Logic CS8409
License: GPL
URL:     https://github.com/egorenar/snd-hda-codec-cs8409

Group:          System Environment/Kernel

Source:         %{url}/archive/refs/heads/master.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch:  x86_64

BuildRequires: kmodtool
BuildRequires: kernel-devel
BuildRequires: make
BuildRequires: gcc

%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux Kernel Sound Driver for Cirrus Logic CS8409 (e.g. for iMac27 5k)

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo %{repo} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -T -a 0

for kernel_version in %{?kernel_versions} ; do
    pwd
    cp -av * _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    make V=1 %{?_smp_mflags} -C /lib/modules/${kernel_version%%___*}/build CFLAGS_MODULE="-DAPPLE_PINSENSE_FIXUP -DAPPLE_CODECS -DCONFIG_SND_HDA_RECONFIG=1 -Wno-unused-variable -Wno-unused-function" M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done

%install
rm -rf ${RPM_BUILD_ROOT}

for kernel_version in %{?kernel_versions}; do
    install -dm 755 %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}
    install -D -m 755 _kmod_build_${kernel_version%%___*}/snd-hda-codec-cs8409.ko  ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/%{modname}.ko

done
%{?akmod_install}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Feb 22 2025 Alexander Egorenkov <egorenar-dev@posteo.net> - 1.0.0-1
- Initial version of the package
