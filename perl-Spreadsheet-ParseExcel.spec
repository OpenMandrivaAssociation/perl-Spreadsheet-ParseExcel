%define upstream_name		Spreadsheet-ParseExcel
%define upstream_version 0.58

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
Epoch:		1

Summary:	Spreadsheet::ParseExcel - Get information from Excel file
License:	GPL
Group:		Office
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Spreadsheet/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Scalar)
BuildRequires: perl(OLE::Storage_Lite)
BuildRequires: perl-devel
BuildArch:	noarch

%description
Spreadsheet::ParseExcel makes you to get information
from Excel95, Excel97, Excel2000 file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Spreadsheet
%{_mandir}/*/*


%changelog
* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.580.0-1mdv2011.0
+ Revision: 596645
- update to 0.58

* Mon Jan 25 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.570.0-1mdv2011.0
+ Revision: 495704
- update to 0.57

* Sat Dec 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.560.0-1mdv2010.1
+ Revision: 477630
- update to 0.56

* Thu Oct 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.550.0-1mdv2010.0
+ Revision: 451998
- update to 0.55

* Wed Aug 26 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.540.0-1mdv2010.0
+ Revision: 421388
- update to 0.54

* Tue Aug 25 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.530.0-1mdv2010.0
+ Revision: 421129
- update to 0.53

* Mon Aug 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.520.0-1mdv2010.0
+ Revision: 420265
- update to 0.52

* Thu Aug 20 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.510.0-1mdv2010.0
+ Revision: 418376
- update to 0.51

* Wed Aug 19 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.500.0-1mdv2010.0
+ Revision: 418115
- update to 0.50

* Wed Jul 08 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.490.0-1mdv2010.0
+ Revision: 393421
- update to 0.49 (for real this time)
- using %%perl_convert_version (and bumping epoch to get rid of previous
  buggy version)

* Fri Feb 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4900-1mdv2009.1
+ Revision: 338018
- update to new version 0.4900

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4700-1mdv2009.1
+ Revision: 333409
- update to new version 0.4700

* Mon Jan 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4500-1mdv2009.1
+ Revision: 331149
- update to new version 0.4500

* Tue Oct 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3300-1mdv2009.1
+ Revision: 293550
- update to new version 0.3300

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3200-3mdv2009.0
+ Revision: 241898
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.3200-1mdv2008.0
+ Revision: 48403
- fix buildrequires
- 0.32


* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 17:22:09 (54054)
- rebuild
- make test
- adjust buildrequires

* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 17:18:35 (54050)
Import perl-Spreadsheet-ParseExcel

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2603-2mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Tue Aug 23 2005 Olivier Thauvin <nanardon@mandriva.org> 0.2603-1mdk
- From trem <trem@zarb.org>
  - first mdk release

