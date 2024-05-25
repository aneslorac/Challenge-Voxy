from django.shortcuts import render
from .forms import CounterForm
from django.http import HttpResponse

def word_counter(request):

    if (request.method == 'POST'):
        form = CounterForm(request.POST)

        if form.is_valid():
            text_content = form.cleaned_data['text']
            word_count = len(text_content.split())

            return render(request, 'counter.html', {'form': form, 'wordcount': word_count})


    form = CounterForm()
    return render(request, 'counter.html', {'form': form, 'wordcount': 0})

def home(request):
    return render(request, 'home.html')