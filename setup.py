from setuptools import setup

setup(
    name='google_api_service_helper',
    version='0.0.3',
    description='A simple library for convenient work with the Google API for'
                ' Drive and Sheets',
    url='',
    install_requires=[
        'httplib2',
        'oauth2client',
        'google-api-python-client',
    ],
    packages=['google_api_service_helper'],
    author_email='sergey.natalenko@mail.ru',
    author='Sergey Natalenko',
)
