from django.shortcuts import (
    render, get_object_or_404)
from django.views import View
from django.views.generic import ListView

from lottery.models import Bet, Lottery


class BetsListView(ListView):
    paginate_by = 10
    ordering = 'pk'
    queryset = Bet.objects.all()
    template_name = 'lottery/bet_list.html'

    def get_queryset(self, lottery):
        queryset = self.queryset
        queryset = lottery.active_bets

        ordering = self.ordering
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset

    def get(self, request, *args, **kwargs):
        context = {}

        try:
            lottery_seq = self.request.GET.get(
                'lottery')
            lottery = Lottery.get_current_lottery()

            if lottery_seq:
                if lottery_seq.isdigit():
                    lottery = get_object_or_404(
                        Lottery, seq=int(lottery_seq))
                else:
                    raise Exception('Opps. Lottery not found.')

            if lottery is None:
                raise Exception('No active lottery today.')

            self.object_list = self.get_queryset(lottery)
            allow_empty = self.get_allow_empty()

            if not allow_empty:
                # When pagination is enabled and object_list is a queryset,
                # it's better to do a cheap query than to load the unpaginated
                # queryset in memory.
                if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                    is_empty = not self.object_list.exists()
                else:
                    is_empty = not self.object_list
                if is_empty:
                    raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                        'class_name': self.__class__.__name__,
                    })
            context = self.get_context_data()
            context['lottery'] = lottery

            return self.render_to_response(context)

        except Exception as e:
            context = {'error': e}

        return render(request, self.template_name, context)