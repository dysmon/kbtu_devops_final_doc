# Profit maximization problem
This task involves optimizing the production of two products, Product A and Product B, to maximize profit under resource constraints. The production process is limited by the availability of raw materials machine hours and labor hours

Maximize the total profit from producing Product A and Product B:  
- **per unit of product A**: $30  
- **per unit of product B**: $20  

| Resource          | Available Units | Required per unit of Product A | Required per unit of Product B |
|--------------------|-----------------|--------------------------------|--------------------------------|
| **Raw material (kg)** | 200             | 4                              | 3                              |
| **Machine hours**     | 120             | 2                              | 1                              |
| **Labor hours**       | 150             | 3                              | 2                              |

- x -> number/unit of Product A  
- y -> number/unit of Product B  

1. **Z -> the total profit**:  
   \
    Z = 30x + 20y
   \  
   

2. **Constraints**:  
   - Raw material:  4x + 3y <= 200  
   - Machine hours:  2x + y <= 120   
   - Labor hours:  3x + 2y <= 150   
   - x and y non negative   

## Solution of task by mathematical analysis
![01](task1b/01b.jpg)
![11](task1b/11b.jpg)

## General solution without overshooting
   ```python
   from pulp import *

   pos = [200, 120, 150]
   a = [4, 2, 3]
   b = [3, 1, 2]
   costa = 30
   costb = 20

   prob = LpProblem("Profit maximization problem", LpMaximize)
   cnta = LpVariable("a", 0, None, LpInteger)
   cntb = LpVariable("b", 0, None, LpInteger)

   prob += costa * cnta + costb * cntb, "Total cost"
   for i in range(len(pos)):
       prob += (cnta * a[i] + cntb * b[i] <= pos[i]), f"Contstraint #{i}"

   prob.writeLP("sol.lp")
   prob.solve()

   print(f"Status: {LpStatus[prob.status]}")
   
   for v in prob.variables():
       print(v.name, "=", v.varValue)
      print(f"Total Profit: {model.objective.value()}")
   ```  
![this code](pyp.py) you can check here 

## Result
![result](task1b/result.png)

## Answer The maximum profit is at (50,0), giving a profit of $1500 by the solution of math and general solution by python(pupl)