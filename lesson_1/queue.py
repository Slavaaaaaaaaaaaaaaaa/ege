# count = int( input( "Type count of containers: " ) )
# sklad = []
#
#
# for i in range(count):
#     container = int( input( 'mass of container: ' ) )
#     sklad.append( container )
#
#
# new_container = int( input( 'input mass of new container: ' ) )
#
# for j in range(count):
#     if new_container > sklad[j]:
#         print( j + 1 )
#         break


# spisak = [1, 2, 3, 4, 5]
# Ka = int( input( 'Input K: ' ) )
#
#
# for i in range( len( spisak ) - Ka ):
#     spisak.append( spisak.pop(0) )
# print( spisak )


# guests = ['Petya', 'Vanya', 'Sasha', 'Lisa', 'Katya']
#
#
#
# while True:
#     print( f'Now on party {len(guests)} humans: ', guests )
#     x = input( 'human come on party or leave?' )
#     if x == 'come':
#         name = input( 'Input name:' )
#         if len(guests) < 6:
#             print( f'hi, {name}' )
#             guests.append(name)
#         else:
#             print( f'sorry, {name}, out ot sits' )
#     elif x == 'leave':
#         name = input( 'Input name: ' )
#         print(f'bye, {name}')
#         guests.remove(name)
#     elif x == "party ended":
#         print( 'party ended, all go to sleep' )
#         break


# spisak_1 = [int( input( f'input {i} number' ) ) for i in range(1,3+1)]
# spisak_2 = [int( input( f'input {i} number' ) ) for i in range(1,7+1)]
#
#
# print( spisak_1 )
# print( spisak_2 )
#
#
# spisak_1.extend(spisak_2)
# for i in range(len(spisak_1)):
#     x = spisak_1.count(i)
#     for j in range(x-1):
#         spisak_1.remove(i)
#
#
# print( spisak_1 )


# main = [1, 5, 3]
# trash_1 = [1, 5, 1, 5]
# trash_2 = [1, 3, 1, 5, 3, 3]
# main.extend(trash_1)
#
# number = main.count(5)
#
# print(number)
#
# while main.count(5) > 0:
#     main.remove(5)
#
# main.extend(trash_2)
# number = main.count(3)
#
# print(number)
# print(main)
