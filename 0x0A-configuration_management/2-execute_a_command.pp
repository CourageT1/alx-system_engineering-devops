# Using Puppet, install flask from pip3.

exec { 'kill_killmenow':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'], # Specify the command's path as needed
  refreshonly => true,
  onlyif      => 'pgrep killmenow',    # Check if the process exists before attempting to kill it
}
