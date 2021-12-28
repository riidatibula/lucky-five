from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from lottery.models import Lottery
from lottery.cardano.operations import (
    generate_payment_address)


class AcceptBuyTicketNotice(View):

    def get(self, request, *args, **kwargs):
        try:
            if request.is_ajax():
                wallet_check = self.request.GET.get('walletCheck')
                terms_check = self.request.GET.get('termsCheck')

                if not (wallet_check == 'true' and terms_check == 'true'):
                    raise Exception('You must accept all terms and conditions.')

                data = {
                    'payment_address': generate_payment_address(),
                    'status_code': 200
                }

                return JsonResponse(data)

            raise Exception('Unable to process request.')

        except Exception as e:
            data = {
                'message': str(e),
                'status_code': 500
            }
            return JsonResponse(data)


class BuyTicketView(View):
    template_name = 'lottery/buy_ticket.html'

    def get(self, request, *args, **kwargs):
        current_lottery = Lottery.get_current_lottery()

        context = {
            'current_lottery': current_lottery
        }
        return render(request, self.template_name, context)