# $Id$
# Authority: dries
# Upstream: Frederic Soriano <fsoriano$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-Nary

Summary: Perl implementation of N-ary search trees
Name: perl-Tree-Nary
Version: 1.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-Nary/

Source: http://search.cpan.org/CPAN/authors/id/F/FS/FSORIANO/Tree-Nary-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The Tree::Nary class implements N-ary trees (trees of data with any 
number of branches), providing the organizational structure for a tree (collection) 
of any number of nodes, but knowing nothing about the specific type of node used. 
It can be used to display hierarchical database entries in an internal application (the
NIS netgroup file is an example of such a database). It offers the capability to select 
nodes on the tree, and attachment points for nodes on the tree. Each attachment point 
can support multiple child nodes.
	
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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tree/Nary.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
