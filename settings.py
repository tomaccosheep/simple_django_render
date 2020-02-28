import os

'''Figure out where the files are'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

'''Mandatory security thing'''
SECRET_KEY = 'fd%2osofj^h67%tg!#owt9yr-^_hqri=hv+iagmq-2m1ov0&+k'

TEMPLATES = [
           {
                       'BACKEND': 'django.template.backends.django.DjangoTemplates',
                        'DIRS': [BASE_DIR],
                    },
]
