from flask import Blueprint, request
from flask import jsonify

from .extensions import mongo

import copy
import json
from bson import ObjectId

main = Blueprint('main', __name__)

#################################begin starturl routes###############################


@main.route('/createkeyword', methods = ['GET', 'POST'])
def createKw():
    keyword_collection = mongo.db.keywords
    keyword_collection.insert(request.get_json())
    return '<h1>Added new keyword!</h1>'


@main.route('/findkeyword')
def findKw():
    keyword_collection = mongo.db.keywords
    keyword = keyword_collection.find_one({'keyword': 'Class B'})
    return f'<h1>Keyword: { keyword["keyword"] } </h1>'


@main.route('/findkeywords')
def findAllKw():
    keyword_collection = mongo.db.keywords
    output = []

    for key in keyword_collection.find():
        output.append({'keyword': key['keyword']})
    return jsonify({'result': output})


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


@main.route('/findstarturls')
def findAllStartUrls():
    starturl_collection = mongo.db.starturls
    output = []

    for url in starturl_collection.find():
        output.append({'starturl': url['starturl']})
    return jsonify({'result': output})


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
#################################begin scraped results routes######################


@main.route('/findpost')
def findpost():
    post_collection = mongo.db.posts
    link = request.args.get('link')

    if link == None:
        posts = post_collection.find()
        q = []
        for post in posts:
            s_p = copy.deepcopy(post)
            s_p['_id'] = str(s_p['_id'])
            q.append(s_p)

            j_d = json.dumps(q)
        return '{"data": "' + j_d + '"}'
    else:
        q = post_collection.find_one({'link': link})
        q['_id'] = str(q['_id'])

        return q
    

#################################end scraped results routes########################
