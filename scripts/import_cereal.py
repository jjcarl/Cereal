#!/usr/bin/env python

import csv
import os
import sys

sys.path.append("..")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_cereal.settings')

from main.models import Cereal, CerealMaker

cereal_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cereals.csv')

csv_file = open(cereal_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    new_maker = CerealMaker()
    new_maker.manufacturer = row['Manufacturer']
    new_maker.save()

    new_cereal = Cereal()
    new_cereal.manufacturer = new_maker
    new_cereal.name = row['Cereal Name']
    new_cereal.kind = row['Type']
    try:
        new_cereal.calories = int(row['Calories'])
    except Exception, e:
        print e
        print row['Calories']

    try:
        new_cereal.protein = int(row['Protein (g)'])
    except Exception, e:
        print e
        print row['Protein (g)']

    try:
        new_cereal.fat = int(row['Fat'])
    except Exception, e:
        print e
        print row['Fat']

    try:
        new_cereal.sodium = int(row['Sodium'])
    except Exception, e:
        print e
        print row['Sodium']

    try:
        new_cereal.fiber = float(row['Dietary Fiber'])
    except Exception, e:
        print e
        print row['Dietary Fiber']

    try:
        new_cereal.carbs = float(row['Carbs'])
    except Exception, e:
        print e
        print row['Carbs']

    try:
        new_cereal.sugars = int(row['Sugars'])
    except Exception, e:
        print e
        print row['Sugars']

    try:
        new_cereal.shelf = int(row['Display Shelf'])
    except Exception, e:
        print e
        print row['Display Shelf']

    try:
        new_cereal.potassium = int(row['Potassium'])
    except Exception, e:
        print e
        print row['Potassium']

    try:
        new_cereal.vitamins = int(row['Vitamins and Minerals'])
    except Exception, e:
        print e
        print row['Vitamins and Minerals']

    try:
        new_cereal.serving_size_weight = float(row['Serving Size Weight'])
    except Exception, e:
        print e
        print row['Serving Size Weight']

    try:
        new_cereal.cups_per_serving = float(row['Cups per Serving'])
    except Exception, e:
        print e
        print row['Cups per Serving']

    new_cereal.save()


csv_file.close()
