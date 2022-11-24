from django.shortcuts import render
from django.views.generic import ListView
from .models import Membership,UserMembership,Subscription


def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first().membership
    return None

def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(
        user_membership=get_user_membership(request)
    )

    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription

    return None

class MembershipListView(ListView):
    model = Membership



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_membership"] = str(get_user_membership(self.request))
        return context


    def post(self,request,**kwargs):
        selected_membership = request.POST.get('membership_type')

        return selected_membership
    
    

