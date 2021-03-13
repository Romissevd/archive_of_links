from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .forms import LinkForm
from .models import Link


class LinkView(LoginRequiredMixin, generic.ListView, generic.CreateView):
    template_name = 'link_list.html'
    form_class = LinkForm
    model = Link
    success_url = '.'

    def get_context_data(self, **kwargs):
        self.object = []
        self.object_list = self.get_queryset()
        kwargs['link_list'] = Link.objects.all()
        kwargs['form'] = LinkForm
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(LinkView, self).form_valid(form)
