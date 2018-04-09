pkg_dnf = {
    'collectd': {},
}

svc_systemd = {
    'collectd': {
        'needs': ['pkg_dnf:collectd'],
    },
}

files = {
    '/etc/collectd.conf': {
        'mode': '0600',
        'content_type': 'mako',
        'context': {
            'collectd': node.metadata.get('collectd', {}),
        },
        'needs': ['pkg_dnf:collectd'],
        'triggers': ['svc_systemd:collectd:restart'],
    },
    '/etc/collectd.d/nut.conf': {
        'delete': True,
        'needs': ['pkg_dnf:collectd'],
    },
}

if node.metadata.get('collectd', {}).get('client'):
    files['/etc/collectd.d/client.conf'] = {
        'mode': '0600',
        'content_type': 'mako',
        'context': {
            'client': node.metadata.get('collectd', {}).get('client', {}),
        },
        'needs': ['pkg_dnf:collectd'],
        'triggers': ['svc_systemd:collectd:restart'],
    }
