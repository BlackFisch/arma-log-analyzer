#!/usr/bin/env python3

from _pyio import TextIOWrapper
from re import findall
from enum import Enum
from patterns import debug, info, warnings, errors, fatal
from flask_babel import gettext


class Loglevel(Enum):
    DEBUG = [0, debug.PATTERNS]
    INFO = [1, info.PATTERNS]
    WARNING = [2, warnings.PATTERNS]
    ERROR = [3, errors.PATTERNS]
    FATAL = [4, fatal.PATTERNS]


def analyze_logfile(file: TextIOWrapper, verbosity_level: Loglevel):

    (verbosity_level, _) = verbosity_level.value
    f_content = file.read()
    found = {}

    for level in Loglevel:
        (prio, patterns) = level.value
        if prio < verbosity_level:
            continue

        found[level.name] = []

        for p_name, val in patterns.items():
            (pattern, desc) = val

            matches = [match[0].split('\n')
                       for match in findall(rf'({pattern})', f_content)]
            if not matches:
                continue
            found[level.name].append([p_name, desc, matches])

    return found
