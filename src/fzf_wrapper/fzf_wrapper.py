#!/usr/bin/env python3
# coding: utf-8

import platform
from subprocess import run, PIPE, DEVNULL
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
        if some commands were not found in Path

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
    command_result = run(command, input=choices_bytes, stdout=PIPE)
    if command_result.returncode == 130:  # User cancel fzf
        return []
    elif command_result.returncode == 1:  # User select empty line
        return []
    results = command_result.stdout.decode().strip().split('\n')
    return results
