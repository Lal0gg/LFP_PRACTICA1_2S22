

from tkinter import CENTER, ttk
import tkinter


#Configuración ventana lista de cursos
wndw_listcourse = tkinter.Tk()
wndw_listcourse.title("Listar Cursos")
wndw_listcourse.iconbitmap("img/list.ico")
wndw_listcourse.geometry("820x580")
wndw_listcourse.config(bg="#9EBCFF")
wndw_listcourse.config(bd=30)
wndw_listcourse.config(relief="groove")

TableListCourse= ttk.Treeview(wndw_listcourse,columns=("col1","col2","col3","col4","col5","col6"))
TableListCourse.column("#0",width=80)
TableListCourse.column("col1",width=80,anchor=CENTER)
TableListCourse.column("col2",width=80,anchor=CENTER)
TableListCourse.column("col3",width=80,anchor=CENTER)
TableListCourse.column("col4",width=80,anchor=CENTER)
TableListCourse.column("col5",width=80,anchor=CENTER)
TableListCourse.column("col6",width=80,anchor=CENTER)

TableListCourse.heading("#0",text="Código",anchor=CENTER)
TableListCourse.heading("col1",text="Nombre",anchor=CENTER)
TableListCourse.heading("col2",text="Pre Requisito",anchor=CENTER)
TableListCourse.heading("col3",text="Opcionalidad",anchor=CENTER)
TableListCourse.heading("col4",text="Semestre",anchor=CENTER)
TableListCourse.heading("col5",text="Créditos",anchor=CENTER)
TableListCourse.heading("col6",text="Estado",anchor=CENTER)
wndw_listcourse.mainloop()