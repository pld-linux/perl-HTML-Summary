%include	/usr/lib/rpm/macros.perl
Summary:	HTML-Summary perl module
Summary(pl):	Modu³ perla HTML-Summary
Name:		perl-HTML-Summary
Version:	0.017
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Summary-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-HTML-Tree
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-Summary module produces summaries from the textual content of web
pages.

%description -l pl
Modu³ HTML-Summary tworzy podsumowania zawarto¶ci stron www.

%prep
%setup -q -n HTML-Summary-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/Summary
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz examples

%{perl_sitelib}/HTML/Summary.pm
%{perl_sitelib}/Lingua/JA/*.pm
%{perl_sitelib}/Text/Sentence.pm
%{perl_sitearch}/auto/HTML/Summary

%dir %{_prefix}/src/examples/%{name}
%attr(755,root,root) %{_prefix}/src/examples/%{name}/*.pl

%{_mandir}/man3/*
