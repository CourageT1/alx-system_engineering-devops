#!/usr/bin/env bash
# Puppet manifest to configure SSH client

file { '/home/your_username/.ssh/config':
  ensure  => 'present',
  owner   => 'your_username',
  group   => 'your_username',
  mode    => '0600',
  content => template('your_module/ssh_config.erb'), # Replace with the actual path to your template
}

file { '/home/your_username/.ssh/school':
  ensure  => 'file',
  owner   => 'your_username',
  group   => 'your_username',
  mode    => '0600',
  source  => 'puppet:///modules/your_module/school', # Replace with the actual path to your private key
}

file_line { 'disable_password_auth':
  path   => '/home/your_username/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication',
  ensure => present,
}
