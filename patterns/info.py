#!/usr/bin/env python3

PATTERNS = {
    'Stringtable entries missing': [
        r'\d\d:\d\d:\d\d Unsupported language \w+ in stringtable[\r\n]{0,}\d\d:\d\d:\d\d .* Context: .*[\r\n]{0,}',
        'The stringtable file specified in the error does not have entries in the specified language for every string.'
    ],
    'Missing characters in (mod) config file': [
        r'\d\d:\d\d:\d\d File .* Missing .*[\r\n]{0,}',
        'There are characters missing, most of the times a comma or semicolon, in the specified config file.'
    ]
}
