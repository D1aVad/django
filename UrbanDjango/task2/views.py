from django.shortcuts import render

def text(request):
    return render(request, 'second_task/class_template.html')
# Create your views here.
def two(request):
    return render(request, 'second_task/func_template.html')