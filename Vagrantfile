# coding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 2.0.0"

Vagrant.configure("2") do |config|

  # Utilisation de box Ubuntu par défaut
  config.vm.box = "centos/7"

  config.vm.box_version = "1801.02"
  config.hostmanager.manage_host = true 

  config.vm.provision "shell", inline: <<-SHELL  
    swapoff -a
    setenforce 0
	SHELL

  config.vm.define "master1.softeam.fr" do |master1_cfg|

    # Hostname pour y accéder depuis l'host
    master1_cfg.vm.hostname = "master1.softeam.fr"
    master1_cfg.vm.network "public_network", :dev => "virbr0", :mode => "bridge", :type => "bridge"
    
    # master1_cfg.vm.network "forwarded_port", guest: 6433, host: 6433

    master1_cfg.vm.provider "libvirt" do |vb|
      vb.memory = "4096"
      vb.cpus = 2
    end
  end

  config.vm.define "slave1.softeam.fr" do |slave1_cfg|

    # Hostname pour y accéder depuis l'host
    slave1_cfg.vm.hostname = "slave1.softeam.fr"
    slave1_cfg.vm.network "public_network", :dev => "virbr0", :mode => "bridge", :type => "bridge"

    # slave1_cfg.vm.network "forwarded_port"

    slave1_cfg.vm.provider "libvirt" do |vb|
      vb.memory = "4096"
      vb.cpus = 2
    end
  end
end
