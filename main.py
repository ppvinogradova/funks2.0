
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
      try:
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
      except TypeError:
        return None 
    return f'''Имя: {self.name} 
Фамилия: {self.surname}
Телефон: {self.phone_num}
В избранных: {fav(self)}
Дополнительная информация:
  {add(self)}'''

jhon = Contact('Jhon', 'Smith', '+71234567809', False, 'любит хот-доги', 'выгуливает собак', telegram='@jhony', email='jhony@smith.com')

mary = Contact('Mary', 'Johnsson', '+9097483553', True, 'массаж')

kate = Contact('Kate', 'Wang', '+0765246789', True, telegram='@w_kate')

data = [jhon, mary, kate]

#print(jhon)

class PhoneBook:

  def __init__(self, book_name):
    self.book_name = book_name
    self.contacts = []
    

  def print_contacts(self):
    print(self.book_name + '\n')
    for name in data:
      print(name)

  def add_contact(self, name, surname, phone_num, fav=False, *args, **kwargs):
    add = Contact(name, surname, phone_num, fav, args, kwargs)
    data.append(add)
    print(self.book_name + '\n')
    for name in data:
      print(name)

  def del_contact(self, number):
    for contact in data:
      if number == contact.phone_num:
        data.remove(contact)
    print(self.book_name + '\n')
    for name in data:
      print(name)

  def find_fav(self):
    print(self.book_name + '\n')
    for contact in data:
      if contact.fav:
        print(contact)

  def search(self, name, surname):
    print(self.book_name + '\n')
    for contact in data:
      if name == contact.name and surname == contact.surname:
        print(contact)
    
 

frirends = PhoneBook('Friends')
#frirends.print_contacts()
#frirends.add_contact('July', 'Fox', '+793745566')
#frirends.del_contact('+71234567809')
#frirends.find_fav()
#frirends.search('Mary', 'Johnsson')
