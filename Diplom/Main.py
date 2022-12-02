

def create():
    print('*' * 50)
    print('creating new DB')
    from create import create
    create()
    print('Creating successful')
    print('*' * 50)

def download():
    print('downloading new DB')

def work():
    print('*' * 50)
    print('working with DB')
    from New_data import new_data
    new_data()
    print('*' * 50)

while True:
    print('Work with DB')
    print('Enter your choice')
    print('1 to create new DB')
    print('2 to download yor DB')
    print('3 to enter new data to DB')
    print('Exit')
    answer = input('Your choice? ')
    if answer in '1':
        create()
    if answer in '2':
        download()
    if answer in '3':
        work()
    if answer.upper() in ("E", "EXIT", "QUIT", "Q"):
        break


