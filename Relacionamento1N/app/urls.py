from django.conf.urls import url
from .views import cadastrar_marca, listar_marca, editar_marca, remover_marca, listar_produtos_marca
from .views import cadastrar_produto, listar_produto, editar_produto, remover_produto

urlpatterns = [
    url(r'^marca/cadastrar/', cadastrar_marca, name='cadastrar_marca'),
    url(r'^marca/listar/', listar_marca, name='listar_marca'),
    url(r'^marca/editar/(?P<pk>[0-9]+)', editar_marca, name='editar_marca'),
    url(r'^marca/produto/(?P<pk>[0-9]+)', listar_produtos_marca, name='marca_produto'),
    url(r'^marca/remover/(?P<pk>[0-9]+)', remover_marca, name='remover_marca'),

    url(r'^produto/cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    url(r'^produto/listar/', listar_produto, name='listar_produto'),
    url(r'^produto/editar/(?P<pk>[0-9]+)', editar_produto, name='editar_produto'),
    url(r'^produto/remover/(?P<pk>[0-9]+)', remover_produto, name='remover_produto'),

]
