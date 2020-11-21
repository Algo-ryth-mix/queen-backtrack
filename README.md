# Queen Backtrack

A backtracking solver to the queen-problem

Usage:
`python main.py` or `python3 main.py`

which produces:
```
constraints=[]
===================
| D # . # . # . # |
| # . # . D . # . |
| . # . # . # . D |
| # . # . # D # . |
| . # D # . # . # |
| # . # . # . D . |
| . D . # . # . # |
| # . # D # . # . |
===================
D=Queen
```

"Advanced" Usage:
additionally you can parse pairs of numbers as constraints to the solver to produce different results.
Note that if the constraints make solving impossible no board will be rendered!
`python main.py 0 1` 
produces:
```
constraints:  [(0, 1)]
===================
| . D . # . # . # |
| # . # D # . # . |
| . # . # . D . # |
| # . # . # . # D |
| . # D # . # . # |
| D . # . # . # . |
| . # . # . # D # |
| # . # . D . # . |
===================
D=Queen
```

if you pass more then one constraints the solver will not check if your constraints adhere to its rules.
Thus this invalid board
```
constraints:  [(0, 0), (1, 1)]
===================
| D # . # . # . # |
| # D # . # . # . |
| . # . D . # . # |
| # . # . # D # . |
| . # . # . # . D |
| # . D . # . # . |
| . # . # D # . # |
| # . # . # . D . |
===================
D=Queen
```
could be produced by calling `python main.py 0 0 1 1`

`7 6 0 3`
