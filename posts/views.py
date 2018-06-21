from django.views.generic import ListView

from . models import Post


class PostListView(ListView):
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()
