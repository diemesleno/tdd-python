from django.urls import resolve
'''
resolve é a função que Django utiliza internamente para resolver URLs
e descobrir para qual função de view eles devem ser mapeados.
'''
from django.test import TestCase

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        '''
        Estamos verificando se resolve, quando é chamado
        com '/', que é a raiz do site, encontra uma função
        chamada home_page.
        '''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
