from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    context = {
         "full_name": "Waed Khalid Ahmed",
        "last_name": "Abu Swise",
        "student_id": "2202555813",
        "address": "Gaza",
        "email": "waed321@gmail.com",
        "extra_info":"I graduated from UCAS with a major in Web Design and Development, and I continued my studies here."
    }
    return render(request, "pages/index.html", context)
