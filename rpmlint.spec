Name: rpmlint
Version: 0.81
Release: %mkrel 1
Summary: RPM correctness checker
License: GPL
Group: Development/Other
URL: http://rpmlint.zarb.org/
Source0: http://rpmlint.zarb.org/download/rpmlint-%{version}.tar.bz2
Source1: rpmlint.config
Requires: binutils
Requires: gcc-cpp 
Requires: python
Requires: rpm-python
BuildRequires: python
BuildRequires: rpm-python
BuildArch: noarch

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
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc COPYING ChangeLog INSTALL README*
%{_bindir}/*
%{_datadir}/%{name}
%_mandir/man1/*
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%dir %{_sysconfdir}/%{name}/
