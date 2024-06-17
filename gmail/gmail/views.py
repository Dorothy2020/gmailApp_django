from django.http import HttpResponse

def index(request):
    return render (request,'contactform2/index.html',{})