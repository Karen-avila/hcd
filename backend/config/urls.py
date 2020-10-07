from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from rest_framework.authtoken.views import obtain_auth_token

from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from graphql_playground.views import GraphQLPlaygroundView


urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # GRAPHQL url
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('playground/', GraphQLPlaygroundView.as_view(endpoint="http://localhost:8081/graphql/")),
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += [
        path("400/",default_views.bad_request,kwargs={"exception": Exception("Bad Request!")},),
        path("403/",default_views.permission_denied,kwargs={"exception": Exception("Permission Denied")},),
        path("404/",default_views.page_not_found,kwargs={"exception": Exception("Page not Found")},),
        path("500/", default_views.server_error),
    ]

