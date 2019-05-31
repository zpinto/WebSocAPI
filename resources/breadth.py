from flask_restful import Resource
from scrapy import get_class_info, get_select
from config import BASE_URL, REQUIRED_ARGS


class Breadth(Resource):
    def get(self, option):
        args = REQUIRED_ARGS
        args['Breadth'] = option
        classes = get_class_info(BASE_URL, "", args)

        if classes:
            return classes, 200
        else:
            return {'message': 'Cannot find classes'}, 404


class BreadthList(Resource):
    def get(self):
        return get_select('Breadth'), 200
