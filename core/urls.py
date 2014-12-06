from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
	urlpatterns = patterns('core.views',
	    url(r'^$', 'home'),
	    url(r'^login$', 'login'),
	    url(r'^logout$', 'logout'),
        url(r'^register$', 'register'),
	    url(r'^dashboard$', 'dashboard'),
	    url(r'^rewards$', 'rewards'),
	    url(r'^avatar$', 'avatar'),
        url(r'^profile/(?P<username>[^/]+)$', 'profile'),
        url(r'^addfriend/(?P<username>[^/]+)$', 'addfriend'),
        url(r'^unfriend/(?P<username>[^/]+)$', 'unfriend'),
        url(r'^group/(?P<group>[^/]+)$', 'group'),
	    url(r'^edit_group/(?P<group>[^/]+)$', 'edit_group'),
	    url(r'^delete_group/(?P<group>[^/]+)$', 'delete_group'),
	    url(r'^new_group_logo/(?P<group>[^/]+)$', 'new_group_logo'),
	    url(r'^add_membership/(?P<group>[^/]+)$', 'add_membership'),
	    url(r'^deny_membership/(?P<membership>[^/]+)$', 'deny_membership'),    
	    url(r'^approve_membership/(?P<membership>[^/]+)$', 'approve_membership'),
        url(r'^add_group$', 'add_group'),
        url(r'^post_update/(?P<goal>[^/]+)$', 'post_update'),
        url(r'^add_actionitem/(?P<goalgroup>[^/]+)$', 'add_actionitem'),
        url(r'^add_goal$', 'add_goal'),
        url(r'^add_reward$', 'add_reward'),
        url(r'^buy_reward/(?P<reward>[^/]+)$', 'buy_reward'),
        url(r'^retire_reward/(?P<reward>[^/]+)$', 'retire_reward'),
        url(r'^delete_goal/(?P<goal>[^/]+)$', 'delete_goal'),
        url(r'^delete_goal/(?P<goal>[^/]+)/(?P<neworder_num>[^/]+)$', 'flip_goals'),
        url(r'^add_friendpoint/(?P<goal>[^/]+)$', 'add_friendpoint'),
        url(r'^add_comment/(?P<update>[^/]+)$', 'add_comment'),
        url(r'^delete_goalgroup/(?P<goalgroup>[^/]+)$', 'delete_goalgroup'),
	)
