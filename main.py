from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from math import sqrt


class MyBoxLayout(BoxLayout):
	def font_size(self, *args):
		return '60sp'
		
	def vrfy_screen(self, btn_text, screen_text): # inpt é um botão
		if 'syntax error' in screen_text:
			return btn_text
		else:
			return screen_text + btn_text	
	
	def calculate(self, expression):			
		if '%' in expression and (expression.count('%') == 1):
			result = expression.split('%')
			result = str((float(result[0]) / 100) * float(result[1]))
			return result			
		else:
			try:
				if '^' in expression:
					expression = expression.replace('^', '**')
				result = str(eval(expression))
				return result
			except:
				return 'syntax error'				




class Calculadora(App):
	def build(self):
		return MyBoxLayout()
	
Calculadora().run()
