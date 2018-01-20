import os
import sys
import tornado.options
import tornado.ioloop
from django.core.management.base import BaseCommand, CommandError
from tornado.options import options, define, parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = 'jetbov.settings'
from django.conf import settings
from django.core.wsgi import get_wsgi_application

port = os.getenv('PORT', 8801)
define('port', type=int, default=port)

TEMPLATE_PATH = os.path.join(settings.BASE_DIR, 'templates')
APP_FOLDER = os.path.dirname(settings.BASE_DIR)
APP_FRONT = os.path.join(APP_FOLDER, 'jetbov', 'app_front_end')
# print9()
print("APP_FRONT: ", APP_FRONT)
STATIC_PATH = settings.STATIC_ROOT
define("template_path", TEMPLATE_PATH, group="application")
define("autoreload", settings.DEBUG, group="application")


def make_app():
    wsgi_app = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(wsgi_app)
    # if settings.DEBUG:
    urls_to_tornado = [
        (r'/api/?(.*)', tornado.web.FallbackHandler, dict(fallback=container)),
        (r'/admin/?(.*)', tornado.web.FallbackHandler, dict(fallback=container)),
        (r'/static/?(.*)', tornado.web.StaticFileHandler, {'path': settings.STATIC_DIR, 'default_filename':'index.html'}),
        (r'/?(.*)', tornado.web.StaticFileHandler, {'path': APP_FRONT, 'default_filename':'index.html'}),
    ]
        
    return tornado.web.Application(
        urls_to_tornado,
        **options.group_dict('application'))


class Command(BaseCommand):
    help = 'Iniciar o projeto django usando o e servindo com o tornado'

    def handle(self, *args, **options):
        tornado.options.parse_command_line()
        tornado_app = make_app()
        server = tornado.httpserver.HTTPServer(tornado_app)
        server.listen(port)
        sys.stdout.write('Starting development server at port: '+str(port)+'\n')
        tornado.ioloop.IOLoop.instance().start()