from django.shortcuts import render, redirect
from .forms import AuthorForm

# Create your views here.
def add_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
        else:
            return render(request, 'authors/add_author.html',
                            {
                                "form": author_form
                            }
                        )

    return render(request, 'authors/add_author.html', {
        "form": AuthorForm()
            }
        )