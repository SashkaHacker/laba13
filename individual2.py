#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from statistics import median, mean, stdev


def calculate_statistic(**data):
    dct = {key: {'mean': mean(value), 'median': median(value),
                 'std_dev': round(stdev(value), 2)}
           for key, value in data.items()}
    return dct


if __name__ == "__main__":
    stats = calculate_statistic(ages=[23, 45, 16, 37, 31],
                                scores=[85, 90, 78, 92, 88])
    print(stats)
