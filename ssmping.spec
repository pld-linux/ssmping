Summary:	Source Specific Multicast diagnostic tool
Name:		ssmping
Version:	0.9.1
Release:	0.1
License:	BSD-like
Group:		Applications
Source0:	http://www.venaas.no/multicast/ssmping/%{name}-%{version}.tar.gz
# Source0-md5:	ad8e3d13f6d72918f73be7e7975d7fad
URL:		http://www.venaas.no/multicast/ssmping/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ssmping is a tool for checking whether one can receive SSM from a
given host. If a host runs ssmpingd, users on other hosts can use the
ssmping client tool to test whether they can receive SSM from the
host.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
