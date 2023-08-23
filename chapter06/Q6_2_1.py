class Cylinder:
    """円柱"""

    pi = 3.14

    def __init__(self, radius=1, height=1):
        """円柱を特徴づける属性"""
        self.radius = float(radius)
        self.height = float(height)

    def calc_base_area(self):
        """底面積を計算"""
        pi = Cylinder.pi
        r = self.radius
        return pi * r * r

    def calc_side_area(self):
        """側面積の計算"""
        pi = Cylinder.pi
        r = self.radius
        h = self.height
        return 2 * pi * r * h

    def calc_surface_area(self):
        """表面積の計算"""
        c = self.calc_base_area()
        s = self.height
        return c * s

    def show_results(self):
        """属性を計算結果を見せる"""
        r = self.radius
        h = self.height
        S = self.calc_surface_area()
        V = self.calc_volume()
        print("半径: {}, 高さ: {}, 表面積: {}, 体積: {}".format(r, h, S, V))
