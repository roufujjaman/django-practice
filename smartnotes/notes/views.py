from django.shortcuts import render
from .models import Notes 
from django.views.generic import ListView, DetailView, CreateView
from .forms import NotesForm
# Create your views here.


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = "/smart/notes"

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {
#         "notes": all_notes
#     })

class NotesDetailView(DetailView):
    model = Notes 
    context_object_name = "note"


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note Does Not Exist")
#     return render(request, 'notes/notes_detail.html', {
#         "note": note
#     })