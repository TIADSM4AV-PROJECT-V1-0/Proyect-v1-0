
# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    
   return render (request,'example/index.html',{"current_time":now})

   def dishes (request):
    list_dishes =list ()
    list_dishes.append({"title":, "enchiladas","descripcion":"de chile rojo"})
    
    return JsonResponse(list_dishes, safe=False)