import os
from flask import Flask
from flask_cors import CORS

from backend.config import Config
from backend.extensions import db, migrate, bcrypt, jwt
from backend.blueprints.auth import bp as auth_bp
from backend.blueprints.roles import bp as roles_bp
from backend.blueprints.users import bp as users_bp
from backend.blueprints.topics import bp as topics_bp
from backend.blueprints.selections import bp as selections_bp
from backend.blueprints.offices import bp as offices_bp
from backend.blueprints.teachers import bp as teachers_bp
from backend.blueprints.students import bp as students_bp
from backend.blueprints.logs import bp as logs_bp
from backend.blueprints.stats import bp as stats_bp
from backend.services.rbac import seed_core_rbac


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(roles_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(topics_bp)
    app.register_blueprint(selections_bp)
    app.register_blueprint(offices_bp)
    app.register_blueprint(teachers_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(logs_bp)
    app.register_blueprint(stats_bp)

    @app.cli.command("seed-rbac")
    def seed_rbac_cmd():
        with app.app_context():
            seed_core_rbac()
            print("RBAC seeded")

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_core_rbac()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))

