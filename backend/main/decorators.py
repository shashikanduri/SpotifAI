from functools import wraps
from flask import request, jsonify

# USE CUSTOM DECORATORS TO HANDLE MANDATORY CONDITIONS TO ACCESS APIs

# missing request parameters
def require_params(*params):
    def require_params_decorator(func):
        @wraps(func)
        def original_function(*args, **kwargs):
            for param in params:
                if param not in request.json:
                    return jsonify({
                                        'message': f'Missing required parameter: {param}',
                                        'error':'Bad Request',
                                        'status': 0
                                    }
                                ), 400
            return func(*args, **kwargs)
        return original_function
    return require_params_decorator
