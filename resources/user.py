from flask_restful import Resource, reqparse


class UserResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field is required.')

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field is required.')

    def get(self, name):
        return {'message': 'User ({}) not found.'.format(name)}, 404

    def post(self):
        _ = UserResource.parser.parse_args()
        return {'message': 'User not found.'}, 404
