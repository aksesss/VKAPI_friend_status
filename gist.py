import matplotlib.pyplot as plt


class Gist:
    # данные гистаграммы

    def __init__(self, age_list):
        self._ages_list = sorted(age_list)
        self.age_dictionary = dict()
        for age in self._ages_list:
            self.age_dictionary.update(
                {age: self.age_dictionary.get(age, 0) + 1})

    def get_data(self):
        return self._ages_list

    def printGist(self):
        for age, count in self.age_dictionary.items():  # dict.items возвращает пары
            print(str(age).ljust(4) + ":" + "#" * count)

    def showBar(self, title1, title_x, title_y):
        plt.bar(list(self.age_dictionary.keys()),
                self.age_dictionary.values(), color='g', width=0.9, linewidth=20)
        plt.show()
