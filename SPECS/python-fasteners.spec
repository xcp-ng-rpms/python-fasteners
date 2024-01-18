%global package_speccommit 3f34939b5615a709cae5701fc2e0a362198acea7
%{!?xsrel: %global xsrel 3}

%global pypi_name fasteners
%global py3_prefix python%{python3_pkgversion}

Name:           python-%{pypi_name}
Version:        0.9.0
Release: %{?xsrel}%{?dist}
Summary:        A python package that provides useful locks

License:        ASL 2.0
URL:            https://github.com/harlowja/fasteners
Source0: fasteners-0.9.0.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-six
BuildRequires:  python2-setuptools
Requires:       python-six

# Disable test as the test suite is not ready on xs8
%bcond_with test

%if %{with test}
# tests:
BuildRequires:  python-futures
BuildRequires:  python-nose
BuildRequires:  python-testtools
%endif

%package -n %{py3_prefix}-%{pypi_name}
Summary:        A python package that provides useful locks

BuildRequires:  %{py3_prefix}-devel
# tests
%if %{with test}
BuildRequires:  %{py3_prefix}-nose
BuildRequires:  %{py3_prefix}-six
BuildRequires:  %{py3_prefix}-testtools
%endif

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

%if %{with test}
%check
nosetests-2.7
nosetests-%{python3_version}
%endif

%files
%doc README.rst
%license LICENSE
%define __python /usr/bin/python2
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python_version}.egg-info

%files -n %{py3_prefix}-%{pypi_name}
%doc README.rst
%license LICENSE
%define __python /usr/bin/python3
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Nov 20 2023 Lin Liu <lin.liu@citrix.com> - 0.9.0-3
- Bump up release to supersede the old build

* Thu Nov 16 2023 Lin Liu <lin.liu@citrix.com> - 0.9.0-1
- First imported release

