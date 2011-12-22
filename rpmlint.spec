Name:		rpmlint
Version:	1.4
Release:	4

Summary:	RPM correctness checker
License:	GPLv2+
Group:		Development/Other

URL:		http://rpmlint.zarb.org/
Source0:	http://rpmlint.zarb.org/download/%{name}-%{version}.tar.xz
Source1:	rpmlint.config

Patch0:		rpmlint-1.4-fix-paths-to-extracted-srpm-files.patch
Patch1:		rpmlint-1.4-add-lgplv21-license.patch
Patch2:		rpmlint-1.4-below-threshold-returns-zero.patch

Requires:	python-rpm python-magic desktop-file-utils
Suggests:	python-enchant rpmlint-%{_target_vendor}-policy

BuildRequires:	python-rpm
BuildArch:	noarch

%description
Rpmlint is a tool to check common errors on rpm packages.
Binary and source packages can be checked.

%prep
%setup -q
%patch0 -p1 -b .srpm_paths~
%patch1 -p1 -b .lgplv21~
%patch2 -p1 -b .threshold~

%build
export COMPILE_PYC=1
%make

%install
%makeinstall_std

install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/%{name}/config
install -d %{buildroot}%{_datadir}/%{name}/config.d/
 
%files
%doc ChangeLog README*
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%dir %{_sysconfdir}/%{name}/
