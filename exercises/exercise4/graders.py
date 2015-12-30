import re
import requests
from exercises.registry import register_grader

def validate(metadata, onion_url):
    for prefix in ['http://', 'https://']:
        if onion_url.startswith(prefix):
            onion_url = onion_url[len(prefix):]
            break

    pattern = re.compile("^[A-Za-z0-9]+\.onion$")
    if not pattern.search(onion_url):
        return False

    r = requests.get('https://' + onion_url + '.to')
    if r.status_code != 200:
        return False

    return metadata.user.email in r.text


register_grader('20.0', validate)
