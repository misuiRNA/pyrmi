import sys

this = sys.modules[__name__]


def register_real_class(klass, alias=None):
    if not klass or not isinstance(klass, type):
        raise Exception(f"[invalid class] {klass} is not a valid class!")
    if not alias:
        alias = klass.__name__
    setattr(this, alias, klass)
