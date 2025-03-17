# 2025-03-16

## Chap05 함수

### 5.1 함수 만들기

-   함수의 기본
    ```python
    def 함수이름(매개변수):
        문장
    ```
-   가변 매개변수
    ```python
    def 함수이름(*가변매개변수):
        문장
    ```
    -   매개변수를 원하는 만큼 입력할 수 있는 함수
    -   가변 매개변수 뒤에는 일반 매개변수가 올 수 없음
    -   가변 매개변수는 하나만 사용할 수 있음
-   기본 매개변수
    ```python
    def 함수이름(매개변수3=값):
        문장
    ```
    -   매개변수를 입력하지 않았을 경우 들어가는 기본값
    -   기본 매개변수 뒤에는 일반 매개변수가 올 수 없음
-   키워드 매개변수

    ```python
    def 함수이름(매개변수, *가변매개변수, 키워드매개변수=기본값):
        문장
    ```

    -   키워드 매개변수는 함수 호출 시 이름을 지정하여 값을 전달
    -   예시:

        ```python
        def 프로필(이름, *취미, 직업="학생"):
            print("이름:", 이름)
            print("취미:", 취미)
            print("직업:", 직업)

        # 함수 호출
        프로필("홍길동", "독서", "게임", 직업="개발자")
        # 출력:
        # 이름: 홍길동
        # 취미: ('독서', '게임')
        # 직업: 개발자
        ```

    -   기본 매개변수 중에서 필요한 값만 입력

        ```python
        def 프로필(이름, 나이=20, 직업="학생"):
            print("이름:", 이름)
            print("나이:", 나이)
            print("직업:", 직업)

        # 기본 매개변수 중 직업만 변경하여 호출
        프로필("홍길동", 직업="개발자")
        # 출력:
        # 이름: 홍길동
        # 나이: 20 (기본값 사용)
        # 직업: 개발자

        # 이름은 반드시 위치 인자로 전달
        # 나이, 직업은 기본값을 사용하거나, 필요할 때만 키워드 인자로 전달하여 원하는 값으로 수정
        ```

-   리턴
    -   함수의 결과값을 반환하는 키워드
    -   자료 없이 리턴
        ```python
        def 함수이름():
            print("함수 실행")
            return
            print("함수 종료")
            # 출력:
            # 함수 실행
        ```
    -   자료와 함께 리턴
        ```python
        def 함수이름():
            # 값 하나 반환
            return 100
            # 출력:
            # 100
        ```
    -   아무것도 리턴하지 않았을 경우
        ```python
        def 함수이름():
            return
            # 출력:
            # None
        ```

### 5.2 함수의 활용

-   재귀 함수

    -   함수 내부에서 자기 자신을 호출하는 함수
        ```python
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        ```

-   재귀함수의 문제

    -   피보나치 수열

        ```python
        def fibonacci(n):
            if n == 1:
                return 1
            if n == 2:
                return 1
            else:
                return fibonacci(n-1) + fibonacci(n-2)
        ```

        ```python
        cnt = 0

        def fibonacci(n):
            global cnt
            cnt += 1
            if n == 1:
                return 1
            if n == 2:
                return 1
            else:
                return fibonacci(n-1) + fibonacci(n-2)
        ```

        -   파이썬은 함수 내부에서 함수 외부에 있는 변수를 참조하지 못함
        -   global 키워드를 사용하여 전역 변수를 사용

-   메모화(memoization)

    ```python
    dict = {
        1: 1,
        2: 1
    }

    def fibonacci(n):
        if n in dict:
            return dict[n]
        else:
            dict[n] = fibonacci(n-1) + fibonacci(n-2)
            return dict[n]

    print(fibonacci(50))
    ```

    -   딕셔너리를 사용해서 한 번 계산한 값을 저장함 >> 메모(memo)한다고 표현함

-   조기 리턴

    ```python
    def fibonacchi(n):
        if n in dict:
            return dict[n]

        dict[n] = fibonacchi(n-1) + fibonacchi(n-2)
        return dict[n]
    ```

    -   조기 리턴은 함수 내부에서 조건문을 사용하여 조건에 맞는 경우 즉시 리턴하는 방법
    -   조기 리턴을 사용하면 코드가 간결해지고, 실행 속도가 빨라짐

-   리스트 평탄화 - 중첩된 리스트가 있을 때 중첩을 모두 제거하고 풀어서 1차원 리스트로 만드는 것
    ```python
    def flatten(data):
        output = []                        # 결과를 저장할 빈 리스트 생성
        for item in data:                  # 입력 데이터의 각 항목을 순회
            if type(item) == list:         # 항목이 리스트인 경우
                output += flatten(item)    # 재귀적으로 flatten 함수 호출하여 결과를 output에 추가
            else:                          # 항목이 리스트가 아닌 경우
                output.append(item)        # 항목을 그대로 output에 추가
        return output                      # 평탄화된 리스트 반환
    ```
    > ### `output.append()`을 `output += item`으로 수정했을 때 안되는 이유
    >
    > `+=` 연산자는 리스트에 다른 리스트를 연결할 때 사용하는데, `item`이 리스트가 아닌 경우(문자열, 숫자 등)에는 리스트와 연결할 수 없기 때문입니다.  
    > 예를 들어, 리스트에 숫자를 `+=` 연산자로 더하려고 하면 "can only concatenate list (not "int") to list"와 같은 TypeError가 발생합니다.  
    > `+=`연산자와 같은 기능을 수행하는 함수는 `extend()` 메서드입니다.  
    > 반면 `append()` 메서드는 어떤 타입의 객체든 리스트의 요소로 추가할 수 있습니다.

### 5.3 함수 고급

-   튜플

    -   함수와 함께 많이 사용되는 리스트와 비슷한 자료형으로, 리스트와 다른 점은 한번 결정된 요소는 바꿀 수 없음

    ```python
    tuple_data = (10, 20, 30)
    tuple_data[0]
    # 출력:
    # 10
    tuple_data[0] = 100
    # 출력:
    # TypeError: 'tuple' object does not support item assignment
    ```

    -   튜플은 내부 요소 변경이 불가능함
    -   요소를 하나만 가지는 리스트 / 튜플
        ```python
        list_data = [10] # 요소를 하나만 가지는 리스트는 이런 형태로 생성함
        tuple_data = (10,) # 컴마를 붙여야 튜플로 인식함
        ```
    -   괄호를 생략할 수 있음

        ```python
        tuple_data = 10, 20, 30
        type(tuple_data)
        print(tuple_data)
        # 출력:
        # <class 'tuple'>
        # (10, 20, 30)
        ```

    -   변수 값 교환
        ```python
        a = 10
        b = 20
        a, b = b, a
        print(a, b)
        # 출력:
        # 20 10
        ```
    -   튜플은 함수의 리턴에 많이 사용됨
        -   함수에서 여러 개의 값을 리턴하고 할당할 수 있기 때문
        ```python
        def test():
            return 10, 20
        a, b = test()
        print(a, b)
        # 출력:
        # 10 20
        ```
    -   튜플도 리스트처럼 +와 \* 연산자 등을 활용할 수 있으나, 리스트로 작성하는 것과 차이가 없어서 튜플을 사용하는 경우는 거의 없음
        > `enumerate()` 함수와 `items()` 함수를 사용하면 반복 변수를 아래 코드처럼 입력할 수 있음<br>
        > 이 때, i, value는 (i, value) 형태의 튜플에서 괄호를 제거한 형태
        >
        > ```python
        > for i in value in enumerate([1,2,3,4,5,6]):
        >     print(i, value)
        > # i, value는 괄호 없는 튜플
        >
        > a, b = 97, 40
        > divmod(a, b) # divmod() 함수는 몫과 나머지를 튜플로 리턴함
        > x, y = divmod(a, b)
        > print(x, y)
        > # 출력:
        > # 2 17
        > ```

-   람다
    -   매개변수로 함수를 전달하기 위해 함수 구문을 작성하는 것이 번거롭고, 코드 공간 낭비라는 생각이 들 때 함수를 간단하고 쉽게 선언하는 방법
    -   1회용 함수를 만들어야 할 때 많이 사용
    - 함수의 매개변수로 함수 전달
        - 함수의 매개변수에 사용하는 함수를 콜백 함수(callback function)라고 함
        ```python
        def call_10_times(func):
            for i in range(10):
                func()

        def hello():
            print("안녕하세요")

        call_10_times(hello)
        # 출력:
        # 안녕하세요
        # 안녕하세요
        # ...
        # 안녕하세요
        ```
    - 함수를 매개변수로 사용하는 대표적인 표준 함수로 `map()`, `filter()` 함수가 있음
        - `map()` 함수
            - 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해주는 함수
        - `filter()` 함수
            - 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로, 새로운 리스트를 구성해주는 함수
        - 예시
            ```python
            # 함수 선언
            def power(item):
                return item * item
            def under_3(item):
                return item < 3

            # 변수 선언
            list_input_a = [1, 2, 3, 4, 5]

            # map() 함수 사용
            output_a = map(power, list_input_a)
            print(output_a)
            print(list(output_a))

            # filter() 함수 사용
            output_b = filter(under_3, list_input_a)
            print(output_b)
            print(list(output_b))

            # 출력:
            # <map object at 0x000001E403921C88>
            # [1, 4, 9, 16, 25]
            # <filter object at 0x000001E403921C88>
            # [1, 2]
            ```
        - `map()` 함수와 `filter()` 함수는 람다를 사용하여 간단하게 표현할 수 있음
