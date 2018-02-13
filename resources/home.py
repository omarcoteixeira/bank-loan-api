from flask_restful import Resource, reqparse


class HomeResource(Resource):

    def get(self):
        return {'message': 'Bank Loan API'}, 200
