import os

from app import blueprint
from app.main import create_app, db
from flask_migrate import Migrate

environment = os.getenv('ENV') or 'dev'
app = create_app(config_name=environment)
app.register_blueprint(blueprint)
app.app_context().push()

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
