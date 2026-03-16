from django.shortcuts import render, redirect
from django.db.models import Q
from .models import ImagePost
from .forms import ImagePostForm


def home(request):
    posts = ImagePost.objects.order_by('-created_at')
    selected_category = request.GET.get('category', '').strip()
    search_query = request.GET.get('q', '').strip()

    if selected_category:
        posts = posts.filter(category=selected_category)

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__icontains=search_query)
        )

    form = ImagePostForm()

    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'gallery/home.html', {
        'posts': posts,
        'form': form,
        'selected_category': selected_category,
        'search_query': search_query,
        'category_choices': ImagePost.CATEGORY_CHOICES,
        'result_count': posts.count(),
    })
