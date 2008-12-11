%define	subv	1
Summary:	Russian dictionary for aspell
Summary(pl.UTF-8):	Rosyjski słownik dla aspella
Summary(ru.UTF-8):	Русская проверка орфографии
Name:		aspell-ru
Version:	0.99f7
Release:	2
Epoch:		1
License:	distributable
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/ru/aspell6-ru-%{version}-%{subv}.tar.bz2
# Source0-md5:	c4c98eaa5e77ad3adccbc5c96cb57cb3
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be put to debug package
%define		_enable_debug_packages	0

%description
Russian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Rosyjski słownik (lista słów) dla aspella.

%description -l ru.UTF-8
Русская проверка орфографии.

%prep
%setup -q -n aspell6-ru-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Copyright
%lang(ru) %doc doc/readme.*
%{_libdir}/aspell/*
%{_datadir}/aspell/*
