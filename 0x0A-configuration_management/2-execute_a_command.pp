# Using Puppet, create a manifest that kills a process named killmenow.
# Requirements:
# Must use the exec Puppet resource
# Must use pkill

exec { 'kill_killmenow':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'], # Specify the command's path as needed
  refreshonly => true,
  onlyif      => 'pgrep killmenow',    # Check if the process exists before attempting to kill it
}
