from django.shortcuts import render
from .models import TodoList
from .forms import TodoForm

def todo_board(request):
    todo_list = TodoList.objects.all()
    return render(request, 'todo_board_list.html', {'todo_list':todo_list})

def check_post(request):

    if request.method == "POST" :
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_save()
            message = "일정을 추가하였습니다."
            return  render(request, 'todo_board_success.html', {'message':message})
            
    else:
        form = TodoForm
        return render(request, 'todo_board_insert.html', {'form':form})
