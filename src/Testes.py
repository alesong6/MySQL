import kivy
kivy.require('2.3.0')  # Versão desejada

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

# Definir o tamanho da tela
Window.size = (338, 600)

# Registrando a nova fonte
LabelBase.register(name="MinhaFonte", fn_regular="Roboto-Light.ttf")

# Carregar a interface do arquivo .kv
Builder.load_file("telas.kv")

tempoSplash = 2

# --------------------------------------------------------------------------------------------
#      Acesso ao Banco de Dados mySQL
# --------------------------------------------------------------------------------------------

def ir_para_login(self, instance):
    self.manager.current = 'login'

def ir_para_cadastro(self, instance):
    self.manager.current = 'cadastro'

# --------------------------------------------------------------------------------------------
#      Telas do App
# --------------------------------------------------------------------------------------------

class SplashScreen(Screen):
    def on_enter(self):
        # Agendar a navegação para a tela de login após X segundos
        Clock.schedule_once(self.go_to_login, tempoSplash)

    def go_to_login(self, dt):
        # Transição para a tela de login
        self.manager.current = 'login'

# tela de login
class LoginScreen(Screen):
    pass
# tela de cadastro
class CadastroScreen(Screen):
    pass

# --------------------------------------------------------------------------------------------
#       Classe principal do App
# --------------------------------------------------------------------------------------------

class Testes(App):
    def build(self):
        # Definir a cor de fundo da janela
        Window.clearcolor = get_color_from_hex('#ffffff')

        # Criar o ScreenManager e adicionar as telas
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(CadastroScreen(name="cadastro"))

        return sm

if __name__ == '__main__':
    Testes().run()
