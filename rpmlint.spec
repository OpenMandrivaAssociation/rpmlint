Name: rpmlint
Version: 0.91
Release: %mkrel 1
Summary: RPM correctness checker
License: GPLv2+
Group: Development/Other
URL: http://rpmlint.zarb.org/
Source0: http://rpmlint.zarb.org/download/rpmlint-%{version}.tar.bz2
Source1: rpmlint.config
Requires: python-rpm python-magic
BuildRequires: python-rpm
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Rpmlint is a tool to check common errors on rpm packages.
Binary and source packages can be checked.

%prep
%setup -q

%build
%{make}

%install
rm -rf %{buildroot}
%{makeinstall_std}
cp -a %{SOURCE1} %{buildroot}/%{_datadir}/%{name}/config

mkdir -p %{buildroot}/%{_datadir}/%{name}/config.d/
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc ChangeLog README*
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%dir %{_sysconfdir}/%{name}/
