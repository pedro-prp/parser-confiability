import pytest
from util import read_file, check_delimiter_valid, output_file
from exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException


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


@pytest.mark.parametrize("path, filename", [('wrong_path/nowhere/', 'out_'), ('../../', 'other_output_test')])
def test_path_access(path, filename):
    with pytest.raises(EscritaNaoPermitidaException):
        output_file(path, filename)
