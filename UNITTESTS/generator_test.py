import unittest
from unittest.mock import patch, Mock
from generator import get_context, generate_protocol
import os

class TestGenerateProtocol(unittest.TestCase):
    def test_generate_protocol_with_valid_filename(self):
        filename = "test_protocol.docx"
        expected_context = {
            'protocolNumber': None,
            'date': None,
            'month': None,
            'year': None,
            'workType': None,
            'surnameNamePatronymic': None,
            'institute': None,
            'formOfEducation': None,
            'codeNameOfDirection': None,
            'nameOfProfile': None,
            'topic': None,
            'ChairmanOfGEC': None,
            'firstMemberOfGEC': None,
            'secondMemberOfGEC': None,
            'thirdMemberOfGEC': None,
            'fourthMemberOfGEC': None,
            'fifthMemberOfGEC': None,
            'headOfFQW': None,
            'consultants': 'None\nNone\nNone',
            'pagesFQW': None,
            'pagesAppendix': None,
            'AssesmentOfHead': None,
            'questions': None,
            'averegeMark': None,
            'opinion': None,
            'disadvantages': None,
            'mark': None,
            'fullAeregeMark': None,
            'fullName': None,
            'Distinction': None,
            'surnameNPChairman': None,
            'surnameNPSecretary': None
        }

        with patch('generator.DocxTemplate') as MockDocxTemplate:
            mock_doc = MockDocxTemplate.return_value  # Mock instance of DocxTemplate
            mock_doc.render = Mock()
            mock_doc.save = Mock()

            context = generate_protocol(filename)

            # Check that the file was created
            self.assertTrue(mock_doc.render.called)
            self.assertTrue(mock_doc.save.called)
            mock_doc.save.assert_called_once_with(filename)
            self.assertEqual(context, expected_context)

        # Clean up any generated files
        if os.path.exists(filename):
            os.remove(filename)

    @patch('os.path.exists')
    def test_generate_protocol_raises_file_exists_error(self, mock_os_path_exists):
        mock_os_path_exists.return_value = True  # Emulate that the file already exists
        filename = "test_protocol.docx"

        with self.assertRaises(FileExistsError) as context:
            generate_protocol(filename)

        self.assertEqual(str(context.exception), f"Файл с именем {filename} уже существует!")

    def test_get_context(self):
        args = {
            'protocolNumber': '123',
            'date': '01',
            'month': 'January',
            'year': '2023',
            'workType': 'Diploma',
            'surnameNamePatronymic': 'Иванов Иван Иванович',
            'institute': 'МГУ',
            'formOfEducation': 'Очная',
            'codeNameOfDirection': '01.01.01',
            'nameOfProfile': 'Профиль',
            'topic': 'Тема дипломной работы',
            'ChairmanOfGEC': 'Петров Петр Петрович',
            'firstMemberOfGEC': 'Сидоров Сидор Сидорович',
            'secondMemberOfGEC': 'Кузнецов Кузьма Кузьмич',
            'thirdMemberOfGEC': 'Васильев Василий Васильевич',
            'fourthMemberOfGEC': 'Михайлов Михаил Михайлович',
            'fifthMemberOfGEC': 'Алексеев Алексей Алексеевич',
            'headOfFQW': 'Иванова Ирина Ивановна',
            'consultants': ['Консультант 1', 'Консультант 2'],
            'pagesFQW': '100',
            'pagesAppendix': '10',
            'AssesmentOfHead': 'Оценка руководителя',
            'questions': 'Вопросы к защите',
            'averegeMark': '5',
            'opinion': 'Мнение комиссии',
            'disadvantages': 'Недостатки работы',
            'mark': 'Отлично',
            'fullAeregeMark': '5',
            'fullName': 'Иванов Иван Иванович',
            'Distinction': 'С отличием',
            'surnameNPChairman': 'Петров П.П.',
            'surnameNPSecretary': 'Сидоров С.С.'
        }
        context = get_context(args)

        self.assertEqual(context['protocolNumber'], '123')
        self.assertEqual(context['date'], '01')
        self.assertEqual(context['month'], 'January')
        self.assertEqual(context['year'], '2023')
        self.assertEqual(context['workType'], 'Diploma')
        self.assertEqual(context['surnameNamePatronymic'], 'Иванов Иван Иванович')
        self.assertEqual(context['institute'], 'МГУ')
        self.assertEqual(context['formOfEducation'], 'Очная')
        self.assertEqual(context['codeNameOfDirection'], '01.01.01')
        self.assertEqual(context['nameOfProfile'], 'Профиль')
        self.assertEqual(context['topic'], 'Тема дипломной работы')
        self.assertEqual(context['ChairmanOfGEC'], 'Петров Петр Петрович')
        self.assertEqual(context['firstMemberOfGEC'], 'Сидоров Сидор Сидорович')
        self.assertEqual(context['secondMemberOfGEC'], 'Кузнецов Кузьма Кузьмич')
        self.assertEqual(context['thirdMemberOfGEC'], 'Васильев Василий Васильевич')
        self.assertEqual(context['fourthMemberOfGEC'], 'Михайлов Михаил Михайлович')
        self.assertEqual(context['fifthMemberOfGEC'], 'Алексеев Алексей Алексеевич')
        self.assertEqual(context['headOfFQW'], 'Иванова Ирина Ивановна')
        self.assertEqual(context['consultants'], 'Консультант 1\nКонсультант 2')
        self.assertEqual(context['pagesFQW'], '100')
        self.assertEqual(context['pagesAppendix'], '10')
        self.assertEqual(context['AssesmentOfHead'], 'Оценка руководителя')
        self.assertEqual(context['questions'], 'Вопросы к защите')
        self.assertEqual(context['averegeMark'], '5')
        self.assertEqual(context['opinion'], 'Мнение комиссии')
        self.assertEqual(context['disadvantages'], 'Недостатки работы')
        self.assertEqual(context['mark'], 'Отлично')
        self.assertEqual(context['fullAeregeMark'], '5')
        self.assertEqual(context['fullName'], 'Иванов Иван Иванович')
        self.assertEqual(context['Distinction'], 'С отличием')
        self.assertEqual(context['surnameNPChairman'], 'Петров П.П.')
        self.assertEqual(context['surnameNPSecretary'], 'Сидоров С.С.')

if __name__ == '__main__':
    unittest.main()
