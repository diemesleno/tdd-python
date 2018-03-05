from selenium import webdriver
'''
Com a classe Keys podemos enviar teclas especiais,
como Enter.
'''
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        '''
        Método executado antes de cada teste.
        Geralmente utilizado para instanciar 
        algum objeto.
        '''
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        '''
        Método executado após cada teste.
        Utilizado aqui para fechar o navegador
        do selenium.
        '''
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        '''
        Edith ouviu falar de uma nova aplicação online interessante
        para lista de tarefas. Ela decide verificar sua homepage.
        '''
        self.browser.get('http://localhost:8000')
        
        '''
        Ela percebe que i título da página e o cabeçalho
        mencionam listas de tarefas (to-do)
        '''
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        '''
        Ela é convidada a inserir um item de tarefa imediatamente

        - O método find_element_ devolve 1 elemento e lança
        uma exceção caso não o encontre.
        '''
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        '''
        Ela digita "Buy peacock feathers" (Comprar penas de pavão) em uma caixa
        de texto (o hoby de Edith é fazer iscas para pesca com fly)

        - Com send_keys utilizamos o selenium para digitar em
        elementos de entrada.
        '''
        inputbox.send_keys('Buy peacock feathers')
        
        '''
        Quando ela tecla enter, a página é atualizada, e agora a página lista
        # "1: Buy peacock feathers" como um item em uma lista de tarefas.

        - Após inserir dados no campo input acima, usanos o selenium
        para pressionar Enter e aguardamos 1 segundo.

        - O método find_elements_ devolve uma lista de elementos,
        caso encontre ou uma lista vazia.

        - A função built-in do Python any, verifica se em
        qualquer um dos elementos se encontra o que foi 
        especificado.
        '''
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.test == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        
        '''
        Ainda continua havendo uma caixa de texto convidando-a a acrescentar 
        outro item. Ela insere "Use peacock feathers to make a fly" (Usar
        penas de pavão para fazer um fly - Edith é bem metódica)
        '''
        self.fail('Finish the test!')
        
        '''
        A página é atualizada novamente e agora mostra os dois itens
        em dua lista.
        '''
        
        '''
        Edith se pergunta se o site lembrará de sua lista. Então ela nota
        que o site gerou um URL únoco para ela -- há um pequeno texto
        explicativo para isso.
        '''
        
        '''
        Ela acessa esse URL - sua lista de tarefas continua lá.
        '''
        
        '''
        Satisfeita, ela volta a dormir.
        '''

if __name__ == '__main__':
    unittest.main()
