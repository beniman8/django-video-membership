from django.urls import path
from .views import MembershipListView


app_name = "memberships"

urlpatterns = [
    path('', MembershipListView.as_view(), name='select'),

]

