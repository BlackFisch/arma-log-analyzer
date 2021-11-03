#!/usr/bin/env python3

PATTERNS = {
    'Overwriting config class': [
        r'\d\d:\d\d:\d\d Conflicting addon .*[\r\n]{0,}',
        'There are classes defined in multiple config files. This might cause unwanted problems.'
    ]
}
