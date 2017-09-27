#!/usr/bin/env python
# -*- coding: utf8 -*-
import re

html = """
    <h2>多云</h2>
"""

if __name__ == '__main__':
    p = re.compile('<[^>]+>')
    print p.sub("", html)