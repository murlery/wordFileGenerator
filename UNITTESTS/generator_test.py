import unittest
from unittest.mock import patch
from generator import generate_protocol, get_context

class TestGenerateProtocol(unittest.TestCase):
    def test_generate_protocol_empty_context(self):
        #Проверяет создание протокола с пустым контекстом
        with patch('builtins.input', return_value='test_protocol.docx'):
            with patch('os.path.exists', return_value=False):
                with patch('os.path.join') as mock_join:
                    generate_protocol('test_protocol.docx')
                    mock_join.assert_called_once()

    def test_generate_protocol_with_context(self):
        #Проверяет создание протокола с заданным контекстом
        test_context = {
            'protocolNumber': "12",
            'date': "12",
            'month': "январь",
            'year': "24",
            'workType': "Очень длинное название работы, которое должно переноситься на следующую строку",
            'surnameNamePatronymic': "Иванов Иван Иванович",
            'institute': "ИТиАД",
            'formOfEducation': "очное",
            'codeNameOfDirection': "код и направление уровня подготовки",
            'nameOfProfile': "Информационные системы и технологии",
            'topic': "какая-то тема",
            'ChairmanOfGEC': "какой-то председатель",
            'firstMemberOfGEC': "первый член",
            'secondMemberOfGEC': "второй",
            'thirdMemberOfGEC': "третий",
            'fourthMemberOfGEC': "четвертый",
            'fifthMemberOfGEC': "пятый",
            'headOfFQW': "руководитель",
            'consultants': ["Консультант 1", "Консультант 2", "Консультант 3"],
            'pagesFQW': "122",
            'pagesAppendix': "34",
            'AssesmentOfHead': "отзыв",
            'questions': "вопрос один, вопрос два, вопрос три",
            'averegeMark': "средний балл",
            'opinion': "мнение",
            'disadvantages': "недостаток 1, недостаток 2",
            'mark': "пять",
            'fullAeregeMark': "пять",
            'fullName': "Иванов Иван Иванович",
            'Distinction': "с отличием",
            'surnameNPChairman': "фамилия ИО",
            'surnameNPSecretary': "фамилия ИО"
        }
        with patch('builtins.input', return_value='test_protocol.docx'):
            with patch('os.path.exists', return_value=False):
                with patch('os.path.join') as mock_join:
                    with patch('docxtpl.DocxTemplate.render') as mock_render:
                        generate_protocol('test_protocol.docx')
                        mock_render.assert_called_once_with(test_context)

    def test_generate_protocol_file_exists(self):
        #Проверяет обработку ошибки, если файл уже существует
        with patch('builtins.input', return_value='test_protocol.docx'):
            with patch('os.path.exists', return_value=True):
                with self.assertRaisesRegex(FileExistsError, "Файл с именем test_protocol.docx уже существует!"):
                    generate_protocol('test_protocol.docx')

    def test_get_context(self):
        #Проверяет функцию get_context
        test_args = {
            'protocolNumber': "12",
            'date': "12",
            'month': "январь",
            'year': "24",
            'workType': "Очень длинное название работы, которое должно переноситься на следующую строку",
            'surnameNamePatronymic': "Иванов Иван Иванович",
            'institute': "ИТиАД",
            'formOfEducation': "очное",
            'codeNameOfDirection': "код и направление уровня подготовки",
            'nameOfProfile': "Информационные системы и технологии",
            'topic': "какая-то тема",
            'ChairmanOfGEC': "какой-то председатель",
            'firstMemberOfGEC': "первый член",
            'secondMemberOfGEC': "второй",
            'thirdMemberOfGEC': "третий",
            'fourthMemberOfGEC': "четвертый",
            'fifthMemberOfGEC': "пятый",
            'headOfFQW': "руководитель",
            'consultants': ["Консультант 1", "Консультант 2", "Консультант 3"],
            'pagesFQW': "122",
            'pagesAppendix': "34",
            'AssesmentOfHead': "отзыв",
            'questions': "вопрос один, вопрос два, вопрос три",
            'averegeMark': "средний балл",
            'opinion': "мнение",
            'disadvantages': "недостаток 1, недостаток 2",
            'mark': "пять",
            'fullAeregeMark': "пять",
            'fullName': "Иванов Иван Иванович",
            'Distinction': "с отличием",
            'surnameNPChairman': "фамилия ИО",
            'surnameNPSecretary': "фамилия ИО"
        }
        context = get_context(test_args)
        self.assertEqual(context, test_args)

    
    