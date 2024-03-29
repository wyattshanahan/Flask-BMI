import pytest
from calculator import * #import functions from calculator.py
#unit tests for processRawHeight
def test_processRawHeight_comma():
    assert processRawHeight("12","6") == 150.0

# boundary tests for categoriseBMI
def test_categorise_9_25(): # test the "interior" point for underweight
    assert categoriseBMI(9.25) == "Underweight"

def test_categorise_18_4(): # test the boundary at 18.4
    assert categoriseBMI(18.4) == "Underweight"

def test_categorise_18_5(): # test the boundary at 18.5
    assert categoriseBMI(18.5) == "Normal Weight"

def test_categorise_21_7(): # test the interior point between bounds 18.5 and 25
    assert categoriseBMI(21.7) == "Normal Weight"

def test_categorise_24_9(): # test the boundary at 24.9
    assert categoriseBMI(24.9) == "Normal Weight"

def test_categorise_25_0(): # test the boundary at 25
    assert categoriseBMI(25.0) == "Overweight"

def test_categorise_27_45(): # test the interior point between bounds 25 and 30
    assert categoriseBMI(27.45) == "Overweight"

def test_categorise_29_9(): # test the boundary at 29.9
    assert categoriseBMI(29.9) == "Overweight"

def test_categorise_30_0(): # test the boundary at 30.0
    assert categoriseBMI(30.0) == "Obese"

def test_categorise_39_25(): # test the "interior" point for values over the boundary at 30.0
    assert categoriseBMI(39.25) == "Obese"
# unit tests for categoriseBMi to verify input types
def test_categorise_int():
    assert categoriseBMI(30) == "Obese"

def test_categorise_flt():
    assert categoriseBMI(30.0) == "Obese"

def test_categorise_str():
    assert categoriseBMI("30") == "Obese"

def test_categorise_invalid():
    with pytest.raises(ValueError) as exc_info:
        categoriseBMI("thirty")
    assert str(exc_info.value) == "Error converting your inputs"


# unit tests for imperialToMetric testing type combinations for both inputs
def test_imperialToMetric_int_int():
    assert imperialToMetric(150,150) == (67.5,14.0625)

def test_imperialToMetric_int_flt():
    assert imperialToMetric(150,150.0) == (67.5,14.0625)

def test_imperialToMetric_int_str():
    assert imperialToMetric(150,"150") == (67.5,14.0625)

def test_imperialToMetric_int_invalid():
    assert imperialToMetric(150,"onefifty") == "Error processing height input"

def test_imperialToMetric_flt_int():
    assert imperialToMetric(150.0,150) == (67.5,14.0625)

def test_imperialToMetric_flt_flt():
    assert imperialToMetric(150.0,150.0) == (67.5,14.0625)

def test_imperialToMetric_flt_str():
    assert imperialToMetric(150.0,"150") == (67.5,14.0625)

def test_imperialToMetric_flt_invalid():
    assert imperialToMetric(150.0,"onefifty") == "Error processing height input"

def test_imperialToMetric_str_int():
    assert imperialToMetric("150",150) == (67.5,14.0625)

def test_imperialToMetric_str_flt():
    assert imperialToMetric("150",150.0) == (67.5,14.0625)

def test_imperialToMetric_str_str():
    assert imperialToMetric("150","150") == (67.5,14.0625)

def test_imperialToMetric_str_invalid():
    assert imperialToMetric("150","onefifty") == "Error processing height input"

def test_imperialToMetric_invalid_int():
    assert imperialToMetric("onefifty",150) == "Error processing weight input"

def test_imperialToMetric_invalid_flt():
    assert imperialToMetric("onefifty",150.0) == "Error processing weight input"

def test_imperialToMetric_invalid_str():
    assert imperialToMetric("onefifty","150") == "Error processing weight input"

def test_imperialToMetric_invalid_invalid():
    assert imperialToMetric("onefifty","onefifty") == "Error processing weight input"



#tests for calculateBMI - checks types int, flt, string, and invalid string for each input combination
def test_calculateBMI_int_int():
    assert calculateBMI(67,14) == 4.785714285714286

def test_calculateBMI_int_flt():
    assert calculateBMI(67,14.0) == 4.785714285714286

def test_calculateBMI_int_str():
    assert calculateBMI(67,"14") == 4.785714285714286

def test_calculateBMI_int_invalid():
    with pytest.raises(ValueError) as exc_info:
        calculateBMI(67, "fourteen")
    assert str(exc_info.value) == "Error converting your inputs"

def test_calculateBMI_flt_int():
    assert calculateBMI(67.0,14) == 4.785714285714286

def test_calculateBMI_flt_flt():
    assert calculateBMI(67.0,14.0) == 4.785714285714286

def test_calculateBMI_flt_str():
    assert calculateBMI(67.0,"14") == 4.785714285714286

def test_calculateBMI_flt_invalid():
    with pytest.raises(ValueError) as exc_info:
        calculateBMI(67.0, "fourteen")
    assert str(exc_info.value) == "Error converting your inputs"

def test_calculateBMI_str_int():
    assert calculateBMI("67",14) == 4.785714285714286

def test_calculateBMI_str_flt():
    assert calculateBMI("67",14.0) == 4.785714285714286

def test_calculateBMI_str_str():
    assert calculateBMI("67","14") == 4.785714285714286

def test_calculateBMI_str_invalid():
    with pytest.raises(ValueError) as exc_info:
        calculateBMI("67", "fourteen")
    assert str(exc_info.value) == "Error converting your inputs"

def test_calculateBMI_invalid_int():
    with pytest.raises(ValueError) as exc_info:
        calculateBMI("sixtyseven", 14)
    assert str(exc_info.value) == "Error converting your inputs"

def test_calculateBMI_invalid_flt():
    with pytest.raises(ValueError) as exc_info:
        calculateBMI("sixtyseven", 14.0)
    assert str(exc_info.value) == "Error converting your inputs"

def test_calculateBMI_invalid_str():
    with pytest.raises(ValueError) as exc_info:
        calculateBMI("sixtyseven", "14")
    assert str(exc_info.value) == "Error converting your inputs"

def test_calculateBMI_invalid_invalid():
    with pytest.raises(ValueError) as exc_info:
        calculateBMI("sixtyseven", "fourteen")
    assert str(exc_info.value) == "Error converting your inputs"

def test_processHost():
    assert processHost(200,5,6,) == (33.05785123966941, "Obese")
