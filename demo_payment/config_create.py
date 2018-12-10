"""Create uWSGI Config YAML file."""
import yaml
from options import options

print(options.demo_payment_website_url)

data = {}
data['uwsgi'] = {
    'socket': options.demo_payment_website_url,
    'protocol': 'http',
    'mount': '/demo-payment-server=demo_payment.server:app'
}

with open('wsgi_config.yaml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
