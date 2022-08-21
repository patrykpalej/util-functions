import json
import pytest
from pathlib import Path

from util_functions import get_json_structure


@pytest.fixture(scope='module')
def mockups():
    inputs_path_str = 'tests/mockups/json_generalizer/inputs'
    structures_path_str = 'tests/mockups/json_generalizer' \
                          '/generalized_structures'

    inputs_path = Path(inputs_path_str)
    structures_path = Path(structures_path_str)

    inputs_paths_to_files = [item for item in sorted(inputs_path.iterdir())
                             if not item.name.startswith('.')]
    structures_paths_to_files = [item for item in
                                 sorted(structures_path.iterdir())
                                 if not item.name.startswith('.')]

    mockups_data = {"inputs": [], "structures": []}
    for input_, structure in zip(inputs_paths_to_files,
                                 structures_paths_to_files):
        with open(input_, "r") as f:
            mockups_data["inputs"].append(json.load(f))
        with open(structure, "r") as f:
            mockups_data["structures"].append(json.load(f))
    return mockups_data


def test__json_structure_from_object(mockups):
    mockups = mockups
    for input_, structure in zip(mockups["inputs"], mockups["structures"]):
        assert get_json_structure(input_) == structure


def test__json_structure_from_path(mockups):
    path_to_mockups = "tests/mockups/json_generalizer/inputs"
    mockup_paths = [Path(path_to_mockups).joinpath(f"input_{i}.json")
                    for i in range(1, 7)]
    expected_structures = mockups["structures"]

    for path, structure in zip(mockup_paths, expected_structures):
        assert get_json_structure(str(path)) == structure
        assert get_json_structure(path) == structure


def test__invalid_paths():
    path_not_to_json_file = "invalid/path/to/file"
    invalid_path_to_json_file = "invalid/path/to/file.json"

    with pytest.raises(TypeError, match="must be a path to .json file"):
        get_json_structure(path_not_to_json_file)

    with pytest.raises(FileNotFoundError, match="No such file"):
        get_json_structure(invalid_path_to_json_file)


def test__invalid_objects():
    tuple_ = (1, 2, 3)
    int_ = 4
    float_ = 5.6

    with pytest.raises(TypeError, match=r"must be a path .* or a JSON object"):
        get_json_structure(tuple_)

    with pytest.raises(TypeError, match=r"must be a path .* or a JSON object"):
        get_json_structure(int_)

    with pytest.raises(TypeError, match=r"must be a path .* or a JSON object"):
        get_json_structure(float_)
