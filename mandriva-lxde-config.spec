Summary: 	Mandriva LXDE configuration files
Name:    	mandriva-lxde-config
Version: 	0.5.2
Release: 	%mkrel 12
Group:   	Graphical desktop/Other
License: 	GPLv2+
URL:		http://www.lxde.org
# (fwang) http://svn.mandriva.com/svn/soft/mandriva-lxde-config/
Source0: 	%{name}-%{version}.tar.bz2
BuildArch: 	noarch
Obsoletes:	%{name}-Flash < %{version}
Obsoletes:	%{name}-Free < %{version}
Obsoletes:	%{name}-One < %{version}
Obsoletes:	%{name}-Powerpack < %{version}
Conflicts:	lxde-common < 0.5.5-0.git20110721.3
Requires:	mandriva-theme
Requires:	fonts-ttf-droid
Requires:	rosa-elementary-theme
Requires:	rosa-icons
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Configuration files for Mandriva LXDE desktop environment.

%prep
%setup -qn %{name}-%{version}

%install
rm -rf %{buildroot}

install -D desktop.conf -m644 %{buildroot}%{_sysconfdir}/xdg/lxsession/LXDE/desktop.conf
install -D openbox-rc.xml -m644 %{buildroot}%{_datadir}/lxde/openbox/rc.xml

%clean
rm -rf %{buildroot}

%pre
update-alternatives --remove-all lxde-config

%files
%defattr(-,root,root)
%{_sysconfdir}/xdg/lxsession/LXDE/desktop.conf
%{_datadir}/lxde/openbox/rc.xml


%changelog
* Fri Aug 19 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.2-9mdv2011.0
+ Revision: 695309
- add to desktop.conf new options for mdvinput touchpad related

* Fri Aug 19 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.2-8
+ Revision: 695258
- add options for new input configure tools - mdvinput

* Sat Aug 13 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.2-7
+ Revision: 694354
- change desktop number to 1 due future 4 desktops on 3d mode only

* Sun Jul 31 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.2-6
+ Revision: 692575
- add elementary theme and icons to requires

* Mon Jul 04 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.2-5
+ Revision: 688714
- fix scrot execute in openbox rc

* Mon Jul 04 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.2-4
+ Revision: 688693
- set openbox keys printscreen to scrot via gpview for screenshooter

* Thu Jun 30 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.2-3
+ Revision: 688396
- change default font to Droid Sans

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.2-2
+ Revision: 684384
- change icon theme for elementary

* Sun May 01 2011 Funda Wang <fwang@mandriva.org> 0.5.2-1
+ Revision: 661328
- use elementary theme for ldxe

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 0.5.1-1
+ Revision: 643871
- 0.5.1: use qtcurve as default theme

* Wed Jun 09 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5-2mdv2010.1
+ Revision: 547799
- fix typo in desktop.conf file in Flash, Powerpack and One editions
  (spotted by Luca Berra); should finally fix (mdv #59624)

* Fri Dec 11 2009 Funda Wang <fwang@mandriva.org> 0.5-1mdv2010.1
+ Revision: 476260
- new version 0.5

* Sun May 03 2009 Funda Wang <fwang@mandriva.org> 0.4-2mdv2010.0
+ Revision: 370897
- fix requires

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.4-1mdv2010.0
+ Revision: 369383
- New version 0.4 (adopt to lxde-common split)

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.1-6mdv2009.0
+ Revision: 268135
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Mon Jun 02 2008 Funda Wang <fwang@mandriva.org> 0.1-5mdv2009.0
+ Revision: 214158
- requires on post and postun

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 0.1-4mdv2009.0
+ Revision: 214138
- Require lxde-common for /usr/share/lxde

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 0.1-3mdv2009.0
+ Revision: 214124
- fix post script of Flash and Free

* Tue May 13 2008 Funda Wang <fwang@mandriva.org> 0.1-2mdv2009.0
+ Revision: 206527
- conflicts with older lxde-common
- fix url

* Sat May 10 2008 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.0
+ Revision: 205380
- fix group
- import source and spec
- Created package structure for mandriva-lxde-config.

