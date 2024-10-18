#!/usr/bin/env python3

import os
import time
from jinja2 import Template

template_file='/etc/nginx/nginx.conf.j2'
output_file='/etc/nginx/nginx.conf'

with open(template_file, 'r') as f:
    template_content = f.read()

template = Template(template_content)

context = {
        "SSL_MODE": os.getenv('SSL_MODE', 'FORCE'), #OFF, ON, FORCE
        "WEB_AUTH": os.getenv('WEB_AUTH', 'ON'), #OFF, ON
        "WR_ENABLED": bool(os.getenv('WR_ENABLED', 'NO') == 'YES'), #NO, YES
        "timestamp": time.strftime("%d %b %y %H:%M"),
}

#print(context)

with open(output_file, 'w') as f:
    f.write(template.render(context))
