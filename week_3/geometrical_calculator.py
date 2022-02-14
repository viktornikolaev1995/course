from tkinter import *
from tkinter import messagebox

from matplotlib.colors import is_color_like
from geometrical_figures import (Circle, Square, Rectangle, Rhombus, Trapezoid, Triangle, Sphere, Cube, Parallelepiped,
                                 Pyramid, Cylinder, Cone)


root = Tk()
# setting the title
root.title('Geometric calculator for calculations performed on flat and three-dimensional figures')
root.iconphoto(True, PhotoImage(file="./geometry.png"))  # setting the icon
root.geometry("700x700")  # dimensions of the main window
fg_header = 'brown'  # color for header of current figure
fg_main = 'purple'  # color for functions of current figure
fg_additional = 'black'  # color for attributes and variables
is_frame_exist = True  # variable which check's if current frame exists
figure = None  # name of current figure


def create_or_delete_and_create_frame():
    """If frame does not exist, frame must be created. If frame exists, firstly it must be deleted, and after created
    frame for adding new labels, entries, buttons for another figure, because older labels, entries, buttons the
    previous figure can be leave and it is not acceptable"""
    global frame

    if not is_frame_exist:
        frame = LabelFrame(root, fg=fg_main, padx=5, pady=5)  # creates new frame
        frame.grid(padx=160, pady=30)
    else:
        frame.grid_remove()  # deletes existing frame
        frame = LabelFrame(root, fg=fg_main, padx=5, pady=5)  # creates new frame
        frame.grid(padx=160, pady=30)


def destroing_labels():
    """Destroying not necessary labels from frame"""
    try:
        if label_area.winfo_exists():  # check's existing label
            label_area.destroy()
        if label_perimeter.winfo_exists():
            label_perimeter.destroy()
        if label_middle_line.winfo_exists():
            label_middle_line.destroy()
        if label_volume.winfo_exists():
            label_volume.destroy()

    except NameError:
        pass


def selected_figure():
    """Getting figure from dropdown menu and created frame at current figure if it's necessary"""
    global figure
    global is_frame_exist
    figure = clicked.get()

    create_or_delete_and_create_frame()
    if figure in ['Circle', 'Sphere']:
        drawing_interface_for_figure('200', label_param1=f'Type the radius value of {figure.lower()}:')

    elif figure in ['Cylinder', 'Cone']:
        drawing_interface_for_figure('200', '100', label_param1='Type the radius value:',
                                     label_param3=f'Type the height value of {figure.lower()}:')
    elif figure in ['Square', 'Cube']:
        drawing_interface_for_figure('200', label_param1=f'Type the length value of the {figure.lower()}:')

    elif figure == 'Rectangle':
        drawing_interface_for_figure('200', '100',
                                     label_param1=f'Type the length value of the {figure.lower()}:',
                                     label_param2=f'Type the width value of {figure.lower()}:',)

    elif figure in ['Parallelepiped', 'Pyramid']:
        drawing_interface_for_figure('200', '100', '300',
                                     label_param1=f'Type the length value of the {figure.lower()}:',
                                     label_param2=f'Type the width value of {figure.lower()}:',
                                     label_param3=f'Type the height value of {figure.lower()}:')
    elif figure == 'Rhombus':
        drawing_interface_for_figure('0, 0; 2, -3; 4, 0; 2, 3', label_param1='Type the vertices of the rhombus:')

    elif figure == 'Trapezoid':
        drawing_interface_for_figure('1, 2; 5, 2; 3, 5; 4, 5', label_param1='Type the vertices of the trapezoid:')

    elif figure == 'Triangle':
        drawing_interface_for_figure('1, 2; 5, 2; 3, 5', label_param1='Type the vertices of the triangle:')

    is_frame_exist = True
    destroing_labels()


options = ['Circle', 'Square', 'Rectangle', 'Rhombus', 'Trapezoid', 'Triangle', 'Sphere', 'Cube', 'Parallelepiped',
           'Pyramid', 'Cylinder', 'Cone']

clicked = StringVar()
clicked.set(options[0])

# drop = OptionMenu(root, clicked, *options)
# drop.grid(pady=15)

btn_choice_figure = Button(root, text='Select figure from the list below and click on me', command=selected_figure)
btn_choice_figure.grid(padx=215, pady=5)

drop = OptionMenu(root, clicked, *options)
drop.grid(pady=5)

frame = LabelFrame(root, fg=fg_main, padx=5, pady=5)
# frame.grid(padx=330, pady=30)


def drawing_interface_for_figure(*args, **kwargs):
    """Drawing frame for current figure with specific labels, entries, buttons and etc"""
    global entry_param1
    global entry_param2
    global entry_param3
    global entry_fill
    global entry_font_color
    global entry_edge_color
    global entry_alpha
    global btn_plotting_graphic
    global btn_calc_area
    global btn_calc_middle_line
    global btn_calc_perimeter
    global btn_calc_volume
    global const_1

    const_1 = args[0]
    label_figure = Label(frame, text=f'{figure}', fg=fg_header, width=50)
    label_figure.grid(row=1, column=0, pady=10)
    label_param1 = Label(frame, text=kwargs['label_param1'], fg=fg_additional, width=50)
    label_param1.grid(row=2, column=0)
    entry_param1 = Entry(frame, width=50, fg=fg_additional, borderwidth='2')
    entry_param1.grid(row=3, column=0)
    entry_param1.insert(0, const_1)

    if figure in ['Rectangle', 'Parallelepiped', 'Pyramid']:
        const_2 = args[1]
        label_param2 = Label(frame, text=kwargs['label_param2'], fg=fg_additional, width=50)
        label_param2.grid(row=4, column=0)

        entry_param2 = Entry(frame, width=50, fg=fg_additional, borderwidth='2')
        entry_param2.grid(row=5, column=0)
        entry_param2.insert(0, const_2)

        if figure in ['Parallelepiped', 'Pyramid']:
            const_3 = args[2]
            label_param3 = Label(frame, text=kwargs['label_param3'], fg=fg_additional, width=50)
            label_param3.grid(row=6, column=0)

            entry_param3 = Entry(frame, width=50, fg=fg_additional, borderwidth='2')
            entry_param3.grid(row=7, column=0)
            entry_param3.insert(0, const_3)

    if figure in ['Cylinder', 'Cone']:
        const_2 = args[1]
        label_param3 = Label(frame, text=kwargs['label_param3'], fg=fg_additional, width=50)
        label_param3.grid(row=4, column=0)

        entry_param3 = Entry(frame, width=50, fg=fg_additional, borderwidth='2')
        entry_param3.grid(row=5, column=0)
        entry_param3.insert(0, const_2)

    label_plotting_sett = Label(frame, text='Override the plotting settings if needed', fg=fg_main, width=50)
    label_plotting_sett.grid(row=8, column=0, pady=15)

    label_fill = Label(frame, text='Filled in the inner area? (Type: yes/no):', fg=fg_additional, width=50)
    label_fill.grid(row=9, column=0)

    entry_fill = Entry(frame, width=50, fg=fg_additional, borderwidth='2')
    entry_fill.grid(row=10, column=0)
    entry_fill.insert(0, 'no')

    label_font_color = Label(frame, text='Set font color:', fg=fg_additional, width=50)
    label_font_color.grid(row=11, column=0)

    entry_font_color = Entry(frame, width=50, fg=fg_additional, borderwidth='2')
    entry_font_color.grid(row=12, column=0)
    entry_font_color.insert(0, 'blue')

    label_edge_color = Label(frame, text='Set edge color:', fg=fg_additional, width=50)
    label_edge_color.grid(row=13, column=0)

    entry_edge_color = Entry(frame, width=50, fg=fg_additional, borderwidth='2')
    entry_edge_color.grid(row=14, column=0)
    entry_edge_color.insert(0, 'green')

    label_alpha = Label(frame, text='Set transparency in range from 0 to 1 inclusive:', fg=fg_additional, width=50)
    label_alpha.grid(row=15, column=0)

    entry_alpha = Entry(frame, width=50, fg=fg_additional, borderwidth='2')
    entry_alpha.grid(row=16, column=0)
    entry_alpha.insert(0, '0.7')

    btn_figure = Button(frame, text='Set the plotting settings', fg=fg_main, command=set_settings)
    btn_figure.grid(row=17, column=0, pady=5)

    btn_calc_area = Button(frame, text='Calculating area', fg=fg_main, command=calc_area)
    btn_calc_area.grid(row=18, column=0, pady=5)

    if figure in ['Trapezoid']:
        btn_calc_middle_line = Button(frame, text='Calculating middle line', fg=fg_main, command=calc_middle_line)
        btn_calc_middle_line.grid(row=19, column=0, pady=5)

    elif figure not in ['Sphere', 'Cube', 'Parallelepiped', 'Pyramid', 'Cylinder', 'Cone']:
        btn_calc_perimeter = Button(frame, text='Calculating perimeter', fg=fg_main, command=calc_perimeter)
        btn_calc_perimeter.grid(row=19, column=0, pady=5)

    else:
        btn_calc_volume = Button(frame, text='Calculating volume', fg=fg_main, command=calc_volume)
        btn_calc_volume.grid(row=19, column=0, pady=5)

    btn_plotting_graphic = Button(frame, text='Plotting graphic', fg=fg_main, command=plot)
    btn_plotting_graphic.grid(row=20, column=0, pady=5)

    if figure in ['Trapezoid']:
        disabled_buttons = disabled_or_enabled_buttons(btn_calc_area, btn_calc_middle_line, btn_plotting_graphic,
                                                       state=DISABLED)
        btn_calc_middle_line = disabled_buttons[1]

    elif figure in ['Sphere', 'Cube', 'Parallelepiped', 'Pyramid', 'Cylinder', 'Cone']:
        disabled_buttons = disabled_or_enabled_buttons(btn_calc_area, btn_calc_volume, btn_plotting_graphic,
                                                       state=DISABLED)
        btn_calc_volume = disabled_buttons[1]

    else:
        disabled_buttons = disabled_or_enabled_buttons(btn_calc_area, btn_calc_perimeter, btn_plotting_graphic,
                                                       state=DISABLED)
        btn_calc_perimeter = disabled_buttons[1]

    btn_calc_area = disabled_buttons[0]
    btn_plotting_graphic = disabled_buttons[2]
    is_clicked = False  # makes buttons disabled


def disabled_or_enabled_buttons(*args, state):
    """Makes the button disabled or enabled"""
    for btn in args:
        btn['state'] = state
    return args


def overriding_state_of_buttons_if_calling_errors(state):
    """Overriding state of buttons if calling errors at validation"""
    if figure in ['Trapezoid']:
        disabled_or_enabled_buttons(btn_calc_area, btn_calc_middle_line, btn_plotting_graphic, state=state)
    elif figure not in ['Sphere', 'Cube', 'Parallelepiped', 'Pyramid', 'Cylinder', 'Cone']:
        disabled_or_enabled_buttons(btn_calc_area, btn_calc_perimeter, btn_plotting_graphic, state=state)
    else:
        disabled_or_enabled_buttons(btn_calc_area, btn_calc_volume, btn_plotting_graphic, state=state)


def validate_variables(**kwargs):
    """Validating gotten variables"""
    if figure not in ['Rhombus', 'Trapezoid', 'Triangle']:
        try:
            param1 = float(kwargs['entry_param'].get())
            if param1 <= 0:
                overriding_state_of_buttons_if_calling_errors(state=DISABLED)
                messagebox.showerror(
                    'ValueError', f'Your input for {kwargs["type_of_param"]}: `{kwargs["entry_param"].get()}`'
                    f' is incorrect! {kwargs["type_of_param"].capitalize()} can not be negative or equal 0!')
                raise Exception(f'{kwargs["type_of_param"].capitalize()} can not be negative or equal 0!')
            return param1
        except ValueError as err:
            overriding_state_of_buttons_if_calling_errors(state=DISABLED)

            messagebox.showerror(f'{err}', f'Your input for {kwargs["type_of_param"]}: `{kwargs["entry_param"].get()}`'
                                           f' is incorrect! {kwargs["type_of_param"].capitalize()} can be a float or '
                                           f'int type!')
            raise ValueError(f'Variable {kwargs["type_of_param"]} is not a float or int type!')
    else:
        try:
            if figure != 'Triangle':
                vertex_1, vertex_2, vertex_3, vertex_4 = kwargs['entry_param'].get().split(';')
                if figure == 'Trapezoid':
                    Trapezoid(vertex_1, vertex_2, vertex_3, vertex_4)
                else:
                    Rhombus(vertex_1, vertex_2, vertex_3, vertex_4)
                return vertex_1, vertex_2, vertex_3, vertex_4

            elif figure == 'Triangle':
                vertex_1, vertex_2, vertex_3 = kwargs['entry_param'].get().split(';')
                Triangle(vertex_1, vertex_2, vertex_3)
                return vertex_1, vertex_2, vertex_3

        except ValueError as err:
            overriding_state_of_buttons_if_calling_errors(state=DISABLED)
            if 'not enough values to unpack' in err.__str__():
                messagebox.showerror('ValueError',
                                     f'Your input for {kwargs["type_of_param"]}: `{kwargs["entry_param"].get()}`'
                                     f' is incorrect! {kwargs["type_of_param"].capitalize()} '
                                     f'expects to receive coordinates in the format: {const_1}')
                raise ValueError(f'{err}')
            messagebox.showerror('ValueError', f'{err}')
            raise ValueError(f'{err}')


def set_settings():
    """Setting of settings of current figure for further work with gotten data"""
    global is_clicked
    global param1
    global param2
    global param3
    global fill
    global fc
    global ec
    global alpha
    global instance_of_figure
    global vertex_1
    global vertex_2
    global vertex_3
    global vertex_4

    if figure in ['Circle', 'Sphere']:
        param1 = validate_variables(entry_param=entry_param1, type_of_param='radius')
    elif figure in ['Square', 'Cube', 'Rectangle', 'Parallelepiped', 'Pyramid']:
        param1 = validate_variables(entry_param=entry_param1, type_of_param='length')
        if figure in ['Rectangle', 'Parallelepiped', 'Pyramid']:
            param2 = validate_variables(entry_param=entry_param2, type_of_param='width')
        if figure in ['Parallelepiped', 'Pyramid']:
            param3 = validate_variables(entry_param=entry_param3, type_of_param='height')

    elif figure in ['Rhombus', 'Trapezoid']:
        vertex_1, vertex_2, vertex_3, vertex_4 = validate_variables(entry_param=entry_param1, type_of_param='vertexes')
    elif figure == 'Triangle':
        vertex_1, vertex_2, vertex_3 = validate_variables(entry_param=entry_param1, type_of_param='vertexes')
    elif figure in ['Cylinder', 'Cone']:
        param1 = validate_variables(entry_param=entry_param1, type_of_param='radius')
        param3 = validate_variables(entry_param=entry_param3, type_of_param='height')

    fill = entry_fill.get().lower()

    if fill in ['yes', 'no']:
        fill = True if fill == 'yes' else False
    else:
        overriding_state_of_buttons_if_calling_errors(state=DISABLED)
        messagebox.showerror('ValueError', f'Your input for `fill in the area`: {fill} is not yes or no string!')
        raise ValueError('Attribute fill not in ["yes", "no"]!')

    fc = entry_font_color.get()

    if is_color_like(fc):
        pass
    else:
        overriding_state_of_buttons_if_calling_errors(state=DISABLED)
        messagebox.showerror('ValueError', f'Your input for font color: {fc} is not in the color list. '
                                           f'Type a correct color!')
        raise ValueError('Attribute fg not in matplotlib color list!')

    ec = entry_edge_color.get()

    if is_color_like(ec):
        pass
    else:
        overriding_state_of_buttons_if_calling_errors(state=DISABLED)
        messagebox.showerror('ValueError', f'Your input for edge color: {ec} is not in the color list. '
                                           f'Type a correct color!')
        raise ValueError('Attribute eg not in matplotlib color list!')

    try:
        alpha = float(entry_alpha.get())
        if round(alpha, 0) in [0, 1]:
            pass
        else:
            overriding_state_of_buttons_if_calling_errors(state=DISABLED)
            messagebox.showerror(f'ValueError', f'Your input for transparency: `{entry_alpha.get()}`'
                                           f' is incorrect! Transparency can be in the range in 0 to 1 inclusive!')
            raise Exception(f'Attribute transparency is not in the range in 0 to 1!')
    except ValueError as err:
        overriding_state_of_buttons_if_calling_errors(state=DISABLED)
        messagebox.showerror(f'{err}', f'Your input for transparency: `{entry_alpha.get()}`'
                                       f' is incorrect! Transparency can be a float or '
                                       f'int type!')
        raise ValueError(f'Attribute transparency is not a float or int type!')

    is_clicked = True  # enabling disabled buttons after tap button set plotting settings

    if is_clicked:
        overriding_state_of_buttons_if_calling_errors(state=NORMAL)

    if figure == 'Circle':
        instance_of_figure = Circle(radius=param1)

    elif figure == 'Square':
        instance_of_figure = Square(length=param1)

    elif figure == 'Rectangle':
        instance_of_figure = Rectangle(length=param1, width=param2)

    elif figure == 'Rhombus':
        instance_of_figure = Rhombus(coord_1=vertex_1, coord_2=vertex_2, coord_3=vertex_3, coord_4=vertex_4)

    elif figure == 'Trapezoid':
        instance_of_figure = Trapezoid(coord_1=vertex_1, coord_2=vertex_2, coord_3=vertex_3, coord_4=vertex_4)

    elif figure == 'Triangle':
        instance_of_figure = Triangle(coord_1=vertex_1, coord_2=vertex_2, coord_3=vertex_3)

    elif figure == 'Sphere':
        instance_of_figure = Sphere(radius=param1)

    elif figure == 'Cube':
        instance_of_figure = Cube(length=param1)

    elif figure == 'Parallelepiped':
        instance_of_figure = Parallelepiped(length=param1, width=param2, height=param3)

    elif figure == 'Pyramid':
        instance_of_figure = Pyramid(length=param1, width=param2, height=param3)

    elif figure == 'Cylinder':
        instance_of_figure = Cylinder(radius=param1, height=param3)

    elif figure == 'Cone':
        instance_of_figure = Cone(radius=param1, height=param3)


def calc_area():
    """Calculating area of current figure if the function will be called current figure instance"""
    global label_area
    label_area = Label(frame, text=f'{instance_of_figure.area()}', fg=fg_additional, width=50)
    label_area.grid(row=21, column=0)


def calc_perimeter():
    """Calculating perimeter of current figure if the function will be called current figure instance"""
    global label_perimeter
    label_perimeter = Label(frame, text=f'{instance_of_figure.perimeter()}', fg=fg_additional, width=50)
    label_perimeter.grid(row=22, column=0)


def calc_middle_line():
    """Calculating middle line of current figure if the function will be called current figure instance"""
    global label_middle_line
    label_middle_line = Label(frame, text=f'{instance_of_figure.middle_line()}', fg=fg_additional, width=50)
    label_middle_line.grid(row=22, column=0)


def calc_volume():
    """Calculating volume of current figure if the function will be called current figure instance"""
    global label_volume
    label_volume = Label(frame, text=f'{instance_of_figure.volume()}', fg=fg_additional, width=50)
    label_volume.grid(row=22, column=0)


def plot():
    """Plotting graphic for current figure"""
    instance_of_figure.__class__.override_plotting_settings(fill=fill, fc=fc, ec=ec, alpha=alpha)
    instance_of_figure.plotting_graphic()


root.mainloop()