

functionality_test_data: dict = {
    "test_0": {
        "params": {
            "n": 2,
            "m": 3,
            "source": [0, 0],
            "target": [1, 2]
        },
        "expected": 3
    },
    "test_1": {
        "params": {
            "n": 1,
            "m": 1,
            "source": [0, 0],
            "target": [0, 0]
        },
        "expected": 1
    },
    "test_2": {
        "params": {
            "n": 0,
            "m": 0,
            "source": [0, 0],
            "target": [0, 0]
        },
        "expected": 0
    },
    "test_3": {
        "params": {
            "n": 3,
            "m": 3,
            "source": [1, 0],
            "target": [2, 1]
        },
        "expected": 2
    }
}
