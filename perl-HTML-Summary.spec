%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Summary
Summary:	HTML::Summary perl module
Summary(pl):	Modu³ perla HTML::Summary
Name:		perl-HTML-Summary
Version:	0.017
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Tree
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Summary module produces summaries from the textual content of web
pages.

%description -l pl
Modu³ HTML::Summary tworzy podsumowania zawarto¶ci stron www.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README examples
%{perl_sitelib}/HTML/Summary.pm
%dir %{perl_sitelib}/Lingua/JA
%{perl_sitelib}/Lingua/JA/*.pm
%{perl_sitelib}/Text/Sentence.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
