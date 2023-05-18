from tkinter import * 
from PIL import Image, ImageTk

master = Tk()
master.title('Unit Converter')

def mass_operation():
	m_u_n = mass_unit_name.get()
	m_u_num = mass_unit_number.get()
	if m_u_n == 'kg':
		g = m_u_num * 1000
		ton = m_u_num * 0.001
		mass_target.config(text=f'{g} g \n {ton} ton')
		return
	elif m_u_n == 'g':
		kg = m_u_num * 0.001
		ton = m_u_num * 0.000001
		mass_target.config(text=f'{kg} kg \n {ton} ton')
		return
	elif m_u_n == 'ton':
		kg = m_u_num * 1000
		g = m_u_num * 1000000
		mass_target.config(text=f'{kg} kg \n {g} g')
		return

def mass():
	global mass_unit_name
	global mass_unit_number
	global mass_target
	mass_unit_number = IntVar()
	mass_unit_name = StringVar()
	mass_screen = Toplevel(master)  # it shows the screen.
	mass_screen.title("Mass's units")
	Label(mass_screen, text='quantity', font=('Courier', 12)).grid(row=0, column=1)
	Label(mass_screen, text='unit(kg, g, ...)', font=('Courier', 12)).grid(row=0, column=2)
	Entry(mass_screen, textvariable=mass_unit_number).grid(row=1, column=1)
	Entry(mass_screen, textvariable=mass_unit_name).grid(row=1, column=2)
	Button(mass_screen, text='submit', font=('Courier', 12), command=mass_operation).grid(row=1, sticky=N, column=3)

	mass_target = Label(mass_screen, font=('Courier', 12))
	mass_target.grid(row=2, sticky=N)

def length_operation():
	m_u_n = length_unit_name.get()
	m_u_num = length_unit_number.get()
	if m_u_n == 'm':
		cm = m_u_num * 100
		km = m_u_num * 0.001
		length_target.config(text=f'{cm} cm \n {km} km')
		return
	elif m_u_n == 'cm':
		m = m_u_num * 0.01
		km = m_u_num * 0.00001
		length_target.config(text=f'{m} m \n {km} km')
		return
	elif m_u_n == 'km':
		m = m_u_num * 1000
		cm = m_u_num * 100000
		length_target.config(text=f'{m} m \n {cm} cm')
		return

def length():
	global length_unit_name
	global length_unit_number
	global length_target
	length_unit_number = IntVar()
	length_unit_name = StringVar()
	length_screen = Toplevel(master)  # it shows the screen.
	length_screen.title("Length's units")
	Label(length_screen, text='quantity', font=('Courier', 12)).grid(row=0, column=1)
	Label(length_screen, text='unit(m, cm, ...)', font=('Courier', 12)).grid(row=0, column=2)
	Entry(length_screen, textvariable=length_unit_number).grid(row=1, column=1)
	Entry(length_screen, textvariable=length_unit_name).grid(row=1, column=2)
	Button(length_screen, text='submit', font=('Courier', 12), command=length_operation).grid(row=1, sticky=N, column=3)

	length_target = Label(length_screen, font=('Courier', 12))
	length_target.grid(row=2, sticky=N)

def area_operation():
	m_u_n = area_unit_name.get()
	m_u_num = area_unit_number.get()
	if m_u_n == 'm2':
		cm2 = m_u_num * 10000
		length_target.config(text=f'{cm2} cm2')
		return
	elif m_u_n == 'cm2':
		m2 = m_u_num * 0.0001
		length_target.config(text=f'{m2} m2')
		return

def area():
	global area_unit_name
	global area_unit_number
	global area_target
	area_unit_number = IntVar()
	area_unit_name = StringVar()
	area_screen = Toplevel(master)  # it shows the screen.
	area_screen.title("Area's units")
	Label(area_screen, text='quantity', font=('Courier', 12)).grid(row=0, column=1)
	Label(area_screen, text='unit(m2, cm2, ...)', font=('Courier', 12)).grid(row=0, column=2)
	Entry(area_screen, textvariable=area_unit_number).grid(row=1, column=1)
	Entry(area_screen, textvariable=area_unit_name).grid(row=1, column=2)
	Button(area_screen, text='submit', font=('Courier', 12), command=area_operation).grid(row=1, sticky=N, column=3)

	area_target = Label(area_screen, font=('Courier', 12))
	area_target.grid(row=2, sticky=N)

def time_operation():
	m_u_n = time_unit_name.get()
	m_u_num = time_unit_number.get()
	if m_u_n == 's':
		minute = m_u_num * 0.016
		hour = m_u_num * 0.000277
		time_target.config(text=f'{minute} min(s) \n {hour} hour(s)')
		return
	elif m_u_n == 'min':
		s = m_u_num * 60
		hour = m_u_num * 0.016
		time_target.config(text=f'{s} second(s) \n {hour} hour(s)')
		return
	elif m_u_n == 'h':
		s = m_u_num * 3600
		minute = m_u_num * 60
		time_target.config(text=f'{s} second(s) \n {minute} min(s)')
		return

def time():
	global time_unit_name
	global time_unit_number
	global time_target
	time_unit_number = IntVar()
	time_unit_name = StringVar()
	time_screen = Toplevel(master)  # it shows the screen.
	time_screen.title("Time's units")
	Label(time_screen, text='quantity', font=('Courier', 12)).grid(row=0, column=1)
	Label(time_screen, text='unit(s, min, h, ...)', font=('Courier', 12)).grid(row=0, column=2)
	Entry(time_screen, textvariable=time_unit_number).grid(row=1, column=1)
	Entry(time_screen, textvariable=time_unit_name).grid(row=1, column=2)
	Button(time_screen, text='submit', font=('Courier', 12), command=time_operation).grid(row=1, sticky=N, column=3)

	time_target = Label(time_screen, font=('Courier', 12))
	time_target.grid(row=2, sticky=N)

def temp_operation():
	m_u_n = temp_unit_name.get()
	m_u_num = temp_unit_number.get()
	if m_u_n == 'C':
		k = m_u_num + 273
		f = (m_u_num*1.8) + 32
		temp_target.config(text=f'{k} K \n {f} F')
		return
	elif m_u_n == 'K':
		c = m_u_num - 273
		f = (c*1.8) + 32
		temp_target.config(text=f'{c} C \n {f} F')
		return
	elif m_u_n == 'F':
		c = (m_u_num*0.55) - 32
		k = c + 273
		temp_target.config(text=f'{c} C \n {k} K')
		return

def temp():
	global temp_unit_name
	global temp_unit_number
	global temp_target
	temp_unit_number = IntVar()
	temp_unit_name = StringVar()
	temp_screen = Toplevel(master)  # it shows the screen.
	temp_screen.title("Temperature's units")
	Label(temp_screen, text='quantity', font=('Courier', 12)).grid(row=0, column=1)
	Label(temp_screen, text='unit(C, K, F, ...)', font=('Courier', 12)).grid(row=0, column=2)
	Entry(temp_screen, textvariable=temp_unit_number).grid(row=1, column=1)
	Entry(temp_screen, textvariable=temp_unit_name).grid(row=1, column=2)
	Button(temp_screen, text='submit', font=('Courier', 12), command=temp_operation).grid(row=1, sticky=N, column=3)

	temp_target = Label(temp_screen, font=('Courier', 12))
	temp_target.grid(row=2, sticky=N)

#images part 
img = Image.open("physics.png")
img = img.resize((495,200))
img = ImageTk.PhotoImage(img)

#labels part
Label(master, text='Choose the quantity ; ', font=('Courier', 12)).grid(row=0, sticky=N)
Label(master, image=img).grid(row=6, sticky=N, pady=15)

#buttons part
Button(master, text='1_ Mass', font=('Courier', 12), command=mass).grid(row=1, sticky=N)
Button(master, text='2_ Length', font=('Courier', 12), command=length).grid(row=2, sticky=N)
Button(master, text='3_ Area', font=('Courier', 12), command=area).grid(row=3, sticky=N)
Button(master, text='4_ Time', font=('Courier', 12), command=time).grid(row=4, sticky=N)
Button(master, text='5_ Temperature', font=('Courier', 12), command=temp).grid(row=5, sticky=N)

master.mainloop()