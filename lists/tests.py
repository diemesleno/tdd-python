from django.urls import resolve
'''
resolve é a função que Django utiliza internamente para resolver URLs
e descobrir para qual função de view eles devem ser mapeados.
'''
from django.test import TestCase
from django.http import HttpRequest

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
    
    def test_home_page_returns_correct_html(self):
        '''
        - Criamos um objeto HttpRequest, que é o que o Django verá quando
        o navegador de um usuário requisitar uma página.

        - Ele é passado para a nossa view home_page, que nos dará uma resposta.

        - Em seguida extraímos 'content' da resposta. Esses são os bytes brutos,
        isto é, os uns e zeros que seriam enviados para o navegador do usuário.
        Chamamos 'decode()' oara convertê-los na string HTML enviada ao usuário.

        - Queremos que ela comece com uma tag <html> que será fechada no final.

        - Além disso, queremos uma tag <title> em algum lugar no meio, contendo as
        palavras "To-Do lists", pois é isso que especificamos em nosso teste funcional.
        '''
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
