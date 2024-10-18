from django.shortcuts import render
from .models import Notes 
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NotesForm
from django.http.response import HttpResponseRedirect
# Create your views here.


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = "/smart/notes"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url()) 

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes"

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = "/smart/notes"

class NotesDetailView(DetailView):
    model = Notes 
    context_object_name = "note"
