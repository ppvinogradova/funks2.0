
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

if __name__ == '__main__':
  print(jhon)