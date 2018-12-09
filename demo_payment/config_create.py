import yaml
from options import options

data = {}
data['uwsgi'] = {
    'socket': options.demo_payment_website_url,
    'logdate': '%d/%m/%Y-%H:%M:%S',
    'protocol': 'http',
    'mount': '/demo-payment-server=demo_payment.server:app'
}

with open('wsgi_config.yaml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
