# $Id$
# Authority: dries
# Upstream: Lincoln D. Stein <lstein$cshl,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-DBI

Summary: Tie hashes to DBI relational databases
Name: perl-Tie-DBI
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-DBI/

Source: http://search.cpan.org/CPAN/authors/id/L/LD/LDS/Tie-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This distribution contains Tie::DBI and Tie::RDBM, two modules that
allow you to tie associative arrays to relational databases using the
DBI library.  The hash is tied to a table in a local or networked
database.  Reading from the hash retrieves values from the datavbase.
Storing into the hash updates the database (if you have sufficient
privileges).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tie/DBI.pm
%{perl_vendorlib}/Tie/RDBM.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
