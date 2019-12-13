import copy

from flask_restful import Resource
from flask import request
from scrapy import get_class_info, get_select
from config import BASE_URL, REQUIRED_ARGS


class Course(Resource):
    def get(self):
        #filter_args = jsonify(filters)
        args = copy.deepcopy(REQUIRED_ARGS)
        for key, value in request.args.items():
            args[key] = value
        classes = get_class_info(BASE_URL, "", args)

        if classes:
            return classes, 200
        else:
            return {'message': 'Cannot find classes'}, 404
