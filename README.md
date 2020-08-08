# nantoniou-algo-assignments

Repository used to host three assignments of the "Algorithms & Data Structures" course. The assignments offer an introduction to basic Algirithms and Data Structures, while helping to get familiar with common Python usage.

### 1- Present Bias
People tend to pay more attention to the short-term cost, which sometimes leads to non-optimised decisions. In that sense, given a graph `G`, a starting node `s` and a terminal node `t`, we can find an optimal path, with the lowest cost possible. However, due to the *present bias*, the user discounts the cost of the future paths by a given parameter b (b<1). Thus, given the graph `G`, the start, end node, and the bias, the script- using a Depth-first search- finds a) the optimal path and b) the path that will be ultimately chosen with the bias. 

The explanation of the assignment (in greek) can be found [here](https://nbviewer.jupyter.org/github/dmst-algorithms-course/assignment-2018-1/blob/master/assignment_2018_1.ipynb?flush_cache=true).

### 2- Graeco-Lating Squares
The script takes a [Latin Square](https://en.wikipedia.org/wiki/Latin_square) as input and returns- if found- the [Greaco-Latin Square](https://en.wikipedia.org/wiki/Mutually_orthogonal_Latin_squares) of that Latin Square.

Starting from a $n \\times n$ Latin Square, we follow the following steps:
1. Finding the transversals.
2. Detecting, if possible, *n* transversals, such as every digit appears in a different position in each of the *n* transversals.
3. Creating a Graeco-Latin Square, from the transversals, replacing the digit *k*, in the initial Latin Square, to the positions indicated by the transversal that starts with *k*. 

The explanation of the assignment can be found [here](https://nbviewer.jupyter.org/github/dmst-algorithms-course/assignment-2018-2/blob/master/assignment_2018_2.ipynb).

### 3- The Logical Complexity of Collaboration

Given a `4X4` matrix with boolean values, the goal is to simplify the boolean values into logical expressions and measure their complexity.

A more thorough explanation of the assingment can be found [here](https://nbviewer.jupyter.org/github/dmst-algorithms-course/assignment-2018-3/blob/master/assignment_2018_3.ipynb).
