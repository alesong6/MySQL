#configurações do app
from kivy.config import Config

# definindo o tamanho da visualização
# Kivy Designer é o que exibe a tela de teste
# alterando a largura do layout de teste
Config.set("graphics", "width", "400")
Config.set("graphics", "height", "600")

import kivy # importa o framework
kivy.require('2.3.0') #versão do kivy a ser usada
from kivy.app import App # componentes principais
from kivy.uix.label import Label # rótulo
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder # importa as telas

#  ----------------------------------------------------------
#     Telas da aplicação
#  ----------------------------------------------------------
class Tela01( Screen ):
    pass
 
#  ----------------------------------------------------------
#     Códigos iniciais do App
#  ----------------------------------------------------------

class GerenciadorDeTelas( ScreenManager ):
    # esta classe herda do Gerenciador de telas do kivy
    pass
 
#  classe principal
class MyApp(App):
 
    # Método principal
    def build(self):
        return GerenciadorDeTelas()
 
 
# condição se estiver no kivy inicia o app
if __name__ == '__main__':
    MyApp().run()