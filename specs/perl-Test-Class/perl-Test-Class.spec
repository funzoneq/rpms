# $Id$
# Authority: dries
# Upstream: Adrian Howard <adrianh$quietstars,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Class

Summary: Easily create test classes in an xUnit/JUnit style
Name: perl-Test-Class
Version: 0.27
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Class/

Source: http://www.cpan.org/modules/by-module/Test/Test-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
Requires: perl >= 1:5.6.1

%description
Easily create test classes in an xUnit/JUnit style.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Test::Class.3pm*
%doc %{_mandir}/man3/Test::Class::*.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Class/
%{perl_vendorlib}/Test/Class.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
