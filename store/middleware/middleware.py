from django.shortcuts import redirect


def auth_middleware(gt_response):


    def middleware(request):
        print("middleware")
        returnUrl=request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customerid'):
            return redirect(f'http://localhost:8000/login?returnUrl={returnUrl}')
        return gt_response(request)
    return middleware