def read() :
    try:
        fle=open('store.csv').read()
        print('file loaded...')
        products=fle.split('\n')
        wl=list()
        for i in range(len(products)) :
            p=products[i].split(',')
            d={'id':p[0] ,'name':p[1],'price':p[2],'count':p[3]}
            wl.append(d)
        return wl
    except:
        print('file not loaded...')


pr=read()


def show_menu() :
    print('1- Add new product :')
    print('2- Search :')
    print('3- Edit : ')
    print('4- Buy : ')
    print('5- Remove :')
    print('6- Show all : ')
    print('7- Show factor : ')
    print('8- Exit')



def add(): 
    id=input('enter id : ') 
    for p in pr :
        if p['id']==id:
            print('this id is exist')
            return
    name=input('enter name : ')
    price=input('enter price : ')
    count=input('enter count : ')
    pr.append({'id':id ,'name':name,'price':price,'count':count})
    return



def search() :
    word=input('enter key word : ')
    flag=False
    for p in pr : 
        if p['id']==word or p['name']==word or p['price'] or p['count'] :
            print(p)
            flag=True
    if not flag:
        print('not found : ')



def write():
    fl=open('store.csv' , 'w')
    fl.writable=True
    c=0
    for p in pr:
        id=p['id']
        name=p['name']
        price=p['price']
        count=p['count']
        fl.write(id+','+name+','+price+','+count)
        c+=1
        if c<len(pr) :
            fl.write('\n')
    fl.close()



def edit():
    a=input('enter code : ')
    for p in pr :
        if a==p['id'] :
            p['name']=input('enter new name : ')
            p['price']=input('enter new price : ')
            p['count']=input('enter count : ')
            return



def buy() :
    buy_list = []
    while True : 
        s = input('enter code : ')
        c = int(input( 'enter count : '))
        for p in pr :
            if s==p['id'] :
                if c<=int(p['count']) :
                    j=int(p['count'])-c
                    p['count']=str(j)
                    c=str(c)
                    buy_list.append({'id' : p['id'] , 'name' : p['name'] , 'price' : p['price'] , 'count' : c})
                    break
                else :
                    print('finish :)')
        else :
            print('not found :(')
        b=input('stop buying ? (yes/no) :')
        if b=='yes' :
            break 
    a=input('save buylist ? (yes/no) :')
    if a=='no' :
        buy_list=[]
        return buy_list
    elif a=='yes' :
        f=open('factor.csv' , 'w')
    f.writable=True
    c=0
    ss=0
    for b in buy_list :
        id=b['id']
        name=b['name']
        price=b['price']
        count=b['count']
        s=int(price)*int(count)
        ss+=s
        f.write('id :'+id+' name :'+name+' price :'+price+' count :'+count+' sum : '+str(s))
        c+=1
        if c<len(buy_list) :
            f.write('\n')
    f.write('\nhole : '+str(ss))
    f.close()



def remove() :
    a=input('enter code : ')
    for p in pr :
        if a==p['id'] : 
            pr.remove(p)
 


def show_all() :
        for p in pr :
            print(p)



def show_factor() :
    try :
        fl=open('factor.csv' , 'r')
        hole = fl.read()
        print(hole)
    except Exception as e :
        print(e)



while True:
    show_menu()
    user=int(input('your choice : '))

    if user==1 :
        add()

    elif user==2 :
        search()

    elif user==3 :
        edit()

    elif user==4 :
        buy()

    elif user==5 :
        remove()

    elif user==6 :
        show_all()
    
    elif user==7 :
        show_factor()

    elif user==8 :
        a=input('save changes ? yes/no : ')
        if a=='no' :
            exit()
        elif a=='yes' :
            write()
            exit()