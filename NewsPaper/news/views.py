from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .filters import NewsFilter
from .forms import PostForm
from django.urls import reverse_lazy


class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime
        return context


class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime
        context['filterset'] = self.filterset
        return context


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'nw_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'ar_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'nw_edit.html'


class ArticlesUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'ar_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'nw_delete.html'
    success_url = reverse_lazy('news_list')


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'ar_delete.html'
    success_url = reverse_lazy('news_list')
