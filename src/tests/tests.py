import pytest

input_files_path = ['analysisTime.out','totalTime.out']
@pytest.mark.parametrize("input", input_files_path)
def test_read_file_sucess():
    readed = read_file(input)
    assert readed is not None
