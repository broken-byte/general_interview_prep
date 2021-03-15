from unittest import TestCase, TestLoader, TextTestRunner
from typing import Callable
import functools
import time

from func_timeout import func_set_timeout


class TestContainerTemplate(TestCase):
    time_elapsed_message: str


def make_test_function(
        t_name: str, t_data: dict, t_function, timed: bool = False, timeout: int = 0) -> Callable[[dict], None]:
    params: dict = t_data["params"]
    expected = t_data["expected"]
    debug_console_line: str = (f"------------------------------------------------ {t_name} "
                               "------------------------------------------------\n")
    test_log_message: str = (f"\n============================== {t_name} ====================================\n"
                             f"\nalgorithm being tested: {t_function.__name__}\n"
                             f"\nparameters: {params}\n")
    if timed:
        @complexity_timer
        @func_set_timeout(timeout)
        def test_template(self):
            print(debug_console_line)
            actual = t_function(**params)
            self.assertEqual(expected, actual, test_log_message)

    else:
        def test_template(self):
            print(debug_console_line)
            actual = t_function(**params)
            self.assertEqual(expected, actual, test_log_message)
    return test_template


def complexity_timer(function_template):
    @functools.wraps(function_template)
    def wrapper_timer(self):
        tic = time.perf_counter()
        function_template(self)
        tock = time.perf_counter()
        time_log = f'finished in {tock - tic:0.10f} seconds\n'
        print(time_log)
    return wrapper_timer


def dynamically_generate_tests(tests: dict, function_being_tested, timed: bool = False, timeout: int = 60):
    for t_name, t_data in iter(tests.items()):
        unittest_function = make_test_function(t_name, t_data, function_being_tested, timed=timed, timeout=timeout)
        setattr(TestContainerTemplate, f"{t_name}", unittest_function)


def run_dynamic_tests():
    suite = TestLoader().loadTestsFromTestCase(TestContainerTemplate)
    TextTestRunner(verbosity=3).run(suite)
