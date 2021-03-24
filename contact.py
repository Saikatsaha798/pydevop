import pickle, prettytable as pt


def fetch():
    try:
        with open('cont.dat', 'rb') as fr:
            d = pickle.load(fr)
        contactsempty = False
        return d, contactsempty
    except:
        d = dict()
        contactsempty = True
        return d, contactsempty


class cont:
    def __init__(self, d):
        self.contactsempty = contactsempty
        self.d = d
        self.con = pt.PrettyTable(['Name', 'Phone Number'])

        print('Options Provided : '
              '\n1. Add Contact'
              '\n2. View Contact')
        ch = int(input('Enter your Choice : '))
        if ch == 1:
            self.add()
            self.save()
        elif ch == 2:
            self.view()
            self.save()
        else:
            print('Wrong Choice !!!')

    def add(self):
        self.n = input('Enter the name : ')
        self.pn = input('Enter the phone number : ')
        self.d[self.n] = self.pn
        self.contactsempty = False

    def save(self):
        if not self.contactsempty:
            print(self.d)
            with open('cont.dat', 'wb') as self.fw:
                pickle.dump(self.d, self.fw)

    def view(self):
        if not self.contactsempty:
            for i in sorted(d):
                self.con.add_row([i, self.d[i]])
            print(self.con)
        elif self.contactsempty:
            print('Contact List is Empty !')


if __name__ == "__main__":
    d, contactsempty = fetch()
    while True:
        contacts = cont(d)
        c1 = input('Want to do more ? [y/n]')
        if c1 == 'n' or c1 == 'N':
            break
        elif c1 == 'y' or c1 == 'Y':
            pass
        else:
            print('Wrong Choice !!!')
            break
