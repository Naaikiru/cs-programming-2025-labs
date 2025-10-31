
# pas = input('введите пароль: ')
# zag = 'QWERTYUIOPASDFGHJKLZXCVBNM'
# sto = 'qwertyuiopasdfghjklzxcvbnm'
# cif = '1234567890'
# sps = '!"#$%&()*+,-./:;<=>?@[\]^_{|}~'
# if len(pas) >= 8:
#     if 'QWERTYUIOPASDFGHJKLZXCVBNM' in pas and '!"#$%&()*+,-./:;<=>?@[\]^_{|}~' in pas and '1234567890' in pas and 'qwertyuiopasdfghjklzxcvbnm' in pas:
#         print('пароль надежный')
#     else:
#         print('пароль ненадежный: ')
#         if zag not in pas:
#             print('отсутсвуют заглавные буквы')
#         elif sto not in pas:
#             print('отсутсвуют строчные буквы')
#         elif cif not in pas:
#             print('отсутсвуют числа')
#         elif sps not in pas:
#             print('отсутсвуют специальные символы')
# else:
#     print('пароль должен быть длиной не меньше 8')


# pas = input("Введите пароль для проверки: ")

# def chp(passs):
#     err = ['пароль ненадежный: ']
#     if len(pas) < 8:
#         err.append('Пароль должен быть не менее 8 символов.')
#     zag = any(c.isupper() for c in pas)
#     if not zag:
#         err.append('отсутсвуют заглавные буквы')
#     sto = any(c.islower() for c in pas)
#     if not sto:
#         err.append('отсутсвуют строчные буквы')
#     chi = any(c.isdigit() for c in pas)
#     if not chi:
#         err.append('отсутсвуют числа')
#     sps = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~"
#     sps = any(c in sps for c in pas)
#     if not sps:
#         err.append('отсутсвуют специальные символы')
    
#     if len(err) == 0:
#         return "Пароль надежный."
#     else:
#         return "\n".join(err)

# print(chp(pas))
pas = 'Asdf89**'
zag = any(c.isupper() for c in pas)
print(zag)