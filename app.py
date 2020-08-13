token="EAAEmPk5qQekBAMkEodRg92UfNv6f5zKROWRpivPxIK3JjMhPvtGz5lcG840tphklvAsI6PTP54G1gJRwPVcd60dAvYCNoXE2nFRjW7k1IgDRRTSt9oyFcbpPNplPNOMQWV3GCrVZB8I9ZBbTTCQNbl6COmmZBRcZBVCc3zlDUQZDZD"
import os
from flask import Flask, request
from messenger import Messenger

app = Flask(__name__)
app.debug = True

messenger = Messenger( token )

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if (request.args.get('hub.verify_token') == token ):
            return request.args.get('hub.challenge')
        raise ValueError('FB_VERIFY_TOKEN does not match.')
    elif request.method == 'POST':
        messenger.handle(request.get_json(force=True))
    return ''


if __name__ == "__main__":
    app.run(host='0.0.0.0')

