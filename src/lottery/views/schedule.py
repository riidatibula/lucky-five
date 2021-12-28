from django.shortcuts import render
from django.views import View


class ScheduleView(View):
    template_name = 'lottery/schedule.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})