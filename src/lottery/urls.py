from django.urls import path

from lottery.views.home import HomeView
from lottery.views.tickets import (
    AcceptBuyTicketNotice, BuyTicketView)
from lottery.views.bets import BetsListView
from lottery.views.lotteries import (
    LotteryListView, LotteryDetailView)
from lottery.views.about import AboutView
from lottery.views.schedule import ScheduleView
from lottery.views.faq import FAQView

app_name = 'lottery'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('buy-ticket/', BuyTicketView.as_view(), name='buy-ticket'),
    path('accept-buy-ticket-notice/', AcceptBuyTicketNotice.as_view(), name='accept-notice'),
    path('bets/', BetsListView.as_view(), name='bet-list'),
    path('lotteries/', LotteryListView.as_view(), name='lottery-list'),
    path('lotteries/<int:pk>/', LotteryDetailView.as_view(), name='lottery-detail'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('about/', AboutView.as_view(), name='about')
]