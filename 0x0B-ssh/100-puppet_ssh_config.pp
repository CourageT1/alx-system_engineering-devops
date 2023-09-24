#!/usr/bin/env bash
# Disable password authentication and configure SSH client to use a specific private key
file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  ensure => present,
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  ensure => present,
}
