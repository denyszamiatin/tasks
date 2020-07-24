import configparser


config = configparser.ConfigParser()
config.read('tasks.ini')


def get_serializer():
    if config['Serializer']['format'] == 'json':
        from serializers import json_
        return json_.JsonSerializer()
    elif config['Serializer']['format'] == 'pickle':
        from serializers import pickle_
        return pickle_.PickleSerializer()
    else:
        raise ImportError
