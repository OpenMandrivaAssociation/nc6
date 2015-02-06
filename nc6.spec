Summary: 	Reads and writes data across network connections using TCP or UDP
Name: 		nc6
Version: 	1.0
Release: 	7
URL:		http://deepspace6.net/projects/netcat6.html
Source0:	ftp://ftp.deepspace6.net/pub/ds6/sources/nc6/%{name}-%{version}.tar.bz2
License: 	GPL
Group: 		Networking/Other
BuildRequires:	autoconf2.5
Provides:	netcat6 = %{version}

%description
The nc6 package contains Netcat (the program is now netcat), a simple
utility for reading and writing data across network connections, using
the TCP or UDP protocols. Netcat is intended to be a reliable back-end
tool which can be used directly or easily driven by other programs and
scripts.  Netcat is also a feature-rich network debugging and exploration
tool, since it can create many different connections and has many
built-in capabilities.

This version is a fork with ipv6 capabilities.

%prep
%setup -q
%build
%configure2_5x
%make

%install
%makeinstall

(cd %{buildroot}%{_bindir}; ln -s %{name} netcat6)

%files
%defattr(-,root,root)
%doc README NEWS TODO CREDITS ChangeLog BUGS AUTHORS 
%{_bindir}/%{name}
%{_bindir}/netcat6
%{_mandir}/man1/%{name}*



%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2011.0
+ Revision: 620480
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2010.0
+ Revision: 430158
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 253652
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0-1mdv2008.1
+ Revision: 130511
- kill re-definition of %%buildroot on Pixel's request


* Mon Jan 23 2006 Pascal Terjan <pterjan@mandriva.org> 1.0-1mdk
- 1.0

* Wed Aug 03 2005 Michael Scherer <misc@mandriva.org> 0.5-1mdk
- first version, based on nc spec

