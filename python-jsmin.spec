#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	jsmin
Summary:	JavaScript minifier
Summary(pl.UTF-8):	Minimalizator JavaScriptu
Name:		python-%{module}
Version:	2.2.1
Release:	1
License:	Freeware
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/jsmin
Source0:	https://pypi.python.org/packages/source/j/jsmin/jsmin-%{version}.tar.gz
# Source0-md5:	89a45a14ed76d1113f1ccd0bcc4b6f4a
URL:		https://pypi.python.org/pypi/jsmin
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JavaScript minifier - Python module.

%description -l pl.UTF-8
Moduł Pythona minimalizujący JavaScript.

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
%dir %{py_sitescriptdir}/jsmin
%{py_sitescriptdir}/jsmin/*.py[co]
%{py_sitescriptdir}/jsmin-%{version}-py*.egg-info
