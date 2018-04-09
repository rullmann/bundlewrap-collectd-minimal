# collectd-minimal

[collectd](https://collectd.org/) is an open-source monitoring tool. Originally developed with rrd files as backend storage it now has the ability to write it's data to multiple targets.

This bundle is build for Raspberry Pi and other devices which may not require a full monitoring solution, but should send specific data to some kind of backend.
As a first step the collectd network protocol has been implemented.
This very well fits together with the [telegraf Bundle](https://github.com/rullmann/bundlewrap-telegraf). It can receive the collectd network protocol data and foreward store the data in a backend, e.g. [InfluxDB](https://github.com/rullmann/bundlewrap-influxdb).

Make sure your collectd config files are being stored within `/etc/collectd.d` as demonstrated for the [Synology monitoring](https://github.com/rullmann/bundlewrap-collectd-synology).

## Integrations

* Bundles:
  * [telegraf](https://github.com/rullmann/bundlewrap-telegraf)

## Metadata

    'metadata': {
        'collectd': {
            'client': {
                'ip': '127.0.0.1', # required, set to your collectd server ip
                'user': 'collectd', # username for authenicating at the target server
                'password': 'mysupersecretpw', # required
            },
        },
    }
