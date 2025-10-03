# Term Project: Feature-Rich Calculator  

## Objective  

Build an extended calculator that:  

- Uses functions for each required mathematical operator.  
- Prints results in the format `a op b = result`.  
- Uses a loop so the program continues until the user types `"quit"`.  
- Uses f-strings for clean output formatting.  

---

## Function Specs (required)  

Each function must take two numbers and return the result (no printing inside the functions).  

- `add(a, b)` → return `a + b`  
- `subtract(a, b)` → return `a - b`  
- `multiply(a, b)` → return `a * b`  
- `divide(a, b)` →  
  - If `b != 0`, return `a / b`  
  - If `b == 0`, return `None`  
- `floor_divide(a, b)` →  
  - If `b != 0`, return `a // b`  
  - If `b == 0`, return `None`  

---

## Bonus Functions (extra credit)  

- `modulus(a, b)` →  
  - If `b != 0`, return `a % b`  
  - If `b == 0`, return `None`  
- `exponent(a, b)` → return `a ** b`  

---

## Main Program (user interaction)  

Loop until the user types `"quit"`.  

In each loop:  
1. Ask for the first number (or `"quit"` to exit).  
2. Ask for the operator (`+`, `-`, `*`, `/`, `//`, `%`, `**`).  
3. Ask for the second number.  
4. Call the correct function.  
5. Print the result as:
```
    4 + 4 = 8
    10 / 0 = Error (division by zero)

