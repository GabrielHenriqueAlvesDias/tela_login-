import PySimpleGUI as sg
import sqlite3

def loigin():
     sg.theme('DarkBlue16')
     layout= [
     [sg.Text()],
     [sg.Text('Login:  '), sg.Input(key='usurio',size=(10,0))],
     [sg.Text('Senha: '), sg.Input(key='senha', password_char='*',size=(10,0))],
     [sg.Button('ENTRAR'), sg.Button('CADASTRA')],
     ]
     return sg.Window('Login', layout=layout, finalize=True)

def cadastro():
	sg.theme('DarkBlue15')
	layout = [
	[sg.Text('Login: '), sg.Input(key='usurio',size=(10,0))],
	[sg.Text('Senha:'), sg.Input(key='senha', password_char='*',size=(10,0))],
	[sg.Text('Senha'), sg.Input(key='csenha', password_char='*',size=(10,0))],
	[sg.Button('ok'), sg.Text(), sg.Button('voltar')]
	]
	
	return sg.Window('Cadastra', layout=layout, finalize=True)
Lon, cads=loigin(), None

while True:
   
   windon, evento, valores = sg.read_all_windows()
   usurio = valores['usurio']
   senha=valores['senha']
   if windon == Lon and evento == sg.WIN_CLOSED:
   	break
   if windon==Lon and evento=='ENTRAR':
    	 if usurio== valores['usurio'] and senha == valores['senha']:
    	   try:
    	   		usurio = valores['usurio']
    	   		senha=valores['senha']
    	   		banco =sqlite3.connect('banco_cadastro.db')
    	   		cursor = banco.cursor()
    	   		cursor.execute("SELECT senha FROM cadastro WHERE usurio='{}'".format(usurio))
    	   		senha_db=cursor.fetchall()
    	   		print(senha_db)
    	   		banco.close()
    	   		sg.popup('Obrigado')
    	   except:
     	     sg.popup('Login não foi achado ')
      
   if windon== Lon and evento =='CADASTRA':
   	cads = cadastro()
   	Lon.hide()
   if windon==cads and evento=='voltar':
   	cads.hide()
   	Lon.un_hide()
   if windon == cads and evento=='ok':
   
   	   if windon==cads and valores['senha']== valores['csenha']:
   	     try:
   	       
   	     	banco = sqlite3.connect('banco_cadastro.db')
   	     	cursor = banco.cursor()
   	     	cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (usurio text,senha text)")
   	     	cursor.execute("INSERT INTO cadastro VALUES ('"+usurio+"','"+senha+"' )")
   	     	banco.commit()
   	     	banco.close()
   	     	cads.hide()
   	     	Lon.un_hide()
   	       # TODO: write code...
   	     except sqlite3.Error as erro:
   	       sg.popup('Erro ao inserir dados',erro)
   	       
   	   else:
   	       sg.popup('senha não são mesmas')
   	       # TODO: write code...