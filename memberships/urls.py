from django.urls import path
from .views import MembershipListView,PaymentView,updateTransactionRecords,profile_view,cancelSubscription


app_name = "memberships"

urlpatterns = [
    path('', MembershipListView.as_view(), name='select'),
    path('profile/', profile_view, name='profile'),
    path('cancel/', cancelSubscription, name='cancel'),
    path('payment/', PaymentView, name='payment'),
    path('update-transactions/<subscription_id>/', updateTransactionRecords, name='update-transactions'),

]

