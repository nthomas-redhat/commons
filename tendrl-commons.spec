Name: tendrl-commons
Version: 1.6.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Common lib for Tendrl sds integrations and node-agent
Source0: %{name}-%{version}.tar.gz
License: LGPLv2+
URL: https://github.com/Tendrl/commons

BuildRequires: pytest
BuildRequires: python2-devel
BuildRequires: python-mock
BuildRequires: python-six
BuildRequires: systemd

Requires: ansible
Requires: python-maps
Requires: python-dateutil
Requires: python-dns
Requires: python-etcd
Requires: python-six
Requires: python2-ruamel-yaml
Requires: pytz
Requires: python-psutil
Requires: python-IPy


%description
Common library for tendrl

%prep
%setup

# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%check
py.test -v tendrl/commons/tests || :

%files -f INSTALLED_FILES
%doc README.rst
%license LICENSE

%changelog
* Thu Mar 22 2018 Rohan Kanade <rkanade@redhat.com> - 1.6.2-1
- Bugfixes (https://github.com/Tendrl/commons/milestone/4)

* Wed Mar 07 2018 Rohan Kanade <rkanade@redhat.com> - 1.6.1-1
- Auto expand clusters managed by Tendrl

* Sat Feb 17 2018 Rohan Kanade <rkanade@redhat.com> - 1.6.0-1
- API to un-manage clusters managed by Tendrl

* Fri Feb 02 2018 Rohan Kanade <rkanade@redhat.com> - 1.5.5-1
- Move gluster.event_utils to commons
- Fix geo-rep classification
- Raise alert when node goes down, when cluster health changes

* Mon Dec 11 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.4-9
- Add dependency on python-IPy, python-dns

* Wed Dec 06 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.4-8
- Bugfixes

* Tue Dec 05 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.4-7
- Bugfixes

* Thu Nov 30 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.4-6
- Fix import cluster hard coded tendrl-gluster-integration sync_interval

* Mon Nov 27 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.4-5
- Fix alert time-stamp when alert status changes

* Tue Nov 21 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.4-4
- Bugfixes-3 tendrl-commons v1.5.4

* Sat Nov 18 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.4-3
- Bugfixes-2 tendrl-commons v1.5.4

* Fri Nov 10 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.4-2
- Bugfixes tendrl-commons v1.5.4

* Thu Nov 02 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.4-1
- Release tendrl-commons v1.5.4

* Thu Oct 12 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.3-1
- Release tendrl-commons v1.5.3

* Fri Sep 15 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.2-1
- Release tendrl-commons v1.5.2

* Fri Aug 25 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.1-1
- Release tendrl-commons v1.5.1

* Fri Aug 04 2017 Rohan Kanade <rkanade@redhat.com> - 1.5.0-1
- Release tendrl-commons v1.5.0

* Mon Jun 19 2017 Rohan Kanade <rkanade@redhat.com> - 1.4.2-1
- Release tendrl-commons v1.4.2

* Sun Jun 11 2017 Rohan Kanade <rkanade@redhat.com> - 1.4.1-2
- Fixes https://github.com/Tendrl/commons/issues/587

* Thu Jun 08 2017 Rohan Kanade <rkanade@redhat.com> - 1.4.1-1
- Release tendrl-commons v1.4.1

* Fri Jun 02 2017 Rohan Kanade <rkanade@redhat.com> - 1.4.0-1
- Release tendrl-commons v1.4.0

* Thu May 18 2017 Rohan Kanade <rkanade@redhat.com> - 1.3.0-1
- Release tendrl-commons v1.3.0

* Tue Apr 18 2017 Rohan Kanade <rkanade@redhat.com> - 1.2.3-1
- Release tendrl-commons v1.2.3

* Sat Apr 01 2017 Rohan Kanade <rkanade@redhat.com> - 1.2.2-1
- Release tendrl-commons v1.2.2

* Tue Dec 06 2016 Martin Bukatovič <mbukatov@redhat.com> - 0.0.1-2
- Fixed https://github.com/Tendrl/commons/issues/72

* Mon Oct 17 2016 Timothy Asir Jeyasingh <tjeyasin@redhat.com> - 0.0.1-1
- Initial build.
