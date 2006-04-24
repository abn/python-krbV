%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(plat_specific=True)")} 

Name: python-krbV
Version: 1.0.12
Release: 1%{?dist}
Summary: Python extension module for Kerberos 5

Group: Development/Languages
License: LGPL

Source: python-krbV-%{version}.tar.gz

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python
BuildRequires: python-devel
BuildRequires: krb5-devel >= 1.2.2
BuildRequires: /bin/awk

Requires: python-abi = %(%{__python} -c "import sys ; print sys.version[:3]")
Requires: krb5-libs >= 1.2.2

%description
python-krbV allows python programs to use Kerberos 5 authentication/security.

%prep
%setup -q -n python-krbV-%{version}

%build
export LIBNAME=%{_lib}
export CFLAGS="%{optflags} -Wextra"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} %{python_sitelib}
%makeinstall
%{__rm} -f $RPM_BUILD_ROOT%{python_sitelib}/*.la

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README krbV-code-snippets.py
%{python_sitelib}/krbVmodule.so

%changelog
* Mon Apr 24 2006 Michael Bonnet <mikeb@redhat.com> - 1.0.12
- bump version number due to API changes

* Fri Mar 24 2006 Mike Bonnet <mikeb@redhat.com>
- fix typo in error definition
- change the return value of recvauth() from ac to (ac, princ), where princ is the principal sent by sendauth()
- rename the package and reorganize the BuildRequires, to be more Extras-friendly

* Tue Sep 25 2001 Elliot Lee <sopwith@redhat.com>
- Initial version