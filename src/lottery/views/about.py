from django.shortcuts import render
from django.views import View


class AboutView(View):
    template_name = 'lottery/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})