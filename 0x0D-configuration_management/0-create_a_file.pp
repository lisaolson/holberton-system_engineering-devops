file { '/tmp/holberton':
    path    => '/tmp/holberton',
    ensure  => file,
    mode    => '0700',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
