import tornado.ioloop
import tornado.web
import tornado.httpclient

import json
import lxml.html
from lxml import etree
import collections

class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        if not self.get_argument('url') or not self.get_argument('xpath'):
            self.write(json.dumps({'status': 'error', 'msg': 'missing url or xpath'}))

        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch(self.get_argument('url'), callback=self.on_response)

    def on_response(self, response):
        if response.error: 
            raise tornado.web.HTTPError(500)
        tree = etree.HTML(response.body)
        r = tree.xpath(self.get_argument('xpath'))
        out = []
        if isinstance(r, list):
            for i in r:
                out.append(lxml.html.tostring(i).strip())
        else:
            print r
            out.append(lxml.html.tostring(r).strip())

        self.write(collections.OrderedDict({'status':'ok', 'result': out}))
        self.finish()

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    port = 8888
    print ' * Running on http://127.0.0.1:%d/ (Press CTRL+C to quit)' % port
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()