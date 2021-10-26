def url_parse(url):
   _t_protocol, _, domain, *resource_address = url.strip('/').split('/')
   t_protocol = _t_protocol[:-1]
   return t_protocol, domain, resource_address


url_1 = 'https://geekbrains.ru/teacher/lessons/7961'
url_1_parsed = url_parse(url_1)
print(url_1_parsed)


nums = ['1578.4', '892.4', '354.1', '871.5']
print((map(float, nums)))
