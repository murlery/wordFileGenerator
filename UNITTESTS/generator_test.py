
import unittest
from unittest.mock import patch
from  generator import get_context, generate_protocol  # Замените "your_module" на имя вашего модуля

class TestGenerateProtocol(unittest.TestCase):

    @patch('os.path.exists')
    @patch('os.path.join')
    @patch('docxtempl.DocxTemplate')
    @patch('docx.Document')
    def test_generate_protocol_creates_file(self, mock_Document, mock_DocxTemplate, mock_os_path_join, mock_os_path_exists):
        mock_os_path_exists.return_value = False  # Эмулируем, что файл не существует
        filename = "test_protocol.docx"
        mock_os_path_join.return_value = "template.docx"  # Эмулируем путь к шаблону

        generate_protocol(filename)

        mock_DocxTemplate.assert_called_once_with("template.docx")
        mock_DocxTemplate.return_value.render.assert_called_once()
        mock_DocxTemplate.return_value.save.assert_called_once_with(filename)

    @patch('os.path.exists')
    def test_generate_protocol_raises_file_exists_error(self, mock_os_path_exists):
        mock_os_path_exists.return_value = True  # Эмулируем, что файл уже существует
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
