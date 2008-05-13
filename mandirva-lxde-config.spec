Summary: 	Mandriva LXDE configuration files
Name:    	mandriva-lxde-config
Version: 	0.1
Release: 	%mkrel 2
Group:   	Graphical desktop/Other
License: 	GPLv2+
URL:		http://www.lxde.org
# (fwang) http://svn.mandriva.com/svn/soft/mandriva-lxde-config/
Source0: 	%{name}-%{version}.tar.bz2
BuildArch: 	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Configuration files for Mandriva LXDE desktop environment.

%package -n %{name}-Flash
Summary: 	Mandriva LXDE Flash configuration files
Group: 		Graphical desktop/Other
Requires:	mandriva-release-Flash
Requires:	mandriva-theme-Flash
Conflicts:	%{name}-Free
Conflicts:	%{name}-One
Conflicts:	%{name}-Powerpack
Conflicts:	lxde-common < 0.3.2.1-6
Provides:	%{name}

%description -n %{name}-Flash
Configuration files for Mandriva Flash LXDE desktop environment.

%package -n %{name}-Free
Summary: 	Mandriva LXDE Free configuration files
Group: 		Graphical desktop/Other
Requires:	mandriva-release-Free
Requires:	mandriva-theme-Free
Conflicts:	%{name}-Flash
Conflicts:	%{name}-One
Conflicts:	%{name}-Powerpack
Conflicts:      lxde-common < 0.3.2.1-6
Provides:	%{name}

%description -n %{name}-Free
Configuration files for Mandriva Free LXDE desktop environment.

%package -n %{name}-One
Summary: 	Mandriva LXDE One configuration files
Group: 		Graphical desktop/Other
Requires:	mandriva-release-One
Requires:	mandriva-theme-One
Conflicts:	%{name}-Flash
Conflicts:	%{name}-Free
Conflicts:	%{name}-Powerpack
Conflicts:      lxde-common < 0.3.2.1-6
Provides:	%{name}

%description -n %{name}-One
Configuration files for Mandriva One LXDE desktop environment.

%package -n %{name}-Powerpack
Summary:	Mandriva LXDE Powerpack configuration files
Group:		Graphical desktop/Other
Requires:	mandriva-release-Powerpack
Requires:	mandriva-theme-Powerpack
Conflicts:	%{name}-Flash
Conflicts:	%{name}-Free
Conflicts:	%{name}-One
Conflicts:      lxde-common < 0.3.2.1-6
Provides:	%{name}

%description -n %{name}-Powerpack
Configuration files for Mandriva Powerpack LXDE desktop environment.

%prep
%setup -qn %{name}-%{version}

%install
rm -rf %{buildroot}

export sysconfdir=%{_sysconfdir}
export localstatedir=%{_localstatedir}

%makeinstall_std 

%clean
rm -rf %{buildroot}

%pre -n %{name}-Flash
if [ -d %{_localstatedir}/mandriva/lxde-profiles/Flash ]; then
  rm -rf %{_localstatedir}/mandriva/lxde-profiles/Flash
fi

%post -n %{name}-Flash
update-alternatives --install %{_datadir}/lxde/config lxde-config %{_localstatedir}/mandriva/lxde-profiles/Flash/lxde 10

%postun -n %{name}-Flash
if ! [ -e /var/lib/mandriva/lxdece-profiles/Flash ]; then
  update-alternatives --remove lxde-config /var/lib/mandriva/lxde-profiles/Flash/config
fi

%pre -n %{name}-Free
if [ -d %{_localstatedir}/mandriva/lxde-profiles/Free ]; then
  rm -rf %{_localstatedir}/mandriva/lxde-profiles/Free
fi

%post -n %{name}-Free
update-alternatives --install %{_datadir}/lxde/config lxde-config %{_localstatedir}/mandriva/lxde-profiles/Free/lxde 10

%postun -n %{name}-Free
if ! [ -e /var/lib/mandriva/lxde-profiles/Free ]; then
  update-alternatives --remove lxde-config /var/lib/mandriva/lxde-profiles/Free/config
fi

%pre -n %{name}-One
if [ -d %{_localstatedir}/mandriva/lxde-profiles/One ]; then
  rm -rf %{_localstatedir}/mandriva/lxde-profiles/One
fi

%post -n %{name}-One
update-alternatives --install %{_datadir}/lxde/config lxde-config %{_localstatedir}/mandriva/lxde-profiles/One/config 10

%postun -n %{name}-One
if ! [ -e /var/lib/mandriva/lxde-profiles/One ]; then
  update-alternatives --remove lxde-config /var/lib/mandriva/lxde-profiles/One/config
fi

%pre -n %{name}-Powerpack
if [ -d %{_localstatedir}/mandriva/lxde-profiles/Powerpack ]; then
  rm -rf %{_localstatedir}/mandriva/lxde-profiles/Powerpack
fi

%post -n %{name}-Powerpack
update-alternatives --install %{_datadir}/lxde/config lxde-config %{_localstatedir}/mandriva/lxde-profiles/Powerpack/config 10

%postun -n %{name}-Powerpack
if ! [ -e /var/lib/mandriva/lxde-profiles/Powerpack ]; then
  update-alternatives --remove lxde-config /var/lib/mandriva/lxde-profiles/Powerpack/config
fi

%files -n %{name}-Flash
%defattr(-,root,root)
%{_localstatedir}/mandriva/lxde-profiles/Flash

%files -n %{name}-Free
%defattr(-,root,root)
%{_localstatedir}/mandriva/lxde-profiles/Free

%files -n %{name}-One
%defattr(-,root,root)
%{_localstatedir}/mandriva/lxde-profiles/One

%files -n %{name}-Powerpack
%defattr(-,root,root)
%{_localstatedir}/mandriva/lxde-profiles/Powerpack
