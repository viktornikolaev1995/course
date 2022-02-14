"""
Description of attributes and methods and plotting graphics of geometric shapes
"""
import math
from math import pi, sqrt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


class Shape:
    """Base class for geometrical figures"""
    title = 'Shape'
    fill = False
    fc = 'blue'
    ec = 'green'
    alpha = 0.6

    @staticmethod
    def override_limits_of_the_current_axes(*args, **kwargs):
        pass

    @classmethod
    def override_plotting_settings(cls, fill: bool, fc: str, ec: str, alpha: float):
        cls.fill = fill
        cls.fc = fc
        cls.ec = ec
        cls.alpha = alpha

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        return self.title


class Circle(Shape):
    """Geometrical figure: circle"""
    title = 'Circle'

    def __init__(self, radius):
        super(Circle, self).__init__()
        self.radius = radius

    def area(self):
        return f'Area of the {self.title.lower()} is equal: {round(pi * self.radius ** 2, 2)}'

    def perimeter(self):
        return f'Perimeter of the {self.title.lower()} is equal: {round(2 * pi * self.radius, 2)}'

    @staticmethod
    def override_limits_of_the_current_axes(radius):
        return [- 1.3 * radius, 1.3 * radius]

    def plotting_graphic(self):
        ax = plt.subplots()[1]
        circle = plt.Circle((0, 0), self.radius, fill=self.fill, fc=self.fc, ec=self.ec, alpha=self.alpha)
        plt.gca().add_patch(circle)
        plt.axis('scaled')
        x_limits = y_limits = self.override_limits_of_the_current_axes(self.radius)
        plt.xlim(x_limits)
        plt.ylim(y_limits)
        ax.set_title(f'{self.title}')
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.grid(True)
        plt.show()


class Square(Shape):
    """Geometrical figure: square"""
    title = 'Square'

    def __init__(self, length):
        super(Square, self).__init__()
        self.length = length

    def area(self):
        return f'Area of the {self.title.lower()} is equal: {round(self.length ** 2, 2)}'

    def perimeter(self):
        return f'Perimeter of the {self.title.lower()} is equal: {round(self.length * 4, 2)}'

    @staticmethod
    def override_limits_of_the_current_axes(length):
        return [- 1.3 * length + length, 1.3 * length]

    def plotting_graphic(self):
        ax = plt.subplots()[1]
        square = plt.Rectangle((0, 0), self.length, self.length, fill=self.fill, fc=self.fc, ec=self.ec,
                               alpha=self.alpha)
        plt.gca().add_patch(square)
        plt.axis('scaled')
        x_limits = y_limits = self.override_limits_of_the_current_axes(self.length)
        plt.xlim(x_limits)
        plt.ylim(y_limits)
        ax.set_title(f'{self.title}')
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.grid(True)
        plt.show()


class Rectangle(Shape):
    """Geometrical figure: rectangle"""
    title = 'Rectangle'

    def __init__(self, length, width):
        super(Rectangle, self).__init__()
        self.length = length
        self.width = width

    def area(self):
        return f'Area of the {self.title.lower()} is equal: {round(self.length * self.width, 2)}'

    def perimeter(self):
        return f'Perimeter of the {self.title.lower()} is equal: {round(2 * (self.length + self.width), 2)}'

    @staticmethod
    def override_limits_of_the_current_axes(length, width, x_limits=False, y_limits=False):
        if x_limits:
            if length > width:
                return [- 1.3 * length + length, 1.3 * length]
            else:
                k = width / length
                return [(- 1.3 * length + length) * k, (1 + 0.3 * k) * length]
        elif y_limits:
            if length > width:
                k = length / width
                return [(- 1.3 * width + width) * k, (1 + 0.3 * k) * width]
            else:
                return [- 1.3 * width + width, 1.3 * width]

    def plotting_graphic(self):
        ax = plt.subplots()[1]
        rectangle = plt.Rectangle((0, 0), self.length, self.width, fill=self.fill, fc=self.fc, ec=self.ec,
                                  alpha=self.alpha)
        plt.gca().add_patch(rectangle)
        plt.axis('scaled')
        x_limits = self.override_limits_of_the_current_axes(self.length, self.width, x_limits=True)
        y_limits = self.override_limits_of_the_current_axes(self.length, self.width, y_limits=True)
        plt.xlim(x_limits)
        plt.ylim(y_limits)
        ax.set_title(f'{self.title}')
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.grid(True)
        plt.show()


class Rhombus(Shape):
    """Geometrical figure: rhombus"""
    title = 'Rhombus'

    def __init__(self, coord_1='0, 0', coord_2='2, -3', coord_3='4, 0', coord_4='2, 3'):
        super(Rhombus, self).__init__()
        self.coord_1 = self.is_digit(coord_1)
        self.coord_2 = self.is_digit(coord_2)
        self.coord_3 = self.is_digit(coord_3)
        self.coord_4 = self.is_digit(coord_4)
        self.coord = [self.coord_1, self.coord_2, self.coord_3, self.coord_4]
        self.sorting_coordinates(self.coord)
        self.are_the_diagonals_mutually_perpendicular(self.coord)
        self.are_the_sides_plotted_by_points_equal()
        self.side_of_rhombus = self.calc_side_of_rhombus(self.coord[0], self.coord[1])
        self.diagonal_of_rhombus_1 = self.coord[3][0] - self.coord[0][0]
        self.diagonal_of_rhombus_2 = self.coord[2][1] - self.coord[1][1]

    @staticmethod
    def sorting_coordinates(coord):
        coord.sort(key=lambda c: (c[0], c[1]))
        return coord

    @staticmethod
    def are_the_diagonals_mutually_perpendicular(sorted_coord: list):
        if sorted_coord[0][1] != sorted_coord[3][1] or sorted_coord[1][0] != sorted_coord[2][0]:
            raise ValueError("The diagonals of the rhombus should be perpendicular to each other! "
                             "Check the entered coordinates of the points.")
        return True

    def are_the_sides_plotted_by_points_equal(self):
        side_of_rhombus_1 = self.calc_side_of_rhombus(self.coord[0], self.coord[1])
        side_of_rhombus_2 = self.calc_side_of_rhombus(self.coord[1], self.coord[3])
        side_of_rhombus_3 = self.calc_side_of_rhombus(self.coord[3], self.coord[2])
        side_of_rhombus_4 = self.calc_side_of_rhombus(self.coord[2], self.coord[0])
        if len({side_of_rhombus_1, side_of_rhombus_2, side_of_rhombus_3, side_of_rhombus_4}) == 1:
            return True
        raise ValueError("The sides must be equal in the property of the rhombus! "
                         "Check the entered coordinates of the points.")

    @staticmethod
    def calc_side_of_rhombus(coord1: tuple, coord2: tuple):
        return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

    @staticmethod
    def is_digit(coord):
        try:
            coord_x, coord_y = map(float, coord.split(','))
            return coord_x, coord_y

        except ValueError:
            raise ValueError("Check the entered values, the format of the coordinates should be `X, Y`, where X is "
                             "the coordinate on the abscissa axis, Y is the coordinate on the ordinate axis. "
                             "Coordinates X and Y must be a int or float type!")

    def area(self):
        return f'Area of the {self.title.lower()} is equal: ' \
               f'{round(self.diagonal_of_rhombus_1 * self.diagonal_of_rhombus_2 / 2, 2)}'

    def perimeter(self):
        return f'Perimeter of the {self.title.lower()} is equal: {round(self.side_of_rhombus * 4, 2)}'

    @staticmethod
    def override_limits_of_the_current_axes(side_of_rhombus, coord, x_limits=False, y_limits=False):
        if x_limits:
            return [- 0.5 * side_of_rhombus, 0.5 * side_of_rhombus + coord[0][0] + coord[3][0]]
        elif y_limits:
            k = 1 if coord[1][1] < 0 else -1
            k1 = -1 if coord[2][1] < 0 else 1
            return [- 0.5 * side_of_rhombus + k * coord[1][1], 0.5 * side_of_rhombus + k1 * coord[2][1]]

    def plotting_graphic(self):
        ax = plt.subplots()[1]
        x1 = [self.coord[0][0], self.coord[1][0], self.coord[3][0], self.coord[2][0]]
        y1 = [self.coord[0][1], self.coord[1][1], self.coord[3][1], self.coord[2][1]]
        rhombus = patches.Polygon(xy=list(zip(x1, y1)), fill=self.fill, fc=self.fc, ec=self.ec, alpha=self.alpha)
        plt.gca().add_patch(rhombus)
        plt.axis('scaled')
        x_limits = self.override_limits_of_the_current_axes(self.side_of_rhombus, self.coord, x_limits=True)
        y_limits = self.override_limits_of_the_current_axes(self.side_of_rhombus, self.coord, y_limits=True)
        plt.xlim(x_limits)
        plt.ylim(y_limits)
        ax.set_title(f'{self.title}')
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.grid(True)
        plt.show()


class Trapezoid(Shape):
    """Geometrical figure: trapezoid"""
    title = 'Trapezoid'

    def __init__(self, coord_1='1, 2', coord_2='5, 2', coord_3='3, 5', coord_4='4, 5'):
        super(Trapezoid, self).__init__()
        self.coord_1 = self.is_digit(coord_1)
        self.coord_2 = self.is_digit(coord_2)
        self.coord_3 = self.is_digit(coord_3)
        self.coord_4 = self.is_digit(coord_4)
        self.coord = [self.coord_1, self.coord_2, self.coord_3, self.coord_4]
        self.sorting_coordinates(self.coord)
        self.is_smaller_trapezoid_base_parallel_with_large_trapezoid_base(self.coord)
        self.smaller_trapezoid_base = self.coord[3][0] - self.coord[2][0]
        self.large_trapezoid_base = self.coord[1][0] - self.coord[0][0]
        self.height_to_large_trapezoid_base = self.coord[2][1] - self.coord[0][1]

    @staticmethod
    def sorting_coordinates(coord):
        coord.sort(key=lambda c: (c[1], c[0]))
        return coord

    @staticmethod
    def is_smaller_trapezoid_base_parallel_with_large_trapezoid_base(sorted_coord: list):
        if sorted_coord[0][1] != sorted_coord[1][1] or sorted_coord[2][1] != sorted_coord[3][1]:
            raise ValueError("The smaller base and the larger base are not parallel, which contradicts the properties "
                             "of the trapezoid!")
        return True

    @staticmethod
    def is_digit(coord):
        try:
            coord_x, coord_y = map(float, coord.split(','))
            return coord_x, coord_y

        except ValueError:
            raise ValueError("Check the entered values, the format of the coordinates should be `X, Y`, where X is "
                             "the coordinate on the abscissa axis, Y is the coordinate on the ordinate axis. "
                             "Coordinates X and Y must be a int or float type!")

    def area(self):
        area = round(self.height_to_large_trapezoid_base * (self.smaller_trapezoid_base +
                                                            self.large_trapezoid_base) / 2, 2)
        return f'Area of the {self.title.lower()} is equal: {area}'

    def middle_line(self):
        middle_line = (self.smaller_trapezoid_base + self.large_trapezoid_base) / 2
        return f'Middle line of the {self.title.lower()} is equal: {round(middle_line, 2)}'

    @staticmethod
    def override_limits_of_the_current_axes(large_trapezoid_base, coord, x_limits=False, y_limits=False):
        if x_limits:
            return [- 0.5 * large_trapezoid_base, 0.5 * large_trapezoid_base + coord[0][0] + coord[1][0]]
        elif y_limits:
            return [- 0.5 * large_trapezoid_base, 0.5 * large_trapezoid_base + coord[0][1] + coord[3][1]]

    def plotting_graphic(self):
        ax = plt.subplots()[1]
        x1 = [self.coord[0][0], self.coord[1][0], self.coord[3][0], self.coord[2][0]]
        y1 = [self.coord[0][1], self.coord[1][1], self.coord[3][1], self.coord[2][1]]
        trapezoid = patches.Polygon(xy=list(zip(x1, y1)), fill=self.fill, fc=self.fc, ec=self.ec, alpha=self.alpha)
        plt.gca().add_patch(trapezoid)
        plt.axis('scaled')
        x_limits = self.override_limits_of_the_current_axes(self.large_trapezoid_base, self.coord, x_limits=True)
        y_limits = self.override_limits_of_the_current_axes(self.large_trapezoid_base, self.coord, y_limits=True)
        plt.xlim(x_limits)
        plt.ylim(y_limits)
        ax.set_title(f'{self.title}')
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.grid(True)
        plt.show()


class Triangle(Shape):
    """Geometrical figure: triangle"""
    title = 'Triangle'

    def __init__(self, coord_1='1, 2', coord_2='5, 2', coord_3='3, 5'):
        super(Triangle, self).__init__()
        self.coord_1 = self.is_digit(coord_1)
        self.coord_2 = self.is_digit(coord_2)
        self.coord_3 = self.is_digit(coord_3)
        self.coord = [self.coord_1, self.coord_2, self.coord_3]
        self.sorting_coordinates(self.coord)
        self.side_of_triangle_1 = self.calc_side(self.coord[0], self.coord[1])
        self.side_of_triangle_2 = self.calc_side(self.coord[1], self.coord[2])
        self.side_of_triangle_3 = self.calc_side(self.coord[2], self.coord[0])
        self.half_perimeter = self.calc_half_perimeter(self.side_of_triangle_1, self.side_of_triangle_2,
                                                       self.side_of_triangle_3)
        self.max_value_of_side_triangle = self.calc_max_value_of_side_triangle(self.side_of_triangle_1,
                                                                               self.side_of_triangle_2,
                                                                               self.side_of_triangle_3)

    @staticmethod
    def calc_max_value_of_side_triangle(side_1, side_2, side_3):
        return max([side_1, side_2, side_3])

    @staticmethod
    def calc_half_perimeter(side_1, side_2, side_3):
        return (side_1 + side_2 + side_3) / 2

    @staticmethod
    def calc_side(coord1, coord2):
        return sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

    @staticmethod
    def sorting_coordinates(coord):
        coord.sort(key=lambda c: c[0])
        return coord

    @staticmethod
    def is_digit(coord):
        try:
            coord_x, coord_y = map(float, coord.split(','))
            return coord_x, coord_y

        except ValueError:
            raise ValueError("Check the entered values, the format of the coordinates should be `X, Y`, where X is "
                             "the coordinate on the abscissa axis, Y is the coordinate on the ordinate axis. "
                             "Coordinates X and Y must be a int or float type!")

    def area(self):
        area_of_triangle = round(sqrt(self.half_perimeter * (self.half_perimeter - self.side_of_triangle_1) *
                                (self.half_perimeter - self.side_of_triangle_2) *
                                (self.half_perimeter - self.side_of_triangle_3)), 2)

        return f'Area of the {self.title.lower()} is equal: {area_of_triangle}'

    def perimeter(self):
        return f'Perimeter of the {self.title.lower()} is equal: {round(self.half_perimeter * 2, 2)}'

    @staticmethod
    def override_limits_of_the_current_axes(max_value_of_side_triangle, coord, x_limits=False,
                                            y_limits=False):
        if x_limits:
            return [- 0.5 * max_value_of_side_triangle, 0.5 * max_value_of_side_triangle + coord[0][0] + coord[2][0]]
        elif y_limits:
            return [- 0.5 * max_value_of_side_triangle, 0.5 * max_value_of_side_triangle + coord[0][1] + coord[1][1]]

    def plotting_graphic(self):
        ax = plt.subplots()[1]
        x1 = [self.coord[0][0], self.coord[1][0], self.coord[2][0]]
        y1 = [self.coord[0][1], self.coord[1][1], self.coord[2][1]]
        triangle = patches.Polygon(xy=list(zip(x1, y1)), fill=self.fill, fc=self.fc, ec=self.ec, alpha=self.alpha)
        plt.gca().add_patch(triangle)
        plt.axis('scaled')
        x_limits = self.override_limits_of_the_current_axes(self.max_value_of_side_triangle, self.coord, x_limits=True)
        y_limits = self.override_limits_of_the_current_axes(self.max_value_of_side_triangle, self.coord, y_limits=True)
        plt.xlim(x_limits)
        plt.ylim(y_limits)
        ax.set_title(f'{self.title}')
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.grid(True)
        plt.show()


class Sphere(Circle, Shape):
    """Geometrical figure: sphere"""
    title = 'Sphere'

    def __init__(self, radius):
        super(Sphere, self).__init__(radius)

    def area(self):
        return f'Area of the {self.title.lower()} is equal: {round(4 * pi * self.radius ** 2, 2)}'

    def volume(self):
        return f'Volume of the {self.title.lower()} is equal: {round((4 / 3) * pi * self.radius ** 3, 2)}'

    def plotting_graphic(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        u, v = np.mgrid[0:2 * np.pi:50j, 0:np.pi:50j]
        x = (self.radius / 2) * np.cos(u) * np.sin(v)
        y = (self.radius / 2) * np.sin(u) * np.sin(v)
        z = (self.radius / 2) * np.cos(v)

        if self.fill:
            ax.plot_surface(x, y, z, color=self.fc, ec=self.ec, alpha=self.alpha)
        else:
            ax.plot_wireframe(x, y, z, ec=self.ec, alpha=self.alpha)
        ax.set_title(f'{self.title}')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.grid(True)
        plt.show()


class Cube(Square, Shape):
    """Geometrical figure: cube"""
    title = 'Cube'

    def __init__(self, length):
        super(Cube, self).__init__(length)

    def area(self):
        return f'Area of the {self.title.lower()} is equal: {round(6 * self.length ** 2, 2)}'

    def volume(self):
        return f'Volume of the {self.title.lower()} is equal: {round(self.length ** 3, 2)}'

    def plotting_graphic(self):
        points = (self.length / 2) * np.array(
            [[-1, -1, -1],
             [1, -1, -1],
             [1, 1, -1],
             [-1, 1, -1],
             [-1, -1, 1],
             [1, -1, 1],
             [1, 1, 1],
             [-1, 1, 1]]
        )
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        r = [-self.length / 2, self.length / 2]
        x, y = np.meshgrid(r, r)
        z = np.full(4, self.length / 2).reshape(2, 2)

        if self.fill:
            print(self.fc)
            ax.plot_surface(x, y, z, color=self.fc, ec=self.ec, alpha=self.alpha)
            ax.plot_surface(x, y, -z, color=self.fc, ec=self.ec, alpha=self.alpha)
            ax.plot_surface(x, -z, y, color=self.fc, ec=self.ec, alpha=self.alpha)
            ax.plot_surface(x, z, y, color=self.fc, ec=self.ec, alpha=self.alpha)
            ax.plot_surface(z, x, y, color=self.fc, ec=self.ec, alpha=self.alpha)
            ax.plot_surface(-z, x, y, color=self.fc, ec=self.ec, alpha=self.alpha)
        else:
            ax.plot_wireframe(x, y, z, ec=self.ec, alpha=self.alpha)
            ax.plot_wireframe(x, y, -z, ec=self.ec, alpha=self.alpha)
            ax.plot_wireframe(x, -z, y, ec=self.ec, alpha=self.alpha)
            ax.plot_wireframe(x, z, y, ec=self.ec, alpha=self.alpha)
            ax.plot_wireframe(z, x, y, ec=self.ec, alpha=self.alpha)
            ax.plot_wireframe(-z, x, y, ec=self.ec, alpha=self.alpha)

        ax.scatter3D(points[:, 0], points[:, 1], points[:, 2], facecolors='white', edgecolors='white', alpha=0)
        ax.set_title(f'{self.title}')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.grid(True)
        plt.show()


class Parallelepiped(Rectangle, Shape):
    """Geometrical figure: parallelepiped"""
    title = 'Parallelepiped'

    def __init__(self, length, width, height):
        super(Parallelepiped, self).__init__(length, width)
        self.height = height

    def area(self):
        return f'Area of the {self.title.lower()} is equal: {round(6 * self.length ** 2, 2)}'

    def volume(self):
        return f'Volume of the {self.title.lower()} is equal: {round(self.length ** 3, 2)}'

    def plotting_graphic(self):
        max_value = max([self.length, self.width, self.height])
        points = 1.3 * (max_value / 2) * np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [-1, -1, 1],
                                               [1, -1, 1], [1, 1, 1], [-1, 1, 1]])
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        xvalues = [-self.length / 2, self.length / 2]
        yvalues = [-self.width / 2, self.width / 2]
        x, y = np.meshgrid(xvalues, yvalues)
        z = np.full(4, self.height / 2).reshape(2, 2)

        if self.fill:
            # plane XY
            ax.plot_surface(x, y, z, color=self.fc, ec=self.ec, alpha=self.alpha)
            ax.plot_surface(x, y, -z, color=self.fc, ec=self.ec, alpha=self.alpha)
            # plane XZ
            y[1] = -1 * y[1]
            z[0] = -1 * z[0]
            ax.plot_surface(x, y, z, color=self.fc, ec=self.ec, alpha=self.alpha)
            ax.plot_surface(-x, -y, z, color=self.fc, ec=self.ec, alpha=self.alpha)
            # plane YZ
            x[0][1] = -1 * x[0][1]
            x[1][1] = x[0][1]
            y[0][0] = -1 * y[0][0]
            y[1][0] = -1 * y[1][0]
            ax.plot_surface(x, y, z, color=self.fc, ec=self.ec, alpha=self.alpha)
            ax.plot_surface(-x, -y, z, color=self.fc, ec=self.ec, alpha=self.alpha)
        else:
            # plane XY
            ax.plot_wireframe(x, y, z, ec=self.ec, alpha=self.alpha)
            ax.plot_wireframe(x, y, -z, ec=self.ec, alpha=self.alpha)
            # plane XZ
            y[1] = -1 * y[1]
            z[0] = -1 * z[0]
            ax.plot_wireframe(x, y, z, ec=self.ec, alpha=self.alpha)
            ax.plot_wireframe(-x, -y, z, ec=self.ec, alpha=self.alpha)
            # plane YZ
            x[0][1] = -1 * x[0][1]
            x[1][1] = x[0][1]
            y[0][0] = -1 * y[0][0]
            y[1][0] = -1 * y[1][0]
            ax.plot_wireframe(x, y, z, ec=self.ec, alpha=self.alpha)
            ax.plot_wireframe(-x, -y, z, ec=self.ec, alpha=self.alpha)

        ax.scatter3D(points[:, 0], points[:, 1], points[:, 2], facecolors='white', edgecolors='white', alpha=0)
        ax.set_title(f'{self.title}')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.grid(True)
        plt.show()


class Pyramid(Rectangle, Shape):
    """Geometrical figure: pyramid"""
    title = 'Pyramid'

    def __init__(self, length, width, height):
        super(Pyramid, self).__init__(length, width)
        # the surface area of the pyramid
        self.area_base = self.length * self.width
        # the height lowered from the top of the pyramid to the intersection point of the diagonals of the pyramid
        self.height = height

    @staticmethod
    def calc_height_of_edge_surface_of_pyramid(length, height):
        return sqrt((length / 2) ** 2 + height ** 2)

    def area(self):
        area_of_pyramid = None
        if self.width == self.length:
            height_of_edge_surface_of_pyramid = self.calc_height_of_edge_surface_of_pyramid(self.length, self.height)
            area_of_pyramid = self.area_base + 4 * (0.5 * self.length * height_of_edge_surface_of_pyramid)

        elif self.width != self.length:
            height_of_edge_surface_of_pyramid_1 = self.calc_height_of_edge_surface_of_pyramid(self.length, self.height)
            height_of_edge_surface_of_pyramid_2 = self.calc_height_of_edge_surface_of_pyramid(self.width, self.height)
            area_of_pyramid = self.area_base + 2 * (0.5 * self.width * height_of_edge_surface_of_pyramid_1) \
                              + 2 * (0.5 * self.length * height_of_edge_surface_of_pyramid_2)
        return f'Area of the {self.title.lower()} is equal: {round(area_of_pyramid, 2)}'

    def volume(self):
        return f'Volume of the {self.title.lower()} is equal: {round((1 / 3) * self.area_base * self.height, 2)}'

    def plotting_graphic(self):
        max_value = max([self.length, self.width, self.height])
        points = 1.3 * (max_value / 2) * np.array(
            [[-1, -1, -1],
             [1, -1, -1],
             [1, 1, -1],
             [-1, 1, -1],
             [0, 0, 1]]
        )
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # vertices of a pyramid
        v = np.array([[-self.length / 2, -self.width / 2, -self.height / 2],
                      [self.length / 2, -self.width / 2, -self.height / 2],
                      [self.length / 2, self.width / 2, -self.height / 2],
                      [-self.length / 2, self.width / 2, -self.height / 2],
                      [0, 0, self.height / 2]])

        # generate list of sides' polygons of our pyramid
        verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]], [v[2], v[1], v[4]], [v[3], v[2], v[4]], [v[3], v[0], v[4]],
                 [v[0], v[1], v[2], v[3]]]
        # plot sides
        if self.fill:
            ax.add_collection3d(Poly3DCollection(verts, color=self.fc, ec=self.ec, linewidths=1, alpha=self.alpha))
        else:
            ax.add_collection3d(Line3DCollection(verts, ec=self.ec, linewidths=1, alpha=self.alpha))

        ax.scatter3D(points[:, 0], points[:, 1], points[:, 2], facecolors='white', edgecolors='white', alpha=0)
        ax.set_title(f'{self.title}')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.grid(True)
        plt.show()


class Cylinder(Shape):
    """Geometrical figure: cylinder"""
    title = 'Cylinder'
    center_x = 0
    center_y = 0

    def __init__(self, radius, height):
        super(Cylinder, self).__init__()
        self.radius = radius
        self.height = height

    def area(self):
        area_of_cylinder = 2 * pi * self.radius * (self.height + self.radius)
        return f'Area of the {self.title.lower()} is equal: {round(area_of_cylinder, 2)}'

    def volume(self):
        return f'Volume of the {self.title.lower()} is equal: {round(pi * self.radius ** 2 * self.height, 2)}'

    def plotting_graphic(self):
        max_value = max([self.radius, self.height])
        points = 1.2 * (max_value / 2) * np.array(
            [[-1, -1, -1],
             [1, -1, -1],
             [1, 1, -1],
             [-1, 1, -1],
             [0, 0, 1]]
        )
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        z_ = np.linspace(-self.height / 2, self.height / 2, 50)
        theta = np.linspace(0, 2 * np.pi, 50)
        theta_grid, z = np.meshgrid(theta, z_)
        x = (self.radius / 2) * np.cos(theta_grid) + self.center_x
        y = (self.radius / 2) * np.sin(theta_grid) + self.center_y
        if self.fill:
            ax.plot_surface(x, y, z, color=self.fc, ec=self.ec, alpha=self.alpha)
        else:
            ax.plot_wireframe(x, y, z, ec=self.ec, alpha=self.alpha)
        ax.scatter3D(points[:, 0], points[:, 1], points[:, 2], facecolors='white', edgecolors='white', alpha=0)
        ax.set_title(f'{self.title}')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.grid(True)
        plt.show()


class Cone(Cylinder, Shape):
    """Geometrical figure: cone"""
    title = 'Cone'

    def __init__(self, radius, height):
        super(Cone, self).__init__(radius, height)

    @staticmethod
    def calc_length_of_forming_cone(radius, height):
        return sqrt(radius ** 2 + height ** 2)

    def area(self):
        edge_area_of_cone = pi * self.radius * self.calc_length_of_forming_cone(self.radius, self.height)
        base_area_of_cone = pi * self.radius ** 2
        return f'Area of the {self.title.lower()} is equal: {round(edge_area_of_cone + base_area_of_cone, 2)}'

    def volume(self):
        return f'Volume of the {self.title.lower()} is equal: {round((1 / 3) * pi * self.radius ** 2 * self.height, 2)}'

    def plotting_graphic(self):
        max_value = 1.3 * max([self.radius, self.height])
        points = 1 * (max_value / 2) * np.array(
            [[-1, -1, -1],
             [1, -1, -1],
             [1, 1, -1],
             [-1, 1, -1],
             [0, 0, 1]]
        )
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        r_ = np.linspace(-self.radius / 2, 0, 50)
        theta = np.linspace(0, 2 * np.pi, 50)
        theta_grid, r = np.meshgrid(theta, r_)
        x = r * np.cos(theta_grid) + self.center_x
        y = r * np.sin(theta_grid) + self.center_y
        z_ = np.linspace(-self.height / 2, self.height / 2, 50)
        z = np.meshgrid(theta, z_)[1]

        if self.fill:
            ax.plot_surface(x, y, z, color=self.fc, ec=self.ec, alpha=self.alpha)
        else:
            ax.plot_wireframe(x, y, z, ec=self.ec, alpha=self.alpha)
        ax.scatter3D(points[:, 0], points[:, 1], points[:, 2], facecolors='white', edgecolors='white', alpha=0)
        ax.set_title(f'{self.title}')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.grid(True)
        plt.show()

