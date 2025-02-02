#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: gitwrapperlibexceptions.py
#
# Copyright 2018 Costas Tyfoxylos
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#

"""
Custom exception code for gitwrapperlib.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

__author__ = '''Costas Tyfoxylos <costas.tyf@gmail.com>'''
__docformat__ = '''google'''
__date__ = '''02-01-2018'''
__copyright__ = '''Copyright 2018, Costas Tyfoxylos'''
__credits__ = ["Costas Tyfoxylos"]
__license__ = '''MIT'''
__maintainer__ = '''Costas Tyfoxylos'''
__email__ = '''<costas.tyf@gmail.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".


class ExecutableNotFound(Exception):
    """The git command was not found on the system."""


class BranchNotFound(Exception):
    """The default branch could not be located."""


class RemoteOriginError(Exception):
    """The remote origin response is not as expected."""
