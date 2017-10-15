#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import os
from ydq_diamond_net_handler import *


def main():
    port = 8888
    handlers = [(r"/in", DiamondNetInStorageHandler),
                (r"/out", DiamondNetOutStorageHandler),
                (r"/showinoutlog", DiamondNetShowInOutStorageLogHandler),
                (r"/showstorageall", DiamondNetShowStorageNumHandler)]
    settings = dict(
       template_path=os.path.join(os.path.dirname(__file__), "templates"),
       static_path=os.path.join(os.path.dirname(__file__), "static"),
       debug=True
    )
    application = tornado.web.Application(handlers=handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port=port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()