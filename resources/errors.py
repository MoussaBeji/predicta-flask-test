class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class TaskAlreadyExistsError(Exception):
    pass

class UpdatingTaskError(Exception):
    pass

class DeletingTaskError(Exception):
    pass

class TaskNotExistsError(Exception):
    pass

class UserNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "TaskAlreadyExistsError": {
         "message": "Task with given name already exists",
         "status": 400
     },
     "UpdatingTaskError": {
         "message": "Updating Task added by other is forbidden",
         "status": 403
     },
     "DeletingTaskError": {
         "message": "Deleting Task added by other is forbidden",
         "status": 403
     },
     "TaskNotExistsError": {
         "message": "Task with given id doesn't exists",
         "status": 400
     },
     "UserNotExistsError": {
         "message": "User with given id doesn't exists",
         "status": 400
     },

     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}
