from django.shortcuts import render
from django.http import HttpResponse

# Returning a Http response
# def index(request):
#     return HttpResponse("index Http Response from first_app/views")



# Returning and rendering a template as a response
def index(request):
    my_dict ={'insert_this':"This is from views.py!"}
    return render(request, 'first_app/index.html', context=my_dict)