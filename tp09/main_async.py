import asyncio
import threading
async def add(a,b):
    print(threading.current_thread().name)
    await asyncio.sleep(0.5)
    return a+b

async def main():
    print(threading.current_thread().name)
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    # r = await add(1,2)
    
    all_r = [add(1,2),add(1,2),add(1,2)]
    
    r = await asyncio.gather(*all_r)
    print(r)
    

if __name__=='__main__':
    print(threading.current_thread().name)
    asyncio.run(main())
