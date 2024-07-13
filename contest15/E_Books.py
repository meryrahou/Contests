books , time = map(int, input().split())

minutes = list(map(int, input().split()))

consumed = 0
left = 0
nb_books = 0
for right in range(books):
    consumed += minutes[right]

    while consumed > time:
        consumed -= minutes[left]
        left += 1
    
    nb_books = max(nb_books, right - left + 1)

print(nb_books)