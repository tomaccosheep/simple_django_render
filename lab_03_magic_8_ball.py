'''DJANGO STUFF'''
import os
from django.shortcuts import render
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


'''MAGIC 8 BALL LAB'''
import random
input("What's your question?\n:")
with open('lab_03_out.html', 'w') as f:
    f.write(render(None, 'lab_03_in.html', {'answer': random.choice(['It will happen', "It won't happen"])}).content.decode('utf-8'))
