Vagrant.configure("2") do |config|
    config.vm.define "jenkins-selenium-vm"
    config.vm.box = "debian/buster64"

    # port jenkins 8080
    config.vm.network "forwarded_port", guest: 8080, host: 7070
    # port for prestashop (suppose that ps docker container map ports by this may  : -p 8001:80)
    config.vm.network "forwarded_port", guest: 8001, host: 7001  
    # vm local prestashop server
    config.vm.network "forwarded_port", guest: 80, host: 7000

    config.vm.network "private_network", ip: "192.168.34.100" 
    
    
    config.vm.provider "virtualbox" do |v|
      v.cpus = 4
      v.memory = 4096
    end
    
    #config.vm.synced_folder '.', '/vagrant', type: "rsync", rsync__exclude: ".vagrant/"
    config.vm.synced_folder '.', '/vagrant', type: "virtualbox", rsync__exclude: ".vagrant/"
    config.vm.provision :shell, path: "ext/ansible.sh"
    config.vm.provision :shell, inline: "export ANSIBLE_HOST_KEY_CHECKING=False"
    config.vm.provision 'ansible' do |ansible|
        ansible.playbook = "ext/docker.yml"
        ansible.verbose = 'vv'
        ansible.become = true
    end
  end


  #vagrant plugin install vagrant-vbguest