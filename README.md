# CMPS 2200  Recitation 02

**Name (Team Member 1):** Sophie Strobl

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

Recurrence relation of W(n) = aW(n/b) + f(n):

Case 1: f(n) = 1

Using the Master Theorem:
c = 0 (since n^0 = 1)
log_b(a) = log_2(2) = 1
Since c < log_b(a), this falls under Case 1 of the Master Theorem.
Asymptotic Behavior: W(n) = Theta(n^(log_b a)) = Theta(n)

Case 2: f(n) = log n

Here, c is not constant, but log n grows slower than n^(log_b a).
This again falls under Case 1 since log n < n^(log_2(2)) = n.
Asymptotic Behavior: W(n) = Theta(n)

Case 3: f(n) = n

c = 1 and log_b(a) = 1 for a = 2, b = 2.
Since c = log_b(a), this is Case 2 of the Master Theorem.
Asymptotic Behavior: W(n) = Theta(n log n)

Empirical Confirmation:
Running the code for these cases shows trends that match the theoretical derivations.

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

Case 1: c < log_b(a)

Example: c = 0.5, a = 2, b = 2
Since c < 1, this is Case 1.
Asymptotic Behavior: W(n) = Theta(n)

Case 2: c > log_b(a)

Example: c = 2, a = 2, b = 2
Since 2 > 1, this is Case 3.
Asymptotic Behavior: W(n) = Theta(n^2)

Case 3: c = log_b(a)

Example: c = 1, a = 2, b = 2
This is Case 2.
Asymptotic Behavior: W(n) = Theta(n log n)

Empirical Confirmation:

Empirical results from compare_work match these predictions.
Growth rates differ as expected based on the value of c.

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

The span recurrence is:

S(n) = max(S(n/b)) + f(n)

Derivations:

For f(n) = 1: S(n) = Theta(log n)
For f(n) = log n: S(n) = Theta(log^2 n)
For f(n) = n: S(n) = Theta(n)
Empirical Confirmation:
The code outputs confirm:

Logarithmic growth for constant work per level.
Linear growth when the work per level dominates.
