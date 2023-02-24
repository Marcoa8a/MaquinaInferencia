import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.geometry("800x600")
ventana.title("Máquina de inferencia")
ventana.resizable(0,0)

tamanio = tkFont.Font(family = "Lucida Grande", size = 20)

etiqueta = tk.Label(ventana, text = "Escoge una fruta y trataré de adivinarla!!", font = tamanio)
etiqueta.pack()

aguacate = Image.open("./Frutas/aguacate.jpg")
aguacate = aguacate.resize((100,100), Image.Resampling.LANCZOS)
aguacateImg = ImageTk.PhotoImage(aguacate)
aguacate_etiqueta = tk.Label(ventana, image = aguacateImg).place(x=50, y=50)
aguacate_txt = tk.Label(ventana, text="Aguacate").place(x=50, y=50)

arandano = Image.open("./Frutas/arandano.jpg")
arandano = arandano.resize((100,100), Image.Resampling.LANCZOS)
arandanoImg = ImageTk.PhotoImage(arandano)
arandano_etiqueta = tk.Label(ventana, image = arandanoImg).place(x=50, y=150)
arandano_txt= tk.Label(ventana, text="Arandano").place(x=50, y=150)

cereza = Image.open("./Frutas/cereza.jpg")
cereza = cereza.resize((100,100), Image.Resampling.LANCZOS)
cerezaImg = ImageTk.PhotoImage(cereza)
cereza_etiqueta = tk.Label(ventana, image = cerezaImg).place(x=50, y=250)
cereza_text = tk.Label(ventana, text="Cereza").place(x=50, y=250)

frambuesa = Image.open("./Frutas/frambuesa.jpg")
frambuesa = frambuesa.resize((100,100), Image.Resampling.LANCZOS)
frambuesaImg = ImageTk.PhotoImage(frambuesa)
frambuesa_etiqueta = tk.Label(ventana, image = frambuesaImg).place(x=50, y=350)
frambuesa_text = tk.Label(ventana, text="Frambuesa").place(x=50, y=350)

fresa = Image.open("./Frutas/fresa.jpeg")
fresa = fresa.resize((100,100), Image.Resampling.LANCZOS)
fresaImg = ImageTk.PhotoImage(fresa)
fresa_etiqueta = tk.Label(ventana, image = fresaImg).place(x=50, y=450)
fresa_text = tk.Label(ventana, text="Fresa").place(x=50, y=450)

granada = Image.open("./Frutas/granada.jpg")
granada = granada.resize((100,100), Image.Resampling.LANCZOS)
granadaImg = ImageTk.PhotoImage(granada)
granada_etiqueta = tk.Label(ventana, image = granadaImg).place(x=200, y=50)
granada_text = tk.Label(ventana, text="Granada").place(x=200, y=50)

guanabana = Image.open("./Frutas/guanabana.png")
guanabana = guanabana.resize((100,100), Image.Resampling.LANCZOS)
guanabanaImg = ImageTk.PhotoImage(guanabana)
guanabana_etiqueta = tk.Label(ventana, image = guanabanaImg).place(x=200, y=150)
guanabana_text = tk.Label(ventana, text="Guanabana").place(x=200, y=150)

higo = Image.open("./Frutas/higo.png")
higo = higo.resize((100,100), Image.Resampling.LANCZOS)
higoImg = ImageTk.PhotoImage(higo)
higo_etiqueta = tk.Label(ventana, image = higoImg).place(x=200, y=250)
higo_text = tk.Label(ventana, text="Higo").place(x=200, y=250)

kiwi = Image.open("./Frutas/kiwi.jpeg")
kiwi = kiwi.resize((100,100), Image.Resampling.LANCZOS)
kiwiImg = ImageTk.PhotoImage(kiwi)
kiwi_etiqueta = tk.Label(ventana, image = kiwiImg).place(x=200, y=350)
kiwi_text = tk.Label(ventana, text="Kiwi").place(x=200, y=350)

lichi = Image.open("./Frutas/lichi.png")
lichi = lichi.resize((100,100), Image.Resampling.LANCZOS)
lichiImg = ImageTk.PhotoImage(lichi)
lichi_etiqueta = tk.Label(ventana, image = lichiImg).place(x=200, y=450)
lichi_text = tk.Label(ventana, text="Lichi").place(x=200, y=450)

limon = Image.open("./Frutas/limon.png")
limon = limon.resize((100,100), Image.Resampling.LANCZOS)
limonImg = ImageTk.PhotoImage(limon)
limon_etiqueta = tk.Label(ventana, image = limonImg).place(x=350, y=50)
limon_text = tk.Label(ventana, text="Limon").place(x=350, y=50)

mamey = Image.open("./Frutas/mamey.png")
mamey = mamey.resize((100,100), Image.Resampling.LANCZOS)
mameyImg = ImageTk.PhotoImage(mamey)
mamey_etiqueta = tk.Label(ventana, image = mameyImg).place(x=350, y=150)
mamey_text = tk.Label(ventana, text="Mamey").place(x=350, y=150)

mango = Image.open("./Frutas/mango.png")
mango = mango.resize((100,100), Image.Resampling.LANCZOS)
mangoImg = ImageTk.PhotoImage(mango)
mango_etiqueta = tk.Label(ventana, image = mangoImg).place(x=350, y=250)
mango_text = tk.Label(ventana, text="Mango").place(x=350, y=250)

manzana = Image.open("./Frutas/manzana.png")
manzana = manzana.resize((100,100), Image.Resampling.LANCZOS)
manzanaImg = ImageTk.PhotoImage(manzana)
manzana_etiqueta = tk.Label(ventana, image = manzanaImg).place(x=350, y=350)
manzana_text = tk.Label(ventana, text="Manzana").place(x=350, y=350)

maracuya = Image.open("./Frutas/maracuya.png")
maracuya = maracuya.resize((100,100), Image.Resampling.LANCZOS)
maracuyaImg = ImageTk.PhotoImage(maracuya)
maracuya_etiqueta = tk.Label(ventana, image = maracuyaImg).place(x=350, y=450)
maracuya_text = tk.Label(ventana, text="Maracuya").place(x=350, y=450)

melocoton = Image.open("./Frutas/melocoton.jpg")
melocoton = melocoton.resize((100,100), Image.Resampling.LANCZOS)
melocotonImg = ImageTk.PhotoImage(melocoton)
melocoton_etiqueta = tk.Label(ventana, image = melocotonImg).place(x=500, y=50)
melocoton_text = tk.Label(ventana, text="Melocoton").place(x=500, y=50)

melon = Image.open("./Frutas/melon.jpg")
melon = melon.resize((100,100), Image.Resampling.LANCZOS)
melonImg = ImageTk.PhotoImage(melon)
melon_etiqueta = tk.Label(ventana, image = melonImg).place(x=500, y=150)
melon_text = tk.Label(ventana, text="Melón").place(x=500, y=150)

mora = Image.open("./Frutas/mora.png")
mora = mora.resize((100,100), Image.Resampling.LANCZOS)
moraImg = ImageTk.PhotoImage(mora)
mora_etiqueta = tk.Label(ventana, image = moraImg).place(x=500, y=250)
mora_text = tk.Label(ventana, text="Mora azul").place(x=500, y=250)

naranja = Image.open("./Frutas/naranja.jpg")
naranja = naranja.resize((100,100), Image.Resampling.LANCZOS)
naranjaImg = ImageTk.PhotoImage(naranja)
naranja_etiqueta = tk.Label(ventana, image = naranjaImg).place(x=500, y=350)
naranja_text = tk.Label(ventana, text="Naranja").place(x=500, y=350)

pera = Image.open("./Frutas/pera.jpg")
pera = pera.resize((100,100), Image.Resampling.LANCZOS)
peraImg = ImageTk.PhotoImage(pera)
pera_etiqueta = tk.Label(ventana, image = peraImg).place(x=500, y=450)
pera_text = tk.Label(ventana, text="Pera").place(x=500, y=450)

persimo = Image.open("./Frutas/persimo.jpg")
persimo = persimo.resize((100,100), Image.Resampling.LANCZOS)
persimoImg = ImageTk.PhotoImage(persimo)
persimo_etiqueta = tk.Label(ventana, image = persimoImg).place(x=650, y=50)
persimo_text = tk.Label(ventana, text="Persimo").place(x=650, y=50)

piña = Image.open("./Frutas/piña.jpg")
piña = piña.resize((100,100), Image.Resampling.LANCZOS)
piñaImg = ImageTk.PhotoImage(piña)
piña_etiqueta = tk.Label(ventana, image = piñaImg).place(x=650, y=150)
piña_text = tk.Label(ventana, text="Piña").place(x=650, y=150)

pitahaya = Image.open("./Frutas/pitahaya.jpg")
pitahaya = pitahaya.resize((100,100), Image.Resampling.LANCZOS)
pitahayaImg = ImageTk.PhotoImage(pitahaya)
pitahaya_etiqueta = tk.Label(ventana, image = pitahayaImg).place(x=650, y=250)
pitahaya_text = tk.Label(ventana, text="Dragon fruit (Pitahaya)").place(x=650, y=250)

sandia = Image.open("./Frutas/sandia.png")
sandia = sandia.resize((100,100), Image.Resampling.LANCZOS)
sandiaImg = ImageTk.PhotoImage(sandia)
sandia_etiqueta = tk.Label(ventana, image = sandiaImg).place(x=650, y=350)
sandia_text = tk.Label(ventana, text="Sandía").place(x=650, y=350)

uva = Image.open("./Frutas/uva.jpg")
uva = uva.resize((100,100), Image.Resampling.LANCZOS)
uvaImg = ImageTk.PhotoImage(uva)
uva_etiqueta = tk.Label(ventana, image = uvaImg).place(x=650, y=450)
uva_text = tk.Label(ventana, text="Uva").place(x=650, y=450)


def preguntas():
    prueba = messagebox.askyesno(message="La fruta en la que estás pensando, ¿es grande?", title="Pregunta 1")
    if prueba:
        prueba = messagebox.askyesno(message="La fruta, ¿tiene semillas?", title="pregunta 2")
        if prueba:
            prueba = messagebox.askyesno(message="¿Las semillas son de color negro?", title="pregunta 3")
            if prueba:
                while True:
                    prueba = messagebox.askyesno(message="El exterior de la fruta es liso", title="pregunta 4")
                    if prueba:
                        break
                while True:
                    prueba = messagebox.askyesno(message="¿El color interno es rojo?", title="pregunta 5")
                    if prueba:
                        print("La fruta que estás pensando es la sandía")
                        break
            else:
                prueba = messagebox.askyesno(message="La forma de la fruta, ¿es redonda?", title="pregunta 9")
                if prueba:
                    prueba = messagebox.askyesno(message="¿Su color interno es naranja?", title="pregunta 10")
                    if prueba:
                        prueba = messagebox.askyesno(message="¿Su cáscara está rasposa?", title="pregunta 11")
                        if prueba:
                            print("La fruta que estais pensando es el melón")
                    else:
                        print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                else:
                    print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
        else:
            prueba = messagebox.askyesno(message="¿Su color interno es amarillo?", title="pregunta 6")
            if prueba:
                prueba = messagebox.askyesno(message="¿Su cáscara está rasposa?", title="pregunta 7")
                if prueba:
                    prueba = messagebox.askyesno(message="En esta fruta, ¿vive bob esponja?", title="pregunta 8")
                    if prueba:
                        print("La fruta que estás pensando es la piña")
                else:
                    print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
            else:
                print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
    else:
        prueba = messagebox.askyesno(message="¿Su color interno es rojo?", title="pregunta 12")
        if prueba:
            prueba = messagebox.askyesno(message="¿Tiene semillas en su exterior?", title="pregunta 13")
            if prueba: 
                prueba = messagebox.askyesno(message="El color externo de la fruta que piensas, ¿es rojo?", title="pregunta 14")
                if prueba:
                    prueba = messagebox.askyesno(message="¿La fruta crece en un arbusto?", title="pregunta 15")
                    if prueba:
                        print("La fruta que estais pensando es la fresa")
                    else:
                        print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                else:
                    print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
            else:
                prueba = messagebox.askyesno(message="En su interior, ¿su contenido tiene forma de grano?", title="pregunta 16")
                if prueba:
                    prueba = messagebox.askyesno(message="La fruta que piensas, ¿proviene de un árbol?", title="pregunta 17")
                    if prueba:
                        prueba = messagebox.askyesno(message="¿Su interior está dividido en secciones?", title="pregunta 18")
                        if prueba:
                            print("La fruta que estais pensando es la granada")
                    else:
                        print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                else:
                    prueba = messagebox.askyesno(message="La forma de la fruta, ¿es la de un círculo u óvalo?", title="pregunta 39")
                    if prueba:
                        prueba = messagebox.askyesno(message="La fruta, ¿cuenta con un hueso en su interior?", title="pregunta 40")
                        if prueba:
                            prueba = messagebox.askyesno(message="¿La fruta tiene un tallo verde?", title="pregunta 41")
                            if prueba:
                                print("La fruta en la que estás pensando es la cereza")
                        else:
                            prueba = messagebox.askyesno(message="El exterior de la fruta, ¿está formado por pequeñas bolitas?", title="pregunta 42")
                            if prueba:
                                prueba = messagebox.askyesno(message="El sabor de la fruta, ¿es agridulce?", title="pregunta 43")
                                if prueba:
                                    print("La fruta en la que estás pensando es la frambuesa")
                            else:
                                prueba = messagebox.askyesno(message="El color exterior de la fruta, ¿es morado?", title="pregunta 44")
                                if prueba:
                                    prueba = messagebox.askyesno(message="El interior de la fruta, ¿es rojo y tiene en el centro pequeñas semillas blancas?", title="pregunta 45")
                                    if prueba:
                                        print("La fruta que estás pensando es el higo")
                                else:
                                    print("No funciona")
                    else:
                        print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
        else:
            prueba = messagebox.askyesno(message="El color externo de tu fruta, ¿es naranja?", title="pregunta 20")
            if prueba:
                prueba = messagebox.askyesno(message="¿Tiene semillas en el interior?", title="pregunta 21")
                if prueba:
                    prueba = messagebox.askyesno(message="¿Tiene más de una semilla?", title="pregunta 22")
                    if prueba:
                        prueba = messagebox.askyesno(message="La fruta, ¿se puede dividir en gajos (partes)?", title="pregunta 23")
                        if prueba:
                            print("La fruta que piensas es la naranja")
                    else:
                        prueba = messagebox.askyesno(message="¿La semilla es lisa?", title="pregunta 24")
                        if prueba:
                            prueba = messagebox.askyesno(message="La textura de la fruta, ¿es áspera?", title="pregunta 25")
                            if prueba:
                                prueba = messagebox.askyesno(message="El color externo de la fruta, ¿es de color café?", title="pregunta 26")
                                if prueba:
                                    print("La fruta que estás pensando es el mamey")
                            else:
                                print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                        else:
                            prueba = messagebox.askyesno(message="El color interno de la fruta, ¿es amarillo?", title="pregunta 26")
                            if prueba:
                                prueba = messagebox.askyesno(message="Su cáscara, ¿es vellosa?", title="pregunta 27")
                                if prueba:
                                    print("La fruta que estás pensando es el melocotón")
                            else:
                                print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                else:
                    prueba = messagebox.askyesno(message="¿La cáscara de la fruta es delgada?", title="pregunta 28")
                    if prueba:
                        prueba = messagebox.askyesno(message="El color interno de la fruta que piensas, ¿es naranja?", title="pregunta 29")
                        if prueba:
                            print("La fruta que estás pensando es el pérsimo")
                    else:
                        print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
            else:
                prueba = messagebox.askyesno(message="La fruta en la que estás pensando, ¿su color interno es beige?", title="pregunta 30")
                if prueba:
                    prueba = messagebox.askyesno(message="El color externo de la fruta, ¿es rosa?", title="pregunta 31")
                    if prueba:
                        prueba = messagebox.askyesno(message="En su exterior, su cáscara ¿tiene escamas?", title="pregunta 32")
                        if prueba:
                            prueba = messagebox.askyesno(message="La fruta que piensas, ¿tiene nombre de un animal mitológico?", title="pregunta 33")
                            if prueba:
                                print("La fruta que estás pensando es la dragonfruit (Pitahaya)")
                        else:
                            print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                    elif messagebox.askyesno(message="El sabor de la fruta, ¿es dulce?", title="pregunta 34"):
                        prueba = messagebox.askyesno(message="Esta fruta, ¿se cosecha en un árbol?", title="pregunta 35")
                        if prueba:
                            prueba = messagebox.askyesno(message="La forma de la fruta, ¿es cómo una bombilla?", title="pregunta 36")
                            if prueba:
                                print("La fruta que estás pensando es la pera")
                            else:
                                prueba = messagebox.askyesno(message="Su exterior, ¿es irregular, rasposo y tiene picos?", title="pregunta 37")
                                if prueba:
                                    print("La fruta que estás pensando es la guanabana")
                                else:
                                    prueba = messagebox.askyesno(message="¿Se considera la fruta prohibida?", title="pregunta 38")
                                    if prueba:
                                        print("La fruta que estás pensando es la manzana")
                        else:
                            print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                    else:
                        prueba = messagebox.askyesno(message="El color externo de la fruta, ¿es rojo?", title="pregunta 46")
                        if prueba:
                            prueba = messagebox.askyesno(message="La fruta, ¿es considerada parte del grupo de las bayas?", title="pregunta 47")
                            if prueba:
                                print("La fruta que estás pensando es el arándano")
                        else:
                            print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                elif messagebox.askyesno(message="El color interno de la fruta que piensas, ¿es amarillo?", title="pregunta 48"):
                    prueba = messagebox.askyesno(message="¿Tiene semillas en el interior?", title="pregunta 49")
                    if prueba:
                        prueba = messagebox.askyesno(message="La fruta, ¿Tiene solo una semilla en su interior?", title="pregunta 50")
                        if prueba:
                            prueba = messagebox.askyesno(message="La semilla de la fruta, ¿es áspera?", title="pregunta 51")
                            if prueba:
                                prueba = messagebox.askyesno(message="El color externo de la fruta que piensas, ¿es amarillo?", title="pregunta 52")
                                if prueba:
                                    print("La fruta que estás pensando es el mango")
                            else:
                                print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                        else:
                            print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                else:
                    prueba = messagebox.askyesno(message="La fruta que estás pensando, ¿su color interno es verde?", title="pregunta 59")
                    if prueba:
                        prueba = messagebox.askyesno(message="¿Tiene sabor ácido?", title="pregunta 60")
                        if prueba:
                            prueba = messagebox.askyesno(message="En su exterior, ¿su cáscara tiene vellosidades?", title="pregunta 61")
                            if prueba:
                                prueba = messagebox.askyesno(message="¿Su color externo es café?", title="pregunta 62")
                                if prueba:
                                    print("La fruta que estás pensando es el kiwi")
                            else:
                                prueba = messagebox.askyesno(message="En su exterior, ¿su cáscara es lisa?", title="pregunta 63")
                                if prueba:
                                    prueba = messagebox.askyesno(message="La fruta, ¿tiene forma cirular y pequeña?", title="pregunta 64")
                                    if prueba:
                                        prueba = messagebox.askyesno(message="¿Su color externo es verde?", title="pregunta 65")
                                        if prueba:
                                            print("La fruta que estás pensando es el limon")
                                        else:
                                            prueba = messagebox.askyesno(message="El color externo de la fruta, ¿es morado?", title="pregunta 66")
                                            if prueba:
                                                print("La fruta que estás pensando es la moraazul")
                                    else:
                                        print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                                else:
                                    print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                        else:
                            prueba = messagebox.askyesno(message="¿Su color externo es verde y cuando está maduro es negro?", title="pregunta 67")
                            if prueba:
                                prueba = messagebox.askyesno(message="La fruta es usada, ¿para hacer guacamole?", title="pregunta 68")
                                if prueba:
                                    print("La fruta que estás pensando es el aguacate")
                            else:
                                print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                    else:
                        prueba = messagebox.askyesno(message="En su interior, ¿su contenido tiene forma de grano?", title="pregunta 16")
                        if prueba:
                            prueba = messagebox.askyesno(message="La fruta que piensas, ¿proviene de un árbol?", title="pregunta 17")
                            if prueba:
                                prueba = messagebox.askyesno(message="La fruta que piensas, ¿tiene el color interno un poco naranja y el color externo amarillo?", title="pregunta 19")
                                if prueba:
                                    prueba = messagebox.askyesno(message="Los granos que contiene la fruta, son de color negro?")
                                    if prueba:
                                        print("La fruta que estais pensando es la maracuya")
                        else:
                            prueba = messagebox.askyesno(message="La fruta que piensas, ¿es transparente por dentro?", title="pregunta 53")
                            if prueba:
                                prueba = messagebox.askyesno(message="El exterior de la fruta que piensas, ¿es de color rojo?", title="pregunta 54")
                                if prueba:
                                    prueba = messagebox.askyesno(message="La fruta que piensas, ¿tiene una sola semilla grande?", title="pregunta 55")
                                    if prueba:
                                        prueba = messagebox.askyesno(message="El tamaño de la fruta, ¿es pequeño?", title="pregunta 56")
                                        if prueba:
                                            print("La fruta que estás pensando es el lichi")
                                    else:
                                        print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")
                                else:
                                    prueba = messagebox.askyesno(message="La fruta que piensas, ¿a veces tiene semillas?", title="pregunta 57")
                                    if prueba:
                                        prueba = messagebox.askyesno(message="El color externo de la fruta, ¿es morado?", title="pregunta 58")
                                        if prueba:
                                            print("La fruta que estás pensando es la uva")
                                    else:
                                        print("Las características que describes no pertenece a ninguna de las frutas que se mostraron, vuelve a intentarlo!")

boton = tk.Button(ventana, text = "Iniciar", command = preguntas) 
boton.pack(side = "bottom")

ventana.mainloop()