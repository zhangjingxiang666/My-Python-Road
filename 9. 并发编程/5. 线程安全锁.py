import threading
import time

class Account():
    def __init__(self,balance):
        self.balance=balance

#不加锁时：
account=Account(1000)

def no_lock_takeout(account,money):
    if account.balance>=money:
        time.sleep(0.1)
        account.balance=account.balance-money
        print('余额为',account.balance)
    else:
        print('余额不足')

t1=threading.Thread(target=no_lock_takeout,args=(account,800),name='无锁第一线程')
t2=threading.Thread(target=no_lock_takeout,args=(account,800),name='无锁第二线程')
t1.start()
t2.start()
t1.join()
t2.join()
'''上述可见，在不锁的情况下，两个线程同时跑，趁一个线程sleep还没来得及减的时候，另一个线程也把if判断给做了。就会出现余额为负的状况'''

'''为线程加锁：这个线程没执行完时,别开始下一个线程'''
'''加锁的过程是先定义一个锁，然后将后续要代入线程的函数本身放在with里面加上锁'''
lock=threading.Lock()   #定义一个锁
print(type(threading.Lock()))
def lock_takeout(account,money):
    with lock:  #将后续要代入线程的函数本身放在with里面加上锁
            if account.balance>=money:
                time.sleep(0.1)
                account.balance=account.balance-money
                print('余额为',account.balance)
            else:
                print('余额不足')
account=Account(1000)
t3=threading.Thread(target=lock_takeout,args=(account,800),name='有锁第一线程')
t4=threading.Thread(target=lock_takeout,args=(account,800),name='有锁第二线程')
t3.start()
t4.start()