# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 2.0.0"

Vagrant.configure("2") do |config|

	# Utilisation de box Ubuntu par défaut
	config.vm.box = "centos/7"

	config.vm.box_version = "1801.02"

	config.vm.provision "shell", inline: <<-SHELL
	#sudo yum install -y epel-release
	#sudo yum update

    #sudo yum install -y \
    #  redhat-lsb-core \
	#  net-tools \
	#  python-lxml  \
	#  python-pip \
	#  wget \
	#  policycoreutils-python \
	#  telnet

	swapoff -a

    #echo "10.0.0.2 master1.softeam.fr master1 > /tmp/hosts.back
    #echo "10.0.0.3 slave1.softeam.fr slave1" >> /tmp/hosts.back
	#cat  /etc/hosts | grep -v 10.0.2.2 | grep -v 10.0.2.3 | grep -v 'slave1' |  grep -v 'master1' >> /tmp/hosts.back
    #cat /tmp/hosts.back > /etc/hosts

	SHELL

	config.vm.define "master1" do |master1_cfg|

		# Hostname pour y accéder depuis l'host
		master1_cfg.vm.hostname = "master1.softeam.fr"

		master1_cfg.vm.network "private_network", ip: "10.0.0.2"

		# Redirection des ports
		master1_cfg.vm.network "forwarded_port", guest: 80,    host: 11080

        # master1_cfg.vm.synced_folder ".", "/home/vagrant/ansible"

		master1_cfg.vm.provider "virtualbox" do |vb|
			vb.memory = "2048"
			vb.cpus = 1
		end
	end

	###########################################################
	# Définition de la VM Ansible pour provisionner l'ensemble
	config.vm.define "slave1" do |slave1_cfg|

		# Hostname pour y accéder depuis l'host
		slave1_cfg.vm.hostname = "slave1.softeam.fr"

        slave1_cfg.vm.network "private_network", ip: "10.0.0.3"

		slave1_cfg.vm.network "forwarded_port", guest: 61616,    host: 61616
	    slave1_cfg.vm.network "forwarded_port", guest: 27017,    host: 27017
	    slave1_cfg.vm.network "forwarded_port", guest:  5432,    host:  5432

		slave1_cfg.vm.provider "virtualbox" do |vb|
			vb.memory = "1024"
			vb.cpus = 1
		end

		# config.vm.synced_folder ".", "/home/vagrant/ansible
	end

	###########################################################
	# Définition de la VM Ansible pour provisionner l'ensemble
	config.vm.define "slave2" do |slave2_cfg|

		# Hostname pour y accéder depuis l'host
		slave2_cfg.vm.hostname = "slave2.softeam.fr"

        slave2_cfg.vm.network "private_network", ip: "10.0.0.4"

		slave2_cfg.vm.provider "virtualbox" do |vb|
			vb.memory = "1024"
			vb.cpus = 1
		end

		# config.vm.synced_folder ".", "/home/vagrant/ansible
	end
end
