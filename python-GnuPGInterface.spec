Summary:	Python interface to GnuPG
Name:		python-GnuPGInterface
Version:	0.3.2
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/py-gnupg/GnuPGInterface-%{version}.tar.gz
# Source0-md5:	d4627d83446f96bd8c22f8d15db3f7c2
URL:		http://py-gnupg.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#%pyrequires_eq	python-libs
%pyrequires_eq	python-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyton GnuPGInterface is meant to be a filehandle-concentrating Python
interface to GnuPG, the GNU Privacy Guard. It has an API similar to
the Perl module GnuPG::Interface.

%prep
%setup -q -n GnuPGInterface-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog MANIFEST NEWS README THANKS
%{py_sitescriptdir}/GnuPGInterface.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/GnuPGInterface-*.egg-info
%endif
