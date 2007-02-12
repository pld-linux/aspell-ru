Summary:	Russian dictionary for aspell
Summary(pl.UTF-8):	Rosyjski słownik dla aspella
Summary(ru.UTF-8):	юЦААзпО ъЮчруЮзп чЮДчсЮпДьь
Name:		aspell-ru
Version:	0.99f7
%define	subv	1
Release:	1
Epoch:		1
License:	distributable
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/ru/aspell6-ru-%{version}-%{subv}.tar.bz2
# Source0-md5:	c4c98eaa5e77ad3adccbc5c96cb57cb3
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Russian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Rosyjski słownik (lista słów) dla aspella.

%description -l ru.UTF-8
юЦААзпО ъЮчруЮзп чЮДчсЮпДьь.

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
