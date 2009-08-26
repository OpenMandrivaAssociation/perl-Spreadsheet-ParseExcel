%define upstream_name		Spreadsheet-ParseExcel
%define upstream_version 0.54

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
Epoch:      1

Summary:	Spreadsheet::ParseExcel - Get information from Excel file
License:	GPL
Group:		Office
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Spreadsheet/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Scalar)
BuildRequires: perl(OLE::Storage_Lite)
Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Spreadsheet::ParseExcel makes you to get information
from Excel95, Excel97, Excel2000 file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


