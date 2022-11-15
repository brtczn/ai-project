import pandas
import pygame
from sklearn.tree import DecisionTreeClassifier


def predict_from_decision_tree(age, sex, vegetarian, budget, d_type, temperature, weight):
    dataset = pandas.read_csv("decision_tree/tests.csv")
    # print(dataset)

    d = {'F': 1, 'M': 2}
    dataset['Sex'] = dataset['Sex'].map(d)
    d = {'NO': 0, 'YES': 1}
    dataset['Vegetarian'] = dataset['Vegetarian'].map(d)
    d = {'LOW': 1, 'AVERAGE': 2, 'HIGH': 3}
    dataset['Budget'] = dataset['Budget'].map(d)
    d = {'MAIN': 1, 'DESSERT': 2}
    dataset['Type'] = dataset['Type'].map(d)
    d = {'COLD': 1, 'HOT': 2}
    dataset['Temperature'] = dataset['Temperature'].map(d)
    d = {'LIGHT': 1, 'HEAVY': 2}
    dataset['Weight'] = dataset['Weight'].map(d)
    d = {'SOUP': 1, 'SCALLOPS': 2, 'CHICKEN': 3, 'PORKCHOP': 4,
         'RISOTTO': 5, 'DUCK': 6, 'STEAK': 7, 'RATATOUILLE': 8,
         'ICECREAM': 9, 'PAVLOVA': 10, 'PANNACOTTA': 11, 'SOUFFLE': 12}
    dataset['Dish'] = dataset['Dish'].map(d)

    features = ['Age', 'Sex', 'Vegetarian', 'Budget', 'Type', 'Temperature', 'Weight']

    x = dataset[features]
    y = dataset['Dish']

    decision_tree = DecisionTreeClassifier()
    decision_tree = decision_tree.fit(x.values, y)

    # export tree.dot
    # data = tree.export_graphviz(decision_tree, out_file='tree.dot', feature_names=features)

    # legend
    # age
    # sex          1 - Female,     2 - Male
    # vegetarian   0 - No,         1 - Yes
    # budget       1 - Low,        2 - Average,      3 - High
    # type         1 - Main,       2 - Dessert
    # temperature  1 - Cold,       2 - Hot
    # weight       1 - Light,      2 - Heavy
    # dish         1 - Soup,       2 - Scallops,     3 - Chicken,
    #              4 - Pork chop,  5 - Risotto,      6 - Duck,
    #              7 - Steak,      8 - Ratatouille,  9 - Ice Cream,
    #              10 - Pavlova,   11 - Panna Cotta  12 - Souffle

    predict = decision_tree.predict([[age, sex, vegetarian, budget, d_type, temperature, weight]])
    return predict


def dish_name(number):
    print('Selected dish: ')
    if number == [1]:
        print('Soup')
        return 'Soup'
    if number == [2]:
        print('Scallops')
        return 'Scallops'
    if number == [3]:
        print('Chicken')
        return 'Chicken'
    if number == [4]:
        print('Pork chop')
        return 'Pork chop'
    if number == [5]:
        print('Risotto')
        return 'Risotto'
    if number == [6]:
        print('Duck')
        return 'Duck'
    if number == [7]:
        print('Steak')
        return 'Steak'
    if number == [8]:
        print('Ratatouille')
        return 'Ratatouille'
    if number == [9]:
        print('Ice cream')
        return 'Ice cream'
    if number == [10]:
        print('Pavlova')
        return 'Pavlova'
    if number == [11]:
        print('Panna Cotta')
        return 'Panna Cotta'
    if number == [12]:
        print('Souffle')
        return 'Souffle'


