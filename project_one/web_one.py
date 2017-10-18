# -*- coding=utf-8 -*-
from tornado import web, httpserver, ioloop
from tornado.options import define, options

define(name='port', default=8001, type=int)


class IndexHandler(web.RequestHandler):

    def get(self):
        self.write('server web one')


if __name__ == '__main__':
    options.parse_command_line()
    app = web.Application(handlers=[(r'/index', IndexHandler)])
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()