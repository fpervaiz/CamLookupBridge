import datetime
import os
import requests
import sys

from flask import Flask, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

sys.stdout = open('/home/user/camlookupbridge/logs/' +
                  str(datetime.datetime.now()) + '.log', 'w')
sys.stderr = sys.stdout

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'admin': generate_password_hash(os.environ.get('CAMLOOKUPBRIDGE_ADMIN_PWD')),
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/lookup/user/<crsid>')
@auth.login_required
def lookup(crsid):
    r = requests.get(
        'https://www.lookup.cam.ac.uk/api/v1/person/crsid/' + crsid + '?fetch=all_insts', headers={'Accept': 'application/json'})

    response = r.json()['result']

    if 'person' in response:
        return {
            'crsid': response['person']['identifier']['value'],
            'visibleName': response['person']['visibleName'],
            'cancelled': response['person']['cancelled'],
            'isStudent': response['person']['student'],
            'isStaff': response['person']['staff'],
            'affiliation': response['person']['misAffiliation'],
            'college': [institution['instid'] for institution in response['person']['institutions'] if 'College' in institution['name'] and not institution['cancelled']]
        }

    else:
        abort(400, 'Invalid crsid')


if __name__ == '__main__':
    app.run()
