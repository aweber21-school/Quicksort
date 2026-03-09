# Quicksort
This repository contains the Quicksort algorithm for EN.605.621 Programming Assignment 2

## Implementation
The Quicksort algorithm is implemented in Python. This algorithm can be ran the
same way as any other Python script, along wiht flags to control functionality.
An example command line command is shown below:

```
python Quicksort.py -t -A 500 -m -i inputFile.txt -o outputFile.txt
```

## Files
This repository contains this README, the source code for the Quicksort
algorithm, traces, and test cases. The file structure is shown below:

```
Quicksort
|---> README.md
|---> Quicksort.py
|---> traces/
|     |---> trace-A#[-m]/
|     |     |---> input-A#[-m].txt
|     |     |---> output-A#[-m].txt
|     |     |---> results-A#[-m].txt
|     |     |---> traceOutput-A#[-m]/
|     |           |---> Quicksort.cover
|     |           |---> random.cover
|     |---> ...
|---> testCases/
      |---> medianOfThree/
      |     |---> testCase-A#-m/
      |     |     |---> input-A#-m.txt
      |     |     |---> output-A#-m.txt
      |     |     |---> results-A#-m.txt
      |     |     |---> traceOutput-A#-m/
      |     |           |---> Quicksort.cover
      |     |           |---> random.cover
      |     |---> ...
      |---> normal/
            |---> testCase-A#/
            |     |---> input-A#.txt
            |     |---> output-A#.txt
            |     |---> results-A#.txt
            |     |---> traceOutput-A#/
            |           |---> Quicksort.cover
            |           |---> random.cover
            |---> ...
```
