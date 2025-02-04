This repository provides a Python implementation of a compound interest calculator designed to illustrate different approaches to input validation.  The project includes three distinct versions, each with its own validation strategy, offering a practical learning experience in handling user input and preventing errors.

Version 1: Strict Validation (No Zeros)

This version employs a strict validation approach.  It requires all input values—principal, interest rate, and time (in years)—to be positive numbers (greater than zero).  The program uses while loops to repeatedly prompt the user for each input until a valid positive value is provided.  If the user enters a zero or negative number, an error message is displayed, and they are asked to re-enter the value.  This strict approach ensures that the compound interest calculation is performed with valid data, preventing potential errors or unexpected results.

Version 2: Flexible Validation (Zeros Allowed for Rate and Time)

This version offers a more flexible validation strategy. While it still requires the principal amount to be positive, it allows the interest rate and time to be zero.  This flexibility can be useful in certain scenarios, such as calculating the growth of an investment over zero years or with a zero interest rate. The input validation still utilizes loops to ensure the principal is a valid positive number, but employs different loop control structures to handle the optional zero values for interest rate and time.

Version 3: Bug Demonstration (Initial Value Trap)

This version is intentionally designed to showcase a common pitfall in input validation—the "initial value trap."  The variables representing the principal, rate, and time are initially set to zero. The validation loops use conditions like "while principle < 0," meaning these loops will be skipped entirely if the initial value is already zero (or any non-negative number for that matter). The program then proceeds to the compound interest calculation using these initial zero values, leading to an incorrect or meaningless result. This example demonstrates the critical importance of carefully considering initial variable states and their interaction with validation logic to prevent subtle but impactful bugs.

The core calculation in all (except version 3 when the bug occurs) versions uses the standard compound interest formula:  Total = Principal * (1 + Rate / 100) ^ Time.  Once valid inputs are received (or bypassed due to the bug), the formula is used to calculate the final balance, which is then printed to the user, formatted appropriately.

This project serves as a valuable educational resource for anyone learning about input validation in Python. It highlights different validation techniques, the importance of thorough testing, and the potential consequences of overlooking details like initial variable values.
