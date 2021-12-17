import appdirs
import pathlib
import toml
import logging
import importlib

def SaveClient(name, client_type, url, key, overwrite = False, *args, **kwargs):
    APPNAME = "GradeStar"
    dir = appdirs.user_config_dir(appname=APPNAME)
    path = pathlib.Path(dir)
    if not path.exists():
        path.mkdir(parents=True)

    client_path = path / "clients.toml"
    if not client_path.exists():
        client_path.touch()
    
    data = toml.load(client_path)
    if name in data.keys():
        if not overwrite:
            logging.error("Client {} already saved!".format(name))
            return
        else:
            logging.warning("Client {} will be overwritten".format(name))
    
    payload = {"client_type": client_type, "url": url, 'api_key': key}
    data.update({name: payload})
    with open(client_path, 'w') as f:
        toml.dump(data, f)


def GetClient(name, *args, **kwargs):
    APPNAME = "GradeStar"
    dir = appdirs.user_config_dir(appname=APPNAME)
    path = pathlib.Path(dir) / "clients.toml"
    if not path.exists():
        logging.error("Unable to find any saved clients!")
        return
    
    data = toml.load(path)
    if name not in data.keys():
        logging.error("Unable to find client {}".format(name))

    data = data[name]
    client_type = data['client_type']
    try:
        modname = "gradestar.clients.{}".format(client_type)
        module = importlib.import_module(modname)

    except Exception as e:
        print(e)
        logging.error("Unable to import client type {}".format(client_type))
        return
    
    try:
        f = getattr(module, "GetClient")
        return f(**data)
    except Exception as e:
        print(e)
        logging.error("Unable to find GetClient method in module {}".format(name))

