# Amazon ElastiCache Cluster Client spec files for RHEL distros

Tested on:
 CentOS 6.3 x86_64

## Create a RPM Build Environment

You'll need to perform these tasks:

### Prepare the RPM Build Environment

    sudo yum install rpmdevtools
    rpmdev-setuptree

### Install Prerequisites for RPM Creation

    sudo yum install gcc-c++ php php-pear

## Download the source code

Please refer to: http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Appendix.PHPAutoDiscoverySetup.html#Appendix.PHPAutoDiscoverySetup.Downloading

Put the recently downloaded package in ~/rpmbuild/SOURCES

## Put the spec file in place

    cp amazon-elasticache-cluster-client-rpm/specs/PEAR_AmazonElastiCacheClusterClient-1.0.1-PHP53-64bit.spec ~/rpmbuild/SPECS/

## Build the RPM

    cd ~/rpmbuild/
    # the QA_RPATHS var tells the builder to ignore file path errors
    QA_RPATHS=$[ 0x0002 ] rpmbuild -ba SPECS/PEAR_AmazonElastiCacheClusterClient-1.0.1-PHP53-64bit.spec

The resulting RPM will be:

    ~/rpmbuild/RPMS/x86_64/php-pecl-AmazonElastiCacheClusterClient-1.0.1-1.x86_64.rpm

Remember to build the RPM using an unprivileged user! More information on http://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch-creating-rpms.html

## More information

    http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Appendix.PHPAutoDiscoverySetup.htm

Special thanks to http://pear.php.net/package/PEAR_Command_Packaging