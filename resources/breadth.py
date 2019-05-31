from flask_restful import Resource
from scrapy import get_class_info, get_select


class Breadth(Resource):
    def get(self, option):
        get_class_info()


class BreadthList(Resource):
    def get(self):
        return get_select('Breadth')
