# Importando o Tkinnter
from tkinter import *
from tkinter import ttk

#cores
cor1 = "#474f49" # cor cinza escuro
cor2 = "#feffff" # cor gelo
cor3 = "#38576b" # cor azul gradiente
cor4 = "#ECEFF1" # cor azul claro
cor5 = "#FFAB40" # cor laranja
cor6 = "#ebf5f5" # cor branca


janela =Tk()
janela.title("Calculadora")
janela.geometry("450x490")
janela.config(bg=cor1)

# criando frames
frame_tela = Frame(janela, width=640, height=80, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=640, height=400)
frame_corpo.grid(row=1, column=0)

# Criando a função da calculadora

def entrar_valores():
  resultado =eval('9*9')

  # Passando o valor para à tela
  valor_texto.set(resultado)



# criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=19, height=2, padx=7, bg=cor3,fg=cor6 ,relief=FLAT, anchor="e", justify="left", font=('Tvy 25 bold'))
app_label.place(x=0,y=0)

# criando botoes

b_1 = Button(frame_corpo, command=valor_texto, text="C", justify="center", width=30, height=3, bg=cor4, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", justify="center", width=9, height=3, bg=cor5, fg=cor6, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=220, y=0)
b_3 = Button(frame_corpo, text="/", justify="center", width=9, height=3, bg=cor5, fg=cor6, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=335, y=0)


b_4 = Button(frame_corpo, text="7", width=9, height=3, bg=cor2, fg=cor1, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=80)
b_5 = Button(frame_corpo, text="8", width=9, height=3, bg=cor2, fg=cor1, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=110, y=80)
b_6 = Button(frame_corpo, text="9", width=9, height=3, bg=cor2, fg=cor1, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=220, y=80)
b_7 = Button(frame_corpo, text="*", width=9, height=3, bg=cor5, fg=cor6, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=335, y=80)

b_8 = Button(frame_corpo, text="4", width=9, height=3, bg=cor2, fg=cor1, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=160)
b_9 = Button(frame_corpo, text="5", width=9, height=3, bg=cor2, fg=cor1, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=110, y=160)
b_10 = Button(frame_corpo, text="6", width=9, height=3, bg=cor2, fg=cor1, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=220, y=160)
b_11 = Button(frame_corpo, text="-", width=9, height=3, bg=cor5, fg=cor6, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=335, y=162)

b_12 = Button(frame_corpo, text="1", width=9, height=3, bg=cor2, fg=cor1, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=240)
b_13 = Button(frame_corpo, text="2", width=9, height=3, bg=cor2, fg=cor1, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=110, y=240)
b_14 = Button(frame_corpo, text="3", width=9, height=3, bg=cor2, fg=cor1, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=220, y=240)
b_15 = Button(frame_corpo, text="+", width=9, height=3, bg=cor5, fg=cor6, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=335, y=242)

b_16 = Button(frame_corpo, text="0", width=30, height=3, bg=cor2, fg=cor1, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=320)
b_17 = Button(frame_corpo, text=".", width=9, height=3, bg=cor5, fg=cor6, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=220, y=320)
b_18 = Button(frame_corpo, text="=", width=9, height=3, bg=cor5, fg=cor6, font=('Tvy 15 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=335, y=320)

# https://www.youtube.com/watch?v=i24MxljM-Bw&t=334s


janela.mainloop()