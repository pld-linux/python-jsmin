#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	jsmin
Summary:	JavaScript minifier
Name:		python-%{module}
Version:	2.0.2
Release:	2
License:	Freeware
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/j/jsmin/jsmin-%{version}.tar.gz
# Source0-md5:	cd87c582cf897692df63c506e309249b
URL:		http://pypi.python.org/pypi/jsmin
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JavaScript minifier - Python module

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/test.*
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-*.egg-info
