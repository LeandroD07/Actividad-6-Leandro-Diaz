from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import pymysql

global guardar, dni_1
guardar="sin valor"





def InicioSesion():
	global ventana1
	ventana1=Tk()
	ventana1.title("Bibloteca")
	btn_inicio = Button(ventana1,text="Iniciar Sesion",command=v1_a_v2,height="1",width="20",bg="#2214b9",fg="white")
	btn_inicio.pack()
	btn_inicio.place(x=175,y=200)
	
	
	
	
	
	imagen_net= Image.open("Imágenes/net.gif") 
	resized= imagen_net.resize((270,170))
	imagen_net=ImageTk.PhotoImage(resized)
	label_net=Label(ventana1, image=imagen_net)
	label_net.pack()
	label_net.place(x=115,y=15)

	
	
	w = 500
	h = 250
	ws = ventana1.winfo_screenwidth()
	hs = ventana1.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
	mainloop()










def Login():
	global ventana2
	ventana2=Tk()
	ventana2.title("Bibloteca")

	btn_registro= Button(ventana2,text="Registrate",height="1",width="20",bg="#2214b9",fg="white",command=venlog_venr)
	btn_registro.pack()
	btn_registro.place(x=55,y=220)

	def iniciosesion():
		bd=pymysql.connect(host="localhost",user="root",passwd="",db="sistema_gestion_libreria")
		fcursor=bd.cursor()



		fcursor.execute("SELECT Usuario FROM admin WHERE Usuario='"+usuario.get()+"'and contrasena='"+pasw.get()+"'")

		if fcursor.fetchall():
			v2_v3()
		else:
			messagebox.showwarning("Inicio Sesion" ,"No se a podido iniciar sesion correctamente")
		bd.close()

		
		

	imagen_logo= Image.open("Imágenes/logo_ProA.jpg") 
	resized= imagen_logo.resize((200,200))
	imagen_logo=ImageTk.PhotoImage(resized)
	label=Label(ventana2, image=imagen_logo).place(x=275,y=15)
	
	usuario= StringVar()
	entry_usuario=Entry(ventana2,textvariable=usuario)
	entry_usuario.pack()
	entry_usuario.place(x=100,y=50)

	lbl_usuario = Label(ventana2,text="Usuario:")
	lbl_usuario.pack()
	lbl_usuario.place(x=20,y=50)
	
	pasw= StringVar()
	entry_pass=Entry(ventana2,textvariable=pasw,show="•")
	entry_pass.pack()
	entry_pass.place(x=100,y=90)

	lbl_pass = Label(ventana2,text="Contraseña:")
	lbl_pass.pack()
	lbl_pass.place(x=20,y=90)
	
	w = 500
	h = 260
	ws = ventana2.winfo_screenwidth()
	hs = ventana2.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana2.geometry('%dx%d+%d+%d' % (w, h, x, y))

    		
	
	btn_siguiente= Button(ventana2,text="Siguiente",height="1",width="20",bg="#2214b9",fg="white",command=iniciosesion)
	btn_siguiente.pack()
	btn_siguiente.place(x=55,y=180)

	
	mainloop()

def registrar():
	global ventanareg
	ventanareg=Tk()
	ventanareg.title("Bibloteca")

	btn_Registrate= Button(ventanareg,text="Registrate", default=DISABLED)
	btn_Registrate.pack()
	btn_Registrate.place(x=0,y=180)
	
	w = 250
	h = 250
	ws = ventanareg.winfo_screenwidth()
	hs = ventanareg.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventanareg.geometry('%dx%d+%d+%d' % (w, h, x, y))



	mail = StringVar()
	entry_email=Entry(ventanareg,textvariable=mail,width="15")
	entry_email.pack()
	entry_email.place(x=115,y=50)

	lbl_email = Label(ventanareg,text="Correo:")
	lbl_email.pack()
	lbl_email.place(x=35,y=50)

	usuarior = StringVar()
	entry_usuarior=Entry(ventanareg,textvariable=usuarior,width="15")
	entry_usuarior.pack()
	entry_usuarior.place(x=115,y=10)

	lbl_usuarior = Label(ventanareg,text="Usuario:")
	lbl_usuarior.pack()
	lbl_usuarior.place(x=35,y=10)

	contraseña= StringVar()
	entry_passnue=Entry(ventanareg,textvariable=contraseña,show="•",width="15")
	entry_passnue.pack()
	entry_passnue.place(x=115,y=90)

	lbl_passnue = Label(ventanareg,text="Contraseña:")
	lbl_passnue.pack()
	lbl_passnue.place(x=35,y=90)

	def comp_register():  
		if usuarior.get()=="":
			messagebox.showinfo("Faltan Datos", "Ingrese usuario")
			entry_usuarior.focus()
			return

		if mail.get()=="":
			messagebox.showinfo("Faltan Datos", "Ingrese mail")
			entry_email.focus()
			return

		if contraseña.get()=="":
			messagebox.showinfo("Faltan Datos", "Ingrese contraseña")
			entry_passnue.focus()
			return
			
		else:
			bd=pymysql.connect(host="localhost",user="root",passwd="",db="sistema_gestion_libreria")
			fcursor=bd.cursor()
			sql="INSERT INTO admin (usuario, mail, contrasena) VALUES('{0}','{1}','{2}')".format(usuarior.get(), mail.get(), contraseña.get())
			try:
				fcursor.execute(sql)
				bd.commit()
				completar_reg=messagebox.showinfo("Registro","Usuario Registrado Correctamente")
				if completar_reg==messagebox.OK:
					venreg_venlog()
			except:
				bd.rollback()
				messagebox.showinfo("Registro","Usuario no se a podido registrar correctamente")
				
	btn_registrar = Button(ventanareg,text="Registrar",command=comp_register,height="1",width="20",bg="#2214b9",fg="white")
	btn_registrar.pack()
	btn_registrar.place(x=50,y=170)





def secciones():
	global ventana3
	ventana3=Tk()
	ventana3.title("Seleccion")


	w = 350
	h = 200
	ws = ventana3.winfo_screenwidth()
	hs = ventana3.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana3.geometry('%dx%d+%d+%d' % (w, h, x, y))

	btn_irC= Button(ventana3,text="Cliente",height="1",width="20",bg="#2214b9",fg="white",command=Vop_Vcre)
	btn_irC.pack()
	btn_irC.place(x=20,y=20)

	btn_irL= Button(ventana3,text="Libro",height="1",width="20",bg="#2214b9",fg="white",command=selec_libro)
	btn_irL.pack()
	btn_irL.place(x=180,y=20)

	btn_irAL= Button(ventana3,text="Alquileres",height="1",width="20",bg="#2214b9",fg="white")
	btn_irAL.pack()
	btn_irAL.place(x=20,y=80)

	btn_irAD= Button(ventana3,text="Administradores",height="1",width="20",bg="#2214b9",fg="white")
	btn_irAD.pack()
	btn_irAD.place(x=180,y=80)

	btn_irS= Button(ventana3,text="Salir",height="1",width="20",bg="#b91414",fg="white")
	btn_irS.pack()
	btn_irS.place(x=100,y=150)

	mainloop()







	
def cliente():
	global guardar
	global ventanacliente
	ventanacliente=Tk()
	ventanacliente.title("Seleccion")


	w =750
	h =600
	ws = ventanacliente.winfo_screenwidth()
	hs = ventanacliente.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventanacliente.geometry('%dx%d+%d+%d' % (w, h, x, y))

	label_flame=ttk.Labelframe(ventanacliente,width=715, height=100,text="Consulta")
	label_flame.pack()
	label_flame.place(x=18,y=470)

	def cargar_tabla_clientes ():
			conexionbd=pymysql.connect(host="localhost",user="root",passwd="",db="sistema_gestion_libreria")
			fcursor=conexionbd.cursor()
			fcursor.execute ("SELECT * FROM cliente")

			for item in grid.get_children():
				grid.delete(item)

			for row in fcursor:
				grid.insert("", 0, text=row[0],values=(row[1],row[2],row[3],row[4]))
			conexionbd.close()
	def creacion():
		global guardar
		print(guardar)
		if guardar == "nuevo":
			if apellido.get()== "":
				messagebox.showinfo("Faltan Datos", "Ingrese Apellido")
				print("error")
				entry_apellido.focus()
				return
			ap=apellido.get()
			if ap.isdigit() == True:
				messagebox.showinfo("Datos Erroneos","Su apellido solo puede contener letras")
			
			if nombre.get()== "":
				messagebox.showinfo("Faltan Datos", "Ingrese Nombre")
				entry_nombre.focus()
				return
			nom=nombre.get()
			if nom.isdigit() == True:
				messagebox.showinfo("Datos Erroneos","Su nombre solo puede contener letras")

			if dnicli.get()== "":
				messagebox.showinfo("Faltan Datos", "Ingrese DNI")
				entry_dnicli.focus()
				return
			dni_ = dnicli.get()

			if len(dni_) != 8:
				messagebox.showinfo("Datos Incorrectos","Ingrese su DNI correctamente")
				return

			if dni_.isdigit() == False:
				messagebox.showinfo("Datos Erroneos","Su DNI solo puede contener numeros")

			if seleccioncli.get()==0:
				messagebox.showinfo("Datos Erroneos","Diga si es socio")
				return

			asociado = ""
		
			if seleccioncli.get() == 1:
				asociado = "Si"
			if seleccioncli.get() == 2:
				asociado = "No"
			conexionbd=pymysql.connect(host="localhost",user="root",passwd="",db="sistema_gestion_libreria")
			fcursor=conexionbd.cursor()
			fcursor.execute ("SELECT DNI FROM cliente WHERE DNI ='" + dnicli.get() +"' ")

			if fcursor.fetchall():
				messagebox.showinfo("Cliente", "Usuario ya registrado verificar DNI")
			else:
				sql= "INSERT INTO cliente (nombre,apellido,DNI,Socio) VALUES ('{0}','{1}','{2}','{3}')".format(apellido.get(),nombre.get(),dnicli.get(),asociado)
				fcursor.execute (sql)
				conexionbd.commit()
				messagebox.showinfo("Datos Correctos","El cliente se registro correctamente")
				conexionbd.close()
				guardar = "sin valor"
				cargar_tabla_clientes()
				normalidad()
	
		if guardar == "modificar":
			selected=grid.focus()
			id_select=grid.item(selected,'text')
			print("nashe",id_select)

	
	def nuevo():
		global guardar
		guardar = "nuevo"
		entry_apellido.config(state=NORMAL)
		entry_nombre.config(state=NORMAL)
		entry_dnicli.config(state=NORMAL)
		rbtn_nocli.config(state=NORMAL)
		rbtn_sicli.config(state=NORMAL)


	def limpiar():
		apellido.set("")
		nombre.set("")
		dnicli.set("")
		seleccioncli.set("0")
	def normalidad():
		apellido.set("")
		nombre.set("")
		dnicli.set("")
		seleccioncli.set("0")
		entry_apellido.config(state=DISABLED)
		entry_nombre.config(state=DISABLED)
		entry_dnicli.config(state=DISABLED)
		rbtn_nocli.config(state=DISABLED)
		rbtn_sicli.config(state=DISABLED)
	
	#_______________Borrar Casilla de grid______________________

	
	def borrar():
		selected=grid.focus()
		id_seleccion= grid.item(selected,'text')
		print("asdas: "+ str(id_seleccion))
		if id_seleccion == '': 
			messagebox.showwarning('Borrar','Bebes seleccionar un cliente')
		else:
			valores=grid.item(selected, 'values')
			dato=valores [0] + " " + valores [1] + ",DNI: " + valores [2]
			respuesta=messagebox.askquestion("Borrar","Estas seguro de que decea borrar a: "+ dato)
			
		

			if respuesta==messagebox.YES:
				conexion=pymysql.connect(host="localhost", user="root", passwd="", db="sistema_gestion_libreria")
				fcursor=conexion.cursor()
				sql="DELETE FROM cliente WHERE id_cliente = {0}".format(id_seleccion)
				fcursor.execute(sql)
				conexion.commit()
				cargar_tabla_clientes()
				messagebox.showinfo("Borrar","Cliente eliminado correctamente")
			else:
				messagebox.showinfo("Borrar","Proceso de eliminacion cancelado")




	def volver1():
		ventanacliente.close()
		secciones()






	
			
			

				
	#_________________________Modificar______________________________
	def modificar_cli():
		global guardar, dni_1
		guardar="modificar"
		selectedmod=grid.focus()
		id_seleccion= grid.item(selectedmod,'text')
		dni_1 = dnicli.get()
		#bd=pymysql.connect(host="localhost", user="root", passwd="", db="sistema_gestion_libreria")
		#fcursor=bd.cursor()
		#fcursor.execute()
		#bd.commit()
		
		if id_seleccion == '': 
			messagebox.showwarning('Modificar','debes seleccionar un cliente')
		else:
			valores=grid.item(selectedmod, 'values')
			dato=valores [0] + " " + valores [1] + ",DNI: " + valores [2]
			respuesta=messagebox.askquestion("Modificar","Estas seguro de que decea modificar a: "+ dato)
			if respuesta==messagebox.YES:
				entry_apellido.config(state=NORMAL)
				entry_nombre.config(state=NORMAL)
				entry_dnicli.config(state=NORMAL)
				rbtn_nocli.config(state=NORMAL)
				rbtn_sicli.config(state=NORMAL)

				valores=grid.item(selectedmod,'values')
				

				apellido2=valores[0]
				nombre2=valores[1]
				dni2=valores[2]
				seleccionado2=valores[3]

				apellido.set(apellido2)
				nombre.set(nombre2)
				dnicli.set(dni2)
				
				if seleccionado2 == "si":
					seleccioncli.set(2)
				else:
					seleccioncli.set(1)
					



				
	#________________________________________________________________


	apellido = StringVar()
	entry_apellido=Entry(ventanacliente,textvariable=apellido,width="15",state=DISABLED)
	entry_apellido.pack()
	entry_apellido.place(x=130,y=50)

	lbl_apellido = Label(ventanacliente,text="apellido")
	lbl_apellido.pack()
	lbl_apellido.place(x=80,y=50)
	#------------------------------------------------------------------

	nombre= StringVar()
	entry_nombre=Entry(ventanacliente,textvariable=nombre,width="15",state=DISABLED)
	entry_nombre.pack()
	entry_nombre.place(x=310,y=50)

	lbl_nombre = Label(ventanacliente,text="Nombre")
	lbl_nombre.pack()
	lbl_nombre.place(x=250,y=50)

	#------------------------------------------------------------------
	idcli= StringVar()
	entry_idcli=Entry(ventanacliente,textvariable=idcli,width="5", state=DISABLED)
	entry_idcli.pack()
	entry_idcli.place(x=35,y=50)

	lbl_idcli = Label(ventanacliente,text="ID")
	lbl_idcli.pack()
	lbl_idcli.place(x=15,y=50)

	#-------------------------------------------------------------------

	dnicli= StringVar()
	entry_dnicli=Entry(ventanacliente,textvariable=dnicli,width="15",state=DISABLED)
	entry_dnicli.pack()
	entry_dnicli.place(x=470,y=50)

	lbl_dnicli = Label(ventanacliente,text="DNI")
	lbl_dnicli.pack()
	lbl_dnicli.place(x=430,y=50)

	#------------------------------------------------------------------

	lbl_sociocli = Label(ventanacliente,text="¿Socio?")
	lbl_sociocli.pack()
	lbl_sociocli.place(x=590,y=50)

	seleccioncli= IntVar()
	seleccioncli.set(0)

	rbtn_sicli=Radiobutton(ventanacliente,text="Si",value=1, variable = seleccioncli,state=DISABLED)
	rbtn_sicli.pack()
	rbtn_sicli.place(x=650,y=50)

	rbtn_nocli=Radiobutton(ventanacliente,text="No",value=2, variable = seleccioncli,state=DISABLED)
	rbtn_nocli.pack()
	rbtn_nocli.place(x=690,y=50)






	#------------------------------------------------------------------

	btn_nuevocli= Button(ventanacliente,text="🢀",height="1",width="4",bg="#2214b9",fg="white",command=cli_selec)
	btn_nuevocli.pack()
	btn_nuevocli.place(x=5,y=5)

	btn_nuevocli= Button(ventanacliente,text="Nuevo",height="1",width="10",bg="#2214b9",fg="white",command=nuevo)
	btn_nuevocli.pack()
	btn_nuevocli.place(x=100,y=10)

	btn_modificarcli= Button(ventanacliente,text="Modificar",height="1",width="10",bg="#2214b9",fg="white",command=modificar_cli)
	btn_modificarcli.pack()
	btn_modificarcli.place(x=220,y=10)

	btn_guardar= Button(ventanacliente,text="Guardar",height="1",width="10",bg="#3ab914",fg="white",command=creacion)
	btn_guardar.pack()
	btn_guardar.place(x=340,y=10)

	btn_limpiar= Button(ventanacliente,text="Limpiar",height="1",width="10",bg="#2214b9",fg="white",command=limpiar)
	btn_limpiar.pack()
	btn_limpiar.place(x=460,y=10)

	btn_borrar= Button(ventanacliente,text="Borrar",height="1",width="10",bg="#b91414",fg="white",command=borrar)
	btn_borrar.pack()
	btn_borrar.place(x=580,y=10)
	#-----------------------------------------------------------------------
	grid = ttk.Treeview(ventanacliente, columns=("col1", "col2", "col3", "col4"))

	grid.column("#0", width=50)
	grid.column("col1", width=140, anchor=CENTER)
	grid.column("col2", width=140, anchor=CENTER)
	grid.column("col3", width=140, anchor=CENTER)
	grid.column("col4", width=140, anchor=CENTER)

	grid.heading("#0", text="id", anchor=CENTER)
	grid.heading("col1", text="Apellido", anchor=CENTER)
	grid.heading("col2", text="Nombre", anchor=CENTER)
	grid.heading("col3", text="DNI", anchor=CENTER)
	grid.heading("col4", text="Socio", anchor=CENTER)

	grid.pack()
	grid.place(x=18, y=100, width=715, height=350)






	#-------------------------------------------------------------------------
	dni_buscar= StringVar()
	entry_dnibus=Entry(ventanacliente,textvariable=dni_buscar,width="15")
	entry_dnibus.pack()
	entry_dnibus.place(x=230,y=500)

	lbl_dnibus = Label(ventanacliente,text="DNI")
	lbl_dnibus.pack()
	lbl_dnibus.place(x=200,y=500)

	#-------------------------------------------------------------------------
	apellido_buscar= StringVar()
	entry_apellidobus=Entry(ventanacliente,textvariable=apellido_buscar,width="15")
	entry_apellidobus.pack()
	entry_apellidobus.place(x=90,y=500)

	lbl_apellidobus = Label(ventanacliente,text="Apellido")
	lbl_apellidobus.pack()
	lbl_apellidobus.place(x=30,y=500)
	#-------------------------------------------------------------------------
	lbl_sociobus = Label(ventanacliente,text="¿Socio?")
	lbl_sociobus.pack()
	lbl_sociobus.place(x=350,y=500)

	seleccionclibus= IntVar()
	seleccionclibus.set(0)

	rbtn_siclibus=Radiobutton(ventanacliente,text="Si",value=1, variable = seleccionclibus)
	rbtn_siclibus.pack()
	rbtn_siclibus.place(x=400,y=500)

	rbtn_noclibus=Radiobutton(ventanacliente,text="No",value=2, variable = seleccionclibus)
	rbtn_noclibus.pack()
	rbtn_noclibus.place(x=450,y=500)



	
	#-------------------------------------------------------------------------
	btn_bus= Button(ventanacliente,text="Buscar",height="1",width="20",bg="#2214b9",fg="white")
	btn_bus.pack()
	btn_bus.place(x=540,y=490)
	#-------------------------------------------------------------------------
	btn_limbus= Button(ventanacliente,text="Limpiar",height="1",width="20",bg="#2214b9",fg="white")
	btn_limbus.pack()
	btn_limbus.place(x=540,y=530)

	cargar_tabla_clientes()
	mainloop()

def libro ():
	global ventanalibro
	ventanalibro=Tk()
	ventanalibro.title("Libro")


	w =950
	h =600
	ws = ventanalibro.winfo_screenwidth()
	hs = ventanalibro.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventanalibro.geometry('%dx%d+%d+%d' % (w, h, x, y))

	btn_back= Button(ventanalibro,text="🢀",height="1",width="3",bg="#2214b9",fg="white",command=libro_selec)
	btn_back.pack()
	btn_back.place(x=5,y=5)

	label_flame2=ttk.Labelframe(ventanalibro,width= 930, height=100,text="Consulta")
	label_flame2.pack()
	label_flame2.place(x=10,y=475)

	grid = ttk.Treeview(ventanalibro, columns=("col1", "col2", "col3", "col4","col5","col6"))

	grid.column("#0", width=50)
	grid.column("col1", width=140, anchor=CENTER)
	grid.column("col2", width=140, anchor=CENTER)
	grid.column("col3", width=140, anchor=CENTER)
	grid.column("col4", width=140, anchor=CENTER)
	grid.column("col5", width=140, anchor=CENTER)
	grid.column("col6", width=140, anchor=CENTER)

	grid.heading("#0", text="id", anchor=CENTER)
	grid.heading("col1", text="Codigo", anchor=CENTER)
	grid.heading("col2", text="Titulo", anchor=CENTER)
	grid.heading("col3", text="Autor", anchor=CENTER)
	grid.heading("col4", text="Genero", anchor=CENTER)
	grid.heading("col5", text="Precio", anchor=CENTER)
	grid.heading("col6", text="Estado", anchor=CENTER)

	grid.pack()
	grid.place(x=18, y=100, width=910, height=350)

	codigo = StringVar()
	entry_codigo=Entry(ventanalibro,textvariable=codigo,width="15",state=DISABLED)
	entry_codigo.pack()
	entry_codigo.place(x=100,y=65)

	lbl_codigo = Label(ventanalibro,text="Codigo")
	lbl_codigo.pack()
	lbl_codigo.place(x=100,y=40)
	#------------------------------------------------------------------

	titulo= StringVar()
	entry_titulo=Entry(ventanalibro,textvariable=titulo,width="15",state=DISABLED)
	entry_titulo.pack()
	entry_titulo.place(x=225,y=65)

	lbl_titulo = Label(ventanalibro,text="Titulo")
	lbl_titulo.pack()
	lbl_titulo.place(x=225,y=40)

	#------------------------------------------------------------------
	idlibro= StringVar()
	entry_idlibro=Entry(ventanalibro,textvariable=idlibro,width="5", state=DISABLED)
	entry_idlibro.pack()
	entry_idlibro.place(x=35,y=65)

	lbl_ididlibro= Label(ventanalibro,text="ID")
	lbl_ididlibro.pack()
	lbl_ididlibro.place(x=35,y=40)

	#-------------------------------------------------------------------

	autor= StringVar()
	entry_autor=Entry(ventanalibro,textvariable=autor,width="15",state=DISABLED)
	entry_autor.pack()
	entry_autor.place(x=350,y=65)

	lbl_autor = Label(ventanalibro,text="Autor")
	lbl_autor.pack()
	lbl_autor.place(x=350,y=40)

	lbl_genero = Label(ventanalibro,text="Genero")
	lbl_genero.pack()
	lbl_genero.place(x=475,y=40)

	listaG=["Drama", "Terror", "Comedia"]
	genero= ttk.Combobox(ventanalibro, values=listaG, state=DISABLED)
	genero.set("Genéro")
	genero.pack()
	genero.place(x=475,y=65)

	lbl_estado = Label(ventanalibro,text="Estado")
	lbl_estado.pack()
	lbl_estado.place(x=650,y=40)

	listaE=["Reservado", "Disponible", "Baja"]
	estado= ttk.Combobox(ventanalibro, values=listaE,state=DISABLED)
	estado.set("Estado")
	estado.pack()
	estado.place(x=650,y=65)

	lbl_precio = Label(ventanalibro,text="Precio")
	lbl_precio.pack()
	lbl_precio.place(x=830,y=40)

	
	autor= StringVar()
	entry_autor=Entry(ventanalibro,textvariable=autor,width="15",state=DISABLED)
	entry_autor.pack()
	entry_autor.place(x=830,y=65)

	#--------------------------------------------------------------------------------------------

	btn_nuevo= Button(ventanalibro,text="Nuevo",height="1",width="10",bg="#2214b9",fg="white")
	btn_nuevo.pack()
	btn_nuevo.place(x=190,y=10)

	btn_modificar= Button(ventanalibro,text="Modificar",height="1",width="10",bg="#2214b9",fg="white")
	btn_modificar.pack()
	btn_modificar.place(x=310,y=10)

	btn_guardar= Button(ventanalibro,text="Guardar",height="1",width="10",bg="#3ab914",fg="white")
	btn_guardar.pack()
	btn_guardar.place(x=430,y=10)

	btn_limpiar= Button(ventanalibro,text="Limpiar",height="1",width="10",bg="#2214b9",fg="white")
	btn_limpiar.pack()
	btn_limpiar.place(x=550,y=10)

	btn_borrar= Button(ventanalibro,text="Borrar",height="1",width="10",bg="#b91414",fg="white")
	btn_borrar.pack()
	btn_borrar.place(x=670,y=10)
	#----------------------------------------------------------------------------------------------
	lbl_autorconsul = Label(ventanalibro,text="Autor")
	lbl_autorconsul.pack()
	lbl_autorconsul.place(x=300,y=500)

	autorconsul= StringVar()
	entry_autorconsul=Entry(ventanalibro,textvariable=autorconsul,width="15")
	entry_autorconsul.pack()
	entry_autorconsul.place(x=300,y=520)

	lbl_estadoconsul = Label(ventanalibro,text="Estado")
	lbl_estadoconsul.pack()
	lbl_estadoconsul.place(x=600,y=500)

	listaEconsul=["Reservado", "Disponible", "Baja"]
	estadoconsul= ttk.Combobox(ventanalibro, values=listaEconsul,state="readonly")
	estadoconsul.set("Estado")
	estadoconsul.pack()
	estadoconsul.place(x=600,y=520)

	codigoconsul = StringVar()
	entry_codigoconsul=Entry(ventanalibro,textvariable=codigoconsul,width="15")
	entry_codigoconsul.pack()
	entry_codigoconsul.place(x=50,y=520)

	lbl_codigoconsul = Label(ventanalibro,text="Codigo")
	lbl_codigoconsul.pack()
	lbl_codigoconsul.place(x=50,y=499)

	tituloconsul= StringVar()
	entry_tituloconsul=Entry(ventanalibro,textvariable=tituloconsul,width="15")
	entry_tituloconsul.pack()
	entry_tituloconsul.place(x=175,y=520)

	lbl_tituloconsul = Label(ventanalibro,text="Titulo")
	lbl_tituloconsul.pack()
	lbl_tituloconsul.place(x=175,y=499)

	lbl_generoconsul = Label(ventanalibro,text="Genero")
	lbl_generoconsul.pack()
	lbl_generoconsul.place(x=425,y=500)

	listaGconsul=["Drama", "Terror", "Comedia"]
	generoconsul= ttk.Combobox(ventanalibro, values=listaGconsul,state="readonly")
	generoconsul.set("Genéro")
	generoconsul.pack()
	generoconsul.place(x=425,y=520)

	btn_bus= Button(ventanalibro,text="Buscar",height="1",width="15",bg="#2214b9",fg="white")
	btn_bus.pack()
	btn_bus.place(x=760,y=500)

	btn_limconsulta= Button(ventanalibro,text="Limpiar",height="1",width="15",bg="#2214b9",fg="white")
	btn_limconsulta.pack()
	btn_limconsulta.place(x=760,y=535)




	mainloop()

















def v1_a_v2():
	ventana1.destroy()
	Login()
def v2_v3():
	ventana2.destroy()
	secciones()
def Vop_Vcre():
	ventana3.destroy()
	cliente()
def venlog_venr():
	ventana2.destroy()
	registrar()
def venreg_venlog():
    ventanareg.destroy()
    Login()
def cli_selec():
	ventanacliente.destroy()
	secciones()
def libro_selec():
	ventanalibro.destroy()
	secciones()
def selec_libro():
	ventana3.destroy()
	libro()
libro()
#InicioSesion()