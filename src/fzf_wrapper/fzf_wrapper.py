#!/usr/bin/env python3
# coding: utf-8

# MIT License
#
# Copyright (c) 2021 Jan Kubovy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import platform
from subprocess import run, PIPE, DEVNULL, CalledProcessError
from typing import List

FZF_URL = "https://github.com/junegunn/fzf"


def __check_fzf_in_path() -> bool:
    try:
        cmd = 'where' if platform.system().lower() == 'windows' else 'which'
        return_code = run([cmd, 'fzf'], stderr=DEVNULL, stdout=DEVNULL).returncode
        return return_code == 0
    except IOError:
        return False


def prompt(choices: List[str], fzf_options: str = '') -> List[str]:
    """ Summary
        Let user interactively choose from given choices using fzf program

    Parameters
    ----------
      choices : List[str]
        list of choices
      fzf_options : str
        additional fzf arguments

    Raises
    ======
      ValueError
        if given wrong arguments
      AttributeError
        if fzf command was not found in Path
        or if there is some problem while running fzf

    Returns
    =======
      List[str]
        user choice/choices or empty if user cancel process or select empty line
    """
    if choices is None or len(choices) == 0:
        raise ValueError("Argument 'choices' has to be set!")
    if fzf_options is None:
        fzf_options = ''
    if not all([isinstance(x, str) for x in choices]):
        raise ValueError("Argument 'choices' has to contaions only str!")
    if not isinstance(fzf_options, str):
        raise ValueError("Argument 'fzf_options' has to be str!")
    if not __check_fzf_in_path():
        raise AttributeError(f"Unable to find 'fzf' in PATH!\nInstall fzf from {FZF_URL}")

    command = ['fzf']
    command.extend(filter(None, fzf_options.split(' ')))
    choices_bytes = '\n'.join(choices).encode()
    try:
        command_result = run(command, input=choices_bytes, check=True, stdout=PIPE)
        results = command_result.stdout.decode().strip().split('\n')
        return results
    except CalledProcessError as e:
        if e.returncode == 130:  # User cancel fzf
            return []
        elif e.returncode == 1:  # User select empty line
            return []
        elif e.returncode != 0:
            raise AttributeError(str(e.stderr))
