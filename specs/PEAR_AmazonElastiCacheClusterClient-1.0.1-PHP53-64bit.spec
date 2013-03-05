%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define xmldir  /var/lib/pear

Summary: PEAR: PHP extension for interfacing with memcached compatible Amazon ElastiCache service via libmemcached library
Name: php-pecl-AmazonElastiCacheClusterClient
Version: 1.0.1
Release: 1
License: PHP, Amazon Software License
Group: Development/Libraries
Source0: AmazonElastiCacheClusterClient-%{version}-PHP53-64bit.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildRequires: php-pear
Requires: php = 5.3
Requires: php-pear
Conflicts: php-pecl-memcached 
Conflicts: php-pecl-memcache
BuildArch: x86_64

%description
This extension uses Amazon ElastiCache fork of libmemcached library to
provide API for communicating with memcached servers.

%prep
%setup -c -T
pear -v -c pearrc \
        -d php_dir=%{peardir} \
        -d doc_dir=/docs \
        -d bin_dir=%{_bindir} \
        -d data_dir=%{peardir}/data \
        -d test_dir=%{peardir}/tests \
        -d ext_dir=%{_libdir} \
        -s

%build

%install
rm -rf %{buildroot}
pear -c pearrc install --nodeps --packagingroot %{buildroot} %{SOURCE0}
        
# Clean up unnecessary files
rm pearrc
rm %{buildroot}/%{peardir}/.filemap
rm %{buildroot}/%{peardir}/.lock
rm -rf %{buildroot}/%{peardir}/.registry
rm -rf %{buildroot}%{peardir}/.channels
rm %{buildroot}%{peardir}/.depdb
rm %{buildroot}%{peardir}/.depdblock

mv %{buildroot}/docs .


# Install XML package description
mkdir -p %{buildroot}%{xmldir}
tar -xzf %{SOURCE0} package.xml
cp -p package.xml %{buildroot}%{xmldir}/AmazonElastiCacheClusterClient.xml

# Install memcached.ini into /etc/php.d
mkdir -p %{buildroot}/etc/php.d
tar -xzf %{SOURCE0} AmazonElastiCacheClusterClient-%{version}/memcached.ini
cp -p AmazonElastiCacheClusterClient-%{version}/memcached.ini %{buildroot}/etc/php.d/memcached.ini

%clean
rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/AmazonElastiCacheClusterClient.xml
echo "extension=amazon-elasticache-cluster-client.so" >> /etc/php.ini

%postun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only __uri/AmazonElastiCacheClusterClient
    sed -i 's/extension=amazon-elasticache-cluster-client.so//g' /etc/php.ini
fi

%files
%defattr(-,root,root)
%doc docs/AmazonElastiCacheClusterClient/*
/etc/php.d/*
%{_libdir}/*
%{xmldir}/AmazonElastiCacheClusterClient.xml
