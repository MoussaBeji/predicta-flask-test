from .task import TasksApi, TaskApi
from .auth import SignupApi, LoginApi, UserApi, UsersApi

def initialize_routes(api):
    api.add_resource(TasksApi, '/api/tasks')
    api.add_resource(TaskApi, '/api/tasks/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(UsersApi, '/api/auth')
    api.add_resource(UserApi, '/api/auth/<id>')
