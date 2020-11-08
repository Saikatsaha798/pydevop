import mysql.connector
import pickle
import prettytable as pt


def joint(ab):
    if ab == '':
        pass
    else:
        j = input('Enter (\'and\'/\'or\')')
        return j


with open('../School Management system GUI/data.dat', 'rb+') as fr:
    a = pickle.load(fr)

host, user, password = a[0], a[1], a[2]

con = mysql.connector.connect(host=host, user=user, password=password, db='school')
c = con.cursor()

ofn = ['adm_no', 'name', 'class', 'section', 'attendance', 'english', 'bengali_or_hindi', 'science', 'social_science',
       'maths']

tri = 0

try:
    print('You are a : \n'
          '1. Teacher \n'
          '2. Student')

    attempt = 0

    c1 = int(input('Enter the number of Choice : '))

    if c1 == 1:

        trial = 'notended'

        while trial != 'ended':

            print('It\'s time, you verify your authorization !!!!!')

            u = str(input('Enter your Username : '))
            p = str(input('Enter your Password : '))

            if u == a[3] and p == a[4]:

                trial = 'ended'

                print('Welcome Back, you are provided your permissions below !!!!')
                print('1. View details'
                      '\n2. Add entries'
                      '\n3. Modify entries'
                      '\n4. delete entries'
                      '\n5. reset')

                c2 = int(input('Enter your Choice : '))

                if c2 == 1:

                    alil = []
                    sout = ''
                    fout = ''
                    aout = ''

                    print('Select from below which columns you want to see :\n'
                          'adm_no, name, class, section, attendance, english, bengali_or_hindi, science, '
                          'social_science, maths, *(for all columns)')

                    colsel = str(input('Please select columns mentioned above separated with \',\' : '))
                    sort = str(input('Sorting needed ? (y/n) : '))
                    filters = str(input('Filtering needed ? (y/n) : '))
                    alias = str(input('Aliasing Required(calculating existing column) ? (y/n) : '))

                    if sort == 'y' or sort == 'Y':
                        s = str(
                            input('Enter the Column mentioned above according to which needs to be sorted : '))

                        sout = f' order by {s}'

                    if filters == 'y' or filters == 'Y':

                        nfilter = int(input('How many filters required (\'not more than 2\') ? : '))

                        for i in range(nfilter):

                            jv = joint(fout)

                            f = str(input('Enter the column with which to be filtered : '))
                            o = str(input('Enter the operator from mentioned one (=, <, >, <=, >=, !=) :'))
                            r = str(input('Enter the value : '))

                            ifout = f + o + r

                            if fout == '':
                                fout = f' where {ifout} '
                            else:
                                fout += f'{jv} {ifout}'

                    if alias == 'y' or alias == 'Y':

                        nal = int(input('Enter the number of alias : '))

                        for i in range(nal):
                            al = str(input('Enter the alias name : '))
                            fo = str(input('Enter the value of alias with respect to columns mentioned : '))
                            iaout = f',{fo} as {al}'
                            aout += iaout
                            alil.append(al)

                    cmd = f'select {colsel}{aout} from student{fout}{sout};'

                    try:
                        c.execute(cmd)
                        v = c.fetchall()
                        norcol = colsel.split(',')

                        if '*' in norcol:
                            norcol.remove('*')
                            norcol = ['adm_no', ' name', 'class', 'section', 'attendance', 'english',
                                      'bengali_or_hindi',
                                      'science',
                                      'social_science', 'maths']

                        fieldname = norcol + alil

                        vtab = pt.PrettyTable()
                        vtab.field_names = fieldname

                        for i in v:
                            vtab.add_row(i)

                        print(vtab)

                    except mysql.connector.errors.ProgrammingError:
                        print('Please be precise on entry of data !!!!!!!')

                elif c2 == 2:

                    c2c = 'y'

                    while c2c == 'y' or c2c == 'Y':
                        print('Please fill the below mentioned => ')
                        adm = int(input('Admission Number            = '))
                        name = str(input('Name                        = '))
                        clas = int(input('Class           (in Number) = '))
                        sec = str(input('Section                     = '))
                        att = int(input('Attendance      (in %)      = '))
                        eng = int(input('English         (in %)      = '))
                        beng = int(input('Bengali/Hindi   (in %)      = '))
                        sc = int(input('Science         (in %)      = '))
                        sst = int(input('Social Science  (in %)      = '))
                        math = int(input('Mathematics     (in %)      = '))

                        c.execute(f'insert into student values('
                                  f'{adm},\'{name}\',{clas},\'{sec}\',{att},{eng},{beng},{sc},{sst},{math});')
                        con.commit()
                        print('Data Entered !!!!')
                        c2c = input('Want to enter more data (y/n) : ')

                elif c2 == 3:

                    mout = ''
                    md = {}

                    print('first let\'s see, which rows you need to modify ....')

                    fout = ''

                    nfilter = int(input('How many conditions required (\'not more than 2\') ? : '))

                    for i in range(nfilter):
                        jv = joint(fout)
                        f = str(input('Enter the column with which to be identified : '))
                        o = str(input('Enter the operator from mentioned one (=, <, >, <=, >=, !=) :'))
                        r = str(input('Enter the value : '))

                        ifout = f + o + r

                        if fout == '':
                            fout = f'{ifout}'
                        else:
                            fout += f'{jv} {ifout}'

                    print('Please fill the required ones from below mentioned and put \'null\' in other ones => ')
                    adm = str(input('Admission Number            = '))
                    name = str(input('Name                        = '))
                    clas = str(input('Class           (in Number) = '))
                    sec = str(input('Section                     = '))
                    att = str(input('Attendance      (in %)      = '))
                    eng = str(input('English         (in %)      = '))
                    beng = str(input('Bengali/Hindi   (in %)      = '))
                    sc = str(input('Science         (in %)      = '))
                    sst = str(input('Social Science  (in %)      = '))
                    math = str(input('Mathematics     (in %)      = '))

                    mr = [adm, name, clas, sec, att, eng, beng, sc, sst, math]

                    for i in ofn:
                        for t in mr:
                            if t != 'null' and (i != 'name' or i != 'section'):
                                md[i] = t
                            if i == 'name' or i == 'section':
                                md[i] = f'\'{t}\''
                            mr.remove(t)
                            break

                    for i in list(md.keys()):
                        if mout == '':
                            mout = f'{i}={md[i]}'

                        else:
                            mout += f',{i}={md[i]}'

                    cmd = f'update student set {mout} where {fout};'
                    c.execute(cmd)
                    con.commit()

                    print('Data Modified Successfully !!!!!')

                elif c2 == 4:

                    print('first let\'s see, which rows you need to delete ....')
                    fout = ''
                    nfilter = int(input('How many conditions required (\'not more than 2\') ? : '))

                    for i in range(nfilter):
                        jv = joint(fout)
                        f = str(input('Enter the column with which to be deleted : '))
                        o = str(input('Enter the operator from mentioned one (=, <, >, <=, >=, !=) :'))
                        r = str(input('Enter the value : '))

                        if f == 'name' or f == 'section':
                            r = f'\'{r}\''

                        ifout = f'{f}{o}{r}'
                        if fout == '':
                            fout = f'{ifout}'
                        else:
                            fout += f'{jv} {ifout}'

                    cmd = f'delete from student where {fout};'
                    c.execute(cmd)
                    con.commit()
                    print('The Row you selected is successfully deleted!!!!!')

                elif c2 == 5:

                    while True:

                        print('Please re-enter the username and password to proceed !!!')

                        u = str(input('Enter your Username : '))
                        p = str(input('Enter your Password : '))

                        if u == a[3] and p == a[4]:
                            c.execute('truncate table student;')
                            print('Your database is cleaned !!!!!!')
                            break

                        if tri == 5:
                            print('As I suspected, you are an intruder !!!!!')
                            exit()

                        else:
                            tri += 1
                            print(f'Wrong Username and Password !!!!!, Retrying.... {5 - tri} left ....')

                else:
                    print(f'Not able to find Your choice({c2}) !!!!!!!! ')

            elif attempt == 4:
                print('\'Limits Crossed !!!!,UNAUTHORIZED ACCESS DETECTED !!!!!!, SERVERS CLOSING DOWN!!!!')
                exit()

            else:
                attempt += 1
                print(f'Wrong Username and Password !!!!!, Retrying.... {5 - attempt} left ....')

    elif c1 == 2:

        adm_no = int(input('Enter your Admission Number : '))
        c.execute(f'select * from student where adm_no={adm_no};')
        a = c.fetchone()

        if a is None:
            print(f'You are not registered , admission number = {adm_no}')

        else:
            print('             Your Details                '
                  f'\nAdmission Number            = {a[0]}'
                  f'\nName                        = {a[1]}'
                  f'\nClass           (in Number) = {a[2]}'
                  f'\nSection                     = {a[3]}'
                  f'\nAttendance      (in %)      = {a[4]}'
                  f'\nEnglish         (in %)      = {a[5]}'
                  f'\nBengali/Hindi   (in %)      = {a[6]}'
                  f'\nScience         (in %)      = {a[7]}'
                  f'\nSocial Science  (in %)      = {a[8]}'
                  f'\nMathematics     (in %)      = {a[9]}')

    else:
        print(f'Not able to find Your choice({c1}) !!!!!!!! ')

except ValueError:
    print('Aren\'t you are being illogical, please enter the data according to field names !!!!')

except SyntaxError:
    print('First install through setup, then try this !!!!!!!!')

except EOFError:
    print('Delete all files (data.dat) except program ones from this folder, it is causing hindrances !!!!')

except mysql.connector.ProgrammingError and mysql.connector.DatabaseError:
    print('Due to some manipulations, our connections are failing, so try uninstalling and reinstalling !!!!!')

finally:
    print('Have a good day !! :)')
