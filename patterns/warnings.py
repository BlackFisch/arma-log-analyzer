#!/usr/bin/env python3

PATTERNS = {
    'CBA: Class does not support Extended Eventhandlers': [
        r'\d\d:\d\d:\d\d \[CBA\] \(xeh\) WARNING: .*[\r\n]{0,}',
        'For more information, please consult the <a href="https://github.com/CBATeam/CBA_A3/wiki/Advanced-XEH" target="_blank">CBA Wiki on Github</a>.'
    ],
    'CBA Framework Warning': [
        r'\d\d:\d\d:\d\d \[\w+\] \(\w+\) WARNING: .*[\r\n]{0,}',
        'This error was emitted by an addon using CBA. See error message for more information.'
    ],
    'Warning: No Entry': [
        r'\d\d:\d\d:\d\d Warning Message: No entry .*[\r\n]{0,}',
        'A config class is missing an attribute. This can be caused by outdated mods using legacy parent classes. Consider removing them or inheriting from something like <code>class ThingX</code>'
    ],
    'Warning: not a value': [
        r'\d\d:\d\d:\d\d Warning Message: .* is not a value[\r\n]{0,}',
        'An attribute of a config class has an invalid value. This can be caused by outdated mods. Consider removing them or try to find the value causing the problem. This might be hard, since most of the times the class is unknown.'
    ],
    'Error creating ....': [
        r'\d\d:\d\d:\d\d Warning Message: Error: creating .* with scope=private[\r\n]{0,}',
        'A class with entry <code>scope=private</code> or <code>scope=0</code> was tried to be instantiated. Consider changing the entry to <code>scope=2</code>.'
    ],
    "Warning: not an array": [
        r'\d\d:\d\d:\d\d Warning Message: .*not an array[\r\n]{0,}',
        'The specified config attribute was expected to be an array but is not. Fixing this might be hard, since most of the times the class is unknown.'
    ],
    'Bone doesn\'t exist': [
        r'\d\d:\d\d:\d\d Error: Bone .* doesn\'t exist in skeleton .*[\r\n]{0,}',
        'There is bones missing in the specified skeleton. This might be caused by ported content from an older ArmA title. This has to be fixed in the model.'
    ],
}
