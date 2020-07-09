from django.shortcuts import render
from .forms import TextForm
from django.http import HttpResponseRedirect
from .functions import handle_question
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def ask_question(request):

    if request.method == 'POST':
        form = TextForm(data = request.POST)
        print(form.errors)
        if form.is_valid():
            text = request.POST['text']
            results = handle_question(text)
            return render(request, 'app/index.html', {'form': form, 'results': results})
    else:
        form = TextForm()
    return render(request, 'app/index.html', {'form': form})
