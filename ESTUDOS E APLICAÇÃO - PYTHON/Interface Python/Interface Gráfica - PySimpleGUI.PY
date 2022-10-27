import PySimpleGUI as psg

class TelaEstudosNewave:
    """
    Primeiro código testando uma biblioteca de interface gráfica
    Para ter uma tela você necessita de um layout, uma janela e a
    extração dos dados.
    
    Versão PySimpleGUI == 0.4.0
    """
    
    def __init__(self):
        #Layout
        layout = [
            [psg.Text('Arquivo NEWAVE', size=(11,0)), psg.Input(size=(30,0), key=('Path'))],
            [psg.Text('Dê um nome para caso (apenas Strings)')],
            [psg.Text('Nome do Caso', size=(11,1)), psg.Input(size=(15,1), key=('nome_do_caso'))],
            [psg.Text('Cálculo da Garantia Física?')],
            [psg.Checkbox('Sim'), psg.Checkbox('Não')],
            [psg.Button('Enviar Dados')]
            ]
        #Janela
        #Obrigatório aspas dupla
        janela = psg.Window("Leitor NEWAVE").layout(layout)
        #values recebe todas as informações de loyaout e janela
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        """Extrai os dados na tela"""
        path = self.values['Path']
        nome_do_caso = self.values['nome_do_caso']
        
        print(f'Arquivo NEWAVE: {path}')
        print(f'Nome do Caso: {nome_do_caso}')


tela = TelaEstudosNewave()
tela.Iniciar()
#%%Código Auxiliar        

"""
CODE EXAMPLE:
Code UI de entrada

psg.theme("LightPurple")
#define layout
layout=[[psg.Text("Name",size=(15, 1), font='Lucida',justification='right'),psg.Input()],
        [psg.Text("Date of Birth",size=(15, 1), font=("Verdana",11),text_color='Black',background_color='Yellow', justification='right'),psg.Input()],
        [psg.Text("Class",size=(15, 1), font=("Verdana",11),text_color='Red',justification='right'),psg.Input('M.Sc', background_color='Yellow')],
        [psg.Text("Address",size=(15, 1), font=("Arial",11),text_color='Green',justification='right'),psg.Multiline()],
        [psg.Button("SAVE", font=("Times New Roman",12)),psg.Button("CANCEL", font=("Times New Roman",12))]]
#Define Window
win =psg.Window("Data Entry",layout)
#Read  values entered by user
e,v=win.read()
#close first window
win.close()
---------------------------------------------------------------------------------
Code UI de sáida

#define layout for second windows to display data entered by user in first window
layout1=[[psg.Text("The data you entered is  :", size=(20,1), font='Lucida', text_color='Magenta')],
        [psg.Text("Name :"+v[0], size=(20,1), font='Lucida', text_color='Blue')],
        [psg.Text("DOB :"+v[1], size=(20,1), font='Lucida', text_color='Lime')],
        [psg.Text("Class  :"+v[2], size=(len(v[2])+10,1), font='Lucida', text_color='Yellow')],
        [psg.Text("Address  :"+v[3], size=(int(len(v[3])/4),4), font='Lucida', text_color='Brown', justification='center')]]
#Define Window and display the layout to print output        
win1=psg.Window("Output Screen",layout1)

e,v=win1.read()
#close second window
win1.close()

"""