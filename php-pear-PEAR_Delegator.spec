%define		_class		PEAR
%define		_subclass	Delegator
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.1.0
Release:	16
Summary:	Delegation for PHP
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/PEAR_Delegator/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-fix-path.patch
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package implements traditional and unorthodox delegation in PHP.
This allows for pseudo multiple inheritance and other interesting
design paradigms.


%prep
%setup -q -c
%patch0 -p 1
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-14mdv2012.0
+ Revision: 742174
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-13
+ Revision: 679553
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-12mdv2011.0
+ Revision: 613746
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-11mdv2010.1
+ Revision: 467962
- rediff path patch
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.1.0-10mdv2010.0
+ Revision: 441502
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-9mdv2009.1
+ Revision: 322516
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-8mdv2009.0
+ Revision: 237040
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-7mdv2007.0
+ Revision: 82497
- Import php-pear-PEAR_Delegator

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdk
- initial Mandriva package (PLD import)

