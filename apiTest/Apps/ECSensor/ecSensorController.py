from flask import Blueprint

app_ecsensor = Blueprint('app_ecsensor', __name__)
@app_ecsensor.route("/ecsensor/hello")
def ecsensor_hello():
    return "hello from ec sensor"