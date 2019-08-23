from django.http import HttpResponse



# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# def index(request):
#     response=HttpResponse(
#     "Hello,world.You're at the polls index.")
#     return response
#

def bye(request):
    response = HttpResponse(
        "Bye Bye"
    )
    return response



def index(request):
    response = HttpResponse(
        """<html>
            <h1>HELLO</h1>
            <b> World</b>
            <br />
            <br />
            <br />
            <hr />
            <b> Salam </b>
        </html>""",
        status=404
    )
    return response
