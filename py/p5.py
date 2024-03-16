 def get_number():
    try:
        val1 = int(input('Enter a number: '))
        while val1 < 1 or val1 > 10:
            val1 = int(input('Enter a number: '))

        str_to_print = '{:.1f}'.format(val1)
        return str_to_print

    except ValueError:
        return get_number()

print(get_number())
