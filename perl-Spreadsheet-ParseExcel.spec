%define module		Spreadsheet-ParseExcel
%define name		perl-%{module}
%define realver     0.32
%define version		%{realver}00
%define release		%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Spreadsheet::ParseExcel - Get information from Excel file
License:	GPL
Group:		Office
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Spreadsheet/%{module}-%{realver}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRequires: perl-OLE-Storage_Lite
BuildRequires: perl(IO::Scalar)
Buildarch:	noarch

%description
Spreadsheet::ParseExcel makes you to get information
from Excel95, Excel97, Excel2000 file.

%prep
%setup -q -n %{module}-%{realver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Spreadsheet
%{_mandir}/*/*


