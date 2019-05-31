from flask_restful import Resource
from scrapy import get_select


class YearTermList(Resource):
    def get(self):
        return get_select('YearTerm'), 200
