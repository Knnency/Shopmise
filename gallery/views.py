from django.shortcuts import render, redirect
from .models import ImagePost
from .forms import ImagePostForm


def home(request):
    posts = ImagePost.objects.order_by('-created_at')
    form = ImagePostForm()

    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'gallery/home.html', {
        'posts': posts,
        'form': form
    })
