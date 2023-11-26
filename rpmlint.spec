Summary:	RPM correctness checker
Name:		rpmlint
Version:	2.5.0
Release:	1
License:	GPLv2+
Group:		Development/Other
URL:		https://github.com/rpm-software-management/rpmlint
Source0:	https://github.com/rpm-software-management/rpmlint/archive/refs/tags/%{version}.tar.gz
Source1:	rpmlint.config
BuildRequires:	pkgconfig(python)
BuildRequires:	python-rpm
BuildRequires:	pkgconfig(bash-completion)
Requires:	python > 3.0
Requires:	python-rpm
Requires:	python3dist(file-magic)
Requires:	desktop-file-utils
Suggests:	python-enchant
Requires:	distro-release-rpmlint-policy
Requires:	cpio
Requires:	binutils
Requires:	pigz
Requires:	pbzip2
Requires:	xz
Requires:	zstd
# Needed for man page check in FilesCheck.py
Requires:	groff-for-man
Suggests:	myspell-en
BuildArch:	noarch

%description
Rpmlint is a tool to check common errors on rpm packages.
Binary and source packages can be checked.

%prep
%autosetup -p1

install -pm 644 %{SOURCE1} config

%build
%make_build COMPILE_PYC=1 PYTHON=%{__python}
%py_build

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
%py_install

install -d %{buildroot}%{_datadir}/%{name}/config.d/

%files
%{_bindir}/*
%{py_puresitedir}/rpmlint
%{py_puresitedir}/rpmlint*.*-info
