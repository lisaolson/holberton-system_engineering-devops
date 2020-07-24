# Creates a file

file { '/tmp/clo':
    path    => '/tmp/clo',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
