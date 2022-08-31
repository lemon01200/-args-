# from lzx
import threading
import time

def test1(g_nums):
    g_nums.append(1)
    print("---test1---%s--" %g_nums)

def test2(g_nums):
    #global g_nums
    g_nums+=[4]
    print("---test2---%s---" %g_nums)

g_nums = [1,2]

def main():
    t1=threading.Thread(target=test1, args=(g_nums,))
    t2=threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    t2.start()
    print("--main--%s--" %g_nums)

if __name__ == "__main__":
    main()