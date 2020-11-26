import pytest
import os
from pathlib import Path
from util import read_file, check_delimiter_valid, output_file, parse_file, build_response
from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from tests.mock.parsed_data_mock import parsed_mock
from tests.mock.response_data_mock import analysis_mock, total_mock

@pytest.mark.parametrize('input', ['analysisTime.out', 'totalTime.out'])
def test_read_file_sucess(input):
    base_path = './src/input_files/'
    readed = read_file(base_path + input)

    assert readed is not None


@pytest.mark.parametrize('input', ['teste1.out', 'asdf.out', 'qwerty.out', 'system.out'])
def test_read_file_fail(input):
    base_path = './src/input_files/'

    with pytest.raises(ArquivoNaoEncontradoException):
        readed = read_file(base_path + input)

        assert readed


@pytest.mark.parametrize('input', [';', '|', ',', '=', '+', '\t', '.', ':', '~'])
def test_delimiter_sucess(input):
    assert check_delimiter_valid(input) is True


@pytest.mark.parametrize('input', ['<>', ';;', ':;', '??', '~^', '[]', '==='])
def test_delimiter_fail(input):

    with pytest.raises(DelimitadorInvalidoException):
        check_delimiter_valid(input)


@pytest.mark.parametrize("path, filename", [('wrong_path/nowhere/', 'out_'), ('./tests/mock/protected_dir', 'out.out')])
def test_path_access(path, filename):
    with pytest.raises(EscritaNaoPermitidaException):
        output_file(path, filename)

@pytest.mark.parametrize("path, filename", [('./tests/mock', 'output.out'), ('./somewhere', 'out.out')])
def test_path_access(tmp_path, path, filename):
    p = tmp_path / path
    f = p / filename
    print(p)
    os.makedirs(p)
    output_file(p, filename)
    assert f.exists() is True


@pytest.mark.parametrize("input_file, expected_out", [
    ('analysisTime.out', parsed_mock['analysis_time']),
    ('totalTime.out', parsed_mock['total_time'])
])
def test_parse_file(input_file, expected_out):
    base_path = Path(os.getcwd())
    f = base_path / "src" / "input_files" / input_file
    content = read_file(f)
    parsed = parse_file(content)
    assert parsed == expected_out


@pytest.mark.parametrize("parsed_data, delimiter, direction, ftype", [
    (parsed_mock['analysis_time'], ';', 'linhas', 'analysis'),
    (parsed_mock['total_time'], ';', 'colunas', 'total')
])
def test_build_response(parsed_data, delimiter, direction, ftype):
    res = build_response(parsed_data, delimiter, direction)
    result_file = ftype + 'TimeTab.out'

    with open(f'./src/tests/mock/{result_file}', 'r') as f:
        mock = f.read()
        assert mock == res
