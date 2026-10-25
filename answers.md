# Ответы на вопросы:

## 3 вопрос
в момент когд встречается `await` в цикле событий нет других задач, на которые можно было бы переключиться, поэтому все вызовы `work()` обрабатываются последовательно

## 5 вопрос

Вывод без `await`:
```text
RuntimeWarning: coroutine 'work' was never awaited
print(work(n))
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
<coroutine object work at 0x1060b3100>
<coroutine object work at 0x1060b3100>
<coroutine object work at 0x1060b3100>
<coroutine object work at 0x1060b3100>
<coroutine object work at 0x1060b3100>
<coroutine object work at 0x1060b3100>
<coroutine object work at 0x1060b3100>
<coroutine object work at 0x1060b3100>
<coroutine object work at 0x1060b3100>
Time elapsed: 0.00s
```
ниодна из корутин не исполняетя, вызов `work()` возвращает `coroutine object`

## 6 вопрос
фактически `gather()` создает 10 задач, в момент когда первая задача доходит до `await asyncio.sleep(1)` происходит переход к следущей задаче и так далее, по прошествии 1 секунды печатается следущее сообщение от каждой задачи последовательно

## 8 вопрос 
```text
[  0.0s] alice: запрос принят
[  0.5s] alice: ответ отпрален
[  0.5s] bob: запрос принят
[  5.5s] bob: ответ отпрален
[  5.5s] carol: запрос принят
[  6.0s] carol: ответ отпрален
[  6.0s] dave: запрос принят
[  6.5s] dave: ответ отпрален
[  6.5s] eve: запрос принят
[  7.0s] eve: ответ отпрален
Time elapsed: 7.03s
```
из вывода прграммы видно что `alice` и `carol` получают ответ в 0.5 и 6.0 соответственно, `carol` ожидал своей очереди 5.5 секунд так как сервер обрабатывает клиентов последовательно

## 11 вопрос
благодаря асинхронности клиентам после `bob` не надо ждать пока будет обработан его запрос, экономится время других клиентов