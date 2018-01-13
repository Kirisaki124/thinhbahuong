import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds247327.mlab.com:47327/thinhbahuong

host = 'ds247327.mlab.com'
port = 47327
db_name = "thinhbahuong"
user_name = "admin"
password = "admin"

def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
