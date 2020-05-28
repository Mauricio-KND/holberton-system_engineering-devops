# Changes limits of in Nginx.

exec { 'change':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx; sudo service nginx restart'
}
