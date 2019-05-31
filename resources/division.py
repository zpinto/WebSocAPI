from flask_restful import Resource
from scrapy import get_select


class DivisionList(Resource):
    def get(self):
        return get_select('Division'), 200
