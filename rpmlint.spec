Name:		rpmlint
Version:	1.4
Release:	34

Summary:	RPM correctness checker
License:	GPLv2+
Group:		Development/Other

URL:		http://rpmlint.zarb.org/
Source0:	http://rpmlint.zarb.org/download/%{name}-%{version}.tar.xz
Source1:	rpmlint.config

Patch0:		rpmlint-1.4-fix-paths-to-extracted-srpm-files.patch
Patch1:		rpmlint-1.4-add-lgplv21-license.patch
Patch2:		rpmlint-1.4-below-threshold-returns-zero.patch
Patch3:		rpmlint-1.4-fix-setup-checks.patch
Patch4:		rpmlint-1.4-external-depfilter-with-internal-depgen.patch
Patch5:		rpmlint-1.4-shared-lib-not-executable.patch
# proper fix for rhbz#487855
Patch6:		rpmlint-1.4-only-report-actual-errors-as-spec_error.patch
Patch7:		rpmlint-1.4-install-info-trigger.patch
Patch8:		rpmlint-1.4-legacy-mandriva-filetriggers.patch
Patch9:		rpmlint-1.4-double-slash-in-path.patch
Patch10:	rpmlint-1.4-make-tests-pass.patch
Patch11:	rpmlint-1.4-dont-check-use-of-RPM_SOURCE_DIR-in-changelog.patch
Patch12:	rpmlint-1.4-dont-use-_RPMVSF_NOSIGNATURES.patch
Patch13:	rpmlint-1.4-encoding.patch
Patch14:	rpmlint-1.4-incoherent-pkgname-description.patch
Patch15:	rpmlint-1.4-only-report-non-versioned-files-for-libs.patch
Patch16:	rpmlint-1.4-dont-barf-on-missing-locales.patch
Patch17:	rpmlint-1.4-links-against-library-in-usr.patch
Patch18:	rpmlint-1.4-apply-patches-macro-disables-patch-not-applied-check.patch
Patch19:	rpmlint-non-utf8-in-changelog-warning.patch
Patch20:        rpmlint-1.4-spec-subpackage-desc.patch

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
%patch3 -p1 -b .setup~
%patch4 -p1 -b .dep_filter~
%patch5 -p1 -b .shlib_exec~
%patch6 -p1 -b .spec_error~
%patch7 -p1 -b .info~
%patch8 -p1 -b .triggers~
%patch9 -p1 -b .slash~
%patch10 -p1 -b .test~
%patch11 -p1 -b .sourcedir_changelog~
%patch12 -p1 -b .nosig~
%patch13 -p1
%patch14 -p1
%patch15 -p0
%patch16 -p1 -b .locales~
%patch17 -p1 -b .usrlib_ldd~
%patch18 -p1 -b .apply_patches~
%patch19 -p1 -b .utf8changelog~
# %patch20 -p0 -b .subpackage_desc_line~

%build
export COMPILE_PYC=1
%make

%check
make check

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
%dir %{_sysconfdir}/%{name}/
# Which of these exists depends on the version of bash_completion.
# Let's support both.
%optional %config(noreplace) %_sysconfdir/bash_completion.d/*
%optional %config(noreplace) %_datadir/bash-completion/completions/*
