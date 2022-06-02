'''字符串f可以用来在字符串中插入变量的值.然后将要插入的值放在花括号内'''
name1='张三'
name2='李四'
forever=f'{name1}loves{name2}forever'
print(forever)

'''f字符串也可以用于循环中,把循环写在后面'''
urls=[
    f'https://www.cnblogs.com/#p{page}'
    for page in range(1,50)
]
print(urls)