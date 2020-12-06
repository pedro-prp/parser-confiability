from itertools import zip_longest


class Parser:
    def parse_file(content):
        lines = content.split('\n')
        parsed = {}
        evolution = 0

        for line in lines:
            if not line.isnumeric():
                if not line:
                    break

                evolution += 1
                parsed[evolution] = []
            else:
                parsed[evolution].append(int(line))

        return parsed

    def build_response(parsed_data, delimiter, direction):
        if direction in ['linhas', 'l']:
            response = []
            for key in parsed_data:
                values = parsed_data[key]
                values.insert(0, key)
                line = delimiter.join(str(x) for x in values)
                response.append(line)

            result = '\n'.join(response)
            return result
        else:
            response = []
            for key in parsed_data:
                values = parsed_data[key]
                values.insert(0, key)
                response.append([str(x) for x in values])

            result = list(zip_longest(*response, fillvalue=' '))
            res = []
            for line in result:
                res.append(delimiter.join(line))

            res = '\n'.join(res)
            return res