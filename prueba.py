from tkinter import filedialog, Tk, messagebox
messagebox.showerror("Hola","gg")
# lista = []

# def abrir():
#     Tk().withdraw()
#     archivo = filedialog.askopenfile(
#         title = "Seleccionar un archivo",
#         initialdir = "./",
#         filetypes = [
#             ("archivos LFP", "*.lfp"),
#             ("todos los archivos",  "*.*")
#         ]
#     )

#     if archivo is None:
#         print('No se selecciono ningun archivo\n')
#         return None
#     else:
#         texto = archivo.read()
#         archivo.close()
#         return texto

# if __name__ == '__main__':
#     lista = []
#     txt = abrir()

#     if txt is not None:
#         # print(txt)
#         if(len(txt) > 0):
#             for c in txt:
#                 # print(c, end="\n")
#                 if c == '\n':
#                     pass
#                 elif c == ' ':
#                     pass
#                 else:
#                     # print(c + " - " + str( ord(c) ))
#                     listaAux = [ord(c), c]
#                     lista.append(listaAux)
#             for e in lista:
#                 print('Ascii: ' + str(e[0]) + ' - Caracter: ' + e[1])
#         else:
#             print('No hay texto :v F')
#     else:
#         print('No se puede procesar\n')


#     idcourseaux=0
#     namecourseaux=""
#     prerequisiteaux=0
#     optinalityaux=0
#     semesteraux=0
#     creditsaux=0
#     statusaux=0
#     niuLine[1]= idcourseaux
#     niuLine[2]=namecourseaux
#     niuLine[3]=prerequisiteaux
#     niuLine[4]=optinalityaux
#     niuLine[5]=semesteraux
#     niuLine[6]=creditsaux
#     niuLine[7]=statusaux
#     Cursonew=Curso(idcourseaux,namecourseaux,prerequisiteaux,optinalityaux,creditsaux,statusaux)
# ListaCursos.append(Cursonew)