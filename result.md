# Issue 1 #
### command: $ python -m doctest -o NORMALIZE_WHITESPACE -v tests/test_issue1.py ###

----------------------------------------------------------------------
Trying:  
    encode("SOS")  
Expecting:  
    '... --- ...'  
ok  

Trying:  
    encode("Hello World")  
Expecting:  
    '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'  
ok  

Trying:  
    encode("123")  
Expecting:  
    '.---- ..--- ...--'  
ok  

Trying:  
    encode("")  
Expecting:  
    ''  
ok  

Trying:  
    encode("!")  
Expecting:  
    Traceback (most recent call last):  
        ...  
    KeyError: '!'  
ok  

Trying:  
    encode("Hello, World")  
Expecting:  
    Traceback (most recent call last):  
        ...  
    KeyError: ','  
ok  

1 items had no tests:  
    test_issue1  
1 items passed all tests:  
   6 tests in test_issue1.test_encode  
6 tests in 2 items.  
6 passed and 0 failed.  
Test passed.  

----------------------------------------------------------------------
# Issue 2 # 
### command: $ python -m pytest tests/test_issue2.py ###
collected 5 items  

----------------------------------------------------------------------
tests/test_issue2.py::test_decode[... --- ...-SOS]P ASSED [ 20%]   
tests/test_issue2.py::test_decode[.... . .-.. .-.. ----HELLO] PASSED [40%]   
tests/test_issue2.py::test_decode[.- ...- .. - ----AVITO] PASSED [ 60%]   
tests/test_issue2.py::test_decode[.---- ..--- ...---123] PASSED [ 80%]   
tests/test_issue2.py::test_decode[.... . .-.. .-.. ---   .-- --- .-. .-.. -..-HELLO WORLD] FAILED [100%]  

----------------------------------------------------------------------

### FAILURES ###  
test_decode[.... . .-.. .-.. ---   .-- --- .-. .-.. -..-HELLO WORLD]  

morse_message = '.... . .-.. .-.. ---   .-- --- .-. .-.. -..', expected = 'HELLO WORLD'

```python    @pytest.mark.parametrize("morse_message, expected", [
        ('... --- ...', 'SOS'),
        ('.... . .-.. .-.. ---', 'HELLO'),
        ('.- ...- .. - ---', 'AVITO'),
        ('.---- ..--- ...--', '123'),
        ('.... . .-.. .-.. ---   .-- --- .-. .-.. -..', 'HELLO WORLD')])
    def test_decode(morse_message, expected):  
    ->   assert decode(morse_message) == expected
E       AssertionError: assert 'HELLOWORLD' == 'HELLO WORLD'  
E         - HELLO WORLD  
E         ?      -  
E         + HELLOWORLD  

test_issue2.py:12: AssertionError
```

# Issue 3 #
### command: $ python -m unittest -v tests/test_issue3.py ###

----------------------------------------------------------------------
test_fit_transform_duplicate_categories (test_issue3.FitTransformTestCase.test_fit_transform_duplicate_categories) ... ok
test_fit_transform_empty_string (test_issue3.FitTransformTestCase.test_fit_transform_empty_string) ... ok
test_fit_transform_multiple_args (test_issue3.FitTransformTestCase.test_fit_transform_multiple_args) ... ok
test_fit_transform_no_args (test_issue3.FitTransformTestCase.test_fit_transform_no_args) ... ok
test_fit_transform_one_category (test_issue3.FitTransformTestCase.test_fit_transform_one_category) ... ok
test_fit_transform_single_arg (test_issue3.FitTransformTestCase.test_fit_transform_single_arg) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK

# Issue 4 #
### command: $ python -m pytest -v tests/test_issue4.py ###
collected 4 items

----------------------------------------------------------------------
test_issue4.py::test_fit_transform_single_argument PASSED  [ 25%]\
test_issue4.py::test_fit_transform_empty_argument PASSED [ 50%]\
test_issue4.py::test_fit_transform_duplicate_arguments PASSED [ 75%]\
test_issue4.py::test_fit_transform_duplicate_categories PASSED [100%]\

----------------------------------------------------------------------
 4passed in 0.02s  

# Issue 5 #
### command: $ python -m pytest -v tests/test_issue5.py ###
collected 3 items

----------------------------------------------------------------------
tests/test_issue5.py::test_what_is_year_now_ymd_format PASSED [ 33%]\
tests/test_issue5.py::test_what_is_year_now_dmy_format PASSED [ 66%]\
tests/test_issue5.py::test_what_is_year_now_invalid_format PASSED [100%]

----------------------------------------------------------------------

<h3> Для просмотра coverage только для Issuе5 можно воспользоваться командой  
$ python -m pytest -q tests/test_issue5.py --cov=what_is_year_now </h3>

| Name | Stmts | Miss | Cover |
|-----:|:-----:|:----:|:-----:|
| what_is_year_now.py | 19 | 0 | 100% | 
| TOTAL | 19 | 0 | 100% | 

3 passed in 0.10s

<h3> Для создания html-отчета исполнить команду 
$ python -m pytest --cov . --cov-report html </h3>