#!/usr/bin/env python3
from .common import TIMESTAMP as TS
from .common import NEWLINE as NL

PATTERNS = {
    'Embedded skeleton differs': [
        rf'\d\d:\d\d:\d\d Warning Message: Embedded skeleton.*{NL}',
        'The skeleton in the specified P3D-file differs from the embedded P3D. This might cause this model/skeleton to not work correctly. This might be caused by a typo somewhere.'
    ],
    'Unknown animation source': [
        rf'\d\d:\d\d:\d\d .* unknown animation source.*{NL}',
        'The specified animation source is not (correctly) defined in the model. This might impact function or visual appearance of the model.'
    ],
    'Command is not allowed to be remotely executed': [
        rf'\d\d:\d\d:\d\d Scripting command .* is not allowed to be remotely executed{NL}',
        'The command specified is not whitelisted in <code>CfgRemoteExec</code>. For information on how to do that, visit <a href="https://community.bistudio.com/wiki?title=Arma_3:_CfgRemoteExec" target="_blank">Bohemia Wiki: CfgRemoteExec</a>'
    ],
    'Function is not allowed to be remotely executed': [
        rf'\d\d:\d\d:\d\d Scripting function .* is not allowed to be remotely executed{NL}',
        'The function specified is not whitelisted in <code>CfgRemoteExec</code>. For information on how to do that, visit <a href="https://community.bistudio.com/wiki?title=Arma_3:_CfgRemoteExec" target="_blank">Bohemia Wiki: CfgRemoteExec</a>'
    ],
    'Script Error: missing ...': [
        rf'{TS} Error in expression .*{NL}.*{NL}{TS}Error position.*{NL}.*{NL}{TS}Error .*{NL}({TS} File .*)?',
        'There is most likely a parenthesis <code>()</code>, bracket <code>[]</code> or semicolon <code>;</code> missing somewhere. Check the specified file.<br/>Keep in mind, line numbers are counting <code>#include</code>-Files too.'
    ],
    'Script Error: Type X, expected Y': [
        rf'^{TS} Error in expression .*{NL}(.*{NL}){{2,5}}{TS}Error position.*{NL}(.*{NL}){{1,2}}{TS}.*Type [\w, ]+, expected \w+({NL}{TS} File .*)?',
        'The <a href="https://community.bistudio.com/wiki/Category:Data_Types" target="_blank">Data Type</a> of the provided variable/element does not match type expected by the function/command. Make sure you use the correct value.'
    ],
    'Script Error: Generic Error in expression': [
        rf'{TS}Error in expression .*{NL}(.*{NL}){{2,5}}{TS}Error position.*{NL}(.*{NL}){{0,3}}{TS}Error Generic .*({NL}{TS} File .*)?',
        'This is a Generic error. Please make sure you have used valid syntax and variable data types are correct within your script.'
    ],
    # not working

    # 'Script Error: variable undefined': [
    #     r'\d\d:\d\d:\d\d Error in expression .*{NL}.*{NL}(.*{NL}){{1,}}\d\d:\d\d:\d\d\s+Error position.*{NL}(.*{NL})+\d\d:\d\d:\d\d\s+Error .* variable .*{NL}\d\d:\d\d:\d\d File .*{NL}',
    #     'The variable specified in the error is not defined. Make sure it is initialized before being accessed and that it is available in current scope.<br/>Keep in mind, line numbers are counting <code>#include</code>-Files too.'
    # ]
}
