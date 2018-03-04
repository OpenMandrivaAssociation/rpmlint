# (ngompa) disable rpmlint to avoid terrible cyclic dependency problem in rpm5->rpm4 + python2->python3 transition
# remove after rpm5->rpm4 transition is complete
%undefine _build_pkgcheck_set
%undefine _build_pkgcheck_srpm
%undefine _nonzero_exit_pkgcheck_terminate_build
###

Summary:	RPM correctness checker
Name:		rpmlint
Version:	1.10
Release:	1
License:	GPLv2+
Group:		Development/Other
URL:		https://github.com/rpm-software-management/rpmlint
Source0:	https://github.com/rpm-software-management/rpmlint/archive/%{name}-%{version}.tar.gz
Source1:	rpmlint.config
# Backports from upstream

# Mageia specific patches
Patch1001:	1001-Add-some-licenses-allowed-in-Fedora-as-they-are-allo.patch
Patch1002:	1002-Throw-an-error-with-a-deprecation-notice-for-apply_p.patch

BuildRequires:	pkgconfig(python)
BuildRequires:	python-rpm
BuildRequires:	bash-completion
Requires:	python > 3.0
Requires:	python-rpm
Requires:	python-magic
Requires:	desktop-file-utils
Suggests:	python-enchant
Requires:	rpmlint-%{_target_vendor}-policy
Requires:	cpio
Requires:	binutils
Requires:	gzip
Requires:	bzip2
Requires:	xz
# Needed for man page check in FilesCheck.py
Requires:	groff-for-man
Suggests:	myspell-en
BuildArch:	noarch

%description
Rpmlint is a tool to check common errors on rpm packages.
Binary and source packages can be checked.

%prep
%setup -q
%apply_patches

cp -p config config.example
install -pm 644 %{SOURCE1} config

%build
export COMPILE_PYC=1
%make

# (tpg) disable it for now
# [02:35] <King_InuYasha> _TPG: py.test -> pytest
# [02:36] <King_InuYasha> make check ignorable for now
# [02:36] <King_InuYasha> I have to fix this later
# [02:36] <King_InuYasha> apparently pytest changed the binary from py.test to pytest :(
%if 0
%check
make check
%endif

%install
%makeinstall_std

install -d %{buildroot}%{_datadir}/%{name}/config.d/

%files
%doc README.md config.example COPYING
%{_bindir}/*
%{_datadir}/rpmlint/
%{_mandir}/man1/rpmlint.1*
%{_mandir}/man1/rpmdiff.1*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config
%{_datadir}/bash-completion/completions/rpmlint
%{_datadir}/bash-completion/completions/rpmdiff
