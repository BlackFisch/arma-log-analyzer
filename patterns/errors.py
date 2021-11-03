#!/usr/bin/env python3

PATTERNS = {
    'Bone doesn\'t exist': [
        r'\d\d:\d\d:\d\d Error: Bone .* doesn\'t exist in skeleton .*[\r\n]{0,}',
        'There is bones missing in the specified skeleton. This might be caused by ported content from an older ArmA title. This has to be fixed in the model.'
    ],
    'Embedded skeleton differs': [
        r'\d\d:\d\d:\d\d Warning Message: Embedded skeleton.*[\r\n]{0,}',
        'The skeleton in the specified P3D-file differs from the embedded P3D. This might cause this model/skeleton to not work correctly. This might be caused by a typo somewhere.'
    ],
    'Unknown animation source': [
        r'\d\d:\d\d:\d\d .* unknown animation source.*[\r\n]{0,}',
        'The specified animation source is not (correctly) defined in the model. This might impact function or visual appearance of the model.'
    ],
    'Command is not allowed to be remotely executed': [
        r'\d\d:\d\d:\d\d Scripting command .* is not allowed to be remotely executed[\r\n]{0,}',
        'The command specified is not whitelisted in <code>CfgRemoteExec</code>. For information on how to do that, visit <a href="https://community.bistudio.com/wiki?title=Arma_3:_CfgRemoteExec" target="_blank">Bohemia Wiki: CfgRemoteExec</a>'
    ],
    'Function is not allowed to be remotely executed': [
        r'\d\d:\d\d:\d\d Scripting function .* is not allowed to be remotely executed[\r\n]{0,}',
        'The function specified is not whitelisted in <code>CfgRemoteExec</code>. For information on how to do that, visit <a href="https://community.bistudio.com/wiki?title=Arma_3:_CfgRemoteExec" target="_blank">Bohemia Wiki: CfgRemoteExec</a>'
    ],
    'Script Error: missing ...': [
        r'\d\d:\d\d:\d\d Error in expression .*[\r\n]{0,}.*[\r\n]{0,}\d\d:\d\d:\d\d\s+Error position.*[\r\n]{0,}.*[\r\n]{0,}\d\d:\d\d:\d\d\s+Error .*[\r\n]{0,}\d\d:\d\d:\d\d File .*[\r\n]{0,}',
        'There is most likely a parenthesis <code>()</code>, bracket <code>[]</code> or semicolon <code>;</code> missing somewhere. Check the specified file.<br/>Keep in mind, line numbers are counting <code>#include</code>-Files too.'
    ],
    # not working

    # 'Script Error: variable undefined': [
    #     r'\d\d:\d\d:\d\d Error in expression .*[\r\n]{0,}.*[\r\n]{0,}(.*[\r\n]{0,}){1,}\d\d:\d\d:\d\d\s+Error position.*[\r\n]{0,}(.*[\r\n]{0,})+\d\d:\d\d:\d\d\s+Error .* variable .*[\r\n]{0,}\d\d:\d\d:\d\d File .*[\r\n]{0,}',
    #     'The variable specified in the error is not defined. Make sure it is initialized before being accessed and that it is available in current scope.<br/>Keep in mind, line numbers are counting <code>#include</code>-Files too.'
    # ]
}
