Name: rpmlint
Version: 0.81
Release: %mkrel 11
Summary: RPM correctness checker
License: GPLv2+
Group: Development/Other
URL: http://rpmlint.zarb.org/
Source0: http://rpmlint.zarb.org/download/rpmlint-%{version}.tar.bz2
Source1: rpmlint.config
Patch0:	rpmlint-0.81-rpm5.org-support.patch
Patch1:	rpmlint-non-std-group_is_error.patch
Patch2:	rpmlint-hardcoded-library-path_is_warning.patch
Patch3:	rpmlint-prereq-use_is_error.patch
Patch4: rpmlint-non-executable-script_is_warning.patch
Patch5: rpmlint-script-without-shebang_is_warning.patch
Patch6: rpmlint-non-standard-Xid_is_warning.patch
Patch7: rpmlint-wrong-script-interpreter_is_warning.patch
Patch9: rpmlint-statically-linked-binary_is_warning.patch
Patch10: rpmlint-no-cleaning-of-buildroot_is_warning.patch
Patch11: rpmlint-invalid-lc-messages-dir_is_warning.patch
Patch12: rpmlint-shared-lib-without-dependency-information_is_warning.patch
Patch13: rpmlint_only-non-binary-in-usr-lib_is_warning.patch
Patch14: rpmlint_update-menus-without-menu-file-in-_is_warning.patch

Requires: binutils
Requires: gcc-cpp 
Requires: python
Requires: rpm-python
BuildRequires: python
BuildRequires: rpm-python
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Rpmlint is a tool to check common errors on rpm packages.
Binary and source packages can be checked.

%prep
%setup -q
%patch0 -p0 -b .rpm5
%patch1 -p0 -b .group
%patch2 -p0 -b .libpath
%patch3 -p0 -b .prereq
%patch4 -p0 
%patch5 -p0 
%patch6 -p0 
%patch7 -p0 
%patch9 -p0 
%patch10 -p0 
%patch11 -p0 
%patch12 -p0 
%patch13 -p0 
%patch14 -p0 

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
%doc ChangeLog README*
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%dir %{_sysconfdir}/%{name}/
