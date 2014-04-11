# spec file for package sca-server-report
#
# Copyright (C) 2014 SUSE LLC
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

%define sca_common sca
%define libbase /usr/lib/%{sca_common}
%define pybase %{libbase}/python

Name:         sca-server-report
Summary:      Supportconfig Analysis Server Report
URL:          https://bitbucket.org/g23guy/sca-server-report
License:      GPL-2.0
Group:        System/Monitoring
Autoreqprov:  on
Version:      0.9
Release:      18
Source:       %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Requires:     sca-patterns-base
Requires:     python
Requires:     w3m

%description
A tool that primarily analyzes the local server, but can analyze other 
supportconfigs that have been copied to the server. It uses the 
Supportconfig Analysis patterns to perform the analysis.

Authors:
--------
    David Hamner <dhamner@suse.com>
    Jason Record <jrecord@suse.com>

%prep
%setup -q

%build
gzip -9f man/*8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/sbin
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -d $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -d $RPM_BUILD_ROOT/%{pybase}
install -m 444 man/COPYING.GPLv2 $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -m 544 bin/scatool $RPM_BUILD_ROOT/usr/sbin
install -m 644 bin/scatool.py $RPM_BUILD_ROOT/%{pybase}
install -m 644 man/*.8.gz $RPM_BUILD_ROOT/usr/share/man/man8

%files
%defattr(-,root,root)
/usr/sbin/*
%dir %{libbase}
%dir %{pybase}
%{pybase}/*
%dir /usr/share/doc/packages/%{name}
%doc /usr/share/doc/packages/%{name}/*
%doc /usr/share/man/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

