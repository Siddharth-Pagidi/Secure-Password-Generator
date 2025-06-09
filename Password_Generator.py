# -*- coding: utf-8 -*-
"""
Password Enhancer

Created on Thu Mar 27 09:15:20 2025

@author: sidd
"""

import numpy as np
import random as rand
from sys import exit

old_password = input("Please input your password here: ")
old_password_lowered = old_password.lower()

translation_table = str.maketrans({
    'a' : 'α',
    'b' : 'β',
    'c' : 'γ',
    'd' : 'δ',
    'e' : 'ε',
    'f' : 'ζ',
    'g' : 'η',
    'h' : 'θ',
    'i' : 'ι',
    'j' : 'κ',
    'k' : 'λ',
    'l' : 'μ',
    'm' : 'ν',
    'n' : 'ξ',
    'o' : 'ο',
    'p' : 'π',
    'q' : 'Γ',
    'r' : 'ρ',
    's' : 'σ',
    't' : 'τ',
    'u' : 'υ',
    'v' : 'φ',
    'w' : 'χ',
    'x' : 'ψ',
    'y' : 'Ξ',
    'z' : 'ω',
})

new_password = old_password_lowered.translate(translation_table)

print(new_password)
