import argparse
import random
import trace

# Global flag for whether to use the Median-Of-Three partition element
useMedianOfThree = False

# Global counter for the number of values compared to the pivot
pivotComparisons = 0

# Global counter for the number of swaps
numSwaps = 0


def quicksort(A, p, r) -> None:
    """Performs the Quicksort algorithm"""
    if p < r:
        # Partition the subarray around the pivot, which ends up A[q].
        q = partition(A, p, r)
        quicksort(A, p, q - 1)  # recursively sort the low side
        quicksort(A, q + 1, r)  # recursively sort the high side


def partition(A, p, r) -> int:
    """Performs the partition element of the Quicksort algorithm"""
    global pivotComparisons
    global numSwaps

    # If Median-Of-Three is used, find the median pivot and move it to the end
    if useMedianOfThree:
        k = (p + r) // 2

        # Order the three elements in-place in the array A[p] <= A[k] <= A[r]
        if A[p] > A[k]:
            A[p], A[k] = A[k], A[p]

        if A[p] > A[r]:
            A[p], A[r] = A[r], A[p]

        if A[k] > A[r]:
            A[k], A[r] = A[r], A[k]

        # Now A[k] is the median, move it to the end to become the pivot
        A[k], A[r] = A[r], A[k]

    x = A[r]  # the pivot
    i = p - 1  # highest index into the low side
    for j in range(p, r):  # process each element other than the pivot
        if A[j] <= x:  # does this element belong on the low side?
            A[i], A[j] = A[j], A[i]  # put this element there
            numSwaps += 1
        pivotComparisons += 1

    A[i + 1], A[r] = A[r], A[i + 1]  # pivot goes just ot the right of the low side

    return i + 1


def generateInput(n: int) -> list[int]:
    """Generates a list of n integers"""
    return [random.randint(0, n) for _ in range(n)]


def getArguments() -> argparse.Namespace:
    """Get the program's arguments"""
    # Program information
    parser = argparse.ArgumentParser(
        prog="Quicksort",
        description="Executes the Quicksort algorithm",
    )

    # Run a trace
    parser.add_argument(
        "-t",
        "--trace",
        action="store_true",
        help="Runs a trace on the algorithm",
    )

    # Specify specific input file if desired
    parser.add_argument(
        "-i",
        "--input",
        action="store",
        default="input.txt",
        help="Specify input file name; can be used for specific inputs when the "
        "'P' flag is omitted, otherwise will save input file to given location",
    )

    # Number of values to use in the Quicksort algorithm
    parser.add_argument(
        "-A",
        "--numValues",
        action="store",
        default=0,
        help="The number of values to use in the Quicksort algorithm",
    )

    # Flag for whether to use Median-Of-Three partition element in the Quicksort algorithm
    parser.add_argument(
        "-m",
        "--medianOfThree",
        action="store_true",
        help="Flag for whether to use Median-Of-Three partition element in the Quicksort algorithm",
    )

    # Output file
    parser.add_argument(
        "-o",
        "--output",
        action="store",
        default="output.txt",
        help="Specify output file name",
    )

    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    """The main function of the program"""
    A: list[int] = []

    # Set the global Median-Of-Three flag
    global useMedianOfThree
    useMedianOfThree = args.medianOfThree

    # Generate
    if args.numValues is not None:
        with open(args.input, "w") as f:
            for value in generateInput(int(args.numValues)):
                print(value, file=f)

    # Input
    try:
        with open(args.input, "r") as f:
            for line in f.readlines():
                A.append(int(line))
    except FileNotFoundError:
        print(f"Could not find {args.input}")
        exit()

    # Run the Quicksort algorithm
    quicksort(A, 0, len(A) - 1)

    # Print algorithm results
    print(f"Number of values compared to the pivot: {pivotComparisons}")
    print(f"Number of swaps: {numSwaps}")

    # Save the output
    with open(args.output, "w") as f:
        for value in A:
            print(value, file=f)


if __name__ == "__main__":
    # Get the program's arguments
    args = getArguments()

    # Run a trace
    if args.trace:
        # Create Trace object
        tracer = trace.Trace(
            ignoredirs=[],
            trace=0,
            count=1,
        )

        # Run trace
        tracer.run("main(args)")

        # Make a report
        r = tracer.results()
        r.write_results(show_missing=True, coverdir="traceOutput")

    # Run normally
    else:
        main(args)
