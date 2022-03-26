def palindrome(pal):
    pal = input()
    return 'Палиндром' if pal == pal[::-1] else 'Не палиндром'

print(palindrome(''))
