# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import functools
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

