Vagrant.configure("2") do |config|
        config.vm.define "s1" do |s1|
                s1.vm.box = "p4-onos"
		s1.vm.network "private_network",ip: "10.10.1.101", netmask: "255.255.255.0",virtualbox__intnet: "controller"
                s1.vm.network "private_network",ip: "172.16.1.12", netmask: "255.255.255.0", virtualbox__intnet: "s1-s2"
                s1.vm.network "private_network",ip: "172.16.1.13", netmask: "255.255.255.0", virtualbox__intnet: "s1-s3"
                s1.vm.network "private_network",ip: "172.16.10.10", netmask: "255.255.255.0", virtualbox__intnet: "src*-s1"
                s1.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "1024"
                        virtualbox.cpus = "1"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc3", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc4", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc5", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "s2" do |s2|
                s2.vm.box = "p4-onos"
		s2.vm.network "private_network",ip: "10.10.1.102", netmask: "255.255.255.0",virtualbox__intnet: "controller"
                s2.vm.network "private_network",ip: "172.16.1.21", netmask: "255.255.255.0", virtualbox__intnet: "s1-s2"
		s2.vm.network "private_network",ip: "172.16.4.24", netmask: "255.255.255.0", virtualbox__intnet: "s2-s4"
		s2.vm.network "private_network",ip: "172.16.20.10", netmask: "255.255.255.0", virtualbox__intnet: "src2-s2"
                s2.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "1024"
                        virtualbox.cpus = "1"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc3", "allow-all"]
			virtualbox.customize ["modifyvm", :id,"--nicpromisc4", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc5", "allow-all"]
			virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "s3" do |s3|
                s3.vm.box = "p4-onos"
                s3.vm.network "private_network",ip: "10.10.1.103", netmask: "255.255.255.0", virtualbox__intnet: "controller"
                s3.vm.network "private_network",ip: "172.16.3.31", netmask: "255.255.255.0", virtualbox__intnet: "s1-s3"
                s3.vm.network "private_network",ip: "172.16.3.34", netmask: "255.255.255.0", virtualbox__intnet: "s3-s4"
                s3.vm.network "private_network",ip: "172.16.30.10", netmask: "255.255.255.0", virtualbox__intnet: "src3-s3"
                s3.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "1024"
                        virtualbox.cpus = "1"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc3", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc4", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc5", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "s4" do |s4|
                s4.vm.box = "p4-onos"
                s4.vm.network "private_network",ip: "10.10.1.104", netmask: "255.255.255.0", virtualbox__intnet: "controller"
                s4.vm.network "private_network",ip: "172.16.4.42", netmask: "255.255.255.0", virtualbox__intnet: "s2-s4"
                s4.vm.network "private_network",ip: "172.16.4.43", netmask: "255.255.255.0", virtualbox__intnet: "s3-s4"
                s4.vm.network "private_network",ip: "172.16.40.11", netmask: "255.255.255.0", virtualbox__intnet: "s4-sink1"
                s4.vm.network "private_network",ip: "172.16.40.12", netmask: "255.255.255.0", virtualbox__intnet: "s4-sink2"
                s4.vm.network "private_network",ip: "172.16.40.13", netmask: "255.255.255.0", virtualbox__intnet: "s4-sink3"
                s4.vm.network "private_network",ip: "172.16.40.14", netmask: "255.255.255.0", virtualbox__intnet: "s4-sink4"
                s4.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "1024"
                        virtualbox.cpus = "1"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc3", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc4", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc5", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc6", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc7", "allow-all"]
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc8", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "sink1" do |sink1|
                sink1.vm.box = "loadgen"
                sink1.vm.network "private_network",ip: "172.16.40.101", netmask: "255.255.255.0", virtualbox__intnet: "s4-sink1"
                sink1.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "2048"
                        virtualbox.cpus = "2"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "sink2" do |sink2|
                sink2.vm.box = "loadgen"
                sink2.vm.network "private_network",ip: "172.16.40.102", netmask: "255.255.255.0", virtualbox__intnet: "s4-sink2"
                sink2.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "2048"
                        virtualbox.cpus = "2"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "sink3" do |sink3|
                sink3.vm.box = "loadgen"
                sink3.vm.network "private_network",ip: "172.16.40.103", netmask: "255.255.255.0", virtualbox__intnet: "s4-sink3"
                sink3.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "2048"
                        virtualbox.cpus = "2"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "sink4" do |sink4|
                sink4.vm.box = "loadgen"
                sink4.vm.network "private_network",ip: "172.16.40.104", netmask: "255.255.255.0", virtualbox__intnet: "s4-sink4"
                sink4.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "2048"
                        virtualbox.cpus = "2"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "src5" do |src5|
                src5.vm.box = "loadgen"
                src5.vm.network "private_network",ip: "172.16.10.105", netmask: "255.255.255.0", virtualbox__intnet: "src*-s1"
                src5.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "512"
                        virtualbox.cpus = "1"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "src1" do |src1|
                src1.vm.box = "loadgen"
                src1.vm.network "private_network",ip: "172.16.10.101", netmask: "255.255.255.0", virtualbox__intnet: "src*-s1"
                src1.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "512"
                        virtualbox.cpus = "1"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "src2" do |src2|
                src2.vm.box = "loadgen"
                src2.vm.network "private_network",ip: "172.16.10.102", netmask: "255.255.255.0", virtualbox__intnet: "src*-s1"
                src2.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "512"
                        virtualbox.cpus = "1"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "src3" do |src3|
                src3.vm.box = "loadgen"
                src3.vm.network "private_network",ip: "172.16.10.103", netmask: "255.255.255.0", virtualbox__intnet: "src*-s1"
                src3.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "512"
                        virtualbox.cpus = "1"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "src4" do |src4|
                src4.vm.box = "loadgen"
                src4.vm.network "private_network",ip: "172.16.10.104", netmask: "255.255.255.0", virtualbox__intnet: "src*-s1"
                src4.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "512"
                        virtualbox.cpus = "1"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
        config.vm.define "controller" do |controller|
                controller.vm.box = "p4-onos"
                controller.vm.network "private_network",ip: "10.10.1.100", netmask: "255.255.255.0",virtualbox__intnet: "controller"
                controller.vm.provider "virtualbox" do |virtualbox|
                        virtualbox.memory = "1024"
                        virtualbox.cpus = "1"
                        virtualbox.customize ["modifyvm", :id,"--nicpromisc2", "allow-all"]
                        virtualbox.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 1000 ]
                end
        end
end
