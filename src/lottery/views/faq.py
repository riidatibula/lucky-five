from django.shortcuts import render
from django.views import View


class FAQView(View):
    template_name = 'lottery/faq.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})