Summary: Rpm correctness checker
Name: rpmlint
Version: 0.77
Release: %mkrel 3
Source0: http://rpmlint.zarb.org/download/%{name}-%{version}.tar.bz2
Patch0:  Changeset1205.diff
Source1: rpmlint.config
URL: http://rpmlint.zarb.org/
License: GPL
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: python rpm-python binutils gcc-cpp 
BuildArch: noarch
BuildRequires: python rpm-python

%description
Rpmlint is a tool to check common errors on rpm packages.
Binary and source packages can be checked.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/%{name}/config
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc COPYING ChangeLog INSTALL README*
%{_bindir}/*
%{_datadir}/%{name}
%_mandir/man1/*
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%dir %{_sysconfdir}/%{name}/

