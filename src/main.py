from pathlib import Path
from util import (
    check_delimiter_valid,
    check_file_type,
    check_direction,
    build_response,
    parse_file)

from persistencia import read_file, output_file


if __name__ == '__main__':
    input_path = input('Insira caminho para o arquivo de entrada: ')
    input_path = Path(input_path).resolve()
    print(input_path)

    ftype = input('Insira tipo de arquivo (analysis/total): ')
    check_file_type(ftype)

    delimiter = input('Insira caractere delimitador: ')
    check_delimiter_valid(delimiter)

    direction = input('Insira orientação desejada (colunas/linhas/c/l): ')
    check_direction(direction)

    out_path = input('Insira caminho de saida desejado: ')
    out_path = Path(out_path).resolve()
    filename = ftype + "TimeTab.out"
    full_output_path = out_path / filename
    print(full_output_path)

    content_raw = read_file(input_path)
    parsed_content = parse_file(content_raw)
    response = build_response(parsed_content, delimiter, direction)
    output_file(out_path, filename, response)
