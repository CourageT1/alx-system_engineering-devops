# Using Puppet, create a file in /tmp.
# Requirements:
# File path is /tmp/school
# File permission is 0744
# File owner is www-data
# File group is www-data
# File contains I love Puppet

file { '/tmp/school':
  ensure  => 'file',         # Ensure it's a file
  mode    => '0744',         # File permissions
  owner   => 'www-data',     # File owner
  group   => 'www-data',     # File group
  path    => '/tmp/holberton',
  content => 'I love Puppet',
}
