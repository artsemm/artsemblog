import urllib.parse as parse

from django.views.generic import TemplateView
from django.shortcuts import render
from blog.models import Post
from taggit.models import Tag

# Create your views here.

class PostListView(TemplateView):
    template_name = 'post_list.html'

    def get(self, request, tag_slug=None):
        if(tag_slug is None):
            posts = Post.objects.all().order_by('-created_on')
            tag_name = None
        else:
            tag_slug = parse.unquote(tag_slug)
            posts = Post.objects.filter(tags__slug__in=[tag_slug])
            tag_name = self._get_name(tag_slug)
        args = {'posts' : posts, 'tag_name' : tag_name}
        return render(request, self.template_name, args)

    def _get_name(self, slug):
        return Tag.objects.get(slug=slug).name

class PostSingleView(TemplateView):
    template_name = 'post_single.html'

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        args = {'post' : post}
        return render(request, self.template_name, args)

class PostTitlesView(TemplateView):
    template_name = 'post_titles.html'
    
    def get(self, request):
        posts = Post.objects.all().order_by('-created_on')
        args = {'posts': posts}
        return render(request, self.template_name, args)

        
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        number_of_posts = len(Post.objects.all())
        args = {'number_of_posts' : number_of_posts}
        return render(request, self.template_name, args)