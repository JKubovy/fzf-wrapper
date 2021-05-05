fzf-wrapper
===========

**Python wrapper for junegunn's fzf. Let user interactively choose from given choices**
![](https://github.com/JKubovy/fzf-wrapper/blob/master/fzf-wrapper.gif)

fzf-wrapper is python **multiplatform** library without any other dependency then fzf itself. Recommended tool to improve user experience in your scripts.

Requirements
-----------
* Python 3.6+
* [fzf](https://github.com/junegunn/fzf)

Install
-------
	pip install fzf-wrapper

Usage
-----
	from fzf_wrapper import prompt
	prompt(['one', 'two', 'three'])
	# Start fzf and return selected item / items in list
	# eg. ['two']

You can add fzf arguments as second parameter:

	prompt(['1', '2', '3'], '--multi --cycle')

Licence
-------
MIT
