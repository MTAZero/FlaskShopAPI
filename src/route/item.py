from flask import Blueprint, jsonify, current_app
from flask.ext.restful import Api
from bson.json_util import dumps

from model import item

# ans = [
#     {
#         "name": u"Macbook Air",
#         "price": 2500
#     },
#     {
#         "name": u"Iphone XS MAX",
#         "price": 1500
#     },
#     {
#         "name": u"Samsung note 9",
#         "price": 1500
#     }
# ]

item_blueprint = Blueprint('item', __name__)
item_blueprint_api = Api(item_blueprint)

@item_blueprint.route("")
def listItems():
    print("call get list item api")

    res = item.getAllItem()
    #print(res)

    return dumps(res)