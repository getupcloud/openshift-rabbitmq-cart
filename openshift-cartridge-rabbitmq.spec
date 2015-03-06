%global cartridgedir %{_libexecdir}/openshift/cartridges/rabbitmq

Summary:       Provides embedded RabbitMQ support
Name:          openshift-cartridge-rabbitmq
Version:       1.0.0
Release:       2%{?dist}
Group:         Network/Daemons
License:       ASL 2.0
URL:           http://www.rabbitmq.com
Source0:       %{name}-%{version}.tar.gz
Requires:      erlang = R14B
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Provides:      openshift-cartridge-rabbitmq
BuildArch:     noarch

%description
Provides RabbitMQ cartridge support to OpenShift.

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__rm -rf %{buildroot}%{cartridgedir}/rel-eng

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/conf/
%attr(0755,-,-) %{cartridgedir}/env/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}/metadata
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/LICENSE

%changelog
* Fri Mar 06 2015 Builder <getup@getupcloud.com> 1.0.0-1
- new package built with tito

