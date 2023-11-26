Summary:	RPM correctness checker
Name:		rpmlint
Version:	2.5.0
Release:	2
License:	GPLv2+
Group:		Development/Other
URL:		https://github.com/rpm-software-management/rpmlint
Source0:	https://github.com/rpm-software-management/rpmlint/archive/refs/tags/%{version}.tar.gz
Source1:	openmandriva.toml
Source2:	licenses.toml
BuildRequires:	pkgconfig(python)
BuildRequires:	python-rpm
BuildRequires:	pkgconfig(bash-completion)
Requires:	python > 3.0
Requires:	python-rpm
Requires:	python%{pyver}dist(file-magic)
Requires:	python%{pyver}dist(pybeam)
Requires:	python%{pyver}dist(pyxdg)
Requires:	python%{pyver}dist(tomli-w)
Requires:	python%{pyver}dist(zstandard)
Requires:	python%{pyver}dist(packaging)
Suggests:	python%{pyver}dist(pyenchant)
Requires:	desktop-file-utils
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

%build
%py_build

%install
%py_install

mkdir -p %{buildroot}%{_sysconfdir}/xdg/rpmlint
cp %{S:1} %{S:2} %{buildroot}%{_sysconfdir}/xdg/rpmlint

%files
%{_bindir}/*
%{py_puresitedir}/rpmlint
%{py_puresitedir}/rpmlint*.*-info
%dir %{_sysconfdir}/xdg/rpmlint
# Intentionally not noreplace -- distro-provided files here
# should not be overwritten, users should add their own files
# overriding values instead.
%config %{_sysconfdir}/xdg/rpmlint/*.toml
