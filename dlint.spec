%define name dlint
%define version 1.4.1
%define release  %mkrel 1

Summary: A DNS error checking utility
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://www.domtools.com/pub/%{name}%{version}.tar.gz
Patch0: %{name}-rrfilt.patch
Patch1: %{name}-tempdir.patch
License: GPLv2+
URL: http://www.domtools.com
Group: Networking/Other
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: bind-utils, perl

%description 
This program analyzes any DNS zone you specify, and reports any
problems it finds by displaying errors and warnings.  Then it descends
recursively to examine all zones below the given one (this can be
disabled with a command line option).

%prep
%setup -q -n %{name}%{version}
%patch0 -p1 -b .rrfilt
%patch1 -p1 -b .tempdir
%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_datadir}/%{name} \
	$RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 dlint digparse $RPM_BUILD_ROOT%{_bindir}
install -m 755 digparse $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 dlint.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING CHANGES COPYRIGHT TESTCASES
%{_bindir}/*
%{_datadir}/%{name}/*
%{_mandir}/*/*

