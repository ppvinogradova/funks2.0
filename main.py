
class Contact:
  
  def __init__(self, name, surname, phone_num, fav=False, *args, **kwargs):
    self.name = name
    self.surname = surname
    self.phone_num = phone_num
    self.fav = fav
    self.args = args
    self.kwargs = kwargs

  def __str__(self):

    def fav(self):
      x = str()
      if self.fav==False:
        x = 'Нет'
      else:
        x = 'Да'
      return x

    def add(self):
      args = []
      for arg in self.args:
        args.append(arg)
        args.append('\n')
      together = '  '.join(args)
      info = list(self.kwargs.items())
      kwargs = []
      for pair in info:
        b = ': '.join(pair)
        kwargs.append(b)
        kwargs.append('\n')
      result = '  '.join(kwargs)
      return '{}  {}'.format(together, result)

    return f'''Имя: {self.name} 
Фамилия: {self.surname}
Телефон: {self.phone_num}
В избранных: {fav(self)}
Дополнительная информация:
  {add(self)}'''

jhon = Contact('Jhon', 'Smith', '+71234567809', False, 'любит хот-доги', 'выгуливает собак', telegram='@jhony', email='jhony@smith.com')

mary = Contact('Mary', 'Johnsson', '+9097483553', True, 'массаж')

kate = Contact('Kate', 'Wang', '+0765246789', True, telegram='@w_kate')

data = [[jhon.name, jhon.surname, jhon.phone_num, jhon.fav, jhon.args, jhon.kwargs],[mary.name, mary.surname, mary.phone_num, mary.fav, mary.args, mary.kwargs], [kate.name, kate.surname, kate.phone_num, kate.fav, kate.args, kate.kwargs]]

#print(type(jhon))

class PhoneBook:

  def __init__(self, book_name):
    self.book_name = book_name
    

  def print_contacts(self):
    if self.book_name == Contact:
      for name in data:
        print(name)

  def add_contact(self, name, surname, phone_num, fav=False, *args, **kwargs):
    if self.book_name == Contact:
      info = [name, surname, phone_num, fav, args, kwargs]
      data.append(info)
      print(data)

  def del_contact(self, number):
    if self.book_name == Contact:
      for contact in data:
        if number in contact:
          data.remove(contact)
      print(data)

  def find_fav(self):
    if self.book_name == Contact:
      for contact in data:
        if True in contact:
          print(contact)

  def search(self, name, surname):
    if self.book_name == Contact:
      for contact in data:
        if name and surname in contact:
          print(contact)
 

book = PhoneBook(Contact)
# book.print_contacts()
# book.add_contact('July', 'Fox', '+793745566')
# book.del_contact('+71234567809')
# book.find_fav()
# book.search('Mary', 'Johnsson')
