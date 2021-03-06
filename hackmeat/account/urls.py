from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('hackmeat.account.views',
    url(r'processors/(?P<zipcode>\d+)/?$', r'processors'),
    url(r'signup/farmer/?$', r'signup_farmer'),
    url(r'signup/processor/?$', r'signup_processor'),
    url(r'settings/farmer/?$', r'settings_farmer'),
    url(r'settings/processor?$', r'settings_processor'),
    url(r'processor/(?P<processor>\d+)/?$', r'processor'),
    url(r'farmer/dashboard/$', direct_to_template, {'template': 'account/farmer_dashboard.html'}, name='farmer_dash'),
    url(r'processor/dashboard/$', direct_to_template, {'template': 'account/processor_dashboard.html'}),
    url(r'user/signup/$', 'user_signup', name='user_signup'),
    url(r'farmer/signup/$', 'signup_farmer', name='farmer_signup'),
    url(r'processor/signup/$', 'signup_processor', name='processor_signup'),
    url(r'user/edit/$', 'user_edit', name='user_edit'),

)
