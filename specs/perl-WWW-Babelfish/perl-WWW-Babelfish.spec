# $Id$
# Authority: dries
# Upstream: Dan Urist <durist$frii,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Babelfish

Summary: Perl extension for translation via babelfish
Name: perl-WWW-Babelfish
Version: 0.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Babelfish/

Source: http://search.cpan.org/CPAN/authors/id/D/DU/DURIST/WWW-Babelfish-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is a simple perl front-end to the Babelfish translation
server.  It's more fun than useful, but it might have a place in
IRC/talk clients or perhaps a translating web proxy. It makes an
attempt at breaking longer pieces of text up into chunks that
Babelfish can handle and then reassembling them. This version also
contains preliminary support for the Google translation engine.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%{perl_vendorlib}/WWW/Babelfish.pm
%{perl_vendorlib}/auto/WWW/Babelfish

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
