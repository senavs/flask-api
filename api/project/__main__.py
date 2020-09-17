from . import create_app
from .settings import werkzeug_env

if __name__ == '__main__':
    app = create_app()

    app.run(host=werkzeug_env.HOST, port=werkzeug_env.PORT, debug=werkzeug_env.DEBUG)
