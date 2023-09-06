# Monitor
This package helps to visualize live 2D graph. The package is based on famous **matplotlib**.

# How to use
Let's create two plot and update it in a for loop. We will visualize the update in the runtime.


## `class Plot`
```python

p1 = Plot(title="A")
p2 = Plot(title="B")
```
Here we are initiating plot variable. We can give them a title which will be shown as *legend*.

To update the points of plot we can do this.
```python
p1.update_plot(a,b)
```

## `class LiveMonitor`
```python
live = LiveMonitor(pause=0)
live.plot_list = [p1, p2]
```
Here we are initiing  `live` object of `LiveMonitor` class. This class helps us to draw the live graph.

To update the visualization in a loop we write the following program inside the loop. 
```python
live.update()
```

Full example is shown bellow
```python
from monitor import LiveMonitor

live = LiveMonitor(pause=0)

p1 = Plot(title="A")
p2 = Plot(title="B")
live.plot_list = [p1, p2]

for i in range(100):
    a = i
    b = 2*i**0.5

    # monitor live graph
    p1.update_plot(a,b)
    p2.update_plot(b,a)
    live.update()

# keep the graph on screen after the loop
live.keep_showing()
```
