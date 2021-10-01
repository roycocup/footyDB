from datetime import datetime, timedelta 
import pickle 
import os
import json
from hashlib import md5

class cached:
    
    def __call__(self, func):
        def p(o):
            print(o)
            quit()

        def inner(*args, **kwargs):
            name = func.__name__ 
            hashed_args = md5(str.encode(json.dumps(kwargs))).hexdigest()
            filename = name + "-" + hashed_args[:6] + ".pkl"
            if os.path.isfile(filename):
                with open(filename, 'rb') as f:
                    data = pickle.load(f)
            else:
                data = func(**kwargs)
                with open(filename, 'wb') as f:
                    pickle.dump(data, f)

            return data
        return inner