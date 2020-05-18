import os

class Config:
    """
    Config class to store all the configuration
    for the application

    Usage:
        Config
    """

    #General information
    FLASK_APP = os.environ.get('FLASK_APP','binational_amazon')
    ENV = os.environ.get('ENVIROMENT', 'dev')