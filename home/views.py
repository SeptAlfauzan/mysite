from django.shortcuts import render
from home.models import Question
# Create your views here.
def home_view(request):
    data = {}
    data['myname'] = "Septa Alfauzan"

    listnum = []
    listnum.append("first data")
    listnum.append("second data")
    listnum.append("third data")
    listnum.append("fourth data")

    data['listnum'] = listnum

    q = Question.objects.all()
    data["question"] = q
    
    return render(request, "home/home_content.html", data)

def aboutus_view(request):
    return render(request, "aboutus/aboutus_content.html")