Summary: 	Mandriva LXDE configuration files
Name:    	mandriva-lxde-config
Version: 	0.5.2
Release: 	%mkrel 1
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
