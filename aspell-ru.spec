Summary:	Russian dictionary for aspell
Summary(pl):	S³ownik rosyjski dla aspella
Summary(ru):	òÕÓÓËÁÑ ÐÒÏ×ÅÒËÁ ÏÒÆÏÇÒÁÆÉÉ
Name:		aspell-ru
Version:	0.50
%define	subv	2
Release:	4
Epoch:		1
License:	GPL (?)
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/ru/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	d7add85adeef2ea36457ea811d52c295
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Russian dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik (lista s³ów) rosyjski dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

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
%{_libdir}/aspell/*
%{_datadir}/aspell/*
