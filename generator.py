from docxtpl import DocxTemplate
from docx import Document
import os
def get_context(args):
  context = {
    'protocolNumber': args.get('protocolNumber'),
    'date': args.get('date'),
    'month': args.get('month'),
    'year': args.get('year'),
    'workType': args.get('workType'),
    'surnameNamePatronymic': args.get('surnameNamePatronymic'),
    'institute': args.get('institute'),
    'formOfEducation': args.get('formOfEducation'),
    'codeNameOfDirection': args.get('codeNameOfDirection'),
    'nameOfProfile': args.get('nameOfProfile'),
    'topic': args.get('topic'),
    'ChairmanOfGEC': args.get('ChairmanOfGEC'),
    'firstMemberOfGEC': args.get('firstMemberOfGEC'),
    'secondMemberOfGEC': args.get('secondMemberOfGEC'),
    'thirdMemberOfGEC': args.get('thirdMemberOfGEC'),
    'fourthMemberOfGEC': args.get('fourthMemberOfGEC'),
    'fifthMemberOfGEC': args.get('fifthMemberOfGEC'),
    'headOfFQW': args.get('headOfFQW'),
    'consultants': "\n".join(args.get('consultants', [])),
    'pagesFQW': args.get('pagesFQW'),
    'pagesAppendix': args.get('pagesAppendix'),
    'AssesmentOfHead': args.get('AssesmentOfHead'),
    'questions': args.get('questions'),
    'averegeMark': args.get('averegeMark'),
    'opinion': args.get('opinion'),
    'disadvantages': args.get('disadvantages'),
    'mark': args.get('mark'),
    'fullAeregeMark': args.get('fullAeregeMark'),
    'fullName': args.get('fullName'),
    'Distinction': args.get('Distinction'),
    'surnameNPChairman': args.get('surnameNPChairman'),
    'surnameNPSecretary': args.get('surnameNPSecretary')
  }
  return context
def generate_protocol(filename):
  if os.path.exists(filename):
    raise FileExistsError(f"Файл с именем {filename} уже существует!")
  template_path = os.path.join(os.path.dirname(__file__), "template.docx")  
  doc = DocxTemplate(template_path)
  args = {
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
    'consultants': ['None', 'None', 'None'],
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
  context = get_context(args)
  doc.render(context)
  doc.save(filename)
  return context
if __name__ == "__main__":
  filename = input("Введите имя файла для сохранения (например, protocol.docx): ")
  try:
    generate_protocol(filename)
    print(f"Файл {filename} успешно создан!")
  except FileExistsError as e:
    print(f"Ошибка: {e}") 
  