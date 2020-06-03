#%global debug_package %{nil}

Name:    webbench
Version: 1.5
Release: 1
Summary: simple tool for benchmarking WWW or proxy servers
License: GPL
URL:	 http://home.tiscali.cz/~cz210552/webbench.html
Source0: http://home.tiscali.cz/~cz210552/distfiles/%{name}-%{version}.tar.gz

Patch0: webbench-remove-socket-file-and-reimplement-function.patch

BuildRequires: 	gcc

%description
Web Bench is very simple tool for benchmarking WWW or proxy servers. Uses fork() for simulating multiple clients and can use HTTP/0.9-HTTP/1.1 requests. This benchmark is not very realistic, but it can test if your HTTPD can realy handle that many clients at once (try to run some CGIs) without taking your machine down. Displays pages/min and bytes/sec. Can be used in more aggressive mode with -f switch

%prep
%setup -q -n %{name}-%{version}/
#remove unclear license file socket.c and reimplement socket function. 
%patch0 -p1

%build
%make_build

%install
%{__make} install PREFIX="%{buildroot}%{_prefix}"

%pre
%preun
%post
%postun

%check

%files
%license COPYRIGHT
%doc ChangeLog
%{_bindir}/*
%{_mandir}/*

%changelog
* Sun Mar 29 2020 Wei Xiong <myeuler@163.com>
- Package init

