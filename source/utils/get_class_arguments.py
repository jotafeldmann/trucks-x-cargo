from inspect import signature


def get_class_arguments_order(class_ref):
    return [params for params in signature(class_ref).parameters]
