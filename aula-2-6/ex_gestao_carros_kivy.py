from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config

class AppCarros ( App ):
    lista = []

    carro_atual = None
    
    txt_marca = TextInput(size_hint=(0.7,1.0))
    txt_modelo = TextInput(size_hint=(0.7,1.0))
    txt_ano = TextInput(size_hint=(0.7,1.0))
    txt_placa = TextInput(size_hint=(0.7,1.0))
    

    def submit(self, e):
        print("Botão Pressionado")
        obj_carro = {
            "marca": self.txt_marca.text,
            "modelo": self.txt_modelo.text,
            "ano": self.txt_ano.text,
            "placa": self.txt_placa.text,
        }
        self.lista.append(obj_carro)
        self.txt_ano.text = ""
        self.txt_marca.text = ""
        self.txt_modelo.text = ""
        self.txt_placa.text = ""
        print(self.lista)


    def excluir(self, e):
        if self.carro_atual is not None:
            carro_passado = self.txt_placa.text
            self.lista.remove(self.carro_atual)
            self.carro_atual = None
            self.txt_ano.text = ""
            self.txt_marca.text = ""
            self.txt_modelo.text = ""
            self.txt_placa.text = ""
            print(f"Carro com placa {carro_passado} excluido com sucesso!")
            print(self.lista)

    def pesquisar(self, e):
        placa_digitada = self.txt_placa.text.lower()
        for carro in self.lista:
            if placa_digitada == carro["placa"].lower():
                self.carro_atual = carro
                self.txt_ano.text = carro["ano"]
                self.txt_marca.text = carro["marca"]
                self.txt_modelo.text = carro["modelo"]
                self.txt_placa.text = carro["placa"]
                break
        print(self.lista)

    def build(self):
        box = BoxLayout(orientation="vertical")
        box_placa = BoxLayout(orientation="horizontal",size_hint = (1.0,0.2))
        box_modelo = BoxLayout(orientation="horizontal",size_hint = (1.0,0.2))
        box_marca = BoxLayout(orientation="horizontal",size_hint = (1.0,0.2))
        box_ano = BoxLayout(orientation="horizontal",size_hint = (1.0,0.2))
        box_botoes = BoxLayout(orientation="horizontal", size_hint=(1.0,0.2))

        lbl_placa = Label(text="Placa", size_hint=(0.3,1.0))
        lbl_modelo = Label(text="Modelo", size_hint=(0.3,1.0))
        lbl_marca = Label(text="Marca", size_hint=(0.3,1.0))
        lbl_ano = Label(text="Ano", size_hint=(0.3,1.0))

        btn_gravar = Button(text="Gravar", size_hint=(1,1), on_release = self.submit)
        btn_excluir = Button(text="Excluir", size_hint=(1,0.5), on_release = self.excluir)
        btn_pesquisar = Button(text="Pesquisar", size_hint=(1,1), on_release = self.pesquisar)

        box_placa.add_widget(lbl_placa)
        box_placa.add_widget(self.txt_placa)

        box_modelo.add_widget(lbl_modelo)
        box_modelo.add_widget(self.txt_modelo)

        box_marca.add_widget(lbl_marca)
        box_marca.add_widget(self.txt_marca)

        box_ano.add_widget(lbl_ano)
        box_ano.add_widget(self.txt_ano)

        box_botoes.add_widget(btn_gravar)
        box_botoes.add_widget(btn_excluir)
        box_botoes.add_widget(btn_pesquisar)

        box.add_widget(box_placa)
        box.add_widget(box_modelo)
        box.add_widget(box_marca)
        box.add_widget(box_ano)
        box.add_widget(box_botoes)
        return box
    
if __name__ == "__main__":
    app = AppCarros()
    app.run()

        
