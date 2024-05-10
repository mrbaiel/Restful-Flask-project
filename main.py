from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

datas = {
    1: {"audi": "q7", "eng_capacity": 4.7},
    2: {"audi": "rs7", "eng_capacity": 3},
    3: {"audi": "a8", "eng_capacity": 2}
}


def checking_num(car_number):
    if car_number in datas:
        return True
    return False


def not_in_date(car_num) -> str:
    return f"{car_num} is not in dict"


parser = reqparse.RequestParser()
parser.add_argument("audi", type=str)
parser.add_argument("engine_capacity", type=float)


class Index(Resource):
    def get(self, car_num):
        if checking_num(car_num):
            return datas[car_num]
        elif car_num == 0:
            return datas
        return not_in_date(car_num)

    def delete(self, car_num):
        if checking_num(car_num):
            del datas[car_num]
            return datas
        return not_in_date(car_num)

    def post(self, new_car_num):
        datas[new_car_num] = parser.parse_args()
        return datas

    def put(self, id_car):
        datas[id_car] = parser.parse_args()
        return datas


api.add_resource(Index, '/api/index/<int:car_num>')
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5001, host='127.0.0.1')
