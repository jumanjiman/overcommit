Name:		overcommit
Version:	0.1
Release:	1%{?dist}
Summary:	Set memory overcommit policy

Group:		System Environment/Base
License:	GPLv3+
URL:		https://github.com/jumanjiman/overcommit
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

Requires:	apply-sysctl

%description
Apply kernel tunables at boot-time to set overcommit policy.
See README.policies for more information, including how
to override the defaults.

This package includes three policy configs:
* heuristic (same as kernel default)
* always
* never



%prep
%setup -q


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/rc.d/init.d
%{__install} -pm 755 src/overcommit %{buildroot}/%{_sysconfdir}/rc.d/init.d
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/sysconfig
%{__install} -pm 644 src/configs/overcommit.sample %{buildroot}/%{_sysconfdir}/sysconfig
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/%{name}
%{__install} -pm 644 src/configs/never-overcommit.conf %{buildroot}/%{_sysconfdir}/%{name}
%{__install} -pm 644 src/configs/default-overcommit.conf %{buildroot}/%{_sysconfdir}/%{name}
%{__install} -pm 644 src/configs/always-overcommit.conf %{buildroot}/%{_sysconfdir}/%{name}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING.GPLv3
%doc README.memory
%doc README.policies
%doc %{_sysconfdir}/sysconfig/overcommit.sample
%config %{_sysconfdir}/%{name}/default-overcommit.conf
%config %{_sysconfdir}/%{name}/always-overcommit.conf
%config %{_sysconfdir}/%{name}/never-overcommit.conf
%{_sysconfdir}/rc.d/init.d


%preun
if [ $1 -eq 0 ]; then
  service overcommit stop || :
  chkconfig --del overcommit || :
fi


%post
if [ $1 -gt 0 ]; then
  chkconfig --add overcommit &> /dev/null || :
fi


%changelog
* Tue Feb 08 2011 Paul Morgan <jumanjiman@gmail.com> 0.1-1
- new package built with tito

* Tue Feb 08 2011 Paul Morgan <jumanjiman@gmail.com> 0.1-1
- new package built with tito


