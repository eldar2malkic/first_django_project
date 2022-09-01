from django.shortcuts import HttpResponse, redirect, render # add redirect to import statement
from django.http import JsonResponse

def root_method(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

def hello_name(request, name):
    context = {
        "indexname":name,
    }
    return render(request, "indexname.html", context)

def some_function(request):
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]

def success(request):
    return render(request, "success.html")



# def root_method(request):
#     return HttpResponse("String response from root_method")
# def another_method(request):
#     return redirect("/redirected_route")
# def redirected_method(request):
#     return JsonResponse({"response": "JSON response from redirected_method", "status": True})

