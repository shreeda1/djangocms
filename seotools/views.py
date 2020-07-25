from django.views.generic import DetailView, TemplateView

from seo.mixins.views import (
    ViewSeoMixin,
    ModelInstanceViewSeoMixin,
    UrlSeoMixin
)

from apps.article.models import Article


class IndexView(ViewSeoMixin, TemplateView):
    seo_view = 'index'
    template_name = 'index.html'


class IndexViewJinja(ViewSeoMixin, TemplateView):
    seo_view = 'index'
    template_name = 'jinja/index.jinja'


class ArticleDetailView(ModelInstanceViewSeoMixin, DetailView):
    template_name = 'article.html'
    model = Article
    pk_url_kwarg = 'id'


class ArticleDetailViewJinja(ModelInstanceViewSeoMixin, DetailView):
    template_name = 'jinja/article.jinja'
    model = Article
    pk_url_kwarg = 'id'


class IndexUrlSeoView(UrlSeoMixin, TemplateView):
    template_name = 'index.html'


class ArticleUrlSeoDetailView(UrlSeoMixin, DetailView):
    template_name = 'article.html'
    model = Article
    pk_url_kwarg = 'id'