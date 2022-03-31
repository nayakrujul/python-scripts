This program times 7 different sort methods
(Bubble Sort, Bucket Sort, Insertion Sort,
Quick Sort, Radix Sort, Selection Sort and
Comb Sort) by doing each one 100 times on
each length.
You can change the lengths by altering the
constants `START`, `END` and `INCREMENT` at
the start of get_data.py.

NOTE: get_data.py APPENDS to times.csv so
to get rid of my data you need to delete
times.csv, otherwise the graph may not work.

I have got data from each 10 from 10 to 1000
(10, 20, 30, 40, ..., 970, 980, 990, 1000).

It then takes the average time for all 100
runs on that length for each sort method.

In main.py, it plots a graph of the data
using matplotlib.
You can see a graph of my data in Graph.png.

You will need to have matplotlib installed (use
`pip install matplotlib` in the shell to install)

By nayakrujul (RN09), March 2022