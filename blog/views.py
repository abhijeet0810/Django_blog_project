from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# class PostListView(ListView):
#     model = Post
#     template_name = 'index.html' # <app>/<model>_<viewtype>.html
#     context_object_name = 'post_list'
#     ordering = ['-date_posted']

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'content']
    #template_name_suffix = ''

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    success_url = '/blog'
    # template_name = 'post_detail.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# def search_titles(request):
#     if request.method == 'POST':
#         search_text = request.POST['search_text']
#     else:
#         search_text = ''

#     classes = Post.objects.filter(title__contains=search_text)

#     return render_to_response('blog/ajax_search.html', {'classes': classes})

# LoginRequiredMixin is not working

# I need to mention the path of templates here like: template_name='main/home.html'
# to template_name='blog/index.html',
# and template_name='blog/post_detail.html',