import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview

wndw_menu = None
wndw_fileupload = None
wndw_managecourse = None
wndw_listcourse = None
wndw_addcourse = None
wndw_editcourse = None
wndw_deletecourse = None
wndw_credicount = None

ListaCursos=[]

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
    buttonSelectRoute=Button(wndw_fileupload,text="Seleccionar",width=11,bg="#C9A4F9", font=("Courier 13 bold"),relief="ridge",bd=8)
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
    buttonListCourses.place(x=250,y=70)

    buttonAddCourse=Button(wndw_managecourse,text="Agregar Curso",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=window_addcourse)
    buttonAddCourse.place(x=250,y=130)

    buttonEditCourse=Button(wndw_managecourse,text="Editar Curso",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=window_editcourse)
    buttonEditCourse.place(x=250,y=190)

    buttonDeleteCourse=Button(wndw_managecourse,text="Eliminar Curso",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=window_deleteCourse)
    buttonDeleteCourse.place(x=250,y=250)

    buttonBackmainmenu=Button(wndw_managecourse,text="Regresar",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackMainMenuFromManage)
    buttonBackmainmenu.place(x=250,y=310)
    wndw_managecourse.mainloop()

def window_listcouse():
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
    TableListCourse.pack()
    TableListCourse.place(x=20,y=35)

    #Configuración botones
    buttonBackManageCourse=Button(wndw_listcourse,text="Regresar",width=15,bg="#9EBCFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackManageCourseFromListCourse)
    buttonBackManageCourse.place(x=575,y=460)
    wndw_listcourse.mainloop()

def window_addcourse():
    global wndw_managecourse
    global wndw_addcourse
    wndw_managecourse.destroy()

    wndw_listcourse
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
    textboxCourseid=Entry(wndw_addcourse)
    textboxCourseid.place(x=265,y=55,width=370,height=25)
    
    textboxCoursename=Entry(wndw_addcourse)
    textboxCoursename.place(x=265,y=105,width=370,height=25)

    textboxCoursePreRequis=Entry(wndw_addcourse)
    textboxCoursePreRequis.place(x=265,y=155,width=370,height=25)

    textboxCourseSemester=Entry(wndw_addcourse)
    textboxCourseSemester.place(x=265,y=205,width=370,height=25)

    textboxCourseOptionality=Entry(wndw_addcourse)
    textboxCourseOptionality.place(x=265,y=255,width=370,height=25)

    textboxCourseCredits=Entry(wndw_addcourse)
    textboxCourseCredits.place(x=265,y=305,width=370,height=25)

    textboxCourseStatus=Entry(wndw_addcourse)
    textboxCourseStatus.place(x=265,y=355,width=370,height=25)
    
    #Configuración botones
    buttonBackManageCoursee=Button(wndw_addcourse,text="Regresar",width=12,bg="#C9A4F9", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackManageCourseFromAddCourse)
    buttonBackManageCoursee.place(x=610,y=465)

    buttonAddCourse=Button(wndw_addcourse,text="Agregar",width=15,bg="#C9A4F9", font=("Courier 13 bold"),relief="ridge",bd=7)
    buttonAddCourse.place(x=340,y=400)

    wndw_addcourse.mainloop()

def window_editcourse():
    global wndw_managecourse
    global wndw_editcourse
    wndw_managecourse.destroy()
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
    textboxEditCourseid=Entry(wndw_editcourse)
    textboxEditCourseid.place(x=265,y=55,width=370,height=25)
    
    textboxEditCoursename=Entry(wndw_editcourse)
    textboxEditCoursename.place(x=265,y=105,width=370,height=25)

    textboxEditCoursePreRequis=Entry(wndw_editcourse)
    textboxEditCoursePreRequis.place(x=265,y=155,width=370,height=25)

    textboxEditCourseSemester=Entry(wndw_editcourse)
    textboxEditCourseSemester.place(x=265,y=205,width=370,height=25)

    textboxEditCourseOptionality=Entry(wndw_editcourse)
    textboxEditCourseOptionality.place(x=265,y=255,width=370,height=25)

    textboxEditCourseCredits=Entry(wndw_editcourse)
    textboxEditCourseCredits.place(x=265,y=305,width=370,height=25)

    textboxEditCourseStatus=Entry(wndw_editcourse)
    textboxEditCourseStatus.place(x=265,y=355,width=370,height=25)
    
    #Configuración botones
    buttonBackManageCoursse=Button(wndw_editcourse,text="Regresar",width=12,bg="#E99EFF", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackManageCourseFromEditCourse)
    buttonBackManageCoursse.place(x=610,y=465)

    buttonEditCourse=Button(wndw_editcourse,text="Editar",width=15,bg="#E99EFF", font=("Courier 13 bold"),relief="ridge",bd=7)
    buttonEditCourse.place(x=340,y=400)
    wndw_editcourse.mainloop()

def window_deleteCourse():
    global wndw_managecourse
    global wndw_deletecourse
    wndw_managecourse.destroy()
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
    textboxidCourse=Entry(wndw_deletecourse)
    textboxidCourse.place(x=250,y=84,width=360,height=24)
    #Configuración Botones
    buttonDeleteCourse=Button(wndw_deletecourse,text="Eliminar",width=11,bg="#AFF5FF", font=("Courier 13 bold"),relief="ridge",bd=8)
    buttonDeleteCourse.place(x=360,y=130)

    buttonBackManageCourssee=Button(wndw_deletecourse,text="Regresar",width=11,bg="#AFF5FF", font=("Courier 13 bold"),relief="ridge",bd=8,command=getBackManageCourseFromDeleteCourse)
    buttonBackManageCourssee.place(x=520,y=235)
    wndw_deletecourse.mainloop()

def window_creditcount():
    global wndw_credicount
    global wndw_menu
    wndw_menu.destroy()
    #Configuración ventana lista de cursos
    wndw_credicount = tk.Tk()
    wndw_credicount.title("Conteo de Créditos")
    wndw_credicount.iconbitmap("img/credit.ico")
    wndw_credicount.geometry("820x580")
    wndw_credicount.config(bg="#48F1D8")
    wndw_credicount.config(bd=30)
    wndw_credicount.config(relief="groove")
    
    #Configuraciones Labels
    labelApprovedCredits=Label(wndw_credicount,text="Créditos Aprobados:",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelApprovedCredits.place(x=20,y=50)

    labelApprovedCreditss=Label(wndw_credicount,text="XX",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelApprovedCreditss.place(x=250,y=50)

    labelTakingCredits=Label(wndw_credicount,text="Créditos Cursando:",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelTakingCredits.place(x=20,y=90)

    labelTakingCreditss=Label(wndw_credicount,text="XX",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelTakingCreditss.place(x=250,y=90)

    labelPendingCredits=Label(wndw_credicount,text="Créditos Pendientes:",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelPendingCredits.place(x=20,y=130)

    labelPendingCreditss=Label(wndw_credicount,text="XX",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelPendingCreditss.place(x=270,y=130)

    labelrequiredCredits=Label(wndw_credicount,text="Créditos Obligatarios hasta semestre N:",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelrequiredCredits.place(x=20,y=170)

    labelSemester=Label(wndw_credicount,text="Semestre",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelSemester.place(x=60,y=220)

    labelCreditsSemester=Label(wndw_credicount,text="Créditos del semestre:",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelCreditsSemester.place(x=20,y=280)

    labelCreditsSemester=Label(wndw_credicount,text="Semestre",fg="black",font=("Courier 15 bold"),bg="#48F1D8")
    labelCreditsSemester.place(x=60,y=340)


    #Configuracion textbox
    textboxNrequiredCredits=Entry(wndw_credicount)
    textboxNrequiredCredits.place(x=500,y=170,width=100,height=30)

    textboxCreditsSemester=Entry(wndw_credicount)
    textboxCreditsSemester.place(x=300,y=280,width=100,height=30)

    #Configuración SpinBox
    spinBoxSemester= Spinbox(wndw_credicount,from_=0, to=10,font=("Courier 15 bold"))
    spinBoxSemester.place(x=190,y=220,width=50,height=30)

    spinBoxCreditsSemester= Spinbox(wndw_credicount,from_=0, to=10,font=("Courier 15 bold"))
    spinBoxCreditsSemester.place(x=190,y=340,width=50,height=30)

    #Configuración botones
    buttonBackManageCouurse=Button(wndw_credicount,text="Regresar",width=15,bg="#48F1D8", font=("Courier 13 bold"),relief="ridge",bd=7,command=getBackMainMenuFromCreditCount)
    buttonBackManageCouurse.place(x=575,y=460)

    buttonCountSemesters=Button(wndw_credicount,text="Contar",width=10,bg="#48F1D8", font=("Courier 11 bold"),relief="groove",bd=7)
    buttonCountSemesters.place(x=280,y=213)

    buttonCreditsSemester=Button(wndw_credicount,text="Contar",width=10,bg="#48F1D8", font=("Courier 11 bold"),relief="groove",bd=7)
    buttonCreditsSemester.place(x=280,y=338)

    wndw_credicount.mainloop()




window_mainMenu()
