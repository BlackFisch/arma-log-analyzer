#!/usr/bin/env python3
from .common import TS, NL, CODE

INCLUDE = '<br/>Keep in mind, line numbers are counting <code>#include</code>-Files too.'

PATTERNS = {
    'Unknown animation source': [
        rf'{TS}.* unknown animation source.*{NL}',
        'The specified animation source is not (correctly) defined in the model. This might impact function or visual appearance of the model.'
    ],
    'Command is not allowed to be remotely executed': [
        rf'{TS}Scripting command .* is not allowed to be remotely executed{NL}',
        'The command specified is not whitelisted in <code>CfgRemoteExec</code>. For information on how to do that, visit <a href="https://community.bistudio.com/wiki?title=Arma_3:_CfgRemoteExec" target="_blank">Bohemia Wiki: CfgRemoteExec</a>'
    ],
    'Function is not allowed to be remotely executed': [
        rf'{TS}Scripting function .* is not allowed to be remotely executed{NL}',
        'The function specified is not whitelisted in <code>CfgRemoteExec</code>. For information on how to do that, visit <a href="https://community.bistudio.com/wiki?title=Arma_3:_CfgRemoteExec" target="_blank">Bohemia Wiki: CfgRemoteExec</a>'
    ],
    'Script Error: missing X': [
        rf'{TS}Error in expression{CODE}{TS}Error position:{CODE}{TS}Error Missing .*({TS} File .*)?',
        f'There is most likely a parenthesis <code>()</code>, bracket <code>[]</code> or semicolon <code>;</code> missing somewhere. Check the specified file.{INCLUDE}.'
    ],
    'Script Error: Type X, expected Y': [
        rf'{TS}Error in expression{CODE}{TS}Error position:{CODE}{TS}.*Type [\w, ]+, expected \w+({TS} File .*)?',
        f'The <a href="https://community.bistudio.com/wiki/Category:Data_Types" target="_blank">Data Type</a> of the provided variable/element does not match type expected by the function/command. Make sure you use the correct value.{INCLUDE}'
    ],
    'Script Error: Generic Error in expression': [
        rf'{TS}Error in expression{CODE}{TS}Error position:{CODE}{TS}Error Generic .*({TS} File .*)?',
        f'This is a Generic error. Please make sure you have used valid syntax and variable data types are correct within your script.{INCLUDE}'
    ],
    'Script Error: undefined variable': [
        rf'{TS}Error in expression{CODE}{TS}Error position:{CODE}{TS}Error \w+ variable.*({TS} File .*)?',
        f'The variable specified in the error is not defined. Make sure it is initialized before being accessed and that it is available in current scope.{INCLUDE}'
    ],
    'Script Error: Zero divisor': [
        rf'{TS}Error in expression{CODE}{TS}Error position:{CODE}{TS}Error Zero divisor.*({TS} File .*)?',
        f'This can mean one of two things: Either you are selecting from an Array and the index is greater than the highest index of the array (Index out of Bounds) or you are trying to do division by 0 which is not permitted.{INCLUDE}'
    ]
}
