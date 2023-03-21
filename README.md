# Week 9 workshop: Chaos and the logistic map

This week you'll be **pair programming**. Choose one of you to be the driver first; then, every 15 minutes or so, **swap roles**. The driver writes code and shares their screen, the navigator is an active observer/helper.

Work in the script `logistic.py`.


## Task 1: The logistic map

In the Week 7 workshop we saw a variant of the logistic differential equation, used to model a population of fish.

The **logistic map** is a related recurrence equation, and is defined by

x<sub>k+1</sub> = ax<sub>k</sub>(1 - x<sub>k</sub>)

Depending on the value of a, the solutions can exhibit *chaotic* behaviour. For more information about the logistic map, see [here for instance](https://mathworld.wolfram.com/LogisticMap.html).

Consider four values for a: a = 2.9, a = 3.1, a = 3.5, and a = 3.7. For each value of a, compute and plot the first 200 terms in the sequence defined by the logistic map. Use the `np.random.rand()` function to generate a pseudorandom value for the initial value x<sub>0</sub>.


## Task 2: Visualising bifurcations

Write code which performs 100 iterations of the logistic map and, on each iteration, plot the current value for x<sub>k</sub> against a. Plot each point one by one *inside the loop* using an `'o'` marker with `markersize=2`, and `color=[0.1]*4` to display each point as a transparent light grey dot (by giving `[red, green, blue, alpha]` values; [see documentation](https://matplotlib.org/stable/tutorials/colors/colors.html)). The darker spots will then correspond to overlapping dots, indicating e.g. convergence to a particular point.

Use a = 2.5, and use the `np.random.rand(1)` command to generate a pseudorandom value for the initial guess x<sub>0</sub>.

Then, edit your code so that, after these 100 iterations have been performed, a is increased to 2.525, and a further 100 iterations of the logistic map are performed, with x<sub>0</sub> now set equal to the final value for x<sub>k</sub> obtained at a = 2.5. Plot each value of x<sub>k</sub> obtained against the current value for a, all on the same figure as you started with.

Continue this procedure, increasing a by 0.025 until a = 3.8 is reached, plotting all obtained values for x<sub>k</sub> against the respective values for a on a single figure. Each time a is increased the new starting value for x<sub>0</sub> should be set to be equal to final value of x<sub>k</sub> reached at the previous value of a.

Recall that, on your final figure, a dark spot corresponds to many overlapping points; and each vertical column of points corresponds to iteration with one value of a. Do these results correspond to your observations from Task 1?

## Task 3: Cobweb diagram

Adapt the script `cobweb.py` from the [Week 9 video](https://github.com/cnu-23/cnu-w09-lecture) (copied in this repo) to generate cobweb diagrams for the logistic map for different values of a. You can make the pause time very small so you can see it appear quickly, and you can use the `alpha` parameter to make a semi-transparent line (to better visualise when/if lines start overlapping).

Does this correspond to your observations from Task 2? What happens around the values of a where you saw a bifurcation in Task 2?

*Note: if you haven't yet reviewed the Week 9 video, the cobweb diagram is explained in the first 10 minutes. What you will need to change is the iteration function G(x), which for this task, is the RHS of the logistic map.*
