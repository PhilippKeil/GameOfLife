__author__ = 'philipp'

class Grid():
    # marker indices:
    # 0 : empty
    # 1 : occupied

    def __init__(self, size_x, size_y, markers):
        self.size_x = size_x
        self.size_y = size_y

        self.__storage = []
        self.markers = markers
        self.init_grid()

    def init_grid(self):
        # Fill the grid with nothing (marker 0) for the first time
        for y in range(self.size_y):
            self.__storage.append([])

            for x in range(self.size_x):
                self.__storage[y].append(self.markers[0])

    def return_grid(self):
        return self.__storage

    def write_to_grid(self, coord_x, coord_y, marker_index):
        self.__storage[coord_y][coord_x] = self.markers[marker_index]

    def is_empty(self, coord_x, coord_y):
        if self.__storage[coord_y][coord_x] == self.markers[0]:
            return True
        else:
            return False
