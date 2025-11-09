"""
Program Name: test_lab11_ssrinivasan3.py

Author: Shrrayash Srinivasan

Purpose: 1.	This file serves as a pytest unit tests for the degree_rotation function defined in lab11_ssrinivasan3.py.


Date: November 4, 2025

""" 
import pytest
from lab11_ssrinivasan3 import degree_rotation

def testing_within_range():
    assert degree_rotation("100") == 100
    assert degree_rotation("200") == 200
    assert degree_rotation("300") == 300
    assert degree_rotation("90") == 90
    assert degree_rotation("180") == 180
    assert degree_rotation("270") == 270

def test_above_360():
    assert degree_rotation("450") == 90
    assert degree_rotation("370") == 10
    assert degree_rotation("1080") == 0
    assert degree_rotation("362") == 2


def test_below_360():
    assert degree_rotation("-100") == 260
    assert degree_rotation("-460") == 260
    assert degree_rotation("-820") == 260
    assert degree_rotation("-2") == 358


def test_at_360():
    assert degree_rotation("360") == 0

def test_at_0():
    assert degree_rotation("0") == 0

def test_not_valid_input():
    assert degree_rotation("abc") == None
    assert degree_rotation("") == None
    assert degree_rotation("!") == None
    assert degree_rotation("+") == None
    assert degree_rotation("-") == None
    assert degree_rotation("*") == None
    assert degree_rotation("90j") == None