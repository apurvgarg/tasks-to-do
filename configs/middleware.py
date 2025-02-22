from werkzeug.wrappers import Request, Response

class Middleware:
    def __init__(self, app):
        self.app = app
        self.userName = 'apurv'
        self.password = 'Welcome@123'
    
    def __call__(self, environ, start_response):
        request = Request(environ)
        
        # Check if authorization is present
        auth = request.authorization

        if not auth or auth.username != self.userName or auth.password != self.password:
            res = Response(
                'Authorization required', 
                status=401, 
                headers={'WWW-Authenticate': 'Basic realm="Login Required"'}
            )
            return res(environ, start_response)
        
        return self.app(environ, start_response)
