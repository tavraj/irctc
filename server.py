import os

from app import blueprint
from app.main import create_app

environment = os.environ.get('ENV', 'development')
app = create_app(config_name=environment)
app.register_blueprint(blueprint)
app.app_context().push()


def main():
    app.run()


if __name__ == '__main__':
    main()
