from django.urls import resolve
'''
resolve é a função que Django utiliza internamente para resolver URLs
e descobrir para qual função de view eles devem ser mapeados.
'''
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        '''
        Testando se a página principal do sistema
        está utilizando o template home.html
        '''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
