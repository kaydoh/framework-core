# By default, the RPM will install to the standard REDHAWK SDR root location (/var/redhawk/sdr)
# You can override this at install time using --prefix /new/sdr/root when invoking rpm (preferred method, if you must)
%{!?_sdrroot: %define _sdrroot /var/redhawk/sdr}
%define _prefix %{_sdrroot}
Prefix: %{_prefix}

# Point install paths to locations within our target SDR root
%define _sysconfdir    %{_prefix}/etc
%define _localstatedir %{_prefix}/var
%define _mandir        %{_prefix}/man
%define _infodir       %{_prefix}/info

Name: bad_init_device
Summary: Device %{name}
Version: 1.0.0
Release: 1
License: None
Group: REDHAWK/Devices
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

Requires: redhawk >= 1.9
BuildRequires: redhawk-devel >= 1.9
BuildRequires: autoconf automake libtool

BuildArch: noarch

%description
Device %{name}


%prep
%setup


%build
# Implementation python
pushd python
./reconf
%define _bindir %{_prefix}/dev/devices/bad_init_device/python
%configure
make %{?_smp_mflags}
popd


%install
rm -rf $RPM_BUILD_ROOT
# Implementation python
pushd python
%define _bindir %{_prefix}/dev/devices/bad_init_device/python
make install DESTDIR=$RPM_BUILD_ROOT
popd


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,redhawk,redhawk)
%dir %{_prefix}/dev/devices/%{name}
%{_prefix}/dev/devices/%{name}/bad_init_device.scd.xml
%{_prefix}/dev/devices/%{name}/bad_init_device.prf.xml
%{_prefix}/dev/devices/%{name}/bad_init_device.spd.xml
%{_prefix}/dev/devices/%{name}/python

