from flask import Blueprint
from flask import jsonify

from .extensions import mongo

import json
from bson import ObjectId

main = Blueprint('main', __name__)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


#################################begin starturl routes###############################

@main.route('/createkeyword')
def createKw():
    keyword_collection = mongo.db.keywords
    keyword_collection.insert({'keyword': 'Class B'})
    return '<h1>Added new keyword!</h1>'


@main.route('/findkeyword')
def findKw():
    keyword_collection = mongo.db.keywords
    keyword = keyword_collection.find_one({'keyword': 'Class B'})
    return f'<h1>Keyword: { keyword["keyword"] } </h1>'





# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
@main.route('/updatekeyword')
def updateKw():
    keyword_collection = mongo.db.keywords
    keyword = keyword_collection.find_one({'keyword': 'Class B'})
    keyword["keyword"] = "Winnebago"

    keyword_collection.save(keyword)

    return '<h1>Updated Keyword!</h1>'


@main.route('/deletekeyword')
def deleteKw():
    keyword_collection = mongo.db.keywords
    keyword = keyword_collection.find_one({'keyword': 'Winnebago'})

    keyword_collection.remove(keyword)

    return '<h1>Deleted Keyword!</h1>'

#################################end keywords routes#################################
#################################begin starturl routes###############################


@main.route('/createstarturl')
def index():
    starturl_collection = mongo.db.starturls
    starturl_collection.insert({'starturl': 'http://www.craigslist.org'})
    return '<h1>Added new Start Url!</h1>'


@main.route('/findstarturl')
def find():
    starturl_collection = mongo.db.starturls
    starturl = starturl_collection.find_one(
        {'starturl': 'http://www.craigslist.org'})
    return f'<h1>Start Url: { starturl["starturl"] } </h1>'


@main.route('/updatestarturl')
def update():
    starturl_collection = mongo.db.starturls
    starturl = starturl_collection.find_one(
        {'starturl': 'http://www.craigslist.org'})
    starturl["starturl"] = "www.google.com"

    starturl_collection.save(starturl)

    return '<h1>Updated Start Url!</h1>'


@main.route('/deletestarturl')
def delete():
    starturl_collection = mongo.db.starturls
    starturl = starturl_collection.find_one(
        {'starturl': 'http://www.craigslist.org'})

    starturl_collection.remove(starturl)

    return '<h1>Deleted Start Url!</h1>'

#################################end starturl routes###############################


# for the find route. find multiple keys.
# Language: { user["language"] }
