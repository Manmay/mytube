import sys
from flask import Flask, send_from_directory
from listener import Listener

application = Flask(__name__)
listener = Listener(sys.argv[1])


@application.route('/watch/<video>')
def watch(video):
    return send_from_directory(sys.argv[1], video)

if __name__ == '__main__':
    listener.start()
    application.run(host='0.0.0.0', port=5555)
