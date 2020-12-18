# 메모이제이션(Memoization)

간단하게 설명하자면, `캐시 메모리(Cache Memory)`에 중복되는 연산의 결과를 저장해 두었다가 연산 수행시 이를 꺼내서 사용하는 기법을 말한다. <br>

- 동적 프로그래밍 : 재귀적 알고리즘 or 반복적으로 호출되는 알고리즘을 찾는 것이 관건이다. <br>

## 피보나치 수열로 알아보는 동적 프로그래밍 접근

- Naive Algorithm

```{.python3}
def fibonacci(i):

    if (i == 0):
        return True
    elif (i == 1):
        return False
    else:
        return fibonacci(i-1) + fibonacci(i-2)
```

위의 코드를 직접 그려보면 알겠지만, n번째 노드를 구하는 경우 구하는 노드의 갯수는 2의 제곱 만큼 증가하므로 O(2^n)이 된다.
실제로는 O(2^n) 보다 수행 시간이 빠르다. 왜 일까? left tree와 right tree의 노드의 증가 비율을 고려하면 2:1의 비율로 증가하는 것을 알 수 있다. 따라서 실제 수행 시간은 O(1.6^n)에 더 가깝다는 것을 알 수 있다. 처음에 시간 복잡도 구하는 것에 소홀히 했었지만, 알고리즘을 공부하면서 시간 복잡도를 정량적으로 추정할 줄 아는 것도 문제 해결에 기본이 되는 태도라는 것을 깨달았다.

위의 코드는 시간 복잡도가 상당히 높으므로, 소프트웨어 개발자라면 메모리와 수행 시간을 적게 사용하는 방향으로 코드를 개선 해야 한다.

## bottom-up approach in dynamic programing

위의 코드를 빠르게 계산하는 방법 중에,
시간 복잡도를 줄일 수 있는 방안을 모색해보자.
시간 복잡도에 영향을 주는 요인은 다양하지만 그 중 한 가지를 꼽는다면 함수 호출이 해당된다.

위의 알고리즘은 불필요한 함수 호출이 반복되므로
더이상의 함수 호출이 없이 다음과 같은 방향으로 해결 할 수 있다.

1. `best case`인 fibonacci(0)과 fibonacci(1)을 계산한다. <br>
2. `재귀 알고리즘`을 사용해서 fibonacci(i)을 구하는데, fibonacci 함수 안에 loop를 걸어서 문제를 해결 하는 것도 하나의 방법이다.

```{.python3}
def fibonacci(n):
    a, b = 1, 1
    if (n == 0):
        return a
    elif (n == 1):
        return b
    for i in range(0, n):
        a, b = b, a+b

    return a
```

## top-down approach in dynamic programming

일반적으로, 동적 프로그래밍 기법을 사용한다고 했을 때 이 기법으로 접근을 한다.
하향식 동적 프로그래밍의 큰 특징은 `중복되는 노드`를 구하는 것에서 출발한다.

1. 중복되는 연산을 먼저 구하고,
2. 메모이제이션을 사용해서 값을 리턴한다.

```{.python3}
memo = []

def fibonacci(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibonacci(n-1) + fibonacci(n-2))
    return memo[n]
```
