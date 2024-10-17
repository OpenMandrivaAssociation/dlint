%define name dlint
%define version 1.4.1
%define release  3

Summary: A DNS error checking utility
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://www.domtools.com/pub/%{name}%{version}.tar.gz
Patch0: %{name}-rrfilt.patch
Patch1: %{name}-tempdir.patch
License: GPLv2+
URL: https://www.domtools.com
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-2mdv2011.0
+ Revision: 617793
- the mass rebuild of 2010.0 packages

* Tue Jun 16 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 1.4.1-1mdv2010.0
+ Revision: 386394
- update to new version 1.4.1
- fix tempdir patch
- bunzip2 patches
- fix license tag

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.4.0-6mdv2009.0
+ Revision: 244356
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.4.0-4mdv2008.1
+ Revision: 124060
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import dlint


* Fri Aug 05 2005 Giuseppe Ghibò <ghibo@mandriva.com> 1.4.0-4mdk
- Rebuilt.

* Sat Feb 07 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.4.0-3mdk
- Added patch from ALT Linux to use mktemp instead of /var/tmp.
- Fixed Patch0 to use digparse into /usr/share/dlint path.

* Wed Feb 19 2003 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.4.0-2mdk
- Rebuilt.

* Fri Jan 11 2002 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.4.0-1mdk
- initial release.
