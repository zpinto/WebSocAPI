from flask import Flask, jsonify
from flask_restful import Api

from resources.filter import FilterList
from resources.breadth import Breadth, BreadthList
from resources.dept import Dept, DeptList
from resources.yearterm import YearTermList
from resources.division import DivisionList
from resources.course import Course

app = Flask(__name__)
api = Api(app)

api.add_resource(FilterList, '/filters')
api.add_resource(Breadth, '/Breadth/<string:breadth_name>')
api.add_resource(BreadthList, '/Breadths')
api.add_resource(Dept, '/Dept/<string:department_name>')
api.add_resource(DeptList, '/Depts')
api.add_resource(YearTermList, '/YearTerms')
api.add_resource(DivisionList, '/Divisions')
api.add_resource(Course, '/class')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
