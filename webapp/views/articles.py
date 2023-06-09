from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm
from webapp.models import Task
from django.contrib.auth.mixins import PermissionRequiredMixin

class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    model = Task
    form_class = TaskForm
    print('article_create.html')

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})




class ArticleDetail(DetailView):
    template_name = 'article.html'
    model = Task



class ArticleUpdateView(PermissionRequiredMixin,UpdateView):
    template_name = 'article_update.html'
    form_class = TaskForm
    model = Task
    permission_required = 'webapp.change_article'
    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk':self.object.pk})


class ArticleDeleteView(DeleteView):
    template_name = 'article_confirm_delete.html'
    model = Task
    success_url = reverse_lazy('index')