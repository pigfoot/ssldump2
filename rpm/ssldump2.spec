%bcond_without backtrace # enabled by default

%global commit0 40-CHARACTER-HASH-VALUE
%global gittag0 GIT-TAG
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})


Summary: SSLSSLv3/TLS network protocol analyzer
Name: ssldump2
Version: 0.9
Release: b4%{?dist}
License: GPL
Group: Applications/Internet
URL: https://github.com/pigfoot/ssldump2
Source0:  https://github.com/pigfoot/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: openssl-devel >= 0.9.6, libpcap >= 0.4, libtool
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
ssldump is an SSLv3/TLS network protocol analyzer. It identifies TCP
connections on the chosen network interface and attempts to interpret
them as SSLv3/TLS traffic. When ssldump identifies SSLv3/TLS traffic,
ssldump decodes the records and displays them in a textual form to
stdout.

If provided with the appropriate keying material, ssldump will also
decrypt the connections and display the application data traffic.

%prep
%setup -n %{name}-%{version}

%build
%cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if %{with backtrace}
        -DENABLE_BACKTRACE:BOOL=ON \
%else
        -DENABLE_BACKTRACE:BOOL=OFF \
%endif
        -DENABLE_DIST:BOOL=ON
make %{?_smp_mflags}

%install
%make_install

%files
%{_sbindir}/ssldump

%changelog
* Mon May 02 2016 Chen, Chih-Chia <pigfoot@gmail.com> - 0.9-0.beta3.2
- Initial version
