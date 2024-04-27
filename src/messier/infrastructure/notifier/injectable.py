from di.dependent import Injectable

from .builder import build_notifier
from .interface import Notifier as _NonInjectableNotifier


class Notifier(_NonInjectableNotifier, Injectable, call=build_notifier, scope='request'):
    pass
