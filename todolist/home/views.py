from django.shortcuts import render
from home.models import Task

# Create your views here.
def home(request):
    context={'success':False}
    if request.method=="POST":

        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)

        ins=Task(taskTitle=title,taskDesc=desc)

        ins.save()

        context={'success':True}

    return render(request,'index.html',context)
    # return HttpResponse("works")

def task(request):
    alltask=Task.objects.all()
    context={'tasks':alltask}
    return render(request,'task.html',context)