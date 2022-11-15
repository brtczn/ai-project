from classes.searching.a_star_strategy import a_star_strategy
from classes.searching.bfsstrategy import bfs


testPath = [(1, 1), (2, 13), (13, 4), (3, 7), (4, 11), (3, 0)]

temp_grd = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13],
            [0, 14], [1, 1], [1, 2], [1, 5], [1, 6], [1, 9], [1, 10], [1, 13], [1, 14], [1, 15], [2, 1], [2, 2], [2, 5],
            [2, 6], [2, 9], [2, 10], [2, 13], [2, 14], [2, 15], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6],
            [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [3, 15], [4, 0], [4, 1], [4, 2],
            [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12], [4, 13], [4, 14],
            [4, 15], [5, 1], [5, 2], [5, 5], [5, 6], [5, 9], [5, 10], [5, 13], [5, 14], [5, 15], [6, 1], [6, 2], [6, 5],
            [6, 6], [6, 9], [6, 10], [6, 13], [6, 14], [6, 15], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7],
            [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [7, 14], [8, 4], [8, 5], [9, 4], [9, 5], [10, 4],
            [10, 5], [11, 4], [11, 5], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11],
            [13, 4], [13, 5], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11]]

tuple_grid = [tuple(x) for x in temp_grd]

bfs_path = bfs((2, 13), (13, 12), "Right", tuple_grid)

banan = 3
water = 10
G_cost = [
    [0, 0, water, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, water, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, banan, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, water, 0, 0, 0, banan, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, water, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, banan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, water, 0],
    [0, 0, 0, 0, 0, water, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, banan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, banan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, water, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, banan, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, water, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, water, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

seats = {1: (1, 0), 2: (2, 0), 3: (5, 0), 4: (6, 0),
         5: (1, 3), 6: (2, 3), 7: (5, 3), 8: (6, 3),
         9: (1, 4), 10: (2, 4), 11: (5, 4), 12: (6, 4),
         13: (1, 7), 14: (2, 7), 15: (5, 7), 16: (6, 7),
         17: (1, 8), 18: (2, 8), 19: (5, 8), 20: (6, 8),
         21: (1, 11), 22: (2, 11), 23: (5, 11), 24: (6, 11),
         25: (1, 12), 26: (2, 12), 27: (5, 12), 28: (6, 12)
         }

free_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

meal_deposit = {1: (14, 4), 2: (14, 5), 3: (14, 6), 4: (14, 7),
                5: (14, 8), 6: (14, 9), 7: (14, 10), 8: (14, 11)}

free_deposits = [1, 2, 3, 4, 5, 6, 7, 8]

