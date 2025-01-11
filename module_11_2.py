import inspect
from pprint import (pprint)


def introspection_info(obj):
    obj_type = type(obj)

    attributes = dir(obj)

    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    attrs_only = [attr for attr in attributes if not callable(getattr(obj, attr))]

    module = inspect.getmodule(obj)

    info = {'тип объекта': obj_type,
            'атрибут': attrs_only,
            'методы объекта': methods,
            'модуль': module,
            'идентификатор': id(obj),
            'документация': obj.__doc__}
    return info


number_info = introspection_info(46)
print(number_info)
pprint(dir(number_info))



