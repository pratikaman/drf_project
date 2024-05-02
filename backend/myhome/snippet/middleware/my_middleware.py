


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("before response")
        print(request.user)
        response = get_response(request)
        print("After response")
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

    
