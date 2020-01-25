#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	HTML
%define		pnam	Summary
Summary:	HTML::Summary - module for generating a summary from a web page
Summary(pl.UTF-8):	HTML::Summary - moduł do generowania streszczeń stron WWW
Name:		perl-HTML-Summary
Version:	0.017
Release:	9
License:	not distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# NoSource0-md5:	a7f29617a26a3f07b3f871751507d9ec
NoSource:	0
URL:		http://search.cpan.org/dist/HTML-Summary/
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML::Summary module produces summaries from the textual content
of web pages. It does so using the location heuristic, which
determines the value of a given sentence based on its position and
status within the document; for example, headings, section titles and
opening paragraph sentences may be favoured over other textual
content. A LENGTH option can be used to restrict the length of the
summary produced.

%description -l pl.UTF-8
Moduł HTML::Summary tworzy streszczenia z tekstowej zawartości stron
WWW. Czyni to przy użyciu heurystyki położenia, określającej wartość
danego zdania w oparciu o położenie i status w dokumencie; na przykład
nagłówki, tytuły sekcji i zdania zaczynające akapity mogą być
preferowane w stosunku do reszty treści. Można użyć opcji LENGTH do
ograniczenia długości tworzonego streszczenia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README examples
%{perl_vendorlib}/HTML/Summary.pm
%dir %{perl_vendorlib}/Lingua/JA
%{perl_vendorlib}/Lingua/JA/*.pm
%{perl_vendorlib}/Text/Sentence.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
