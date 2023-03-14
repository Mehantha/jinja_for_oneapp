from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':"Megha",'age':22}
    return render(request,'jinja_print.html',context=d)