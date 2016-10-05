import json
from kyoukai import Response


def jsonify(obj, status=200, headers=None):
    return Response(status, json.dumps(obj), {
        "Content-Type": "application/json",
        **headers
    })
