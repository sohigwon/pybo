from django.shortcuts import render

from .models import Board 
from django.views import generic 
from django.urls import reverse_lazy 

def detail(request, board_id):
 board = Board.objects.get(id=board_id)
 context = {'board': board}
 return render(request, 'board/board_detail.html', context) 

class create(generic.CreateView):
 model = Board
 fields = ['subject', 'content', 'create_date']
 success_url = reverse_lazy('board:list')
 template_name_suffix = '_create'

# ////////////////////////
def index(request):
    board_list = Board.objects.order.by('-create_date')
    context = {'board_list': board_list}
    return render(request, 'board/index.html', context)

# http://localhost:8000/board/1
def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board': board}
    return render(request, 'board/board_detail.html', context)

# http://localhost:8000/board/create
class create(generic.CreateView):
    model = Board
    fields = ['subject', 'content', 'create_date']
    success_url = reverse_lazy('board:list')
    template_name_suffix = '_create'