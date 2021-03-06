# $Id$
# Authority: dag

Summary: UNFS3 user-space NFSv3 server
Name: unfs3
Version: 0.9.22
Release: 2%{?dist}
License: BSD
Group: Applications/System
URL: http://unfs3.sourceforge.net/

Source0: http://dl.sf.net/unfs3/unfs3-%{version}.tar.gz
Source1: unfsd.init

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: byacc
BuildRequires: bison
BuildRequires: flex

Requires: /sbin/chkconfig
Requires: /sbin/service

%description
UNFS3 is a user-space implementation of the NFS (Network File System)
version 3 server specification. It provides a daemon that supports both
the MOUNT and NFS protocol.

%prep
%setup

%build
%configure \
    --enable-cluster
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/unfsd

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add unfsd
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service unfsd stop &>/dev/null || :
    /sbin/chkconfig --del unfsd
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service unfsd condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc CREDITS LICENSE NEWS README contrib/ doc/
%doc %{_mandir}/man7/tags.7*
%doc %{_mandir}/man8/unfsd.8*
%{_initrddir}/unfsd
%{_sbindir}/unfsd

%changelog
* Tue Mar 22 2011 Yury V. Zaytsev <yury@shurup.com> - 0.9.22-2
- Added an init script (thanks to Chris Butler!)

* Tue Jan 06 2009 Dag Wieers <dag@wieers.com> - 0.9.22-1
- Updated to release 0.9.22.

* Wed Jul 16 2008 Dag Wieers <dag@wieers.com> - 0.9.21-1
- Updated to release 0.9.21.

* Thu Dec 06 2007 Dag Wieers <dag@wieers.com> - 0.9.20-1
- Updated to release 0.9.20.

* Tue Nov 27 2007 Dag Wieers <dag@wieers.com> - 0.9.19-1
- Updated to release 0.9.19.

* Sat Sep 08 2007 Dag Wieers <dag@wieers.com> - 0.9.18-1
- Updated to release 0.9.18.

* Mon Jan 22 2007 Dag Wieers <dag@wieers.com> - 0.9.17-1
- Updated to release 0.9.17.

* Tue Nov 07 2006 Dag Wieers <dag@wieers.com> - 0.9.16-1
- Updated to release 0.9.16.

* Sat Aug 19 2006 Dag Wieers <dag@wieers.com> - 0.9.15-1
- Updated to release 0.9.15.

* Mon Jul 10 2006 Dag Wieers <dag@wieers.com> - 0.9.14-1
- Updated to release 0.9.14.

* Fri Sep 09 2005 Dag Wieers <dag@wieers.com> - 0.9.13-1
- Updated to release 0.9.13.

* Sun Jan 16 2005 Dag Wieers <dag@wieers.com> - 0.9.12-1
- Updated to release 0.9.12.

* Thu Aug 12 2004 Dag Wieers <dag@wieers.com> - 0.9.10-1
- Initial package. (using DAR)
