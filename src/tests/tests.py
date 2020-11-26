import pytest
import os
from pathlib import Path
from util import read_file, check_delimiter_valid, output_file, parse_file
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
    ('analysisTime.out', {
        1: [439, 705, 738, 729, 752, 740, 658, 713, 765, 710],
        2: [470, 828, 760, 668, 884, 721, 720, 802, 777, 735],
        3: [446, 789, 763, 692, 910, 966, 751, 1002, 720, 752],
        4: [457, 852, 739, 710, 763, 838, 761, 763, 742, 699],
        5: [472, 734, 726, 708, 817, 811, 763, 757, 789, 678],
        6: [470, 760, 701, 764, 849, 747, 771, 884, 757, 669],
        7: [462, 737, 714, 729, 788, 836, 687, 772, 694, 776],
        8: [509, 696, 738, 710, 758, 763, 689, 764, 804, 717],
        9: [500, 753, 808, 778, 739, 812, 724, 846, 740, 746],
        10: [493, 740, 717, 728, 839, 722, 736, 810, 703, 756],
        11: [466, 1013, 748, 773, 809, 730, 727, 787, 771, 710],
        12: [514, 1060, 771, 754, 766, 903, 792, 930, 829, 856],
        13: [506, 784, 977, 904, 872, 774, 875, 811, 774, 756],
        14: [676, 876, 905, 762, 929, 825, 728, 853, 822, 798],
        15: [919, 804, 783, 769, 760, 908, 887, 802, 783, 797],
        16: [897, 896, 805, 839, 914, 834, 853, 996, 913, 822],
        17: [862, 846, 970, 999, 982, 1003, 848, 819, 871, 925],
        18: [865, 810, 791, 865, 830, 851, 860, 847, 855, 892],
        19: [835, 875, 866, 875, 820, 833, 928, 901, 870, 836],
        20: [874, 896, 809, 827, 962, 849, 873, 907, 845, 896]
    }),
    ('totalTime.out', {
        1: [776, 1102, 1121, 1134, 1161, 1204, 1070, 1140, 1157, 1091],
        2: [831, 1205, 1164, 1069, 1287, 1173, 1129, 1200, 1181, 1116],
        3: [786, 1180, 1134, 1085, 1302, 1381, 1164, 1389, 1114, 1175],
        4: [790, 1241, 1126, 1140, 1188, 1268, 1155, 1143, 1158, 1077],
        5: [799, 1145, 1137, 1117, 1271, 1290, 1216, 1149, 1207, 1072],
        6: [824, 1170, 1109, 1180, 1251, 1171, 1171, 1297, 1169, 1099],
        7: [795, 1137, 1225, 1167, 1178, 1232, 1154, 1177, 1134, 1208],
        8: [844, 1091, 1201, 1138, 1140, 1191, 1098, 1174, 1235, 1121],
        9: [840, 1208, 1265, 1225, 1155, 1205, 1131, 1276, 1146, 1203],
        10: [849, 1170, 1211, 1184, 1228, 1142, 1198, 1204, 1158, 1170],
        11: [852, 1463, 1202, 1218, 1241, 1112, 1189, 1266, 1244, 1162],
        12: [883, 1520, 1213, 1172, 1196, 1316, 1272, 1347, 1296, 1331],
        13: [880, 1199, 1438, 1352, 1275, 1195, 1348, 1228, 1223, 1203],
        14: [1065, 1312, 1379, 1207, 1343, 1291, 1148, 1269, 1268, 1255],
        15: [1386, 1222, 1218, 1219, 1149, 1418, 1297, 1243, 1239, 1229],
        16: [1342, 1350, 1236, 1333, 1363, 1391, 1299, 1432, 1394, 1254],
        17: [1317, 1302, 1405, 1430, 1427, 1480, 1275, 1255, 1320, 1374],
        18: [1344, 1270, 1231, 1280, 1283, 1357, 1321, 1278, 1290, 1348],
        19: [1258, 1329, 1298, 1332, 1251, 1308, 1371, 1319, 1331, 1306],
        20: [1337, 1338, 1232, 1260, 1408, 1341, 1290, 1357, 1274, 1323]
    })
])
def test_parse_file(input_file, expected_out):
    base_path = Path(os.getcwd())
    f = base_path / "src" / "input_files" / input_file
    content = read_file(f)
    parsed = parse_file(content)
    assert parsed == expected_out
