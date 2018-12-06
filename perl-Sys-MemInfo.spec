#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sys-MemInfo
Version  : 0.99
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/S/SC/SCRESTO/Sys-MemInfo-0.99.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SC/SCRESTO/Sys-MemInfo-0.99.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsys-meminfo-perl/libsys-meminfo-perl_0.99-1.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Sys-MemInfo-lib = %{version}-%{release}
Requires: perl-Sys-MemInfo-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Sys/MemInfo version 0.99
========================
This module return the total amount of free and used physical memory
in bytes in totalmem and freemem variables.

%package dev
Summary: dev components for the perl-Sys-MemInfo package.
Group: Development
Requires: perl-Sys-MemInfo-lib = %{version}-%{release}
Provides: perl-Sys-MemInfo-devel = %{version}-%{release}

%description dev
dev components for the perl-Sys-MemInfo package.


%package lib
Summary: lib components for the perl-Sys-MemInfo package.
Group: Libraries
Requires: perl-Sys-MemInfo-license = %{version}-%{release}

%description lib
lib components for the perl-Sys-MemInfo package.


%package license
Summary: license components for the perl-Sys-MemInfo package.
Group: Default

%description license
license components for the perl-Sys-MemInfo package.


%prep
%setup -q -n Sys-MemInfo-0.99
cd ..
%setup -q -T -D -n Sys-MemInfo-0.99 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Sys-MemInfo-0.99/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sys-MemInfo
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Sys-MemInfo/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Sys/MemInfo.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sys::MemInfo.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Sys/MemInfo/MemInfo.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sys-MemInfo/LICENSE
