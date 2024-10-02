#!/usr/bin/env python3

import os
import time
from jinja2 import Environment, FileSystemLoader

template_file='/etc/nginx/nginx.conf.j2'
output_file='/etc/nginx/nginx.conf'

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(template_file)

context = {
        "SSL_MODE": os.getenv('SSL_MODE', 'OFF'), #OFF, ON, FORCE
        "WEB_AUTH": os.getenv('WEB_AUTH', 'OFF'), #OFF, ON
        "timestamp": time.strftime("%d %b %y %H:%M"),
}

#print(context)

with open(output_file, 'w') as f:
    f.write(template.render(context))