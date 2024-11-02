import os
import pytest
from profiling_tools.profiling_utils import profile

# Directory for storing stats
STATS_DIR = "stats"


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    """Setup and teardown function to ensure a clean stats directory."""
    # Create the stats directory if it does not exist
    if not os.path.exists(STATS_DIR):
        os.makedirs(STATS_DIR)

    # Yield to the test
    yield

    # Remove all files in the stats directory after the test
    for file in os.listdir(STATS_DIR):
        file_path = os.path.join(STATS_DIR, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)


def test_profile_decorator_creates_stats_file():
    """Test that the profile decorator creates a stats file."""

    # Define a sample function to test
    @profile
    def sample_function():
        return "Hello, world!"

    # Run the function
    result = sample_function()

    # Assert the function returns the expected value
    assert result == "Hello, world!"

    # Assert that a stats file has been created
    stats_file = os.path.join(STATS_DIR, "sample_function.stats")
    assert os.path.exists(stats_file)
    assert os.path.isfile(stats_file)


def test_profile_decorator_with_args_and_kwargs():
    """Test that the profile decorator works,
    with arguments and keyword arguments.
    """

    @profile
    def sample_function_with_args(a, b=2):
        return a + b

    # Run the function
    result = sample_function_with_args(3, b=4)

    # Assert the function returns the expected value
    assert result == 7

    # Assert that a stats file has been created
    stats_file = os.path.join(STATS_DIR, "sample_function_with_args.stats")
    assert os.path.exists(stats_file)
    assert os.path.isfile(stats_file)
