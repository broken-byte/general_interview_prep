

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "grid": [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]],
            "sr": 0,
            "sc": 0,
            "tr": 2,
            "tc": 0
        },
        "expected": 8
    },
    "test_1": {
        "params": {
            "grid": [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]],
            "sr": 0,
            "sc": 0,
            "tr": 2,
            "tc": 0
        },
        "expected": -1
    },
}
