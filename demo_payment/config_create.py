import json
from options import options

data = {}
data['uwsgi'] = {
    'socket': ["127.0.0.1:8889"],
    'logdate': '%d/%m/%Y-%H:%M:%S',
    'protocol': 'http -w demo_payment.wsgi',
    'chdir': '/demo-payment-server',
    'module': 'demo_payment.server'
}

print(json.dumps(data, indent=4))

with open('wsgi_config.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
