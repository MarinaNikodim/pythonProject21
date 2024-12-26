import inspect
from pprint import (pprint)


def introspection_info(obj):
    obj_type = type(obj)

    attributes = dir(obj)

    methods = [method for method in attributes if callable(getattr(obj, method))]

    module = inspect.getmodule(obj)

    info = {'тип объекта': obj_type,
            'атрибут': attributes,
            'методы объекта': methods,
            'модуль': module,
            'идентификатор': id(obj),
            'документация': obj.__doc__}
    return info


number_info = introspection_info(42)
print(number_info)
pprint(dir(number_info))



