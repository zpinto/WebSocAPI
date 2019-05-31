from flask import Flask, jsonify
from flask_restful import Api

from resources.breadth import Breadth, BreadthList

app = Flask(__name__)
api = Api(app)

api.add_resource(Breadth, '/Breadth/<string:option>')
api.add_resource(BreadthList, '/Breadths')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
