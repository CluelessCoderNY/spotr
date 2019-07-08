from flask import Flask 
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

a_keyword = api.model('Keyword', {'keyword' : fields.String('The keyword.')})

keywords = []
# python = {'language' : 'Python'}
# languages.append(python)

@api.route('/keywords')
class Keywords(Resource):
    def get(self):
        return keywords

    @api.expect(a_keyword)
    def post(self):
        keywords.append(api.payload)
        return {'result' : 'Keyword added'}, 201

    def delete(self, id):
        keyword = self.get(id)
        self.keywords.remove(keyword) 

if __name__ == '__main__':
    app.run(debug=True)