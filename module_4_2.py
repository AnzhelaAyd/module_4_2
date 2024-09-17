def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()#выводит на экран 'Я в области видимости функции test_function'

test_function()
inner_function()# выводит ошибку, так как находится в не области функции