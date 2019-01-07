# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 2.0.0"

Vagrant.configure("2") do |config|

	# Utilisation de box Ubuntu par défaut
	config.vm.box = "centos/7"

	config.vm.box_version = "1801.02"

	config.vm.provision "shell", inline: <<-SHELL
		swapoff -a

		yum install -y net-tools

		echo "10.0.0.2 master1.softeam.fr master1" > /tmp/hosts.back
		echo "10.0.0.3 slave1.softeam.fr slave1" >> /tmp/hosts.back
		
		cat  /etc/hosts | grep -v 'slave' |  grep -v 'master' >> /tmp/hosts.back
		cat /tmp/hosts.back > /etc/hosts
	SHELL

	config.vm.define "master1.softeam.fr" do |master1_cfg|

		# Hostname pour y accéder depuis l'host
		  master1_cfg.vm.hostname = "master1.softeam.fr"
		  master1_cfg.vm.network "public_network", ip: "10.0.0.2", bridge: "enp0s31f6"

		  master1_cfg.vm.network "forwarded_port", guest: 6433, host: 6433

		  master1_cfg.vm.provider "virtualbox" do |vb|
			vb.memory = "2048"
			vb.cpus = 2
		end
	end

	config.vm.define "slave1.softeam.fr" do |slave1_cfg|

		  # Hostname pour y accéder depuis l'host
		  slave1_cfg.vm.hostname = "slave1.softeam.fr"
		  slave1_cfg.vm.network "public_network", ip: "10.0.0.3", bridge: "enp0s31f6"

		  slave1_cfg.vm.network "forwarded_port", guest: 80, host: 8080

		  slave1_cfg.vm.provider "virtualbox" do |vb|
			vb.memory = "4096"
			vb.cpus = 2
		end
	end
end