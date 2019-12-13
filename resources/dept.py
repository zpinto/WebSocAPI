import copy

from flask_restful import Resource
from scrapy import get_class_info, get_select
from config import BASE_URL, REQUIRED_ARGS


class Dept(Resource):
    def get(self, department_name):
        args = copy.deepcopy(REQUIRED_ARGS)
        args['Dept'] = department_name
        classes = get_class_info(BASE_URL, "", args)

        if classes:
            return classes, 200
        else:
            return {'message': 'Cannot find classes'}, 404


class DeptList(Resource):
    def get(self):
        return get_select('Dept'), 200
