from django.shortcuts import render
from django.views.generic.base import TemplateView

class home(TemplateView):

    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        #context['latest_articles'] = Article.objects.all()[:5]
        return context