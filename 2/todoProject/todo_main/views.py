from django.shortcuts import render
from todo_board.models import TodoList
# Create your views here.
from django.views import generic

# class Todo_main(generic.TemplateView):
#     def get(self, request, *args, **kargs):
#         template_name = 'index.html'
#         return render(request, template_name)

def Todo_main(request):
    # todo_list = TodoList.objects.all()
    return render(request, 'index.html')