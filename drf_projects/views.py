from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """
    This is the root of the API. It provides a list of links to the
    main resources available.
    """

    data = {
        'API Documentation' : {
            'Swagger UI': reverse('swagger-ui', request=request, format=format),
            'ReDoc': reverse('redoc', request=request, format=format),
        },

        'Authentication': {
            'Register': reverse('rest_register', request=request, format=format),
            'Login': reverse('rest_login', request=request, format=format),
            'Logout': reverse('rest_logout', request=request, format=format),
            'Resend Email Verification': reverse('rest_resend_email_verification', request=request, format=format),
            'Change Password': reverse('rest_password_change', request=request, format=format),
            'Reset Password': reverse('rest_password_reset', request=request, format=format),
            'Reset Password Confirmation': reverse('rest_password_reset_confirm', request=request, format=format),
            'Current Logged In User Details': reverse('rest_user_details', request=request, format=format),
        },

        'Application Endpoints': {
            'Books (FBV)': reverse('book-list', request=request, format=format),
            'Todos (CBV)': reverse('todo-list', request=request, format=format),

            # For viewsets, the default name is {basename}-list
            'Posts (Viewset)': reverse('posts-list', request=request, format=format),
            'Users (Viewset)': reverse('users-list', request=request, format=format),
        },
    }

    return Response(data)