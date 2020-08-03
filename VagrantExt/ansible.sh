#!/usr/bin/env bash

set -e # Exit if any subcommand fails
set -x # Print commands for troubleshooting

	#sudo apt-add-repository --remove ppa:ansible/ansible
	## update ansible repo configuration
	sudo apt-get update -y
	sudo apt-get install -y software-properties-common
	
	### install ansible 	
	sudo apt-get install ansible -y

	### generate ssh public en prive key
	#ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -P ""
	echo 'root:1234567890' | chpasswd