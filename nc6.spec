%define name 	nc6
%define version 1.0
%define release %mkrel 3

Summary: 	Reads and writes data across network connections using TCP or UDP
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
URL:		http://deepspace6.net/projects/netcat6.html
Source0:	ftp://ftp.deepspace6.net/pub/ds6/sources/nc6/%{name}-%{version}.tar.bz2
License: 	GPL
Group: 		Networking/Other
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
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
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall

(cd $RPM_BUILD_ROOT%{_bindir}; ln -s %{name} netcat6)

%find_lang  %{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc README NEWS TODO CREDITS ChangeLog BUGS AUTHORS 
%{_bindir}/%{name}
%{_bindir}/netcat6
%{_mandir}/man1/%{name}*

