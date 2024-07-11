from docxtpl import DocxTemplate
from docx import Document
import os
def generate_protocol(filename):
  template_path = os.path.join(os.path.dirname(__file__), "template.docx")  
  doc = DocxTemplate(template_path)
  context = {
    'protocol_number': input("Введите номер протокола: "),
    'date': input("Введите число даты: "),
    'month': input("Введите месяц даты: "),
    'year': input("Введите последние 2 цифры года : "),
    'work_type': input("Введите вид ВКР: "),
    'surname': input("Введите фамилию студента: "),
    'name_patronymic': input("Введите имя и отчество студента: "),
    'institute': input("Введите институт: "),
    'formOfEducation': input("Введите форму обучения: "),
    'code_name_of_direction': input("Введите код и наименование направления подготовки: "),
    'nameOfProfile': input("Введите наименование профиля: "),
    'topic': input("Введите тему: "),
    'ChairmanOfGEC': input("Введите председателя гэк: "),
    'firstMemberOfGEC': input("Введите первого члена: "),
    'secondMemberOfGEC': input("Введите второго члена: "),
    'thirdMemberOfGEC': input("Введите третьего члена: "),
    'fourthMemberOfGEC': input("Введите четвёртого члена: "),
    'fifthMemberOfGEC': input("Введите пятого члена: "),
    'headOfFQW': input("Введите руководителя ВКР: "),
    'consultants': input("Введите консультантов: "),
    'pagesFQW': input("Введите количество страниц ВКР: "),
    'pagesAppendix': input("Введите количество страниц Чертежей/таблиц: "),
    'AssesmentOfHead': input("Введите отзыв руководителя ВКР: "),
    'questions': input("Введите вопросы: "),
    'averegeMark': input("Введите средний балл: "),
    'opinion': input("Введите мнение предсидателя: "),
    'disadvantages': input("Введите недостатки: "),
    'mark': input("Введите оценку прописью: "),
    'fullAeregeMark': input("Введите полную оценку: "),
    'fullName': input("Введите ФИО: "),
    'Distinction': input("Введите с отличием/без отличия: "),
    'surnameNPChairman': input("Введите председателя: "),
    'surnameNPSecretary': input("Введите секветаря: ")
  }
  doc.render(context)
  doc.save(filename)
if __name__ == '__main__': 
  filename = input("Введите имя файла для сохранения (например, protocol.docx): ")
  generate_protocol(filename)
  print(f"Файл {filename} успешно создан!")
  
  
  