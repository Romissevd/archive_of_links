from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .forms import CategoryForm
from .models import Category


class CategoryView(LoginRequiredMixin, generic.ListView, generic.CreateView):
    template_name = 'category_list.html'
    form_class = CategoryForm
    model = Category
    success_url = '.'

    def get_context_data(self, **kwargs):
        self.object = []
        self.object_list = self.get_queryset()
        kwargs['category_list'] = Category.objects.all()
        kwargs['form'] = CategoryForm
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CategoryView, self).form_valid(form)
