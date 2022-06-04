#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sys-MemInfo
Version  : 0.99
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/S/SC/SCRESTO/Sys-MemInfo-0.99.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SC/SCRESTO/Sys-MemInfo-0.99.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsys-meminfo-perl/libsys-meminfo-perl_0.99-1.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Sys-MemInfo-license = %{version}-%{release}
Requires: perl-Sys-MemInfo-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Sys/MemInfo version 0.99
========================
This module return the total amount of free and used physical memory
in bytes in totalmem and freemem variables.

%package dev
Summary: dev components for the perl-Sys-MemInfo package.
Group: Development
Provides: perl-Sys-MemInfo-devel = %{version}-%{release}
Requires: perl-Sys-MemInfo = %{version}-%{release}

%description dev
dev components for the perl-Sys-MemInfo package.


%package license
Summary: license components for the perl-Sys-MemInfo package.
Group: Default

%description license
license components for the perl-Sys-MemInfo package.


%package perl
Summary: perl components for the perl-Sys-MemInfo package.
Group: Default
Requires: perl-Sys-MemInfo = %{version}-%{release}

%description perl
perl components for the perl-Sys-MemInfo package.


%prep
%setup -q -n Sys-MemInfo-0.99
cd %{_builddir}
tar xf %{_sourcedir}/libsys-meminfo-perl_0.99-1.debian.tar.xz
cd %{_builddir}/Sys-MemInfo-0.99
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Sys-MemInfo-0.99/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sys-MemInfo
cp %{_builddir}/Sys-MemInfo-0.99/LICENSE %{buildroot}/usr/share/package-licenses/perl-Sys-MemInfo/a3e8f8a3dd3eb197246feadbf92cab49deaa3bd9
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Sys-MemInfo/c4d9da02531b248cd3265fff9f43d606e9a4ffe2
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sys::MemInfo.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sys-MemInfo/a3e8f8a3dd3eb197246feadbf92cab49deaa3bd9
/usr/share/package-licenses/perl-Sys-MemInfo/c4d9da02531b248cd3265fff9f43d606e9a4ffe2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
