import pytest
from helper import Gundam
import helper


def createGundam(id, name, pilot_name):
    gndm = Gundam()
    gndm.instantiate(id, name, pilot_name)
    return gndm


# Test Scenario 1
def test_min_max_pilot_name():
    id = "0"
    name = "Test"
    pilot = "greaterthantenletters"
    forTest = createGundam(id, name, pilot).pilot_name
    assert helper.checkStringLengthGreaterThan(
        forTest, 10) or helper.checkStringLengthLessThan(forTest, 50)


# Test Scenario 2
def test_alpha_and_dash_pilot_name():
    id = "0"
    name = "Test"
    pilot = "greaterthantenlette-rs"
    forTest = createGundam(id, name, pilot).pilot_name
    assert helper.checkStringAlpha(
        forTest) or helper.countCharaInString(forTest, "-") == 1


# Test Scenario 3
def test_min_max_name():
    id = "0"
    name = "Test"
    pilot = "greaterthantenletters"
    forTest = createGundam(id, name, pilot).name
    assert helper.checkStringLengthGreaterThan(
        forTest, 15) or helper.checkStringLengthLessThan(forTest, 100)

# Test Scenario 4


def test_alnum_name():
    id = "0"
    name = "Test"
    pilot = "greaterthantenletters"
    forTest = createGundam(id, name, pilot).name
    assert helper.checkStringAlNum(forTest)

# Test Scenario 5


def test_istitle():
    id = "0"
    name = "Test Me"
    pilot = "greaterthantenletters"
    forTest = createGundam(id, name, pilot).name
    assert helper.checkifSentenceCase(forTest)
