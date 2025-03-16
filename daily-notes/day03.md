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
