from django.db import models
from django.views.generic import View

class home(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('VACINOU !')