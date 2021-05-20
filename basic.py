import hashlib
from wrenchbox.object import Dict2StrSafe
class Base(Dict2StrSafe):
    def hash(self):
        return hashlib.sha1(str(self.__dict__).encode()).hexdigest()