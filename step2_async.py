"""Шаг 2. Переписываем на asyncio.

Задание 2а:
  1. Сделайте work корутиной (async def).
  2. Замените time.sleep на await asyncio.sleep.
  3. Сделайте main корутиной и вызовите в ней work через await в цикле.
  4. Запустите через asyncio.run.

Замерьте время. Изменилось ли оно по сравнению с шагом 1? Почему?

Задание 2б:
  Перепишите main так, чтобы все 10 задач ждали одновременно.
  Подсказка: asyncio.gather. Что изменилось в порядке вывода?
"""


# шаг а
# import asyncio

# from timer import print_time


# async def work(n: int) -> None:
#     print(f"start {n}")
#     await asyncio.sleep(1)
#     print(f"done {n}")


# async def main() -> None:
#     for n in range(1, 11):
#         await work(n)


# if __name__ == "__main__":
#     with print_time():
#         asyncio.run(main())


# шаг б
import asyncio
from asyncio import Task
from collections.abc import Coroutine

from timer import print_time


async def work(n: int) -> None:
    print(f"start {n}")
    await asyncio.sleep(1)
    print(f"done {n}")


async def main() -> None:
    tasks: list[Task] = []
    
    for n in range(1, 11):
        new_task = asyncio.create_task(work(n))
        tasks.append(new_task)
    
    for task in tasks:
        await task


if __name__ == "__main__":
    with print_time():
        asyncio.run(main())

# шаг в
# import asyncio
# from asyncio import Task
# from collections.abc import Coroutine

# from timer import print_time


# async def work(n: int) -> None:
#     print(f"start {n}")
#     await asyncio.sleep(1)
#     print(f"done {n}")


# async def main() -> None:
#     tasks: list[Task] = [asyncio.create_task(work(n)) for n in range(1, 11)]
#     for task in tasks:
#         await task


# if __name__ == "__main__":
#     coroutines: list[Coroutine] = [work(n) for n in range(1, 11)]

#     with print_time():
#         asyncio.run(main())