# norootforbuild

Name:         oscc 
Version:      0.3
Release:      0.6
BuildRequires: bash
%define _prefix  /opt/gnome
License:      GPL
Group:        System/Network
URL:          http://good-question/
Summary:      Offline check of patchlevel of system in supportconfig archive
Source0:      oscc
Source1:      oscc-repos.tar.bz2
Source2:      oscc.conf
Requires:     bash
Autoreqprov:  on
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch

%description
Find out if the packages installed on the system, from which a supporconfig 
originates, are up to date with the current update repositories.
For use with servers without access to any update repositories when the 
supportconfig tarball is created like helpdesk functions and forensic analysis.
The analysis requires access to a RMT or SMT server containing mirrors of the
repositories applicable to the systems to be analysed.

Authors:
--------
    Andreas Taschner        <ataschner@suse.com>         

%define _repodir /opt/oscc

%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%prep
cp %{S:0} .
cp %{S:1} .
cp %{S:2} .


%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
mkdir -p $RPM_BUILD_ROOT/opt/oscc/
mkdir -p $RPM_BUILD_ROOT/var/opt/oscc/
mkdir -p $RPM_BUILD_ROOT/etc/opt/oscc/
install -Dm 755 oscc $RPM_BUILD_ROOT/usr/local/bin/oscc
install -Dm 664 oscc.conf $RPM_BUILD_ROOT/etc/opt/oscc/oscc.conf
install -Dm 764 oscc-repos.tar.bz2 $RPM_BUILD_ROOT%{_repodir}/oscc-repos.tar.bz2


%files
%defattr(-,root,users)
/usr/local/bin/oscc
%attr (774,root,users) %{_repodir} 
%attr (774,root,users) /var/opt/oscc/
%attr (664,root,users) /etc/opt/oscc/oscc.conf 

%post
cd %{_repodir}
tar -xjf oscc-repos.tar.bz2
rm oscc-repos.tar.bz2

chown root.users %{_repodir}/*
chmod 664 %{_repodir}/*

%postun
rm -rf %{_repodir}

%changelog

* Thu Feb 02 2023 - Andreas Taschner <ataschner@suse.com>
- Version 0.3-0.6
  - Added -v option to show version
  - Filter out product entries where vendor is not SUSE
  - Remove SES and SOC parts of configuration file
  - Cleanup SES leftovers
  - Remove support for SOC
  - Remove support for SES
  - Remove support for SLE 11 SP1 through SP3
  - Remove support for SLE 10 SP4
  - Module Certifications on SLES 15 SP3
  - Workstation Extension on SLES 15 SP3
  - SLES 15 SP2 and SP3 are now in LTSS
  - Handle zypper --xmlout option in SLES 15 SP2+
  - Support SLE 15 SP4
* Fri Feb 05 2021 - Andreas Taschner <ataschner@suse.com>
- Version 0.3-0.5
  - Support .bz2 in case of repacked tarballs
  - Support for SLE 15 SP3
  - SLES 15 SP1 is now in LTSS
  - Work around missing XML product data in updates.txt
  - Support for HPC module on SLE 15

* Mon Oct 05 2020 - Andreas Taschner <ataschner@suse.com>
- Version 0.3.0.4
- SLES 12 SP4 is now in LTSS

* Thu May 14 2020 - Andreas Taschner <ataschner@suse.com>
- Version 0.3-0.3

* Wed May 13 2020 - Andreas Taschner <ataschner@suse.com>
- Service Pack specific modules in SLE 15
- Commit 8f9ad142

* Wed May 13 2020 - Andreas Taschner <ataschner@suse.com>
- Enable SUSE PackageHub 15 SP2
- Commit 11ce20e5

* Fri May 08 2020 - Andreas Taschner <ataschner@suse.com>
- Enable SP-specific auto-add of Cloud module
- Commit fb91eea7

* Fri May 08 2020 - Andreas Taschner <ataschner@suse.com>
- Disable debugging code
- Commit fee760ce

* Fri May 08 2020 - Andreas Taschner <ataschner@suse.com>
- Introduce auto-adding of Container module
- Commit da16a387

* Thu Mar 05 2020 - Andreas Taschner <ataschner@suse.com>
- Version 0.3-0.2
- Added support for 
  - SLES 15 SP2
- SLES 15 is now LTSS
- Ignore release-notes packages
- Fixed bug in wiping of Package-Hub repos

* Wed Oct 30 2019 - Andreas Taschner <ataschner@suse.com>
- Version 0.3-0.1
- Added support for 
  - SLES 15 and 15 SP1
  - SLES 12 SP4 and SP5
  - SUSE Package Hub
  - SOC 8
- SLES 12 SP{2,3} and SLES 11 SP4 are now in LTSS
- Discontinued support for SLE 10 SP{1,2,3}
- Packages with 'src' in their name were not included in 
  repodata cache
- Minor bugfixes

* Thu Sep 21 2017 - Andreas Taschner <ataschner@suse.com>
- Version 0.2-0.15
- Added support for 
  - SLES 12 SP3
  - HA, SDK, WE 12 SP3
  - SLE-Module-HPC

* Thu Jun 29 2017 - Andreas Taschner <ataschner@suse.com>
- Version 0.2-0.14
- SLES 12 SP1 is now LTSS
- Cleanup development-leftovers, that disabled repo refreshing
- Correct permissions in /opt/oscc/

* Thu Mar 16 2017 - Andreas Taschner <ataschner@suse.com>
- Version 0.2-0.12
- Added support for SUSE Enterprise Storage 3 and 4 (v1 dropped)
- Distinguish between legacy ($RCE) and SUSE repos when using -w
- Dropped FCS repos to speed up processing. The historical minor 
  discrepancies between the ISO and Pool-repos are 
  insignificant.
- Refresh of SOC repos fixed
- Fix a bug in handling of version strings containing tilde (~)
- Automatic addition of SLE-Module-Public-Cloud product if 
  cloud-init is installed, but the module extension is not

* Tue Feb 21 2017 - Andreas Taschner <ataschner@suse.com>
- Version 0.2-0.11
- Support for SUSE OpenStack Cloud 6 and 7

* Thu Nov 03 2016 - Andreas Taschner <ataschner@suse.com>
- Version 0.2-0.10
- Added support for 
  - SLES 12 SP2
  - HA, SDK, WE 12 SP2
  - SLE-Module-Certifications
  - SLES12-LTSS

* Mon Jul 4 2016 - Andreas Taschner <ataschner@suse.com> 
- Version 0.2-0.9
- Fixed bug in update_repo_cache that caused multiple "current"
  versions of a package
- Log installed products to output file
- Include version info in update_repo_cache screen output

* Wed Jan 13 2016 - Andreas Taschner <ataschner@suse.com>  
- Version 0.2-0.8
- Added support for 
  - SLES 11 SP3 LTSS
  - SLES 12 SP1
  - HA, SDK, WE 12 SP1

* Mon Oct 12 2015 - Andreas Taschner <ataschner@suse.com> 
- Version 0.2-0.7
- Preserve modified config file during RPM upgrade
- Fixed minor RPM package upgrade/removal bugs

* Fri Oct 09 2015 - Andreas Taschner <ataschner@suse.com> 
- Version 0.2-0.6
- Added support for 
  - SLES 11 SP4
  - HAE, SDK 11 SP4
  - SUSE Enterprise Storage 
  - SLE-Module-Toolchain
  - SLE-Module-Containers
- Added -t option to specify temp directory
- Only extract needed files from the supportconfig
- Dropped *-Extension-Store repos, since they will never be
  populated
- Fixed updating of repository cache 
- SLE-WE now also gets updated
- Fixed handling of supportconfig argument that includes path

* Fri Nov 14 2014 - Andreas Taschner <ataschner@suse.com> 
- Version 0.2-0.5
- Since SUSE Customer Center uses token authentication it would
  require reprogramming of this tool in a different language to
  support repobase pointing to update.suse.com.
  Thus it is now only possible to point repobase to the repo
  structure on an SMT server.
- Fixed setup of SLE-Module* repositories

* Wed Oct 29 2014 - Andreas Taschner <ataschner@suse.com> 
- Version 0.2-0.4
- Added support for SLE-WE 12
- Improved handling of multi-version packages

* Wed Oct 15 2014 - Andreas Taschner <ataschner@suse.com> 
- Version 0.2-0.3
- Added support for SLE12 products (major overhaul) :
  - SLES 12
  - SLE-HA 12
  - SLE-SDK 12
  - SLE-Module-Web-Scripting
  - SLE-Module-Legacy
  - SLE-Module-Adv-Systems-Management
- Append timestamp to report file

* Wed Mar 19 2014 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.11
- Removed debug message in product detection

* Tue Mar 18 2014 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.10
- Putty range error fixed
- Include LTSS repositories in show_supported
- Fixed minor bugs in local repobase handling 
  and output when recreating repository

* Thu Mar 06 2014 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.9
- Write report file with findings

* Fri Feb 14 2014 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.8
- Added support for SLES11-SP2-LTSS
- Check for missing database files
- Fixed more bugs in update_repo_cache

* Wed Oct 09 2013 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.7
- Switched to noarch package
- Added support for SLES10-SP1,2,3 including LTSS
- Fixed handling of existing, but still empty repositories
- Turned hacks for empty repositories into decent code
  This obsoletes hacks for SLE11-HAE-SP3-Updates,  
  *-Extension-Store and SLE11-SMT-SP3-Updates
- Made build_repo_list more structured/maintainable

* Mon Aug 5 2013 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.6b
- Refresh of repodata only - no code update

* Wed Jul 24 2013 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.6
- Fixed various bugs in update_repo_cache
- Handling of packages that get removed from repositories
- Now possible to list desired repositories and architectures
  in the config file. Mainly to avoid errors when trying to 
  update repositories, to which the user has no access.
- Introduced -s option to display supported products,
  repositories and architectures
- Removed .sh extension from script name

* Tue Jun 04 2013 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.5
- Replaced filelists.xml* files with dummies in the package in
  order to reduce the size of the RPM (by 99 %). 
- Support for SLE 11 SP3 ;
  - SLES and SDK are full-blown
  - SLE11-HAE-SP3-Updates and SLE11-SMT-SP3-Updates are still
    empty which requires a temporary hack, that will be removed 
    once the repodata is valid
- Fixed validation of nfs and local repos
- Removed sam dependency/bitching

* Fri May 31 2013 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.4
- Credentials can now be set in /etc/opt/oscc/oscc.conf
- Fixed handling of missing updates.txt

* Wed May 08 2013 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.3
- Support for LTSS for SLES11-SP1
- Added -w maintenance mode switch to enable wiping and
  recreating of the cache for a selected repository in case it
  has gone inconsistent/out of sync with itself :)
- Changed maintenance switch syntax
- Optimized checking if repodata needs updating by checking if
  modification date of repodata is newer upstream before 
  downloading the data. For users without SMT and/or slow links.
- Proactively wipe tempdir for leftovers
- Fixed handling corner case of SLE packages from other product
- Support for SMT 11 SP1

* Wed Apr 03 2013 - Andreas Taschner <ataschner@suse.com> 
- Version 0.1-0.2
- Support for SMT 11 SP2
- Misc. bug fixes

* Mon Feb 18 2013 - Andreas Taschner <ataschner@suse.com> 
- Initial Version 0.1-0.1

