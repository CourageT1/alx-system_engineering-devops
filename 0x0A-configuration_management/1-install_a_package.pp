# Using Puppet, install flask from pip3.
# Requirements:
# Install flask
# Version must be 2.1.0

package { 'flask':
  ensure   => '2.1.0',   # Specify the desired version
  provider => 'pip3',    # Use pip3 as the package provider
}
