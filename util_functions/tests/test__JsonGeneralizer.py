import json
import pytest
from pathlib import Path

from util_functions import JsonGeneralizer


@pytest.fixture(scope='module')
def mockups():
    inputs_path_str = 'util_functions/tests/mockups/json_generalizer/inputs'
    structures_path_str = 'util_functions/tests/mockups/json_generalizer' \
                          '/generalized_structures'
    
    inputs_path = Path(inputs_path_str)
    structs_path = Path(structures_path_str)

    inputs_paths_to_files = [item for item in sorted(inputs_path.iterdir()) 
                             if not item.name.startswith('.')]
    structs_paths_to_files = [item for item in sorted(structs_path.iterdir())
                                 if not item.name.startswith('.')]
    
    mockups_data = {"inputs": [], "structures": []}
    for input_, structure in zip(inputs_paths_to_files, structs_paths_to_files):
        with open(input_, "r") as f:
            mockups_data["inputs"].append(json.load(f))
        with open(structure, "r") as f:
            mockups_data["structures"].append(json.load(f))
    return mockups_data


def test__generalized_structure(mockups):
    mockups = mockups
    for input_, structure in zip(mockups["inputs"], mockups["structures"]):
        jg = JsonGeneralizer(input_)
        jg.generalize()
        generalized_json = jg.generalized_json

        assert generalized_json == structure


def test__postprocessing():
    input_1 = [{"a": "abc", "b": [1, 2, 3]} for _ in range(10)]
    expected_output_1 = input_1[:2]
    actual_output_1 = JsonGeneralizer.postprocess_generalized_json(input_1)

    input_2 = [{"a": "abc", "b": [1, 2, 3]} for _ in range(1)]
    expected_output_2 = input_2
    actual_output_2 = JsonGeneralizer.postprocess_generalized_json(input_2)

    assert actual_output_1 == expected_output_1
    assert actual_output_2 == expected_output_2
