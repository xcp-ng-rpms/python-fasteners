
%global pypi_name fasteners
%global py3_prefix python%{python3_pkgversion}

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        3%{?dist}
Summary:        A python package that provides useful locks

License:        ASL 2.0
URL:            https://github.com/harlowja/fasteners
Source0:        https://codeload.github.com/harlowja/fasteners/tar.gz/%{version}#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-six
Requires:       python-six

# tests:
BuildRequires:  python-futures
BuildRequires:  python-nose
BuildRequires:  python-testtools


%package -n %{py3_prefix}-%{pypi_name}
Summary:        A python package that provides useful locks

BuildRequires:  %{py3_prefix}-devel
# tests
BuildRequires:  %{py3_prefix}-nose
BuildRequires:  %{py3_prefix}-six
BuildRequires:  %{py3_prefix}-testtools

Requires:       %{py3_prefix}-six

%description -n %{py3_prefix}-%{pypi_name}
A python package that provides useful locks.


%description
A python package that provides useful locks.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests-2.7
nosetests-%{python3_version}


%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python_version}.egg-info

%files -n %{py3_prefix}-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Apr 13 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 0.9.0-3
- add Python 3 subpackage

* Fri Jun 12 2015 Matthias Runge <mrunge@redhat.com> - 0.9.0-2
- switch to github sourcecode, license included
- add tests, fix conditionals for python3

* Thu Jun 11 2015 Matthias Runge <mrunge@redhat.com> - 0.9.0-1
- Initial package. (rhbz#1230548)
