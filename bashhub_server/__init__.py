from kyoukai import Kyoukai
from .util import jsonify
from .models import Base
from .api_v1 import api_v1

app = Kyoukai("bashhub")
app.register_blueprint(api_v1)


@app.route("/")
async def index(ctx):
    return jsonify({"_": repr(ctx.dbsession)})


@app.route("/_create_all")
async def _create_all(ctx):
    Base.metadata.create_all(ctx.sql)
    return "OK"


@app.before_request
async def before_request(ctx):
    print(repr(ctx.request.path))
    print(repr(ctx.request.headers))
    print(repr(ctx.request.body))
    print("")
    return ctx
