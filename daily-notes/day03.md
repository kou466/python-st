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
    -   함수의 매개변수로 함수 전달

        -   함수의 매개변수에 사용하는 함수를 콜백 함수(callback function)라고 함

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

    -   함수를 매개변수로 사용하는 대표적인 표준 함수로 `map()`, `filter()` 함수가 있음

        -   `map()` 함수
            -   리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해주는 함수
        -   `filter()` 함수
            -   리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로, 새로운 리스트를 구성해주는 함수
        -   예시

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
            # <map object at 0x000001B4ECF89120>
            # [1, 4, 9, 16, 25]
            # <filter object at 0x000001B4ECF895D0>
            # [1, 2]

            # map object와 filter object는 제너레이터(generator)라고 부름
            ```

    -   람다의 개념

        -   `lambda 매개변수: 리턴값` 형태로 사용

            ```python
            power = lambda x: x * x
            under_3 = lambda x: x < 3

            list_input_a = [1, 2, 3, 4, 5]

            output_a = map(power, list_input_a)
            print(output_a)
            print(list(output_a))

            output_b = filter(under_3, list_input_a)
            print(output_b)
            print(list(output_b))

            # 아래처럼 함수의 매개변수에 람다 함수를 사용할 수 있음

            list_input_a = [1, 2, 3, 4, 5]

            output_a = map(lambda x: x * x, list_input_a)
            print(output_a)
            print(list(output_a))

            output_b = filter(lambda x: x < 3, list_input_a)
            print(output_b)
            print(list(output_b))

            # 실행결과는 이전과 같음
            ```

    -   파일 처리
        -   크게 `텍스트 파일`과 `바이너리 파일`로 나뉨
        -   파일 열기
            -   `open()` 함수를 사용
            -   `파일 객체 = open(문자열: 파일 경로, 문자열: 읽기 모드)` 형식으로 사용
            -   읽기 모드
                -   `r` : 읽기 모드
                -   `w` : 쓰기 모드
                -   `a` : 추가 모드
        -   파일 닫기
            -   `파일 객체.close()` 형식으로 사용
        -   with 키워드
            -   파일을 열고 닫는 것을 자동으로 처리해주는 키워드
                ```python
                with open(문자열: 파일 경로, 문자열: 읽기 모드) as 파일 객체:
                    코드
                ```
            -   with 구문이 종료될 때 파일 객체가 자동으로 닫힘
        -   파일 쓰기 및 읽기
            -   `파일 객체.write(문자열: 쓸 내용)` 형식으로 사용
            -   `파일 객체.read()` 형식으로 사용

-   제너레이터

    -   제너레이터는 이터레이터를 직접 만들 때 사용하는 코드
    -   함수 내부에 yield 키워드를 사용하면 해당 함수는 제너레이터 함수가 되며, 일반 함수와는 달리 함수를 호출해도 함수 내부의 코드가 실행되지 않음

        ```python
        def test():
            print("test함수 호출")
            yield "test"

        print("A지점 통과")
        test()

        print("B지점 통과")
        test()
        print(test())

        # 출력:
        # A지점 통과
        # B지점 통과
        # <generator object test at 0x00000218C359CD00>
        ```

        -   제너레이터 함수는 제너레이터를 리턴
        -   제너레이터 객체는 next() 함수를 사용해 함수 내부의 코드를 실행
        -   yield 부분까지만 실행하며 next() 함수의 리턴값으로 yield 키워드 뒤에 입력한 값을 리턴

-   리스트 함수의 key 키워드 매개 변수

    -   리스트 함수의 key 키워드 매개 변수는 정렬 기준을 정할 수 있는 매개 변수
    -   예시

        ```python
        books = [{
            "title": "혼자 공부하는 파이썬",
            "price": 10000
        }, {
            "title": "혼자 공부하는 자바스크립트",
            "price": 20000
        }, {
            "title": "혼자 공부하는 머신러닝",
            "price": 30000
        }]


        # 함수 사용 방법
        def price(book):
            return book["price"]

        print(min(books, key=price))
        print(max(books, key=price))

        # 람다 사용 방법
        print(min(books, key=lambda book: book["price"]))
        print(max(books, key=lambda book: book["price"]))

        # 출력:
        # {'title': '혼자 공부하는 파이썬', 'price': 10000}
        # {'title': '혼자 공부하는 머신러닝', 'price': 30000}
        ```

        ```python
        # 복합적인 리스트 정렬 방법 (sort() 함수 사용)

        # ...

        books.sort(key=lambda book: book["price"])
        for book in books:
            print(book)

        # 출력:
        # {'title': '혼자 공부하는 파이썬', 'price': 10000}
        # {'title': '혼자 공부하는 자바스크립트', 'price': 20000}
        # {'title': '혼자 공부하는 머신러닝', 'price': 30000}
        ```

-   스택, 힙
    -   기본 자료형은 가볍고 정형화된 자료형
        -   기본 자료형이 정리되어 있는 공간을 `스택(stack)`이라고 함
        -   숫자, 문자열, 불 등 기본 자료형은 스택에 저장됨
    -   복합 자료형은 무겁고 크기가 정형화되어 있지 않음
        -   객체 자료형들이 정리되어 있는 공간을 `힙(heap)`이라고 함
        -   리스트, 딕셔너리, 튜플 등 복합 자료형은 힙에 저장되고, 스택에는 힙의 주소가 저장됨

## Chap06 예외처리

### 6.1 구문 오류와 예외

- 오류
    - 프로그램 실행 전에 발생하는 오류 : 구문 오류(syntax error)
    - 프로그램 실행 중에 발생하는 오류 : 예외(exception) 또는 런타임 에러(runtime error)
    
    - 구문 오류
        - 해결하지 않으면 프로그램이 실행되지 않음
    - 예외 또는 런타임 에러
        - 해결하지 않으면 프로그램이 중단됨

- 기본 예외 처리
    - 예외 처리(exception handling) 방법
        - 조건문을 사용하는 방법
            - 예외 처리 기본 문법
                ```python
                if 조건문:
                    코드
                ```
    - try except 구문을 사용하는 방법
        - 예외 처리 기본 문법
            ```python
            try:
                예외가 발생할 가능성이 있는 코드
            except:
                예외가 발생했을 때 실행할 코드
            ```
    - try except구문과 pass 키워드 조합하기
        - 예외 처리 기본 문법
            ```python
            try:
                예외가 발생할 가능성이 있는 코드
            except:
                pass
            ```
    - try except else 구문
        - 예외 처리 기본 문법
            ```python
            try:
                예외가 발생할 가능성이 있는 코드
            except:
                예외가 발생했을 때 실행할 코드
            else:
                예외가 발생하지 않았을 때 실행할 코드
            ```
    - finally 구문
        - 예외 처리 기본 문법
            ```python
            try:
                예외가 발생할 가능성이 있는 코드
            finally:
                예외 발생 여부와 상관없이 항상 실행할 코드
            ```
    - try, except, finally 구문의 조합
        - 예외 처리 구문은 다음과 같은 규칙을 지켜야 함
            - try 구문은 단독으로 사용할 수 없으며, 반드시 except 구문이나 finally 구문과 함께 사용해야 함
            - else 구문은 반드시 except 구문 뒤에 사용해야 함
        - 가능한 조합
            - try + excpet
            - try + ecpet + else
            - try + except + finally
            - try + except + else + finally
            - try + finally
    - try 구문 내부에서 return 키워드 사용하는 경우
        - finally 구문은 반복문 또는 함수 내부에 있을 때 위력을 발휘
            ```python
            def test():
                print("test() 함수의 첫 줄")
                try:
                    print("try 구문 실행")
                    return
                    print("try 구문의 return 키워드 뒤")
                except:
                    print("except 구문 실행")
                else:
                    print("else 구문 실행")
                finally:
                    print("finally 구문 실행")
                print("test() 함수의 마지막 줄")

            test()

            # 출력:
            # test() 함수의 첫 줄
            # try 구문 실행
            # finally 구문 실행
            ```
        - 함수 내부에서 파일 처리 코드를 깔끔하게 만들고 싶을 때 finally 구문을 활용하는 경우가 많음
    - 반복문과 함께 사용하는 경우
        - finally 구문은 반복문에서 break로 빠져나오거나, continue로 처음으로 돌아가거나, return으로 함수를 빠져나오는 경우에도 실행됨
            ```python
            print("프로그램 시작")
            while True:
                try:
                    print("try 구문 시작")
                    break
                print("try 구문의 break 키워드 뒤")
                except:
                    print("except 구문 실행")
                finally:
                    print("finally 구문 실행")
                print("while 반복문 종료")
            print("프로그램 종료")

            # 출력:
            # 프로그램 시작
            # try 구문 시작
            # finally 구문 실행
            # 프로그램 종료
            ```

### 6.2 예외 고급

- 예외 객체(exception object)
    - 예외가 발생했을 때 예외 객체를 사용해 예외에 대한 정보를 얻을 수 있음
        ```python
        try:
            예외가 발생할 가능성이 있는 코드
        except 예외의 종류 as 예외 객체를 활용할 변수 이름:
            예외가 발생했을 때 실행할 코드
        ```
    - 처음 예외 객체를 사용할 때는 예외의 종류가 무엇인지 모르기에 `Exception`을 사용 (모든 예외의 어머니)
    - 예외 구분하기
        ```python
        list_number = [52, 273, 32, 103, 90]

        try:
            number_input = int(input("정수 입력> "))
            print("{}번째 요소: {}".format(number_input, list_number[number_input]))
        except Exception as exception:
            print(type(exception))
            print(exception)

        # 출력:
        # 정수 입력> 2
        # 1번째 요소: 32

        # 출력:
        # 정수 입력> ok
        # <class 'ValueError'>
        # invalid literal for int() with base 10: 'ok'

        # 출력:
        # 정수 입력> 100
        # <class 'IndexError'>
        # list index out of range
        ```
    - except 구문 뒤에 예외의 종류를 입력해서 예외 구분할 수 있음
        ```python
        try:
            예외가 발생할 가능성이 있는 코드
        except 예외의 종류A:
            예외가 발생했을 때 실행할 코드
        except 예외의 종류B:
            예외가 발생했을 때 실행할 코드
        ```
    - 예외를 구분할 때 각각의 except 구문 뒤에 예외 객체를 붙여 활용할 수도 있음
        - `as 키워드` 사용
        - `except IndexError as exception:` 형식으로 사용
    - `except Exception as exception:`을 try except 구문에서 마지막에 사용하면 모든 예외를 처리할 수 있음

- raise 키워드
    - 예외를 강제로 발생시키는 구문
    - 예외 객체를 직접 만들어서 발생시키는 것도 가능
    - `raise 예외 객체` 형식으로 사용
    - 예시
        ```python
        # NotImplementedError는 아직 구현되지 않은 부분을 표시할 때 사용하는 예외
        # 주로 추상 메서드나 향후 구현 예정인 기능을 표시할 때 사용함
        raise NotImplementedError
        ```        
