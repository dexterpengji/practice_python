import matplotlib.pyplot as plt


class Map:
    def __init__(self, size_height=30, size_width=40, resolution=10):
        self.size_height = size_height  # unit: m
        self.size_width = size_width  # unit: m
        self.resolution = resolution  # unit: dots per m2
        self.map_Matrix = []
        for x in range(size_height * resolution):
            self.map_Matrix.append([0 for y in range(size_width * resolution)])

    def show(self):
        plt.figure('MAP', facecolor='w')
        ax = plt.gca()
        ax.spines['left'].set_color('none')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        plt.ylim(0, self.size_height)
        plt.xlim(0, self.size_width)
        ax.spines['bottom'].set_position(('data', 0))
        maloc = plt.MultipleLocator(1)
        miloc = plt.MultipleLocator(0.1)
        ax.xaxis.set_major_locator(maloc)
        ax.xaxis.set_minor_locator(miloc)
        ax.grid(which='minor', axis='x', color='orange', linestyle=':', linewidth=0.75)
        print(len(self.map_Matrix), len(self.map_Matrix[0]))
        plt.show()


if __name__ == '__main__':
    map_test = Map(10, 10, 100)
    map_test.show()
