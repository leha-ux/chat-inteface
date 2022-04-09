#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""
Talk with a model using a web UI.

## Examples

```shell
parlai interactive_web --model-file "zoo:tutorial_transformer_generator/model"
```
"""


from http.server import BaseHTTPRequestHandler, HTTPServer
#from parlai.scripts.interactive import setup_args
#from parlai.core.agents import create_agent
#from parlai.core.worlds import create_task
from typing import Dict, Any
#from parlai.core.script import ParlaiScript, register_script
#import parlai.utils.logging as logging

import json
import time

#from parlai.agents.local_human.local_human import LocalHumanAgent

HOST_NAME = 'localhost'
PORT = 8080

SHARED: Dict[Any, Any] = {}


class MyHandler(BaseHTTPRequestHandler):
    """
    Handle HTTP requests.
    """

    def _interactive_running(self, opt, reply_text):
        reply = {'episode_done': False, 'text': reply_text}
        #SHARED['agent'].observe(reply)
        #model_res = SHARED['agent'].act()
        #return model_res

    def do_HEAD(self):
        """
        Handle HEAD requests.
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        """
        Handle POST request, especially replying to a chat message.
        """
        if self.path == '/interact':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            print(body.decode('utf-8'))
            #model_response = self._interactive_running(
            #    SHARED.get('opt'), body.decode('utf-8')
            #)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            #json_str = json.dumps(model_response.json_safe_payload())
            #self.wfile.write(bytes(json_str, 'utf-8'))
            #--------- REPLACEMENT -----------------
            self.wfile.write("Test".encode())
        elif self.path == '/reset':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            print(body.decode('utf-8'))
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            #SHARED['agent'].reset()
            #self.wfile.write(bytes("{}", 'utf-8'))
            #----------REPLACEMENT -----------------
            self.wfile.write("RESET".encode())
        else:
            return self._respond({'status': 500})

    '''def do_GET(self):
        """
        Respond to GET request, especially the initial load.
        """
        paths = {
            '/': {'status': 200},
            '/favicon.ico': {'status': 202},  # Need for chrome
        }
        if self.path in paths:
            self._respond(paths[self.path])
        else:
            self._respond({'status': 500})'''

    def _handle_http(self, status_code, path, text=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        #content = WEB_HTML.format(STYLE_SHEET, FONT_AWESOME)
        #return bytes(content, 'UTF-8')

    '''def _respond(self, opts):
        response = self._handle_http(opts['status'], self.path)
        self.wfile.write(response)'''


'''def setup_interweb_args(shared):
    """
    Build and parse CLI opts.
    """
    parser = setup_args()
    parser.description = 'Interactive chat with a model in a web browser'
    parser.add_argument('--port', type=int, default=PORT, help='Port to listen on.')
    parser.add_argument(
        '--host',
        default=HOST_NAME,
        type=str,
        help='Host from which allow requests, use 0.0.0.0 to allow all IPs',
    )
    return parser'''

'''
def shutdown():
    global SHARED
    if 'server' in SHARED:
        SHARED['server'].shutdown()
    SHARED.clear()


def wait():
    global SHARED
    while not SHARED.get('ready'):
        time.sleep(0.01)
'''

def interactive_web(opt):
    global SHARED

    #human_agent = LocalHumanAgent(opt)

    # Create model and assign it to the specified task
    '''agent = create_agent(opt, requireModelExists=True)
    agent.opt.log()
    SHARED['opt'] = agent.opt
    SHARED['agent'] = agent
    SHARED['world'] = create_task(SHARED.get('opt'), [human_agent, SHARED['agent']])

    MyHandler.protocol_version = 'HTTP/1.0'
    httpd = HTTPServer((opt['host'], opt['port']), MyHandler)
    SHARED['server'] = httpd
    logging.info('http://{}:{}/'.format(opt['host'], opt['port']))

    try:
        SHARED['ready'] = True
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


@register_script('interactive_web', aliases=['iweb'], hidden=True)
class InteractiveWeb(ParlaiScript):
    @classmethod
    def setup_args(cls):
        return setup_interweb_args(SHARED)

    def run(self):
        return interactive_web(self.opt)


if __name__ == '__main__':
    InteractiveWeb.main()'''


def main():
    PORT=8082
    server = HTTPServer(('', PORT), MyHandler)
    print("Server running forever")
    try: 
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print("ENd")
if __name__ == '__main__':
    main()