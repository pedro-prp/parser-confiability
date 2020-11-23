import pytest
from util import read_file


@pytest.mark.parametrize("input", ['analysisTime.out', 'totalTime.out'])
def test_read_file_sucess(input):
    base_path = './src/input_files/'
    readed = read_file(base_path + input)

    assert readed is not None
