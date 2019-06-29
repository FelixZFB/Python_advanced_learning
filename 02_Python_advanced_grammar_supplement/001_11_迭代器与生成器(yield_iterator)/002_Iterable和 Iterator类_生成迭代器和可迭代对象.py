# -*- coding:utf-8 -*-

import requests
from collections import Iterable, Iterator

# Iterable, Iterator是可迭代对象和迭代器的类

# 定义一个天气的迭代器，继承迭代器类
class WeatherIterator(Iterator):

    def __init__(self):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'http://www.tianqi.com/{}/'.format(city))
        print(r.status_code)
        data = r.json()
        return data.title

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeatherIterable(Iterable):

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterable(['shanghai', 'chengdu', 'beijing']):
    print(x)












