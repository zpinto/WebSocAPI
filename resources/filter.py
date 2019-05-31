from flask_restful import Resource
from config import FILTERS


class FilterList(Resource):
    def get(self):
        return FILTERS, 200
