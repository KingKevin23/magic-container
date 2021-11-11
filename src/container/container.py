from os import environ
from threading import Semaphore

from sqlitedict import SqliteDict

from .errors import VirtualEnvError

class Container:

    def __init__(self):
        try:
            path = environ["VIRTUAL_ENV"]
        except KeyError:
            raise VirtualEnvError("There was no virtual environment found!")

        path += "/container.db"
        self._storage = SqliteDict(filename=path, tablename="data", autocommit=True)
        self._semaphore = Semaphore()

    def __getitem__(self, key:str) -> object:
        return self.get(key)

    def get(self, key:str, setter=None) -> object:
        with self._semaphore:
            try:
                return self._storage[key]
            except KeyError:
                if setter:
                    value = setter()
                    self._storage[key] = value
                    return value
                else:
                    raise

    def __setitem__(self, key:str, value:object):
        self.set(key, value)

    def set(self, key:str, value:object):
        with self._semaphore:
            self._storage[key] = value

    def __delitem__(self, key:str):
        self.delete(key)

    def delete(self, key:str):
        with self._semaphore:
            del self._storage[key]