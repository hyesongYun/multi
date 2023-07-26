import time##기본형
 
def do_something():
    print('1초간 잠을 잡니다...')
    time.sleep(1)
    print('잠에서 깨었습니다...')
 
if __name__ == '__main__':
 
    start = time.perf_counter()
 
    for _ in range(4):
        do_something()
    
    finish = time.perf_counter()
 
    print(f'{round(finish-start,2)}초 만에 작업이 완료되었습니다.')

import time
import multiprocessing##멀티프로세싱 적용
 
def do_something():
    print('1초간 잠을 잡니다...')
    time.sleep(1)
    print('잠에서 깨었습니다...')
 
if __name__ == '__main__':
 
    start = time.perf_counter()##시작
 
    processes = []
    for _ in range(4):
        p = multiprocessing.Process(target=do_something) 
        p.start()
        processes.append(p)
 
    for process in processes:
        process.join()
    
    finish = time.perf_counter()##종료

    print(f'{round(finish-start,2)}초 만에 작업이 완료되었습니다.')


import time##기본형, cpu연산이 많음


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


start = time.time()

for i in range(4):
    heavy_work(i)

end = time.time()

print("수행시간: %f 초" % (end - start))


import time##스레드를 사용해서 처리


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


if __name__ == '__main__':
    import threading

    start = time.time()
    threads = []
    for i in range(4):
        t = threading.Thread(target=heavy_work, args=(i, ))##args->변수/인수설정?
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  # 스레드가 종료될 때까지 대기

    end = time.time()

    print("수행시간: %f 초" % (end - start))

    ##cpu연산만 수행할 때에는 시간 단축에 도움이 잘 안 됨


import time##멀티 프로세싱을 사용해서 처리


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


if __name__ == '__main__':
    import multiprocessing

    start = time.time()##시작
    procs = []
    for i in range(4):
        p = multiprocessing.Process(target=heavy_work, args=(i, ))##args->변수/인수설정?
        p.start()
        procs.append(p)

    for p in procs:
        p.join()  # 프로세스가 모두 종료될 때까지 대기

    end = time.time()##종료

    print("수행시간: %f 초" % (end - start))
    ##시간 단축 성공