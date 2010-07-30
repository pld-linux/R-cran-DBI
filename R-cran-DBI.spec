%define		fversion	%(echo %{version} |tr r -)
%define		modulename	DBI
Summary:	R Database Interface
Name:		R-cran-%{modulename}
Version:	0.2r5
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	84e598c205ef7c97e16feaf5d11798a3
BuildRequires:	R >= 2.8.1
BuildRequires:	tetex-latex-ae
BuildRequires:	tetex-latex-bibtex
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A database interface (DBI) definition for communication between R and
relational database management systems. All classes in this package are
virtual and need to be extended by the various R/DBMS implementations.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
# R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

#%postun
#if [ -f %{_libdir}/R/bin/Rcmd ];then
#	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
#	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
#fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
