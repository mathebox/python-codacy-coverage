
import json
import os
import unittest

import codacy.reporter


HERE = os.path.abspath(os.path.dirname(__file__))


def _file_location(*args):
    return os.path.join(HERE, *args)


class ReporterTests(unittest.TestCase):

    def compare_parse_result(self, generated_filename, expected_filename):
        def file_get_contents(filename):
            with open(filename) as f:
                return f.read()

        generated = codacy.reporter.parse_report_file(generated_filename)

        json_content = file_get_contents(expected_filename)
        expected = json.loads(json_content)

        self.assertEqual(generated, expected)

    def test_parser_coverage3(self):
        self.maxDiff = None

        self.compare_parse_result(_file_location('coverage3', 'cobertura.xml'),
                                  _file_location('coverage3', 'coverage.json'))

    def test_parser_coverage4(self):
        self.maxDiff = None

        self.compare_parse_result(_file_location('coverage4', 'cobertura.xml'),
                                  _file_location('coverage4', 'coverage.json'))

    def test_parser_git_filepath(self):
        self.maxDiff = None

        self.compare_parse_result(_file_location('filepath', 'cobertura.xml.tpl'),
                                  _file_location('filepath', 'coverage.json'))


if __name__ == '__main__':
    unittest.main()
