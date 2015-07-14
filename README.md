# domain-block-list

List of domains that server spam and/or intrusive ads that I use in my
anti-spam/adblock setup.

Copyright 2013 [Sudaraka Wijesinghe] [url_contact].

This work is licensed under the Creative Commons Attribution 3.0 Unported
License. To view a copy of this license, visit
[http://creativecommons.org/licenses/by/3.0/] [url_cc].

## Usage (with Bind)

If your computer/network uses a Bind (DNS) server you can configure, you can
make the block list effect all the computers that are using that DNs server by
following the instructions below.

1. Place the block-list.conf file somewhere accessible to the Bind server
   process.
2. Include this file into Bind configuration (ex. /etc/bind/named.conf)

    `include "/path/to/block-list.conf";`

3. Create the zone file with following content. Note that block-list.conf have
   the zone file hardcoded as /home/bind/db/blocked but you can place it
   anywhere readable to Bind. In fact you probably need to change this in your
   configuration.

        TTL	31536000
        @	IN	SOA	ns.blocked-domain.nx.	root.nowhere.nx. (
            2013012101
            31536000
            600
            31536000
            600 );
        @	IN	NS	ns.blocked-domain.nx.

4. Restart Bind.

## Usage (with host file)

If you don't have access a DNS server or just want to use the list in a single
computer, you can generate the host file compatible format using the provided
script as follows.

`./generate-host-file.py >> /etc/hosts`

Note that you need to run this as root.

  [url_contact]: http://sudaraka.org/contact/
  [url_cc]: http://creativecommons.org/licenses/by/3.0/
