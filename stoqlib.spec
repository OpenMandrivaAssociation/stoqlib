%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define name stoqlib
%define version 0.9.15
%define release %mkrel 0

Summary: Fiscal driver collection
Name: %{name}
Version: %{version}
Release: %{release}
License: LGPL
Group: System/Libraries
URL: http://www.stoq.com.br/
Source: stoqlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-zope-interface >= 3.0.1, pyserial >= 2.2, python-kiwi >= 1.9.27
BuildRequires: python-kiwi >= 1.9.27
BuildRequires: python-psycopg2
BuildRequires: python-zope-interface
BuildRequires: gazpacho
BuildRequires: python-dateutil
BuildRequires: python-imaging
BuildRequires: python-zope-interface
BuildRequires: python-devel
BuildRequires: python-reportlab
BuildRequires: stoqdrivers >= 0.9.15
BuildArch: noarch

%description
Stoqlib offers many special tools for retail system applications
such reports infrastructure, basic dialogs and searchbars and
domain data in a persistent level.

%prep

%setup -q

%build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{python_sitelib}/stoqlib
%{_libdir}/stoqlib
%{_datadir}/locale/*/LC_MESSAGES/stoqlib.mo
%{_datadir}/stoqlib/fonts
%{_datadir}/stoqlib/glade
%{_datadir}/stoqlib/pixmaps
%{_datadir}/stoqlib/sql
%{_datadir}/stoqlib/csv
%{_datadir}/stoqlib/template
/usr/lib/python2.6/site-packages/stoqlib-0.9.15-py2.6.egg-info
