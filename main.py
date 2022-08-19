from cgitb import text
import os
from queue import Empty
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview
from tokenize import String
from typing import Counter
from curso import Curso

#Variables Para Las Ventanas
wndw_menu = None
wndw_fileupload = None
wndw_managecourse = None
wndw_listcourse = None
wndw_addcourse = None
wndw_editcourse = None
wndw_deletecourse = None
wndw_credicount = None
wndw_showcourse=None

#Lista de Cursos
ListaCursos=[]
#Contador de Cursos
ContaCursos =0

#Variables Para Mostrar Curso
textboxCoursename =None
textboxCoursePreRequis = None
textboxCourseSemester = None
textboxCourseOptionality = None
textboxCourseCredits = None
textboxCourseStatus = None

#Textbos para Agregar curso
textboxCourseidadd= None
textboxCoursenameadd= None
textboxCoursePreRequisadd= None
textboxCourseSemesteradd= None
textboxCourseOptionalityadd= None
textboxCourseCreditsadd= None
textboxCourseStatusadd= None

#TextBox para Editar curso
textboxEditCourseided= None
textboxEditCoursenameed= None
textboxEditCoursePreRequised= None
textboxEditCourseSemestered= None
textboxEditCourseOptionalityed= None
textboxEditCourseCreditsed= None
textboxEditCourseStatused= None

#TextBox Para eliminar Curso
textboxidCoursedel = None

#Variable para el módulo créditos
totalCreditinNSemester=0
def getBackMainMenuFromManage():
    global wndw_managecourse
    wndw_managecourse.destroy()
    window_mainMenu()

def getBackMainMenuFromFileUpload():
    global wndw_fileupload
    wndw_fileupload.destroy()
    window_mainMenu()

def getBackMainMenuFromCreditCount():
    global wndw_credicount
    wndw_credicount.destroy()
    window_mainMenu()

def getBackManageCourseFromListCourse():
    global wndw_listcourse
    wndw_listcourse.destroy()
    window_managecourse()

def getBackManageCourseFromShowCourse():
    global wndw_showcourse
    wndw_showcourse.destroy()
    window_managecourse()

def getBackManageCourseFromAddCourse():
    global wndw_addcourse
    wndw_addcourse.destroy()
    window_managecourse()

def getBackManageCourseFromEditCourse():
    global wndw_editcourse
    wndw_editcourse.destroy()
    window_managecourse()

def getBackManageCourseFromDeleteCourse():
    global wndw_deletecourse
    wndw_deletecourse.destroy()
    window_managecourse()

def goToManageMenuFromMain():
    global wndw_menu
    wndw_menu.destroy()
    window_managecourse()

def window_mainMenu():
    global wndw_menu
    #Configuración ventana menu principal
    wndw_menu = tk.Tk()
    wndw_menu.title("Menu Principal")
    wndw_menu.resizable(0,0)
    wndw_menu.iconbitmap("img/menu.ico")
    wndw_menu.geometry("720x480")
    wndw_menu.config(bg="#48F1D8")
    wndw_menu.config(bd=30)
    wndw_menu.config(relief="groove")
    #Configuraciones Labels
    labelNameCourse=Label(wndw_menu,text="Curso: Lenguajes Formales y de Programación",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelNameCourse.place(x=80,y=20)

    labelNameStudent=Label(wndw_menu,text="Nombre: Eduardo Josué González Cifuentes",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelNameStudent.place(x=80,y=45)

    labelNameidstudent=Label(wndw_menu,text="Carnet: 201900647",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelNameidstudent.place(x=80,y=70)
    #Configuración Botones
    buttonFileUpload=Button(wndw_menu,text="Cargar Archivo",width=20,bg="#48F1D8", font=("Courier 15 bold"),relief="groove",bd=8,command=window_fileupload)
    buttonFileUpload.place(x=220,y=120)

    buttonManageCourse=Button(wndw_menu,text="Gestionar Cursos",width=20,bg="#48F1D8", font=("Courier 15 bold"),relief="groove",bd=8,command=goToManageMenuFromMain)
    buttonManageCourse.place(x=220,y=180)

    buttonCreditCount=Button(wndw_menu,text="Conteo de Créditos",width=20,bg="#48F1D8", font=("Courier 15 bold"),relief="groove",bd=8,command=window_creditcount)
    buttonCreditCount.place(x=220,y=240)

    buttonMainMenuOut=Button(wndw_menu,text="Salir",width=20,bg="#48F1D8", font=("Courier 15 bold"),relief="groove",bd=8,command=exit)
    buttonMainMenuOut.place(x=220,y=300)
    wndw_menu.mainloop()

def readFile(txt):
    global ContaCursos
    global ListaCursos
    print("xd",txt)
    if txt == "":
        mensaje=messagebox.showwarning("Archivos","No se ha cargado ningún archivo")
        return mensaje
    else:
        partsOfnameFile=txt.split('.')
        print(partsOfnameFile)
        print("longitud",len(partsOfnameFile))
        pos1=partsOfnameFile[0]
        if(os.path.exists(str(pos1)+".lfp")):
            if len(partsOfnameFile)!=2:
                messagebox.showwarning("Archivos","Ingrese un archivo correcto")
            else:
                if(partsOfnameFile[1] == 'lfp'):
                    file =open(txt,'r', encoding="utf-8")
                    line=file.read()
                    file.close()
                    #print(line)
                    print("")
                    newLine = line.split("\n")
                    for c in newLine:
                        if c != "":
                            niuLine= c.split(",")
                            print(niuLine)
                            ContaCursos+=1
                            idcourseaux=0
                            namecourseaux=""
                            prerequisiteaux=0
                            optinalityaux=0
                            semesteraux=0
                            creditsaux=0
                            statusaux=0
                            idcourseaux=niuLine[0]
                            namecourseaux = niuLine[1]
                            prerequisiteaux = niuLine[2]
                            optinalityaux =niuLine[3]
                            semesteraux=niuLine[4]
                            creditsaux =niuLine[5]
                            statusaux = niuLine[6]
                            Cursonew=Curso(idcourseaux,namecourseaux,prerequisiteaux,optinalityaux,semesteraux,creditsaux,statusaux)
                            Cursonew.Counter=ContaCursos
                            ListaCursos.append(Cursonew)
                        for r in ListaCursos:
                            print("____________________________________________________________")
                            print("Curso No. ", str(r.Counter))
                            print(" ID Curso: " +r.idCourse + " |Curso: "+r.NameCourse+" |PreReQuisito: " +r.PreRequisite+" |Opcionalidad: " +r.Optionality+ " |Semestre: " + r.Semester + " |Creditos: " + r.Credits + " |Estados: " + r.Status)
                    print("Hay " + str(ContaCursos) + " Cursos")
                    print("")
                    messagebox.showinfo("Archivos","Archivos Cargados")
                else:
                    messagebox.showwarning("Archivos","Ingrese un archivo correcto")
                    print("Ingrese un archivo correcto :( ")
        else:
            messagebox.showwarning("Archivos","Ingrese un archivo correcto")

def window_fileupload():
    global wndw_fileupload
    global wndw_menu
    wndw_menu.destroy()
    #Configuración ventana cargar archivos
    wndw_fileupload = tk.Tk()
    wndw_fileupload.title("Cargar Archivos")
    wndw_fileupload.resizable(0,0)
    wndw_fileupload.iconbitmap("img/file.ico")
    wndw_fileupload.geometry("720x350")
    wndw_fileupload.config(bg="#C9A4F9")
    wndw_fileupload.config(bd=30)
    wndw_fileupload.config(relief="ridge")
    #Configuraciones Labels
    labelNameRoute=Label(wndw_fileupload,text="Ruta:",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelNameRoute.place(x=120,y=80)
    #Configuracion textbox
    textboxRoute=Entry(wndw_fileupload)
    textboxRoute.place(x=195,y=84,width=300,height=24)
    
    #Configuración Botones
    buttonSelectRoute=Button(wndw_fileupload,text="Seleccionar",width=11,bg="#C9A4F9", font=("Courier 13 bold"),relief="ridge",bd=8,command=lambda:readFile(textboxRoute.get().strip()))
    buttonSelectRoute.place(x=270,y=140)

    buttonBackMainMenu=Button(wndw_fileupload,text="Regresar",width=11,bg="#C9A4F9", font=("Courier 13 bold"),relief="ridge",bd=8,command=getBackMainMenuFromFileUpload)
    buttonBackMainMenu.place(x=498,y=230)
    wndw_fileupload.mainloop()

def window_managecourse():
    global wndw_managecourse
    #Configuración ventana gestionar archivos
    wndw_managecourse = tk.Tk()
    wndw_managecourse.title("Gestionar Cursos")
    wndw_managecourse.resizable(0,0)
    wndw_managecourse.iconbitmap("img/course.ico")
    wndw_managecourse.geometry("720x480")
    wndw_managecourse.config(bg="#9EBCFF")
    wndw_managecourse.config(bd=30)
    wndw_managecourse.config(relief="groove")
    #Configuración Botones
    buttonListCourses=Button(wndw_managecourse,text="Listar Cursos",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=window_listcouse)
    buttonListCourses.place(x=250,y=50)

    buttonShowCourses=Button(wndw_managecourse,text="Mostrar Cursos",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=window_showcourse)
    buttonShowCourses.place(x=250,y=110)

    buttonAddCourse=Button(wndw_managecourse,text="Agregar Curso",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=window_addcourse)
    buttonAddCourse.place(x=250,y=170)

    buttonEditCourse=Button(wndw_managecourse,text="Editar Curso",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=window_editcourse)
    buttonEditCourse.place(x=250,y=230)

    buttonDeleteCourse=Button(wndw_managecourse,text="Eliminar Curso",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=window_deleteCourse)
    buttonDeleteCourse.place(x=250,y=290)

    buttonBackmainmenu=Button(wndw_managecourse,text="Regresar",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackMainMenuFromManage)
    buttonBackmainmenu.place(x=250,y=350)
    wndw_managecourse.mainloop()

def window_listcouse():
    global ListaCursos
    global wndw_managecourse
    global wndw_listcourse
    wndw_managecourse.destroy()
    #Configuración ventana lista de cursos
    wndw_listcourse = tk.Tk()
    wndw_listcourse.title("Listar Cursos")
    wndw_listcourse.iconbitmap("img/list.ico")
    wndw_listcourse.geometry("920x580")
    wndw_listcourse.resizable(0,0)
    wndw_listcourse.config(bg="#9EBCFF")
    wndw_listcourse.config(bd=30)
    wndw_listcourse.config(relief="groove")

    #Configuración tabla
    StyleTableColum=ttk.Style()
    StyleTableColum.configure("Treeview.Heading", font=("Courier",10,"bold"))

    TableListCourse= ttk.Treeview(wndw_listcourse,columns=("col0","col1","col2","col3","col4","col5","col6"))
    TableListCourse.column("#0",width=0)
    TableListCourse.column("col0",width=80,anchor=CENTER)
    TableListCourse.column("col1",width=220,anchor=CENTER)
    TableListCourse.column("col2",width=120,anchor=CENTER)
    TableListCourse.column("col3",width=120,anchor=CENTER)
    TableListCourse.column("col4",width=90,anchor=CENTER)
    TableListCourse.column("col5",width=90,anchor=CENTER)
    TableListCourse.column("col6",width=90,anchor=CENTER)
    TableListCourse.heading("col0",text="Código",anchor=CENTER)
    TableListCourse.heading("col1",text="Nombre",anchor=CENTER)
    TableListCourse.heading("col2",text="Pre Requisito",anchor=CENTER)
    TableListCourse.heading("col3",text="Opcionalidad",anchor=CENTER)
    TableListCourse.heading("col4",text="Semestre",anchor=CENTER)
    TableListCourse.heading("col5",text="Créditos",anchor=CENTER)
    TableListCourse.heading("col6",text="Estado",anchor=CENTER)
    Cursosgg=[]
    for uwu in ListaCursos:
        Cursosgg.append((uwu.idCourse,uwu.NameCourse,uwu.PreRequisite,uwu.Optionality,uwu.Semester,uwu.Credits,uwu.Status))
    for ewe in Cursosgg:
        TableListCourse.insert("",tk.END,values=ewe)

    TableListCourse.pack()
    TableListCourse.place(x=20,y=35)

    #Configuración botones
    buttonBackManageCourse=Button(wndw_listcourse,text="Regresar",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackManageCourseFromListCourse)
    buttonBackManageCourse.place(x=575,y=460)
    wndw_listcourse.mainloop()

def showCourse(idgg):
    global textboxCoursename 
    global textboxCoursePreRequis 
    global textboxCourseSemester 
    global textboxCourseOptionality 
    global textboxCourseCredits
    global textboxCourseStatus
    foundd = False 
    for e in ListaCursos:
        if idgg==e.idCourse:
            textboxCoursename.configure(text=e.NameCourse)
            textboxCoursePreRequis.configure(text=e.PreRequisite)
            textboxCourseSemester.configure(text=e.Semester)
            textboxCourseOptionality.configure(text=e.Optionality)
            textboxCourseCredits.configure(text=e.Credits)
            textboxCourseStatus.configure(text=e.Status)
            foundd=True
            print(" ID Curso: " +e.idCourse + " |Curso: "+e.NameCourse+" |PreReQuisito: " +e.PreRequisite+" |Opcionalidad: " +e.Optionality+ " |Semestre: " + e.Semester + " |Creditos: " + e.Credits + " |Estados: " + e.Status)
    if (foundd==True):
        messagebox.showinfo("Curso","Curso Encontrado :)")
    else:
        messagebox.showinfo("Curso","Curso No Encontrado :'v")

def window_showcourse():
    global wndw_managecourse
    global wndw_showcourse
    wndw_managecourse.destroy()

    global textboxCoursename 
    global textboxCoursePreRequis 
    global textboxCourseSemester 
    global textboxCourseOptionality 
    global textboxCourseCredits
    global textboxCourseStatus 
    
    #Configuración ventana gestionar archivos
    wndw_showcourse = tk.Tk()
    wndw_showcourse.title("Mostrar Curso")
    wndw_showcourse.resizable(0,0)
    wndw_showcourse.iconbitmap("img/show.ico")
    wndw_showcourse.geometry("820x580")
    wndw_showcourse.config(bg="#C9A4F9")
    wndw_showcourse.config(bd=30)
    wndw_showcourse.config(relief="groove")

    #Configuraciones Labels
    labelCourseid=Label(wndw_showcourse,text="Codigo: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseid.place(x=70,y=50)

    labelCourseName=Label(wndw_showcourse,text="Nombre: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseName.place(x=70,y=100)

    labelCoursePrerequisite=Label(wndw_showcourse,text="PreRequisito: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCoursePrerequisite.place(x=70,y=150)

    labelCourseSemestre=Label(wndw_showcourse,text="Semestre: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseSemestre.place(x=70,y=200)
    
    labelCourseOptionality=Label(wndw_showcourse,text="Opcionalidad: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseOptionality.place(x=70,y=250)

    labelCourseCredits=Label(wndw_showcourse,text="Créditos: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseCredits.place(x=70,y=300)

    labelCourseStatus=Label(wndw_showcourse,text="Estado: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseStatus.place(x=70,y=350)

    textboxCoursename=Label(wndw_showcourse,fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    textboxCoursename.place(x=265,y=105,width=370,height=25)
    

    textboxCoursePreRequis=Label(wndw_showcourse,fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    textboxCoursePreRequis.place(x=265,y=155,width=370,height=25)
    

    textboxCourseSemester=Label(wndw_showcourse,fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    textboxCourseSemester.place(x=265,y=205,width=370,height=25)
 

    textboxCourseOptionality=Label(wndw_showcourse,fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    textboxCourseOptionality.place(x=265,y=255,width=370,height=25)


    textboxCourseCredits=Label(wndw_showcourse,fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    textboxCourseCredits.place(x=265,y=305,width=370,height=25)


    textboxCourseStatus=Label(wndw_showcourse,fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    textboxCourseStatus.place(x=265,y=355,width=370,height=25)
    
    
    #Configuracion textbox
    textboxCourseid=Entry(wndw_showcourse)
    textboxCourseid.place(x=265,y=55,width=150,height=25)   
    
    #Configuración botones
    buttonBackManageCoursee=Button(wndw_showcourse,text="Regresar",width=12,bg="#C9A4F9", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackManageCourseFromShowCourse)
    buttonBackManageCoursee.place(x=610,y=465)

    buttonShowCourse=Button(wndw_showcourse,text="Mostrar",width=15,bg="#C9A4F9", font=("Courier 13 bold"),relief="ridge",bd=7,command=lambda:showCourse(textboxCourseid.get().strip()))
    buttonShowCourse.place(x=450,y=45)

    wndw_showcourse.mainloop()

def addCourse(niuIdCourse):
    global ContaCursos
    global ListaCursos
    addgg = False 
    global textboxCourseidadd
    global textboxCoursenameadd
    global textboxCoursePreRequisadd
    global textboxCourseSemesteradd
    global textboxCourseOptionalityadd
    global textboxCourseCreditsadd
    global textboxCourseStatusadd
    if checkCourse(textboxCourseidadd.get())==False:
        niuCourse= Curso(textboxCourseidadd.get(),textboxCoursenameadd.get(),textboxCoursePreRequisadd.get(),textboxCourseOptionalityadd.get(),textboxCourseSemesteradd.get(),textboxCourseCreditsadd.get(),textboxCourseStatusadd.get())
        ListaCursos.append(niuCourse)
        ContaCursos+=1
        addgg=True
        for e in ListaCursos:
            print(" ID Curso: " +str(e.idCourse) + " |Curso: "+str(e.NameCourse)+" |PreReQuisito: " +str(e.PreRequisite)+" |Opcionalidad: " +str(e.Optionality)+ " |Semestre: " + str(e.Semester )+ " |Creditos: " + str(e.Credits) + " |Estados: " +str( e.Status))
        print("Cursos ahora: ",ContaCursos)
    else:
        pass
    
    if (addgg==True):
        messagebox.showinfo("Curso","Curso Agregado :)")
    else:
        messagebox.showinfo("Curso","Ingrese un id válido")

def checkCourse(idgg):
    global ListaCursos
    for e in ListaCursos:
        if(e.idCourse==idgg):
            return True
    return False

def window_addcourse():
    global wndw_managecourse
    global wndw_addcourse
    wndw_managecourse.destroy()

    global textboxCourseidadd
    global textboxCoursenameadd
    global textboxCoursePreRequisadd
    global textboxCourseSemesteradd
    global textboxCourseOptionalityadd
    global textboxCourseCreditsadd
    global textboxCourseStatusadd

    #Configuración ventana gestionar archivos
    wndw_addcourse = tk.Tk()
    wndw_addcourse.title("Agregar Curso")
    wndw_addcourse.resizable(0,0)
    wndw_addcourse.iconbitmap("img/add.ico")
    wndw_addcourse.geometry("820x580")
    wndw_addcourse.config(bg="#C9A4F9")
    wndw_addcourse.config(bd=30)
    wndw_addcourse.config(relief="groove")

    #Configuraciones Labels
    labelCourseid=Label(wndw_addcourse,text="Codigo: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseid.place(x=70,y=50)

    labelCourseName=Label(wndw_addcourse,text="Nombre: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseName.place(x=70,y=100)

    labelCoursePrerequisite=Label(wndw_addcourse,text="PreRequisito: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCoursePrerequisite.place(x=70,y=150)

    labelCourseSemestre=Label(wndw_addcourse,text="Semestre: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseSemestre.place(x=70,y=200)
    
    labelCourseOptionality=Label(wndw_addcourse,text="Opcionalidad: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseOptionality.place(x=70,y=250)

    labelCourseCredits=Label(wndw_addcourse,text="Créditos: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseCredits.place(x=70,y=300)

    labelCourseStatus=Label(wndw_addcourse,text="Estado: ",fg="black",font=("Courier 18 bold"),bg="#C9A4F9")
    labelCourseStatus.place(x=70,y=350)

    #Configuracion textbox
    textboxCourseidadd=Entry(wndw_addcourse)
    textboxCourseidadd.place(x=265,y=55,width=370,height=25)
    
    textboxCoursenameadd=Entry(wndw_addcourse)
    textboxCoursenameadd.place(x=265,y=105,width=370,height=25)

    textboxCoursePreRequisadd=Entry(wndw_addcourse)
    textboxCoursePreRequisadd.place(x=265,y=155,width=370,height=25)

    textboxCourseSemesteradd=Entry(wndw_addcourse)
    textboxCourseSemesteradd.place(x=265,y=205,width=370,height=25)

    textboxCourseOptionalityadd=Entry(wndw_addcourse)
    textboxCourseOptionalityadd.place(x=265,y=255,width=370,height=25)

    textboxCourseCreditsadd=Entry(wndw_addcourse)
    textboxCourseCreditsadd.place(x=265,y=305,width=370,height=25)

    textboxCourseStatusadd=Entry(wndw_addcourse)
    textboxCourseStatusadd.place(x=265,y=355,width=370,height=25)
    
    #Configuración botones
    buttonBackManageCoursee=Button(wndw_addcourse,text="Regresar",width=12,bg="#C9A4F9", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackManageCourseFromAddCourse)
    buttonBackManageCoursee.place(x=610,y=465)

    buttonAddCourse=Button(wndw_addcourse,text="Agregar",width=15,bg="#C9A4F9", font=("Courier 13 bold"),relief="ridge",bd=7,command=lambda:addCourse(textboxCourseidadd))
    buttonAddCourse.place(x=340,y=400)

    wndw_addcourse.mainloop()

def editCourse(idxd):
    global ListaCursos
    editgg = False 
    global textboxEditCourseided
    global textboxEditCoursenameed
    global textboxEditCoursePreRequised
    global textboxEditCourseSemestered
    global textboxEditCourseOptionalityed
    global textboxEditCourseCreditsed
    global textboxEditCourseStatused
    if (checkCourse(textboxEditCourseided.get())==True):
        for r in ListaCursos:
            if(str(r.idCourse)==textboxEditCourseided.get()):
                r.idCourse = textboxEditCourseided.get()
                r.NameCourse = textboxEditCoursenameed.get()
                r.PreRequisite = textboxEditCoursePreRequised.get()
                r.Optionality = textboxEditCourseOptionalityed.get()
                r.Semester =  textboxEditCourseSemestered.get()
                r.Credits = textboxEditCourseCreditsed.get()
                r.Status = textboxEditCourseStatused.get()
                editgg=True
    else:
        pass

    if (editgg==True):
        messagebox.showinfo("Curso","Curso Editado :)")
    else:
        messagebox.showinfo("Curso","Ingrese un id válido")

def window_editcourse():
    global wndw_managecourse
    global wndw_editcourse
    wndw_managecourse.destroy()
    

    global textboxEditCourseided
    global textboxEditCoursenameed
    global textboxEditCoursePreRequised
    global textboxEditCourseSemestered
    global textboxEditCourseOptionalityed
    global textboxEditCourseCreditsed
    global textboxEditCourseStatused

    #Configuración ventana gestionar archivos
    wndw_editcourse = tk.Tk()
    wndw_editcourse.title("Editar Curso")
    wndw_editcourse.resizable(0,0)
    wndw_editcourse.iconbitmap("img/edit.ico")
    wndw_editcourse.geometry("820x580")
    wndw_editcourse.config(bg="#E99EFF")
    wndw_editcourse.config(bd=30)
    wndw_editcourse.config(relief="groove")

    #Configuraciones Labels
    labelEditCourseid=Label(wndw_editcourse,text="Codigo: ",fg="black",font=("Courier 18 bold"),bg="#E99EFF")
    labelEditCourseid.place(x=70,y=50)

    labelEditCourseName=Label(wndw_editcourse,text="Nombre: ",fg="black",font=("Courier 18 bold"),bg="#E99EFF")
    labelEditCourseName.place(x=70,y=100)

    labelEditCoursePrerequisite=Label(wndw_editcourse,text="PreRequisito: ",fg="black",font=("Courier 18 bold"),bg="#E99EFF")
    labelEditCoursePrerequisite.place(x=70,y=150)

    labelEditCourseSemestre=Label(wndw_editcourse,text="Semestre: ",fg="black",font=("Courier 18 bold"),bg="#E99EFF")
    labelEditCourseSemestre.place(x=70,y=200)
    
    labelEditCourseOptionality=Label(wndw_editcourse,text="Opcionalidad: ",fg="black",font=("Courier 18 bold"),bg="#E99EFF")
    labelEditCourseOptionality.place(x=70,y=250)

    labelEditCourseCredits=Label(wndw_editcourse,text="Créditos: ",fg="black",font=("Courier 18 bold"),bg="#E99EFF")
    labelEditCourseCredits.place(x=70,y=300)

    labelEditCourseStatus=Label(wndw_editcourse,text="Estado: ",fg="black",font=("Courier 18 bold"),bg="#E99EFF")
    labelEditCourseStatus.place(x=70,y=350)

    #Configuracion textbox
    textboxEditCourseided=Entry(wndw_editcourse)
    textboxEditCourseided.place(x=265,y=55,width=370,height=25)
    
    textboxEditCoursenameed=Entry(wndw_editcourse)
    textboxEditCoursenameed.place(x=265,y=105,width=370,height=25)

    textboxEditCoursePreRequised=Entry(wndw_editcourse)
    textboxEditCoursePreRequised.place(x=265,y=155,width=370,height=25)

    textboxEditCourseSemestered=Entry(wndw_editcourse)
    textboxEditCourseSemestered.place(x=265,y=205,width=370,height=25)

    textboxEditCourseOptionalityed=Entry(wndw_editcourse)
    textboxEditCourseOptionalityed.place(x=265,y=255,width=370,height=25)

    textboxEditCourseCreditsed=Entry(wndw_editcourse)
    textboxEditCourseCreditsed.place(x=265,y=305,width=370,height=25)

    textboxEditCourseStatused=Entry(wndw_editcourse)
    textboxEditCourseStatused.place(x=265,y=355,width=370,height=25)
    
    #Configuración botones
    buttonBackManageCoursse=Button(wndw_editcourse,text="Regresar",width=12,bg="#E99EFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackManageCourseFromEditCourse)
    buttonBackManageCoursse.place(x=610,y=465)

    buttonEditCourse=Button(wndw_editcourse,text="Editar",width=15,bg="#E99EFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=lambda:editCourse(textboxEditCourseided))
    buttonEditCourse.place(x=340,y=400)
    wndw_editcourse.mainloop()

def deleteCourse(idd):
    global ListaCursos
    global ContaCursos
    global textboxidCoursedel
    dele = False
    if (checkCourse(textboxidCoursedel.get())==True):
        for i in ListaCursos:
            if(i.idCourse==str(textboxidCoursedel.get())):
                ListaCursos.remove(i)
                ContaCursos-=1
                dele=True
        print("Cursos Ahora: ",ContaCursos)
    else:
        pass
    if (dele==True):
        messagebox.showinfo("Curso","Curso Eliminado :)")
    else:
        messagebox.showinfo("Curso","Ingrese un id válido")

def window_deleteCourse():
    global wndw_managecourse
    global wndw_deletecourse
    wndw_managecourse.destroy()
    global textboxidCoursedel
    #Configuración ventana cargar archivos
    wndw_deletecourse = tk.Tk()
    wndw_deletecourse.title("Eliminar Curso")
    wndw_deletecourse.resizable(0,0)
    wndw_deletecourse.iconbitmap("img/delete.ico")
    wndw_deletecourse.geometry("720x350")
    wndw_deletecourse.config(bg="#AFF5FF")
    wndw_deletecourse.config(bd=30)
    wndw_deletecourse.config(relief="ridge")
    #Configuraciones Labels
    labelidCourse=Label(wndw_deletecourse,text="Código de Curso:",fg="black",font=("Courier 18 bold"),bg="#AFF5FF")
    labelidCourse.place(x=20,y=80)
    #Configuracion textbox
    textboxidCoursedel=Entry(wndw_deletecourse)
    textboxidCoursedel.place(x=250,y=84,width=360,height=24)
    #Configuración Botones
    buttonDeleteCourse=Button(wndw_deletecourse,text="Eliminar",width=11,bg="#AFF5FF", font=("Courier 13 bold"),relief="ridge",bd=8,command=lambda:deleteCourse(textboxidCoursedel))
    buttonDeleteCourse.place(x=360,y=130)

    buttonBackManageCourssee=Button(wndw_deletecourse,text="Regresar",width=11,bg="#AFF5FF", font=("Courier 13 bold"),relief="ridge",bd=8,command=getBackManageCourseFromDeleteCourse)
    buttonBackManageCourssee.place(x=520,y=235)
    wndw_deletecourse.mainloop()

def CrediCountNsemester():
    global semestern
    global totalCreditinNSemester
    global sendDataCredit
    

    sumApprovedN=0
    sumTakingN=0
    sumPendingN=0
    if(semestern.get()=='1'):
        for r in ListaCursos:
            if(r.Semester=='1'):
                if(r.Status=='0'):
                    credit =int(r.Credits)
                    sumApprovedN=sumApprovedN+credit
                elif(r.Status=='1'):
                    credit1 =int(r.Credits)
                    sumTakingN=sumTakingN+credit1
                elif(r.Status=='-1'):
                    credit2 =int(r.Credits)
                    sumPendingN=sumPendingN+credit2
        totalCreditinNSemester = sumApprovedN+sumTakingN+sumPendingN
        sendDataCredit.set(totalCreditinNSemester)
        print()
        print("El Total de creditos Aprobados es: ",sumApprovedN)
        print("El Total de creditos Cursando es: ",sumTakingN)
        print("El Total de creditos Pendientes es: ",sumPendingN)
        print("Total de Créditos en Semestre 1 es: " +str(totalCreditinNSemester))
    elif(semestern.get()=='2'):
        for r in ListaCursos:
            if(r.Semester=='2'):
                if(r.Status=='0'):
                    credit =int(r.Credits)
                    sumApprovedN=sumApprovedN+credit
                elif(r.Status=='1'):
                    credit1 =int(r.Credits)
                    sumTakingN=sumTakingN+credit1
                elif(r.Status=='-1'):
                    credit2 =int(r.Credits)
                    sumPendingN=sumPendingN+credit2
        totalCreditinNSemester = sumApprovedN+sumTakingN+sumPendingN
        sendDataCredit.set(totalCreditinNSemester)
        print()
        print("El Total de creditos Aprobados es: ",sumApprovedN)
        print("El Total de creditos Cursando es: ",sumTakingN)
        print("El Total de creditos Pendientes es: ",sumPendingN)
        print("Total de Créditos en Semestre 2 es: " +str(totalCreditinNSemester))
    elif(semestern.get()=='3'):
        for r in ListaCursos:
            if(r.Semester=='3'):
                if(r.Status=='0'):
                    credit =int(r.Credits)
                    sumApprovedN=sumApprovedN+credit
                elif(r.Status=='1'):
                    credit1 =int(r.Credits)
                    sumTakingN=sumTakingN+credit1
                elif(r.Status=='-1'):
                    credit2 =int(r.Credits)
                    sumPendingN=sumPendingN+credit2
        totalCreditinNSemester = sumApprovedN+sumTakingN+sumPendingN
        sendDataCredit.set(totalCreditinNSemester)
        print()
        print("El Total de creditos Aprobados es: ",sumApprovedN)
        print("El Total de creditos Cursando es: ",sumTakingN)
        print("El Total de creditos Pendientes es: ",sumPendingN)
        print("Total de Créditos en Semestre 3 es: " +str(totalCreditinNSemester))
    elif(semestern.get()=='4'):
        for r in ListaCursos:
            if(r.Semester=='4'):
                if(r.Status=='0'):
                    credit =int(r.Credits)
                    sumApprovedN=sumApprovedN+credit
                elif(r.Status=='1'):
                    credit1 =int(r.Credits)
                    sumTakingN=sumTakingN+credit1
                elif(r.Status=='-1'):
                    credit2 =int(r.Credits)
                    sumPendingN=sumPendingN+credit2
        totalCreditinNSemester = sumApprovedN+sumTakingN+sumPendingN
        sendDataCredit.set(totalCreditinNSemester)
        print()
        print("El Total de creditos Aprobados es: ",sumApprovedN)
        print("El Total de creditos Cursando es: ",sumTakingN)
        print("El Total de creditos Pendientes es: ",sumPendingN)
        print("Total de Créditos en Semestre 4 es: " +str(totalCreditinNSemester))
    elif(semestern.get()=='5'):
        for r in ListaCursos:
            if(r.Semester=='5'):
                if(r.Status=='0'):
                    credit =int(r.Credits)
                    sumApprovedN=sumApprovedN+credit
                elif(r.Status=='1'):
                    credit1 =int(r.Credits)
                    sumTakingN=sumTakingN+credit1
                elif(r.Status=='-1'):
                    credit2 =int(r.Credits)
                    sumPendingN=sumPendingN+credit2
        totalCreditinNSemester = sumApprovedN+sumTakingN+sumPendingN
        sendDataCredit.set(totalCreditinNSemester)
        print()
        print("El Total de creditos Aprobados es: ",sumApprovedN)
        print("El Total de creditos Cursando es: ",sumTakingN)
        print("El Total de creditos Pendientes es: ",sumPendingN)
        print("Total de Créditos en Semestre 5 es: " +str(totalCreditinNSemester))
    elif(semestern.get()=='6'):
        for r in ListaCursos:
            if(r.Semester=='6'):
                if(r.Status=='0'):
                    credit =int(r.Credits)
                    sumApprovedN=sumApprovedN+credit
                elif(r.Status=='1'):
                    credit1 =int(r.Credits)
                    sumTakingN=sumTakingN+credit1
                elif(r.Status=='-1'):
                    credit2 =int(r.Credits)
                    sumPendingN=sumPendingN+credit2
        totalCreditinNSemester = sumApprovedN+sumTakingN+sumPendingN
        sendDataCredit.set(totalCreditinNSemester)
        print()
        print("El Total de creditos Aprobados es: ",sumApprovedN)
        print("El Total de creditos Cursando es: ",sumTakingN)
        print("El Total de creditos Pendientes es: ",sumPendingN)
        print("Total de Créditos en Semestre 6 es: " +str(totalCreditinNSemester))
    elif(semestern.get()=='7'):
        for r in ListaCursos:
            if(r.Semester=='7'):
                if(r.Status=='0'):
                    credit =int(r.Credits)
                    sumApprovedN=sumApprovedN+credit
                elif(r.Status=='1'):
                    credit1 =int(r.Credits)
                    sumTakingN=sumTakingN+credit1
                elif(r.Status=='-1'):
                    credit2 =int(r.Credits)
                    sumPendingN=sumPendingN+credit2
        totalCreditinNSemester = sumApprovedN+sumTakingN+sumPendingN
        sendDataCredit.set(totalCreditinNSemester)
        print()
        print("El Total de creditos Aprobados es: ",sumApprovedN)
        print("El Total de creditos Cursando es: ",sumTakingN)
        print("El Total de creditos Pendientes es: ",sumPendingN)
        print("Total de Créditos en Semestre 7 es: " +str(totalCreditinNSemester))
    elif(semestern.get()=='8'):
        for r in ListaCursos:
            if(r.Semester=='8'):
                if(r.Status=='0'):
                    credit =int(r.Credits)
                    sumApprovedN=sumApprovedN+credit
                elif(r.Status=='1'):
                    credit1 =int(r.Credits)
                    sumTakingN=sumTakingN+credit1
                elif(r.Status=='-1'):
                    credit2 =int(r.Credits)
                    sumPendingN=sumPendingN+credit2
        totalCreditinNSemester = sumApprovedN+sumTakingN+sumPendingN
        sendDataCredit.set(totalCreditinNSemester)
        print()
        print("El Total de creditos Aprobados es: ",sumApprovedN)
        print("El Total de creditos Cursando es: ",sumTakingN)
        print("El Total de creditos Pendientes es: ",sumPendingN)
        print("Total de Créditos en Semestre 8 es: " +str(totalCreditinNSemester))
    elif(semestern.get()=='9'):
        for r in ListaCursos:
            if(r.Semester=='9'):
                if(r.Status=='0'):
                    credit =int(r.Credits)
                    sumApprovedN=sumApprovedN+credit
                elif(r.Status=='1'):
                    credit1 =int(r.Credits)
                    sumTakingN=sumTakingN+credit1
                elif(r.Status=='-1'):
                    credit2 =int(r.Credits)
                    sumPendingN=sumPendingN+credit2
        totalCreditinNSemester = sumApprovedN+sumTakingN+sumPendingN
        sendDataCredit.set(totalCreditinNSemester)
        print()
        print("El Total de creditos Aprobados es: ",sumApprovedN)
        print("El Total de creditos Cursando es: ",sumTakingN)
        print("El Total de creditos Pendientes es: ",sumPendingN)
        print("Total de Créditos en Semestre 9 es: " +str(totalCreditinNSemester))
    elif(semestern.get()=='10'):
        for r in ListaCursos:
            if(r.Semester=='10'):
                if(r.Status=='0'):
                    credit =int(r.Credits)
                    sumApprovedN=sumApprovedN+credit
                elif(r.Status=='1'):
                    credit1 =int(r.Credits)
                    sumTakingN=sumTakingN+credit1
                elif(r.Status=='-1'):
                    credit2 =int(r.Credits)
                    sumPendingN=sumPendingN+credit2
        totalCreditinNSemester = sumApprovedN+sumTakingN+sumPendingN
        sendDataCredit.set(totalCreditinNSemester)
        print()
        print("El Total de creditos Aprobados es: ",sumApprovedN)
        print("El Total de creditos Cursando es: ",sumTakingN)
        print("El Total de creditos Pendientes es: ",sumPendingN)
        print("Total de Créditos en Semestre 10 es: " +str(totalCreditinNSemester))

def CrediCountNSemesterObligatory():
    global semester
    global sendDataCreditN
    global ListaCursos
    sumObligatory1=0
    sumObligatory2=0
    sumObligatory3=0
    sumObligatory4=0
    sumObligatory5=0
    sumObligatory6=0
    sumObligatory7=0
    sumObligatory8=0
    sumObligatory9=0
    sumObligatory10=0

    if(semester.get()=='1'):
        for e in ListaCursos:
            if(e.Semester=='1'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory1=sumObligatory1+credit
        sendDataCreditN.set(sumObligatory1)
        print("")
        print("Los créditos hasta el semestre   " +  semester.get() + " son: " + str(sumObligatory1))
        sumObligatory1=0
    elif(semester.get()=='2'):
        for e in ListaCursos:
            if(e.Semester=='1'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory1=sumObligatory1+credit
            elif(e.Semester=='2'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory2=sumObligatory2+credit
        tot=sumObligatory1+sumObligatory2
        sendDataCreditN.set(tot)
        print("")
        print("Semestre 1: " + str(sumObligatory1))
        print("Semestre 2: " + str(sumObligatory2))
        print("Los créditos hasta el semestre   " +  semester.get() + " son: " + str(tot))
        sumObligatory1=0
        sumObligatory2=0
    elif(semester.get()=='3'):
        for e in ListaCursos:
            if(e.Semester=='1'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory1=sumObligatory1+credit
            elif(e.Semester=='2'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory2=sumObligatory2+credit
            elif(e.Semester=='3'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory3=sumObligatory3+credit
        tot=sumObligatory1+sumObligatory2+sumObligatory3
        sendDataCreditN.set(tot)
        print("")
        print("Semestre 1: " + str(sumObligatory1))
        print("Semestre 2: " + str(sumObligatory2))
        print("Semestre 3: " + str(sumObligatory3))
        print("Los créditos hasta el semestre   " +  semester.get() + " son: " + str(tot))
        sumObligatory1=0
        sumObligatory2=0
        sumObligatory3=0
    elif(semester.get()=='4'):
        for e in ListaCursos:
            if(e.Semester=='1'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory1=sumObligatory1+credit
            elif(e.Semester=='2'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory2=sumObligatory2+credit
            elif(e.Semester=='3'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory3=sumObligatory3+credit
            elif(e.Semester=='4'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory4=sumObligatory4+credit
        tot=sumObligatory1+sumObligatory2+sumObligatory3+sumObligatory4
        sendDataCreditN.set(tot)
        print("")
        print("Semestre 1: " + str(sumObligatory1))
        print("Semestre 2: " + str(sumObligatory2))
        print("Semestre 3: " + str(sumObligatory3))
        print("Semestre 4: " + str(sumObligatory4))
        print("Los créditos hasta el semestre   " +  semester.get() + " son: " + str(tot))
        sumObligatory1=0
        sumObligatory2=0
        sumObligatory3=0
        sumObligatory4=0
    elif(semester.get()=='5'):
        for e in ListaCursos:
            if(e.Semester=='1'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory1=sumObligatory1+credit
            elif(e.Semester=='2'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory2=sumObligatory2+credit
            elif(e.Semester=='3'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory3=sumObligatory3+credit
            elif(e.Semester=='4'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory4=sumObligatory4+credit
            elif(e.Semester=='5'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory5=sumObligatory5+credit
        tot=sumObligatory1+sumObligatory2+sumObligatory3+sumObligatory4+sumObligatory5
        sendDataCreditN.set(tot)
        print("")
        print("Semestre 1: " + str(sumObligatory1))
        print("Semestre 2: " + str(sumObligatory2))
        print("Semestre 3: " + str(sumObligatory3))
        print("Semestre 4: " + str(sumObligatory4))
        print("Semestre 5: " + str(sumObligatory5))
        print("Los créditos hasta el semestre   " +  semester.get() + " son: " + str(tot))
        sumObligatory1=0
        sumObligatory2=0
        sumObligatory3=0
        sumObligatory4=0
        sumObligatory5=0
    elif(semester.get()=='6'):
        for e in ListaCursos:
            if(e.Semester=='1'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory1=sumObligatory1+credit
            elif(e.Semester=='2'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory2=sumObligatory2+credit
            elif(e.Semester=='3'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory3=sumObligatory3+credit
            elif(e.Semester=='4'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory4=sumObligatory4+credit
            elif(e.Semester=='5'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory5=sumObligatory5+credit
            elif(e.Semester=='6'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory6=sumObligatory6+credit
        tot=sumObligatory1+sumObligatory2+sumObligatory3+sumObligatory4+sumObligatory5+sumObligatory6
        sendDataCreditN.set(tot)
        print("")
        print("Semestre 1: " + str(sumObligatory1))
        print("Semestre 2: " + str(sumObligatory2))
        print("Semestre 3: " + str(sumObligatory3))
        print("Semestre 4: " + str(sumObligatory4))
        print("Semestre 5: " + str(sumObligatory5))
        print("Semestre 6: " + str(sumObligatory6))
        print("Los créditos hasta el semestre   " +  semester.get() + " son: " + str(tot))
        sumObligatory1=0
        sumObligatory2=0
        sumObligatory3=0
        sumObligatory4=0
        sumObligatory5=0
        sumObligatory6=0
    elif(semester.get()=='7'):
        for e in ListaCursos:
            if(e.Semester=='1'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory1=sumObligatory1+credit
            elif(e.Semester=='2'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory2=sumObligatory2+credit
            elif(e.Semester=='3'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory3=sumObligatory3+credit
            elif(e.Semester=='4'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory4=sumObligatory4+credit
            elif(e.Semester=='5'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory5=sumObligatory5+credit
            elif(e.Semester=='6'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory6=sumObligatory6+credit
            elif(e.Semester=='7'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory7=sumObligatory7+credit
        tot=sumObligatory1+sumObligatory2+sumObligatory3+sumObligatory4+sumObligatory5+sumObligatory6+sumObligatory7
        sendDataCreditN.set(tot)
        print("")
        print("Semestre 1: " + str(sumObligatory1))
        print("Semestre 2: " + str(sumObligatory2))
        print("Semestre 3: " + str(sumObligatory3))
        print("Semestre 4: " + str(sumObligatory4))
        print("Semestre 5: " + str(sumObligatory5))
        print("Semestre 6: " + str(sumObligatory6))
        print("Semestre 7: " + str(sumObligatory7))
        print("Los créditos hasta el semestre   " +  semester.get() + " son: " + str(tot))
        sumObligatory1=0
        sumObligatory2=0
        sumObligatory3=0
        sumObligatory4=0
        sumObligatory5=0
        sumObligatory6=0
        sumObligatory7=0
    elif(semester.get()=='8'):
        for e in ListaCursos:
            if(e.Semester=='1'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory1=sumObligatory1+credit
            elif(e.Semester=='2'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory2=sumObligatory2+credit
            elif(e.Semester=='3'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory3=sumObligatory3+credit
            elif(e.Semester=='4'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory4=sumObligatory4+credit
            elif(e.Semester=='5'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory5=sumObligatory5+credit
            elif(e.Semester=='6'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory6=sumObligatory6+credit
            elif(e.Semester=='7'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory7=sumObligatory7+credit
            elif(e.Semester=='8'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory8=sumObligatory8+credit
        tot=sumObligatory1+sumObligatory2+sumObligatory3+sumObligatory4+sumObligatory5+sumObligatory6+sumObligatory7+sumObligatory8
        sendDataCreditN.set(tot)
        print("")
        print("Semestre 1: " + str(sumObligatory1))
        print("Semestre 2: " + str(sumObligatory2))
        print("Semestre 3: " + str(sumObligatory3))
        print("Semestre 4: " + str(sumObligatory4))
        print("Semestre 5: " + str(sumObligatory5))
        print("Semestre 6: " + str(sumObligatory6))
        print("Semestre 7: " + str(sumObligatory7))
        print("Semestre 8: " + str(sumObligatory8))
        print("Los créditos hasta el semestre   " +  semester.get() + " son: " + str(tot))
        sumObligatory1=0
        sumObligatory2=0
        sumObligatory3=0
        sumObligatory4=0
        sumObligatory5=0
        sumObligatory6=0
        sumObligatory7=0
        sumObligatory8=0
    elif(semester.get()=='9'):
        for e in ListaCursos:
            if(e.Semester=='1'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory1=sumObligatory1+credit
            elif(e.Semester=='2'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory2=sumObligatory2+credit
            elif(e.Semester=='3'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory3=sumObligatory3+credit
            elif(e.Semester=='4'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory4=sumObligatory4+credit
            elif(e.Semester=='5'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory5=sumObligatory5+credit
            elif(e.Semester=='6'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory6=sumObligatory6+credit
            elif(e.Semester=='7'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory7=sumObligatory7+credit
            elif(e.Semester=='8'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory8=sumObligatory8+credit
            elif(e.Semester=='9'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory9=sumObligatory9+credit
        tot=sumObligatory1+sumObligatory2+sumObligatory3+sumObligatory4+sumObligatory5+sumObligatory6+sumObligatory7+sumObligatory8+sumObligatory9
        sendDataCreditN.set(tot)
        print("")
        print("Semestre 1: " + str(sumObligatory1))
        print("Semestre 2: " + str(sumObligatory2))
        print("Semestre 3: " + str(sumObligatory3))
        print("Semestre 4: " + str(sumObligatory4))
        print("Semestre 5: " + str(sumObligatory5))
        print("Semestre 6: " + str(sumObligatory6))
        print("Semestre 7: " + str(sumObligatory7))
        print("Semestre 8: " + str(sumObligatory8))
        print("Semestre 9: " + str(sumObligatory9))
        print("Los créditos hasta el semestre   " +  semester.get() + " son: " + str(tot))
        sumObligatory1=0
        sumObligatory2=0
        sumObligatory3=0
        sumObligatory4=0
        sumObligatory5=0
        sumObligatory6=0
        sumObligatory7=0
        sumObligatory8=0
        sumObligatory9=0
    elif(semester.get()=='10'):
        for e in ListaCursos:
            if(e.Semester=='1'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory1=sumObligatory1+credit
            elif(e.Semester=='2'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory2=sumObligatory2+credit
            elif(e.Semester=='3'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory3=sumObligatory3+credit
            elif(e.Semester=='4'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory4=sumObligatory4+credit
            elif(e.Semester=='5'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory5=sumObligatory5+credit
            elif(e.Semester=='6'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory6=sumObligatory6+credit
            elif(e.Semester=='7'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory7=sumObligatory7+credit
            elif(e.Semester=='8'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory8=sumObligatory8+credit
            elif(e.Semester=='9'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory9=sumObligatory9+credit
            elif(e.Semester=='10'):
                if(e.Optionality=='1'):
                    credit =int(e.Credits)
                    sumObligatory10=sumObligatory10+credit
        tot=sumObligatory1+sumObligatory2+sumObligatory3+sumObligatory4+sumObligatory5+sumObligatory6+sumObligatory7+sumObligatory8+sumObligatory9+sumObligatory10
        sendDataCreditN.set(tot)
        print("")
        print("Semestre 1: " + str(sumObligatory1))
        print("Semestre 2: " + str(sumObligatory2))
        print("Semestre 3: " + str(sumObligatory3))
        print("Semestre 4: " + str(sumObligatory4))
        print("Semestre 5: " + str(sumObligatory5))
        print("Semestre 6: " + str(sumObligatory6))
        print("Semestre 7: " + str(sumObligatory7))
        print("Semestre 8: " + str(sumObligatory8))
        print("Semestre 9: " + str(sumObligatory9))
        print("Semestre 10: " + str(sumObligatory10))
        print("Los créditos hasta el semestre   " +  semester.get() + " son: " + str(tot))
        sumObligatory1=0
        sumObligatory2=0
        sumObligatory3=0
        sumObligatory4=0
        sumObligatory5=0
        sumObligatory6=0
        sumObligatory7=0
        sumObligatory8=0
        sumObligatory9=0
        sumObligatory10=0

def window_creditcount():
    global semester
    global semestern
    global sendDataCredit
    global sendDataCreditN
    global totalCreditinNSemester
    global textboxCreditsSemester
    global ListaCursos
    global wndw_credicount
    global wndw_menu
    wndw_menu.destroy()
    #Configuración ventana lista de cursos
    wndw_credicount = tk.Tk()
    wndw_credicount.title("Conteo de Créditos")
    wndw_credicount.resizable(0,0)
    wndw_credicount.iconbitmap("img/credit.ico")
    wndw_credicount.geometry("820x580")
    wndw_credicount.config(bg="#48F1D8")
    wndw_credicount.config(bd=30)
    wndw_credicount.config(relief="groove")

    #Función para el conteo de creditos
    sumApproved=0
    sumTaking=0
    sumPending=0
    for r in ListaCursos:
        if(r.Status=='0'):
            credit =int(r.Credits)
            sumApproved=sumApproved+credit
        elif(r.Status=='1'):
            credit1 =int(r.Credits)
            sumTaking=sumTaking+credit1
        elif(r.Status=='-1'):
            credit2 =int(r.Credits)
            sumPending=sumPending+credit2
    print()
    print("El Total de creditos Aprobados es: ",sumApproved)
    print("El Total de creditos Cursando es: ",sumTaking)
    print("El Total de creditos Pendientes es: ",sumPending)

    #Función para el conteo de 
    
    # one ='1'
    # two ='2'
    # three ='3'
    # four ='4'
    # five ='5'
    # six ='6'
    # seven ='7'
    # eight ='8'
    # nine ='9'
    # ten='10'
    # one,two,three,four,five,six,seven,eight,nine,ten



    #Configuraciones Labels
    labelApprovedCredits=Label(wndw_credicount,text="Créditos Aprobados:",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelApprovedCredits.place(x=20,y=50)

    labelApprovedCreditss=Label(wndw_credicount,fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelApprovedCreditss.place(x=250,y=50)
    labelApprovedCreditss.configure(text=sumApproved)

    labelTakingCredits=Label(wndw_credicount,text="Créditos Cursando:",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelTakingCredits.place(x=20,y=90)

    labelTakingCreditss=Label(wndw_credicount,fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelTakingCreditss.place(x=250,y=90)
    labelTakingCreditss.configure(text=sumTaking)

    labelPendingCredits=Label(wndw_credicount,text="Créditos Pendientes:",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelPendingCredits.place(x=20,y=130)
    
    labelPendingCreditss=Label(wndw_credicount,fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelPendingCreditss.place(x=270,y=130)
    labelPendingCreditss.configure(text=sumPending)

    labelrequiredCredits=Label(wndw_credicount,text="Créditos Obligatarios hasta semestre N:",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelrequiredCredits.place(x=20,y=170)

    labelSemester=Label(wndw_credicount,text="Semestre",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelSemester.place(x=60,y=220)

    labelCreditsSemester=Label(wndw_credicount,text="Créditos del semestre:",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelCreditsSemester.place(x=20,y=280)

    labelCreditsSemester=Label(wndw_credicount,text="SemestreN",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelCreditsSemester.place(x=60,y=340)


    #Configuracion textbox
    sendDataCreditN=StringVar()
    textboxNrequiredCredits=Entry(wndw_credicount,text=sendDataCreditN,state=DISABLED,justify='center',font=("Courier 15 bold"))
    textboxNrequiredCredits.place(x=500,y=170,width=100,height=30)
    
    sendDataCredit=StringVar()
    textboxCreditsSemester=Entry(wndw_credicount,text=sendDataCredit,state=DISABLED,justify='center',font=("Courier 15 bold"))
    textboxCreditsSemester.place(x=300,y=280,width=100,height=30)
    
    #Configuración SpinBox
    semester =StringVar()
    semestern=StringVar()

    spinBoxSemester= Spinbox(wndw_credicount,textvariable=semester,values=("1","2","3","4","5","6","7","8","9","10"),font=("Courier 15 bold"))
    spinBoxSemester.place(x=190,y=220,width=50,height=30)

    spinBoxCreditsSemester= Spinbox(wndw_credicount,textvariable=semestern,values=("1","2","3","4","5","6","7","8","9","10"),font=("Courier 15 bold"))
    spinBoxCreditsSemester.place(x=190,y=340,width=50,height=30)
    

    #Configuración botones
    buttonBackManageCouurse=Button(wndw_credicount,text="Regresar",width=15,bg="#48F1D8", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackMainMenuFromCreditCount)
    buttonBackManageCouurse.place(x=575,y=460)

    buttonCountSemesters=Button(wndw_credicount,text="Contar",width=10,bg="#48F1D8", font=("Courier 11 bold"),relief="groove",bd=7,command=CrediCountNSemesterObligatory)
    buttonCountSemesters.place(x=280,y=213)

    buttonCreditsSemester=Button(wndw_credicount,text="Contar",width=10,bg="#48F1D8", font=("Courier 11 bold"),relief="groove",bd=7,command=CrediCountNsemester)
    buttonCreditsSemester.place(x=280,y=338)
    
    wndw_credicount.mainloop()


window_mainMenu()