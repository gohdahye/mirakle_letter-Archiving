from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from board.forms import BoardForm
from board.models import Board


class BoardList(ListView):
    model = Board
    ordering = '-pk'


class BoardDetail(DetailView):
    model = Board


class BoardCreate(LoginRequiredMixin, CreateView):
    model = Board
    form_class = BoardForm

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            response = super(BoardCreate, self).form_valid(form)

            return response
        else:
            return redirect('/board/')


class BoardUpdate(LoginRequiredMixin, UpdateView):
    model = Board
    form_class = BoardForm
    template_name = 'board/board_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(BoardUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class BoardDelete(DeleteView):
    model = Board
    context_object_name = 'target_board'
    success_url = reverse_lazy('boardList')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(BoardDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

