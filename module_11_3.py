from pprint import pprint


def introspection_info(obj):
    dict_ = {'type': type(obj).__name__,
             'attributes': [x for x in dir(obj) if not callable(getattr(obj, x))],
             'methods': [y for y in dir(obj) if callable(getattr(obj, y))],
             'module': introspection_info.__module__}
    return dict_


number_info = introspection_info(42)
pprint(number_info)
