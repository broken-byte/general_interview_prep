import time
# TODO: I bet you could find a way to not have to repeat that with block....;)


def process_test_file_where_single_line_is_an_int_array(test_file_path: str) -> list:
    with open(test_file_path, "r") as f:
        for line in f:
            processed_data = convert_line_into_integer_list(line)
            return processed_data


def process_test_file_where_single_line_is_a_str_array(test_file_path: str) -> list:
    with open(test_file_path, "r") as f:
        for line in f:
            processed_data = convert_line_into_str_list(line)
            return processed_data


def process_test_file_where_single_line_is_a_string(test_file_path: str) -> str:
    with open(test_file_path, "r") as f:
        for line in f:
            processed_data = convert_line_into_str(line)
            return processed_data


def process_test_file_where_lines_are_int_arrays(test_file_path: str, exclude_index: int = -1) -> list:
    processed_data: list = []
    with open(test_file_path, "r") as f:
        for index, line in enumerate(f):
            if index > exclude_index:
                line = convert_line_into_integer_list(line)
                processed_data.append(line)
        if len(processed_data) == 1:
            return processed_data[0]
        else:
            return processed_data


def process_test_file_where_lines_are_str_arrays(test_file_path: str, exclude_index: int = -1) -> list:
    processed_data: list = []
    with open(test_file_path, "r") as f:
        for index, line in enumerate(f):
            if index > exclude_index:
                line = convert_line_into_str_list(line)
                processed_data.append(line)
    return processed_data


def process_test_file_where_lines_are_int_elements(test_file_path: str, exclude_index: int = -1) -> list:
    processed_data: list = []
    with open(test_file_path, "r") as f:
        for index, line in enumerate(f):
            if index > exclude_index:
                processed_line = convert_line_into_int(line)
                processed_data.append(processed_line)
    if len(processed_data) == 1:
        processed_data = processed_data[0]
    return processed_data


def process_test_file_where_lines_are_str_elements(test_file_path: str, exclude_index: int = -1) -> list:
    processed_data: list = []
    with open(test_file_path, "r") as f:
        for index, line in enumerate(f):
            if index > exclude_index:
                processed_line = convert_line_into_str(line)
                processed_data.append(processed_line)
    if len(processed_data) == 1:
        processed_data = processed_data[0]
    return processed_data


def convert_line_into_integer_list(line: str) -> list:
    line = line.strip("\n")
    line = line.split(" ")
    line = [int(element) for element in line]
    return line


def convert_line_into_str_list(line: str) -> list:
    line = line.strip("\n")
    line = line.split(" ")
    return line


def convert_line_into_int(line: str) -> int:
    line = line.strip("\n")
    return int(line)


def convert_line_into_str(line: str) -> str:
    line = line.strip("\n")
    return line


def get_console_time_logged_result_of(function, *function_args):
    tic = time.perf_counter()
    actual: int = function(*function_args)
    tock = time.perf_counter()
    time_log = f'\n{function.__name__}() finished in {tock - tic:0.10f} seconds'
    print(time_log)
    return actual
