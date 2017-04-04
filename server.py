#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.log as tlog
from os import path
from logger import logger

DEFAULT_ADDRESS = '127.0.0.1'
DEFAULT_PORT = 8888
DEBUG = True
AUTOLOAD = True

handlers = [
]

def run(address, port):
    settings = {
        'static_path': path.join(path.dirname(\
                       path.abspath(__file__)), 'static'),
        'debug': DEBUG,
        'autoload': AUTOLOAD,
    }

    app = tornado.web.Application(handlers=handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    tlog.enable_pretty_logging()
    http_server.listen(port)
    logger.info("server start at %s:%s"%(address, port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", default=DEFAULT_ADDRESS)
    parser.add_argument("-p", "--port", default=DEFAULT_PORT)
    args, unknown = parser.parse_known_args()
    run(args.address, args.port)
