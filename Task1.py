# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок


text='Если в одном списке элементов больше, чем в другом, они не учитываются. Важно иметь одинаковую длину:'
print(f'Текст для редактирования:\n{text}\n')
text1=text.split(" ")

del_text=input("Введите информацию для поиска и удаления из текста: ")

def find_index_for_del(text:str,del_text:str)->list:
    """Находит в исходном тексте индексы слов имеющие совпадения с искомым фрагментом текста
    Args:   Str-текст 
            Str-фрагмент для поиска
    Returns:
        list - развернутый список индексов, где присутствует скомый фрагмент
    """
    temp=''
    index_del=[]

    for i in range(len(text1)):
        temp=str(text1[i])
        temp=text1[i].find(del_text)
        if temp!=-1:
            index_del.append(i)
    index_del.reverse()
    return index_del

index_del=find_index_for_del(text1,del_text)

for i in index_del:
    text1.pop(int(i))
text1=str(text1)
text1=text1[2:(len(text1)-2)]
text1=text1.replace("', '"," ")

print(f'Текст после редактирования:\n{text1}\n')


        


    


