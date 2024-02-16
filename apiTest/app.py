from flask import Flask
from Apps.System.systemController import app_system
from Apps.ECSensor.ecSensorController import app_ecsensor

main_app = Flask(__name__)
main_app.register_blueprint(app_system)
main_app.register_blueprint(app_ecsensor)

if __name__ == "__main__":
    main_app.run()