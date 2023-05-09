from insert_ import insert_
from delete_ import delete_
from query_ import query_
from update_ import update_
from select_ import select_
from sort_ import sort_
while True:
    try:
        command = input('(1)insert,(2)delete,(3)query,(4)update,(5)select,(6)sort,(7)Exit')
        if command=='1':
            insert_()
        elif command =='2':
            delete_()
        elif command == '3':
            query_()
        elif command == '4':
            update_()
        elif command == '5':
            print(select_())
        elif command == '6':
            sort_()
        elif command == '7':
            break
    except:
        print('invalid command')