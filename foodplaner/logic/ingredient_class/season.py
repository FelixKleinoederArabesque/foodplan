import numpy as np


class Season:

    month_start: int
    month_end: int

    def __init__(self):
        pass

    def __init__(self, month_start: int, month_end: int):
        self.month_start = month_start
        self.month_end = month_end

    def copy(self):
        new_item = Season(month_start=self.month_start, month_end=self.month_end)
        return new_item


def get_season_distribution(items: list[Season]):

    output = {}
    for i in range(0, 13):
        output.update({i: 0})

    for i in items:
        item: Season = i.copy()

        if item.month_end < item.month_start:
            item.month_end += 13

        for month in range(item.month_start, item.month_end + 1):
            output[month % 13] += 1

    # Normalize
    denominator = sum(output.values())
    for key in output.keys():
        output[key] = np.round(output[key] / denominator, 2)

    return output
