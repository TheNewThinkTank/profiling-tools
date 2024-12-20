"""
read stats file generated by cProfile,
convert to dataframe and visualize
"""

import pstats
import matplotlib.pyplot as plt
import pandas as pd  # type: ignore


def stats_to_txt(infile: str, outfile: str) -> None:
    """_summary_

    :param infile: _description_
    :type infile: str
    :param outfile: _description_
    :type outfile: str
    """

    with open(outfile, "w") as stream:
        stats = pstats.Stats(infile, stream=stream)
        stats.strip_dirs().sort_stats("cumtime").print_stats()


def txt_to_df(infile: str) -> pd.DataFrame:
    """_summary_

    :param infile: _description_
    :type infile: str
    """

    with open(infile, "r") as rf:
        lines = rf.readlines()
        lines = [line.removesuffix("\n") for line in lines]
    header = lines[6].split()

    data: list[list[str]] = [line.split() for line in lines[7:]]

    data = [d for d in data if len(d) == len(header)]  # Ensure data aligns with header length
    # Convert to DataFrame
    df = pd.DataFrame(data=data, columns=header)
    print(df.head())

    return df


def extract_function_name(entry: str) -> str:
    """Extract the function name from a given 'filename:lineno(function)' entry."""
    if '{' in entry and '}' in entry:
        # Handle built-in methods, e.g., '{built-in method builtins.isinstance}'
        return entry.split()[-1].strip('{}')
    else:
        # Handle regular file-based functions, e.g., 'file.py:47(function_name)'
        return entry.split('(')[-1].split(')')[0]


def visualize(df: pd.DataFrame) -> None:
    """Visualize the most time-consuming functions."""

    df['function_name'] = df['filename:lineno(function)'].apply(extract_function_name)

    # plot cumulative time vs function name
    plt.figure(figsize=(10, 6))
    df = df.sort_values(by='cumtime', ascending=False).head(10)  # Top 10 longest running calls
    plt.barh(df['function_name'], df['cumtime'], color='skyblue')
    plt.xlabel('Cumulative Time (seconds)')
    plt.ylabel('Function')
    plt.title('Top 10 Longest Running Functions')
    plt.gca().invert_yaxis()  # Invert to show the longest at the top
    plt.show()


def main():
    """_summary_
    """
    infile = "stats/get_all_durations.stats"  # "stats/get_workout_duration.stats"

    outfile = infile.split(".")[0] + "_report.txt"

    stats_to_txt(infile, outfile)
    df = txt_to_df(infile=outfile)
    visualize(df)


if __name__ == "__main__":
    main()


# legacy:

# Get 2 longest running calls
# stats.sort_stats("cumtime").print_stats(2)

# get callees of function defined on line 19
# to dig into why a function is taking a long time
# stats.print_callees("get_workout_duration.py:19")

# if a function is taking a long time
# use print_callers to see what is calling it
# stats.print_callers("get_workout_duration.py:13")

# generate profile for snakeviz
# python3 -m cProfile -o stats/get_workout_duration.prof src/utils/get_workout_duration.py

# start SnakeViz from the command line
# snakeviz "stats/get_workout_duration.prof"
