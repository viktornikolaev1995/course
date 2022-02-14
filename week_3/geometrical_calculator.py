import tkinter as tk
from tkinter import ttk, DISABLED, NORMAL, messagebox
from matplotlib.colors import is_color_like
from geometrical_figures import (Circle, Square, Rectangle, Rhombus, Trapezoid, Triangle, Sphere, Cube, Parallelepiped,
                                 Pyramid, Cylinder, Cone)


class ShapeFrame(ttk.Frame):
    def __init__(self, container, figure, fg_header, fg_main, fg_additional):
        super().__init__(container)
        self.figure = figure
        self.fg_header = fg_header
        self.fg_main = fg_main
        self.fg_additional = fg_additional
        self.fill = None
        self.fc = None
        self.ec = None
        self.alpha = None
        self.instance_of_figure = None
        self.param1 = None
        self.param2 = None
        self.param3 = None
        self.vertex_1 = None
        self.vertex_2 = None
        self.vertex_3 = None
        self.vertex_4 = None
        self.is_clicked = False  # makes buttons disabled
        self.const_1 = None
        self.const_2 = None
        self.const_3 = None
        self.text_for_label_param1 = None
        self.text_for_label_param2 = None
        self.text_for_label_param3 = None
        self.label_area = None
        self.label_perimeter = None
        self.label_middle_line = None
        self.label_volume = None

        if self.figure in ['Circle', 'Sphere']:
            self.const_1 = '200'
            self.text_for_label_param1 = f'Type the radius value of the {self.figure.lower()}:'

        elif self.figure in ['Cylinder', 'Cone']:
            self.const_1 = '200'
            self.const_3 = '300'
            self.text_for_label_param1 = f'Type the radius value of the {self.figure.lower()}:'
            self.text_for_label_param3 = f'Type the height value of the {self.figure.lower()}:'

        elif self.figure in ['Square', 'Cube']:
            self.const_1 = '200'
            self.text_for_label_param1 = f'Type the length value of the {self.figure.lower()}:'

        elif self.figure == 'Rectangle':
            self.const_1 = '200'
            self.const_2 = '100'
            self.text_for_label_param1 = f'Type the length value of the {self.figure.lower()}:'
            self.text_for_label_param2 = f'Type the width value of the {self.figure.lower()}:'

        elif self.figure in ['Parallelepiped', 'Pyramid']:
            self.const_1 = '200'
            self.const_2 = '100'
            self.const_3 = '300'
            self.text_for_label_param1 = f'Type the length value of the {self.figure.lower()}:'
            self.text_for_label_param2 = f'Type the width value of the {self.figure.lower()}:'
            self.text_for_label_param3 = f'Type the height value of the {self.figure.lower()}:'

        elif self.figure == 'Rhombus':
            self.const_1 = '0, 0; 2, -3; 4, 0; 2, 3'
            self.text_for_label_param1 = f'Type the vertices of the {self.figure.lower()}:'

        elif self.figure == 'Trapezoid':
            self.const_1 = '1, 2; 5, 2; 3, 5; 4, 5'
            self.text_for_label_param1 = f'Type the vertices of the {self.figure.lower()}:'

        elif self.figure == 'Triangle':
            self.const_1 = '1, 2; 5, 2; 3, 5'
            self.text_for_label_param1 = f'Type the vertices of the {self.figure.lower()}:'

        self.label_figure = tk.Label(self, text=f'{self.figure}', fg=self.fg_header, width=50)
        self.label_figure.grid(row=1, column=0, pady=10)
        self.label_param1 = tk.Label(self, text=self.text_for_label_param1, fg=self.fg_additional, width=50)
        self.label_param1.grid(row=2, column=0)
        self.entry_param1 = tk.Entry(self, width=50, fg=self.fg_additional, borderwidth='2')
        self.entry_param1.grid(row=3, column=0)
        self.entry_param1.insert(0, self.const_1)

        if self.figure in ['Rectangle', 'Parallelepiped', 'Pyramid']:
            self.label_param2 = tk.Label(self, text=self.text_for_label_param2, fg=self.fg_additional, width=50)
            self.label_param2.grid(row=4, column=0)

            self.entry_param2 = tk.Entry(self, width=50, fg=self.fg_additional, borderwidth='2')
            self.entry_param2.grid(row=5, column=0)
            self.entry_param2.insert(0, self.const_2)

            if self.figure in ['Parallelepiped', 'Pyramid']:

                self.label_param3 = tk.Label(self, text=self.text_for_label_param3, fg=self.fg_additional, width=50)
                self.label_param3.grid(row=6, column=0)

                self.entry_param3 = tk.Entry(self, width=50, fg=self.fg_additional, borderwidth='2')
                self.entry_param3.grid(row=7, column=0)
                self.entry_param3.insert(0, self.const_3)

        if self.figure in ['Cylinder', 'Cone']:
            self.const_2 = '100'
            self.label_param3 = tk.Label(self, text='label_param3', fg=self.fg_additional, width=50)
            self.label_param3.grid(row=4, column=0)

            self.entry_param3 = tk.Entry(self, width=50, fg=self.fg_additional, borderwidth='2')
            self.entry_param3.grid(row=5, column=0)
            self.entry_param3.insert(0, self.const_2)

        self.label_plotting_sett = tk.Label(self, text='Override the plotting settings if needed', fg=self.fg_main,
                                            width=50)
        self.label_plotting_sett.grid(row=8, column=0, pady=15)

        self.label_fill = tk.Label(self, text='Filled in the inner area? (Type: yes/no):', fg=self.fg_additional,
                                   width=50)
        self.label_fill.grid(row=9, column=0)

        self.entry_fill = tk.Entry(self, width=50, fg=self.fg_additional, borderwidth='2')
        self.entry_fill.grid(row=10, column=0)
        self.entry_fill.insert(0, 'yes')

        self.label_font_color = tk.Label(self, text='Set font color:', fg=self.fg_additional, width=50)
        self.label_font_color.grid(row=11, column=0)

        self.entry_font_color = tk.Entry(self, width=50, fg=self.fg_additional, borderwidth='2')
        self.entry_font_color.grid(row=12, column=0)
        self.entry_font_color.insert(0, 'pink')

        self.label_edge_color = tk.Label(self, text='Set edge color:', fg=self.fg_additional, width=50)
        self.label_edge_color.grid(row=13, column=0)

        self.entry_edge_color = tk.Entry(self, width=50, fg=self.fg_additional, borderwidth='2')
        self.entry_edge_color.grid(row=14, column=0)
        self.entry_edge_color.insert(0, 'green')

        self.label_alpha = tk.Label(self, text='Set transparency in range from 0 to 1 inclusive:',
                                    fg=self.fg_additional, width=50)
        self.label_alpha.grid(row=15, column=0)

        self.entry_alpha = tk.Entry(self, width=50, fg=self.fg_additional, borderwidth='2')
        self.entry_alpha.grid(row=16, column=0)
        self.entry_alpha.insert(0, '0.7')

        self.btn_figure = tk.Button(self, text='Set the plotting settings', fg=self.fg_main, command=self.set_settings)
        self.btn_figure.grid(row=17, column=0, pady=5)

        self.btn_calc_area = tk.Button(self, text='Calculating area', fg=self.fg_main, command=self.calc_area)
        self.btn_calc_area.grid(row=18, column=0, pady=5)

        if self.figure in ['Trapezoid']:
            self.btn_calc_middle_line = tk.Button(self, text='Calculating middle line', fg=self.fg_main,
                                                  command=self.calc_middle_line)
            self.btn_calc_middle_line.grid(row=19, column=0, pady=5)

        elif self.figure not in ['Sphere', 'Cube', 'Parallelepiped', 'Pyramid', 'Cylinder', 'Cone']:
            self.btn_calc_perimeter = tk.Button(self, text='Calculating perimeter', fg=self.fg_main,
                                                command=self.calc_perimeter)
            self.btn_calc_perimeter.grid(row=19, column=0, pady=5)

        else:
            self.btn_calc_volume = tk.Button(self, text='Calculating volume', fg=self.fg_main, command=self.calc_volume)
            self.btn_calc_volume.grid(row=19, column=0, pady=5)

        self.btn_plotting_graphic = tk.Button(self, text='Plotting graphic', fg=self.fg_main,
                                              command=self.plotting_graphic)
        self.btn_plotting_graphic.grid(row=20, column=0, pady=5)

        if self.figure in ['Trapezoid']:
            self.disabled_buttons = self.disabled_or_enabled_buttons(self.btn_calc_area, self.btn_calc_middle_line,
                                                                     self.btn_plotting_graphic, state=DISABLED)
            self.btn_calc_middle_line = self.disabled_buttons[1]

        elif self.figure in ['Sphere', 'Cube', 'Parallelepiped', 'Pyramid', 'Cylinder', 'Cone']:
            self.disabled_buttons = self.disabled_or_enabled_buttons(self.btn_calc_area, self.btn_calc_volume,
                                                                     self.btn_plotting_graphic, state=DISABLED)
            self.btn_calc_volume = self.disabled_buttons[1]

        else:
            self.disabled_buttons = self.disabled_or_enabled_buttons(self.btn_calc_area, self.btn_calc_perimeter,
                                                                     self.btn_plotting_graphic, state=DISABLED)
            self.btn_calc_perimeter = self.disabled_buttons[1]

        self.btn_calc_area = self.disabled_buttons[0]
        self.btn_plotting_graphic = self.disabled_buttons[2]
        self.grid()

    @staticmethod
    def disabled_or_enabled_buttons(*args, **kwargs):
        """Makes the button disabled or enabled"""
        for btn in args:
            btn['state'] = kwargs['state']
        return args

    def overriding_state_of_buttons_if_calling_errors(self, state):
        """Overriding state of buttons if calling errors at validation"""
        if self.figure in ['Trapezoid']:
            self.disabled_or_enabled_buttons(self.btn_calc_area, self.btn_calc_middle_line, self.btn_plotting_graphic,
                                             state=state)
        elif self.figure not in ['Sphere', 'Cube', 'Parallelepiped', 'Pyramid', 'Cylinder', 'Cone']:
            self.disabled_or_enabled_buttons(self.btn_calc_area, self.btn_calc_perimeter, self.btn_plotting_graphic,
                                             state=state)
        else:
            self.disabled_or_enabled_buttons(self.btn_calc_area, self.btn_calc_volume, self.btn_plotting_graphic,
                                             state=state)

    def validate_variables(self, **kwargs):
        """Validating gotten variables"""
        if self.figure not in ['Rhombus', 'Trapezoid', 'Triangle']:
            try:
                self.param1 = float(kwargs['entry_param'].get())
                if self.param1 <= 0:
                    self.overriding_state_of_buttons_if_calling_errors(state=DISABLED)
                    messagebox.showerror(
                        'ValueError', f'Your input for {kwargs["type_of_param"]}: `{kwargs["entry_param"].get()}`'
                                      f' is incorrect! {kwargs["type_of_param"].capitalize()} can not be negative or '
                                      f'equal 0!')
                    raise Exception(f'{kwargs["type_of_param"].capitalize()} can not be negative or equal 0!')
                return self.param1
            except ValueError as err:
                self.overriding_state_of_buttons_if_calling_errors(state=DISABLED)

                messagebox.showerror(f'{err}',
                                     f'Your input for {kwargs["type_of_param"]}: `{kwargs["entry_param"].get()}`'
                                     f' is incorrect! {kwargs["type_of_param"].capitalize()} can be a float or '
                                     f'int type!')
                raise ValueError(f'Variable {kwargs["type_of_param"]} is not a float or int type!')
        else:
            try:
                if self.figure != 'Triangle':
                    self.vertex_1, self.vertex_2, self.vertex_3, self.vertex_4 = kwargs['entry_param'].get().split(';')
                    if self.figure == 'Trapezoid':
                        Trapezoid(self.vertex_1, self.vertex_2, self.vertex_3, self.vertex_4)
                    else:
                        Rhombus(self.vertex_1, self.vertex_2, self.vertex_3, self.vertex_4)
                    return self.vertex_1, self.vertex_2, self.vertex_3, self.vertex_4

                elif self.figure == 'Triangle':
                    self.vertex_1, self.vertex_2, self.vertex_3 = kwargs['entry_param'].get().split(';')
                    Triangle(self.vertex_1, self.vertex_2, self.vertex_3)
                    return self.vertex_1, self.vertex_2, self.vertex_3

            except ValueError as err:
                self.overriding_state_of_buttons_if_calling_errors(state=DISABLED)
                if 'not enough values to unpack' in err.__str__():
                    messagebox.showerror('ValueError',
                                         f'Your input for {kwargs["type_of_param"]}: `{kwargs["entry_param"].get()}`'
                                         f' is incorrect! {kwargs["type_of_param"].capitalize()} '
                                         f'expects to receive coordinates in the format: {self.const_1}')
                    raise ValueError(f'{err}')
                messagebox.showerror('ValueError', f'{err}')
                raise ValueError(f'{err}')

    def set_settings(self):
        """Setting of settings of current figure for further work with gotten data"""

        if self.figure in ['Circle', 'Sphere']:
            self.param1 = self.validate_variables(entry_param=self.entry_param1, type_of_param='radius')
        elif self.figure in ['Square', 'Cube', 'Rectangle', 'Parallelepiped', 'Pyramid']:
            self.param1 = self.validate_variables(entry_param=self.entry_param1, type_of_param='length')
            if self.figure in ['Rectangle', 'Parallelepiped', 'Pyramid']:
                self.param2 = self.validate_variables(entry_param=self.entry_param2, type_of_param='width')
            if self.figure in ['Parallelepiped', 'Pyramid']:
                self.param3 = self.validate_variables(entry_param=self.entry_param3, type_of_param='height')

        elif self.figure in ['Rhombus', 'Trapezoid']:
            self.vertex_1, self.vertex_2, self.vertex_3, self.vertex_4 = self.validate_variables(
                entry_param=self.entry_param1, type_of_param='vertexes')

        elif self.figure == 'Triangle':
            self.vertex_1, self.vertex_2, self.vertex_3 = self.validate_variables(entry_param=self.entry_param1,
                                                                                  type_of_param='vertexes')
        elif self.figure in ['Cylinder', 'Cone']:
            self.param1 = self.validate_variables(entry_param=self.entry_param1, type_of_param='radius')
            self.param3 = self.validate_variables(entry_param=self.entry_param3, type_of_param='height')

        self.fill = self.entry_fill.get().lower()

        if self.fill in ['yes', 'no']:
            self.fill = True if self.fill == 'yes' else False
        else:
            self.overriding_state_of_buttons_if_calling_errors(state=DISABLED)
            messagebox.showerror('ValueError', f'Your input for `fill in the area`: {self.fill} is not yes or no '
                                               f'string!')
            raise ValueError('Attribute fill not in ["yes", "no"]!')

        self.fc = self.entry_font_color.get()

        if is_color_like(self.fc):
            pass
        else:
            self.overriding_state_of_buttons_if_calling_errors(state=DISABLED)
            messagebox.showerror('ValueError', f'Your input for font color: {self.fc} is not in the color list. '
                                               f'Type a correct color!')
            raise ValueError('Attribute fg not in matplotlib color list!')

        self.ec = self.entry_edge_color.get()

        if is_color_like(self.ec):
            pass
        else:
            self.overriding_state_of_buttons_if_calling_errors(state=DISABLED)
            messagebox.showerror('ValueError', f'Your input for edge color: {self.ec} is not in the color list. '
                                               f'Type a correct color!')
            raise ValueError('Attribute eg not in matplotlib color list!')

        try:
            self.alpha = float(self.entry_alpha.get())
            if round(self.alpha, 0) in [0, 1]:
                pass
            else:
                self.overriding_state_of_buttons_if_calling_errors(state=DISABLED)
                messagebox.showerror(f'ValueError', f'Your input for transparency: `{self.entry_alpha.get()}` '
                                     f'is incorrect! Transparency can be in the range in 0 to 1 '
                                     f'inclusive!')
                raise Exception(f'Attribute transparency is not in the range in 0 to 1!')
        except ValueError as err:
            self.overriding_state_of_buttons_if_calling_errors(state=DISABLED)
            messagebox.showerror(f'{err}', f'Your input for transparency: `{self.entry_alpha.get()}` '
                                 f'is incorrect! Transparency can be a float or '
                                 f'int type!')
            raise ValueError(f'Attribute transparency is not a float or int type!')

        self.is_clicked = True  # enabling disabled buttons after tap button set plotting settings

        if self.is_clicked:
            self.overriding_state_of_buttons_if_calling_errors(state=NORMAL)

        if self.figure == 'Circle':
            self.instance_of_figure = Circle(radius=self.param1)

        elif self.figure == 'Square':
            self.instance_of_figure = Square(length=self.param1)

        elif self.figure == 'Rectangle':
            self.instance_of_figure = Rectangle(length=self.param1, width=self.param2)

        elif self.figure == 'Rhombus':
            self.instance_of_figure = Rhombus(coord_1=self.vertex_1, coord_2=self.vertex_2, coord_3=self.vertex_3,
                                              coord_4=self.vertex_4)

        elif self.figure == 'Trapezoid':
            self.instance_of_figure = Trapezoid(coord_1=self.vertex_1, coord_2=self.vertex_2, coord_3=self.vertex_3,
                                                coord_4=self.vertex_4)

        elif self.figure == 'Triangle':
            self.instance_of_figure = Triangle(coord_1=self.vertex_1, coord_2=self.vertex_2, coord_3=self.vertex_3)

        elif self.figure == 'Sphere':
            self.instance_of_figure = Sphere(radius=self.param1)

        elif self.figure == 'Cube':
            self.instance_of_figure = Cube(length=self.param1)

        elif self.figure == 'Parallelepiped':
            self.instance_of_figure = Parallelepiped(length=self.param1, width=self.param2, height=self.param3)

        elif self.figure == 'Pyramid':
            self.instance_of_figure = Pyramid(length=self.param1, width=self.param2, height=self.param3)

        elif self.figure == 'Cylinder':
            self.instance_of_figure = Cylinder(radius=self.param1, height=self.param3)

        elif self.figure == 'Cone':
            self.instance_of_figure = Cone(radius=self.param1, height=self.param3)

    def calc_area(self):
        """Calculating area of current figure if the function will be called current figure instance"""
        self.label_area = tk.Label(self, text=f'{self.instance_of_figure.area()}', fg=self.fg_additional, width=50)
        self.label_area.grid(row=21, column=0)

    def calc_perimeter(self):
        """Calculating perimeter of current figure if the function will be called current figure instance"""
        self.label_perimeter = tk.Label(self, text=f'{self.instance_of_figure.perimeter()}', fg=self.fg_additional,
                                        width=50)
        self.label_perimeter.grid(row=22, column=0)

    def calc_middle_line(self):
        """Calculating middle line of current figure if the function will be called current figure instance"""
        self.label_middle_line = tk.Label(self, text=f'{self.instance_of_figure.middle_line()}', fg=self.fg_additional,
                                          width=50)
        self.label_middle_line.grid(row=22, column=0)

    def calc_volume(self):
        """Calculating volume of current figure if the function will be called current figure instance"""
        self.label_volume = tk.Label(self, text=f'{self.instance_of_figure.volume()}', fg=self.fg_additional, width=50)
        self.label_volume.grid(row=22, column=0)

    def plotting_graphic(self):
        """Plotting graphic for current figure"""
        self.instance_of_figure.__class__.override_plotting_settings(fill=self.fill, fc=self.fc, ec=self.ec,
                                                                     alpha=self.alpha)
        self.instance_of_figure.plotting_graphic()


class MainApp(tk.Tk):
    """"""
    def __init__(self):
        super().__init__()
        options = {'padx': 187.5, 'pady': 5}
        self.title('Geometric calculator')
        self.geometry('700x800')
        self.iconphoto(True, tk.PhotoImage(file="../../week_3/geometry.png"))
        self.fg_header = 'brown'  # color for header of current figure
        self.fg_main = 'purple'  # color for functions of current figure
        self.fg_additional = 'black'  # color for attributes and variables
        self.figure = 'Circle'  # name of current figure
        self.label = tk.Label(self, text='Hello, This is the geometrical calculator for the 2d and 3d shapes.\n '
                                         'With his help, you can calculate area, perimeter, volume, and median\n '
                                         'lines for the figures from the list below. Also, you can plot graphics\n '
                                         'for the selected shape, visualize the shape!', fg=self.fg_header)
        self.label.grid()
        self.options_of_choice_figures = ['Circle', 'Square', 'Rectangle', 'Rhombus', 'Trapezoid', 'Triangle',
                                          'Sphere', 'Cube', 'Parallelepiped', 'Pyramid', 'Cylinder', 'Cone']
        self.clicked = tk.StringVar()
        self.clicked.set(self.options_of_choice_figures[0])

        self.drop = tk.OptionMenu(self, self.clicked, *self.options_of_choice_figures)
        self.drop.grid(**options)

        self.btn_choice_figure = tk.Button(self, text='Select a shape from the overlying list and click on this button')
        self.btn_choice_figure['command'] = self.selected_figure
        self.btn_choice_figure.grid(**options)

        self.__create_widgets()

    def selected_figure(self):
        self.figure = self.clicked.get()  # selects a shape by the click
        self.__deleted_widgets()  # deletes previous frame
        self.__create_widgets()   # creates new frame

    def __create_widgets(self):
        """Creates a frame"""
        self.frame = ShapeFrame(self, self.figure, self.fg_header, self.fg_main, self.fg_additional)

    def __deleted_widgets(self):
        """Deletes a frame"""
        self.frame.grid_remove()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
