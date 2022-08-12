# create a file
$str = 'I love Puppet'

file { '/tmp/school':
  ensure  => 'present',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => $str,
}
