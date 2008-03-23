#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Dir
%define	pnam	Split
Summary:	Dir::Split - Split files of a directory to subdirectories
Summary(pl.UTF-8):	Dir::Split - dzielenie plików z katalogu na podkatalogi
Name:		perl-Dir-Split
Version:	0.79
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Dir/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ff9e6e91c1b6f6ed4bb908179489c3c
URL:		http://search.cpan.org/dist/Dir-Split/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dir::Split moves files to either numbered or characteristic
subdirectories.

Numeric splitting is an attempt to gather files from a source
directory and split them to numbered subdirectories within a target
directory. Its purpose is to automate the archiving of a great amount
of files, that are likely to be indexed by numbers.

Characteristic splitting allows indexing by using leading characters
of filenames. While numeric splitting is being characterised by
dividing file amounts, characteristic splitting tries to keep up the
contentual recognition of data.

%description -l pl.UTF-8
Dir::Split przenosi pliki do podkatalogów numerowanych lub
charakterystycznych.

Dzielenie liczbowe to próba zebrania plików z katalogu źródłowego i
podzielenia ich na numerowane podkatalogi wewnątrz katalogu
docelowego. Celem jest zautomatyzowanie archiwizowania dużej liczby
plików, które mogą być indeksowane liczbami.

Dzielenie charakterystyczne pozwala na indeksowanie przy użyciu
wiodących znaków nazw plików. O ile dzielenie liczbowe charakteryzuje
się dzieleniem na liczby plików, to dzielenie charakterystyczne
próbuje utrzymać rozpoznawanie danych po zawartości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Dir/*.pm
%{_mandir}/man3/*
