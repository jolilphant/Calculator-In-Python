"""Autograder tests for the Calculator Term Project.

This file checks BOTH:
1. Function correctness (unit tests)
2. Full calculator program output (CLI tests)

- Students should name their file exactly: calculator_code.py
- Required functions: add, subtract, multiply, divide, floor_divide
- Bonus functions: modulus, exponent
- CLI must print results in the format: a op b = result
"""

import subprocess
import sys
import random
from pathlib import Path
import pytest

# ============================================================
# Function Tests
# ============================================================

def test_add_function():
    from calculator_code import add
    a, b = random.randint(-100, 100), random.randint(-100, 100)
    assert add(a, b) == a + b, f"add({a}, {b}) should be {a+b}"

def test_subtract_function():
    from calculator_code import subtract
    a, b = random.randint(-100, 100), random.randint(-100, 100)
    assert subtract(a, b) == a - b, f"subtract({a}, {b}) should be {a-b}"

def test_multiply_function():
    from calculator_code import multiply
    a, b = random.randint(-20, 20), random.randint(-20, 20)
    assert multiply(a, b) == a * b, f"multiply({a}, {b}) should be {a*b}"

def test_divide_function():
    from calculator_code import divide
    a, b = random.randint(-100, 100), random.randint(-100, 100)
    if b == 0:
        assert divide(a, b) is None, f"divide({a}, 0) must return None"
    else:
        assert divide(a, b) == a / b, f"divide({a}, {b}) should be {a/b}"

def test_floor_divide_function():
    from calculator_code import floor_divide
    a, b = random.randint(-100, 100), random.randint(-100, 100)
    if b == 0:
        assert floor_divide(a, b) is None, f"floor_divide({a}, 0) must return None"
    else:
        assert floor_divide(a, b) == a // b, f"floor_divide({a}, {b}) should be {a//b}"

# ---- Bonus Functions ----

def test_modulus_function():
    try:
        from calculator_code import modulus
    except ImportError:
        pytest.skip("modulus not implemented (bonus)")
    a, b = random.randint(-100, 100), random.randint(-100, 100)
    if b == 0:
        assert modulus(a, b) is None, f"modulus({a}, 0) must return None"
    else:
        assert modulus(a, b) == a % b, f"modulus({a}, {b}) should be {a%b}"

def test_exponent_function():
    try:
        from calculator_code import exponent
    except ImportError:
        pytest.skip("exponent not implemented (bonus)")
    a, b = random.randint(0, 10), random.randint(0, 5)
    assert exponent(a, b) == a ** b, f"exponent({a}, {b}) should be {a**b}"


# ============================================================
# CLI Tests (full program)
# ============================================================

PROGRAM = "calculator_code.py"   # student's main program

def run_calc(inputs):
    """
    Run the student's program once:
      - send inputs (list of strings) joined by newlines, plus 'quit'
      - return (stdout, stderr, returncode)
    """
    prog_path = Path(PROGRAM)
    assert prog_path.exists(), f"Could not find {PROGRAM} in repo root."

    user_input = "\n".join(inputs + ["quit"]) + "\n"
    result = subprocess.run(
        [sys.executable, str(prog_path)],
        input=user_input,
        text=True,
        capture_output=True,
        timeout=5,
    )
    return result.stdout, result.stderr, result.returncode


def assert_output_contains(expected, stdout, stderr, returncode):
    """
    Assert program succeeded and stdout (with spaces removed) contains the expected substring.
    """
    assert returncode == 0, f"Program exited with non-zero status.\nSTDERR:\n{stderr}"
    normalized = "".join(stdout.split())  # remove all whitespace
    assert expected in normalized, (
        f"Expected to find '{expected}' in output (whitespace removed).\n"
        f"----- STDOUT -----\n{stdout}\n"
        f"----- STDERR -----\n{stderr}\n"
    )

# -------------------------
# CLI interaction tests
# -------------------------

def test_add_output():
    stdout, stderr, rc = run_calc(["1", "+", "1"])
    assert_output_contains("1+1=2", stdout, stderr, rc)

def test_subtract_output():
    stdout, stderr, rc = run_calc(["10", "-", "3"])
    assert_output_contains("10-3=7", stdout, stderr, rc)

def test_multiply_output():
    stdout, stderr, rc = run_calc(["6", "*", "7"])
    assert_output_contains("6*7=42", stdout, stderr, rc)

def test_divide_output_integer_result():
    stdout, stderr, rc = run_calc(["8", "/", "2"])
    assert_output_contains("8/2=4", stdout, stderr, rc)

def test_divide_by_zero_output():
    stdout, stderr, rc = run_calc(["10", "/", "0"])
    assert_output_contains("10/0=Error(divisionbyzero)", stdout, stderr, rc)

def test_floor_divide_output():
    stdout, stderr, rc = run_calc(["7", "//", "2"])
    assert_output_contains("7//2=3", stdout, stderr, rc)

def test_floor_divide_by_zero_output():
    stdout, stderr, rc = run_calc(["5", "//", "0"])
    assert_output_contains("5//0=Error(divisionbyzero)", stdout, stderr, rc)

# ---- Bonus CLI tests ----

# ---- Bonus CLI tests ----
def test_modulus_output():
    stdout, stderr, rc = run_calc(["7", "%", "3"])
    normalized = "".join(stdout.split())
    if "%" not in normalized:
        pytest.skip("UI for % not implemented (bonus)")
    assert_output_contains("7%3=1", stdout, stderr, rc)

def test_modulus_by_zero_output():
    stdout, stderr, rc = run_calc(["5", "%", "0"])
    normalized = "".join(stdout.split())
    if "%" not in normalized:
        pytest.skip("UI for % not implemented (bonus)")
    assert_output_contains("5%0=Error(divisionbyzero)", stdout, stderr, rc)

def test_exponent_output():
    stdout, stderr, rc = run_calc(["2", "**", "5"])
    normalized = "".join(stdout.split())
    if "**" not in normalized:
        pytest.skip("UI for ** not implemented (bonus)")
    assert_output_contains("2**5=32", stdout, stderr, rc)
