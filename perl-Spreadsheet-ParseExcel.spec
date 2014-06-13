%define modname	Spreadsheet-ParseExcel
%define modver	0.58

Summary:	Spreadsheet::ParseExcel - Get information from Excel file
Name:		perl-%{modname}
Epoch:		1
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2
Group:		Office
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Spreadsheet/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(OLE::Storage_Lite)
BuildRequires:	perl-devel

%description
Spreadsheet::ParseExcel makes you to get information
from Excel95, Excel97, Excel2000 file.

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*

