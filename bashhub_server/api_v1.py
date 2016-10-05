import json
from kyoukai import Blueprint
from .util import jsonify
from .models import User

api_v1 = Blueprint("api_v1", url_prefix="/api/v1")


@api_v1.route("/user", methods=["POST"])
async def register_user(ctx):
    body = json.loads(ctx.request.body)
    user = User(username=body["username"],
                password=body["password"],
                email=body["email"])
    ctx.dbsession.add(user)
    ctx.dbsession.commit()
    return "", 200


@api_v1.route("/login", methods=["POST"])
async def login_user(ctx):
    body = json.loads(ctx.request.body)
    user = User.query.filter_by(username=body["username"]).first()
    if user and user.password == body["password"]:
        return jsonify({"access_token": str(user.access_token)})
    else:
        return "Wrong username or password.", 401


@api_v1.route("/system", methods=["POST"])
async def register_system(ctx):
    body = json.loads(ctx.request.body)
    print(body)
    return "Not implemented", 500
