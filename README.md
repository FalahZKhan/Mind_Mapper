![image](https://github.com/user-attachments/assets/ef458fd5-fc5f-4a4f-843e-8d3982ad9391)

# Mind Mapper

A computational platform implementing two key algorithms: the Closest Pair Problem and Karatsuba Integer Multiplication. This project leverages Flask for the backend and Matplotlib for visualization, providing an interactive experience to explore the divide-and-conquer methodology.

---

## Table of Contents
- [Abstract](#abstract)
- [Introduction](#introduction)
- [Proposed System](#proposed-system)
- [System Architecture](#system-architecture)
- [Closest Pair of Points](#closest-pair-of-points)
- [Karatsuba Integer Multiplication](#karatsuba-integer-multiplication)
- [Execution Times](#execution-times)
  - [Closest Pair Execution Times](#closest-pair-execution-times)
  - [Karatsuba Execution Times](#karatsuba-execution-times)
- [Conclusion](#conclusion)
- [References](#references)

---

## Abstract
This project presents a computational platform implementing two key algorithms:
1. **Closest Pair Problem**: A divide-and-conquer approach to find the closest two points in a given dataset with recursive visualization.
2. **Karatsuba Integer Multiplication**: Optimizes large integer multiplication by recursively breaking numbers into smaller parts.

The Flask-based web application provides interactive visual insights into their operations, showcasing efficiency and accuracy across multiple datasets.

---

## Introduction
Divide and conquer algorithms consist of three steps:
1. **Divide**: Break the problem into smaller sub-problems.
2. **Conquer**: Solve each sub-problem recursively.
3. **Combine**: Merge the solutions of all sub-problems to solve the original problem.

This project demonstrates:
- **Closest Pair of Points** using the Euclidean approach.
- **Karatsuba Multiplication** for large integers.

---

## Proposed System
The system is divided into two main modules:
1. **Closest Pair Problem**
2. **Karatsuba Multiplication**

---

## System Architecture
1. **User Interface**: Allows file uploads and parameter selection for both algorithms.
2. **Backend Algorithms**: Executes Closest Pair and Karatsuba algorithms, storing intermediate results.
3. **Visualization Module**: Generates stepwise plots to illustrate algorithmic progress.
4. **Static Storage**: Manages uploaded files and plot images for display.

---

## Closest Pair of Points
### Algorithm
1. **Divide**: Sort points by x-coordinates and split into two halves.
2. **Conquer**: Recursively solve for the closest pair in both halves.
3. **Combine**: Create a strip near the dividing line and check distances to find the closest pair.
4. **Result**: Compare strip results with left and right half results to determine the overall closest pair.

### Time Complexity
- \( O(n \log n) \)

---

## Karatsuba Integer Multiplication
### Algorithm
1. **Split Numbers**: Split numbers \(X\) and \(Y\) into high and low parts:
   - \(X = X_1 \cdot 10^{n/2} + X_0\)
   - \(Y = Y_1 \cdot 10^{n/2} + Y_0\)
2. **Recursive Multiplications**:
   - \(P1 = X_1 \cdot Y_1\)
   - \(P2 = X_0 \cdot Y_0\)
   - \(P3 = (X_1 + X_0) \cdot (Y_1 + Y_0)\)
3. **Combine Results**:
   - \(XY = P1 \cdot 10^n + (P3 - P1 - P2) \cdot 10^{n/2} + P2\)

---

## Execution Times
### Closest Pair Execution Times
| Dataset Size (Points) | Total Time (s) | Frontend Overhead (s) | Algorithm Execution Time (s) |
|-----------------------|----------------|------------------------|------------------------------|
| 100                  | 38.89          | 30.00                 | 8.89                        |
| 200                  | 60.20          | 38.00                 | 22.20                       |
| 300                  | 100.31         | 45.00                 | 55.31                       |
| 400                  | 160.21         | 50.00                 | 110.21                      |
| 500                  | 251.26         | 56.00                 | 195.26                      |
| 600                  | 362.12         | 61.00                 | 301.12                      |
| 700                  | 498.54         | 72.00                 | 426.54                      |
| 800                  | 638.56         | 86.00                 | 552.56                      |

### Karatsuba Execution Times
| Dataset Size (Digits) | Total Time (s) | Frontend Overhead (s) | Algorithm Execution Time (s) |
|-----------------------|----------------|------------------------|------------------------------|
| 10                   | 2.00           | 1.30                  | 0.70                        |
| 20                   | 4.30           | 2.50                  | 1.80                        |
| 30                   | 7.00           | 3.40                  | 3.60                        |
| 40                   | 11.00          | 4.50                  | 6.50                        |
| 50                   | 16.50          | 5.50                  | 11.00                       |
| 60                   | 23.00          | 7.00                  | 16.00                       |
| 70                   | 31.00          | 8.30                  | 22.70                       |
| 80                   | 40.00          | 9.50                  | 30.50                       |
| 90                   | 51.00          | 11.00                 | 40.00                       |
| 100                  | 64.00          | 13.00                 | 51.00                       |

---

## Conclusion
This project demonstrated two divide-and-conquer algorithms: Closest Pair of Points and Karatsuba Multiplication. Both algorithms were evaluated for efficiency and scalability across various input sizes. The developed interface provides clear visualizations, fostering a deeper understanding of the algorithms' operations.

---

## References
- Thomas H. Cormen et al, *Introduction to Algorithms*, 4th Edition
- Anany Levitin, *Introduction to the Design and Analysis of Algorithms*, 3rd Edition
