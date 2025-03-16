# 2025-02-28

## Chap03 조건문

-   Boolean

    -   True / False

    -   비교 연산자

        -   ==
        -   !=
        -   >
        -   <
        -   > =
        -   <=

        -   문자열에도 비교 연산자 사용 가능
            -   사전순으로 비교

-   논리 연산자

    -   and
        -   조건 중 하나라도 False이면 False
    -   or
        -   조건 중 하나라도 True이면 True
    -   not
        -   True -> False
        -   False -> True

-   조건문

    -   if
    -   elif
    -   else

    -   if 조건문의 매개변수에 Boolean 타입이 아닌 값을 넣으면 자동으로 Boolean 타입으로 변환
    -   False로 변환되는 값은 0, 0.0, None, 빈 컨테이너(빈 문자열, 빈 리스트, 빈 딕셔너리, 빈 튜플, 빈 세트 등)

-   pass 키워드
    -   아무것도 하지 않음
    -   조건문의 매개변수에 들어가는 코드 블록을 작성할 때 사용
    -   예시

```python
if 조건문:
    pass
elif 조건문:
    pass
else:
    pass
```

> ### raise NotImplementedError
>
> -   아직 구현되지 않은 기능을 작성할 때 사용
> -   조건문의 코드블록 내부에 사용 가능

---

## Chap04 반복문

### 4-1. 리스트와 반복문

-   리스트

    -   `array = [1, 2, 3, 4, 5]`
    -   배열의 각 요소에 접근하려면 인덱스를 사용

    1. 요소 접근
        - `array[0]` = 1 (첫 번째 요소)
        - `array[1]` = 2 (두 번째 요소)
        - `array[-1]` = 5 (마지막 요소)
        - `array[-2]` = 4 (뒤에서 두 번째 요소)
    2. 리스트 접근 연산자 이중 사용
        - `list_a = [1,2,3,"문자열", True, False]`
        - `list_a[3] = "문자열"`
        - `list_a[3][0] = "문"`
    3. 리스트 안에 리스트 사용
        - `list_a = [1,2,3,[4,5,6]]`
        - `list_a[3] = [4,5,6]`
        - `list_a[3][0] = 4`

    -   리스트 연산

        -   -   : 리스트 합치기
        -   -   : 리스트 반복
        -   len() : 리스트 길이

    -   리스트 함수

        -   append() : 리스트 마지막에 요소 추가
            -   `list_a.append(요소)`
        -   insert() : 리스트 특정 위치에 요소 추가
            -   `list_a.insert(위치, 요소)`
            -   예시
                ```python
                >>> list_a = [1,2,3,4,5]
                >>> list_a.insert(2, 99)
                >>> list_a
                [1,2,99,3,4,5]
                ```
        -   extend() : 리스트에 다른 리스트를 추가하여 확장 - `list_a.extend(리스트)` - 예시
            `python
         >>> list_a = [1,2,3]
         >>> list_b = [4,5,6]
         >>> list_a.extend(list_b)
         >>> list_a
         [1,2,3,4,5,6]
         `
            > -   `+` 연산자와 `extend()` 함수의 차이
            >     -   비파괴적, 파괴적
            >         -   비파괴적: 원본 데이터를 변경하지 않고 새로운 객체를 생성하는 방식 (예: `+` 연산자)
            >         -   파괴적: 원본 데이터를 직접 수정하는 방식 (예: `extend()` 함수)
            >         -   원래 자료는 비파괴적으로 사용하는 것이 편리함. 원본도 활용할 수 있기 때문.
            >         -   기본 자료형(숫자, 문자열, 불리언)은 비파괴적으로 작동함
            >     -   예시
            >         ```python
            >         >>> list_a = [1,2,3]
            >         >>> list_b = [4,5,6]
            >         >>> list_a + list_b
            >         [1,2,3,4,5,6]
            >         >>> list_a
            >         [1,2,3]
            >         >>> list_b
            >         [4,5,6]
            >         ```
            >         ```python
            >         >>> list_a = [1,2,3]
            >         >>> list_b = [4,5,6]
            >         >>> list_a.extend(list_b)
            >         >>> list_a
            >         [1,2,3,4,5,6]
            >         ```

    -   리스트 요소 제거
        -   인덱스로 제거
            -   `del 리스트명[인덱스]`
                -   범위를 지정하여 리스트의 요소를 한꺼번에 제거할 수 있음
            -   `리스트명.pop(인덱스)`
                -   매개변수 없으면(-1로 취급) 마지막 요소 제거
        -   값으로 제거
            -   `리스트명.remove(값)`
                -   값이 여러 개일 경우 첫 번째 값만 제거
            -   `리스트명.clear()`
                -   리스트의 모든 요소 제거

    > 리스트 슬라이싱
    >
    > -   리스트의 일부를 추출하는 방법
    > -   범위를 지정하여 리스트의 요소를 한꺼번에 추출할 수 있음
    > -   `리스트[시작_인덱스:끝_인덱스:단계]`
    > -   예시
    >     ```python
    >     >>> list_a = [1,2,3,4,5,6,7,8]
    >     >>> list_a[0:5:2]
    >     [1,3,5]
    >     >>> list_a[::-1]
    >     [8,7,6,5,4,3,2,1]
    >     >>> list_a[::2]
    >     [1,3,5,7]
    >     >>> list_a[::-2]
    >     [8,6,4,2]
    >     >>> list_a[3:6]
    >     [4,5,6]
    >     ```

    -   리스트 정렬
        -   `리스트명.sort()`
            -   오름차순 정렬
        -   `리스트명.sort(reverse=True)`
            -   내림차순 정렬
    -   리스트 내부에 있는지 확인
        -   `값 in 리스트명`
            -   값이 리스트 내부에 있으면 True, 없으면 False
        -   `값 not in 리스트명`
            -   값이 리스트 내부에 없으면 True, 있으면 False

---

-   for 반복문

    -   예시

    ```python
    for 변수 in 반복대상:
        반복할 코드
    ```

    ```python
    arr = [1,2,3,4,5]
    for i in arr:
        print(i)
    ```

    -   출력 결과

    ```python
    1
    2
    3
    4
    5
    ```

    -   중첩 반복문과 중첩 리스트

        -   1차원 리스트 : `[1,2,3]`
        -   2차원 리스트 : `[[1,2,3], [4,5,6], [7,8,9]]`
        -   예시

        ```python
        arr = [[1,2,3], [4,5,6], [7,8,9]]
        for i in arr:
            print(i)
        ```

        -   출력 결과

        ```python
        [1,2,3]
        [4,5,6]
        [7,8,9]
        ```

        -   중첩 반복문 예시

        ```python
        arr = [[1,2,3], [4,5,6], [7,8,9]]
        for i in arr:
            for j in i:
                print(j)
        ```

        -   출력 결과

        ```python
        1
        2
        3
        4
        5
        6
        7
        8
        9
        ```

    -   전개 연산자

        -   리스트 요소를 전개해서 입력한 것과 같음
        -   리스트 앞에 `*`를 붙여서 사용
        -   `*리스트명` → `리스트[0], 리스트[1], ...`

        1. 리스트 내부에 사용하는 경우

            ```python
            a = [1,2,3,4]
            b = [*a, *a]
            print(b)
            ```

            - 출력 결과

            ```python
            [1,2,3,4,1,2,3,4]
            ```

            - 전개 연산자 사용

            ```python
            # append() 함수 사용
            a = [1,2,3,4]
            a.append(5)
            print(a) # [1,2,3,4,5]

            # 전개 연산자 사용
            b = [1,2,3,4]
            c = [*b, 5]
            print(b) # [1,2,3,4]
            print(c) # [1,2,3,4,5]
            ```

        2. 함수 매개변수 위치에 사용하는 경우
            ```python
            a = [1,2,3,4]
            print(*a) # 1 2 3 4
            ```

    ### 4-2. 딕셔너리와 반복문

    -   리스트와 딕셔너리의 차이

        -   리스트 : '인덱스를 기반으로 값을 저장하는 것'
        -   딕셔너리 : '키를 기반으로 값을 저장하는 것'

    -   딕셔너리 선언

        -   중괄호 {}로 선언
        -   `키: 값` 형태로 쉼표로 구분
        -   예시
            ```python
            dict_movie = {
                "name": "명량",
                "year": 2014,
                "cast": ["최민식", "류승룡", "황정민", "임하룡"]
            }
            ```
        -   딕셔너리 요소 접근
            -   `dict_movie["name"] # 명량`
            -   [] 사용
            -   `dict_movie["cast"][0] # 최민식`
        -   딕셔너리 요소 추가/제거

            -   `dict_movie["director"] = "최동훈" # 추가`
            -   `dict_movie["name"] = "괴물" # 덮어쓰기`
            -   `del dict_movie["cast"] # 제거`

        -   딕셔너리 내부에 키가 있는지 확인
            -   in 키워드
                ```python
                if key in dict_movie:
                    print(dict_movie[key])
                else:
                    print("키가 존재하지 않습니다.")
                ```
            -   get() 함수
                ```python
                    value = dict_movie.get("cast")
                    if value:
                        print(value)
                    else:
                        print("키가 존재하지 않습니다.")
                ```
                -   존재하지 않는 키를 조회할 경우 None 반환

    -   딕셔너리 반복문
        -   예시
            ```python
            for key in dict_movie:
                print(key, ":", dict_movie[key])
            ```

    ### 4-3. 범위 자료형과 while 반복문

    -   범위 자료형

        -   숫자 범위
            -   `range(시작, 끝, 단계)`
            -   예시
                ```python
                range(5) # 0, 1, 2, 3, 4
                range(1, 5) # 1, 2, 3, 4
                range(1, 5, 2) # 1, 3
                ```
        -   범위 매개변수 내부에 수식 사용
            ```python
            >>> a = range(0, 10 + 1)
            >>> list(a)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            ```
            -   11을 10 + 1로 표현 하는 이유
                -   코드의 가독성을 높이기 위함
                -   범위의 끝 값이 어디서 왔는지 명확하게 표현 가능
                -   예를 들어, 배열의 길이를 기준으로 할 때 `len(array)`를 사용하면 의도가 명확해짐
                -   나중에 코드 수정 시 실수를 줄일 수 있음
            -   수식에 나누기 연산을 사용할 경우 오류가 발생
                -   range 함수의 매개변수는 정수만 사용 가능
                -   사용해야 한다면 `range(0, int(n/2))`보다는 `range(0, n//2)` 형태로 사용

    -   for 반복문

        -   범위와 함께 사용
            ```python
            for 숫자변수 in 범위:
                코드
            # 예시
            for i in range(5):
                print(i)
            ```
        -   리스트와 범위 조합
            ```python
            array = [1,2,3,4,5]
            for i in range(len(array)):
                print("{}번째 요소 : {}".format(i, array[i]))
            ```
        -   반대로 반복
            ```python
            for i in range(4, 0-1,-1):
                print("{}".format(i))
            # 또는
            for i in reversed(range(5)):
                print("{}".format(i))
            ```

    -   while 반복문

        -   예시
            ```python
            while 불 표현식:
                코드
            ```
        -   for 처럼 사용
            ```python
            i = 0
            while i < 10:
                print("{}번째".format(i))
                i += 1
            ```
        -   상태를 기반으로 반복
            ```python
            list_test = [1, 2, 1, 2]
            value = 2
            while value in list_test:
                list_test.remove(value)
            print(list_test)
            ```
        -   시간을 기반으로 반복
            ```python
            import time
            number = 0
            target_tick = time.time() + 5 # 5초 뒤
            while time.time() < target_tick:
                number += 1
            print("{}번 반복했습니다.".format(number))
            ```
        -   break / continue

            -   break : 반복문 중단

                ```python
                i = 0
                while True:
                    print("{}번째 반복문입니다.".format(i))
                    if i == 5:
                        break
                    i += 1

                    input_text = input("> 종료하시겠습니까?(y)")
                    if input_text in ["y", "Y"]:
                        print("반복을 중단합니다.")
                        break
                ```

            -   continue : 현재 반복 중단, 다음 반복으로 넘어감

                ```python
                numbers = [5, 15, 6, 20, 7, 25]

                for number in numbers:
                    if number < 10:
                        continue
                    print(number)
                ```

    ### 4-4. 문자열, 리스트, 딕셔너리와 관련된 기본 함수

    -   리스트에 적용할 수 있는 기본 함수: `min()`, `max()`, `sum()`
        -   `min(리스트명)` : 최소값
        -   `max(리스트명)` : 최대값
        -   `sum(리스트명)` : 합계
    -   리스트 뒤집기: `reversed()`
        ```python
        list_a = [1,2,3,4,5]
        list_reversed = list(reversed(list_a))
        print(list_reversed) # <list_reverseiterator object at 0x...> , 리스트 자체를 뒤집지 않음
        print(list(list_reversed)) # [5, 4, 3, 2, 1]
        for i in list_a:
            print(i)
        ```
        ```python
        temp = reversed([1,2,3,4,5])
        for i in temp:
            print("첫번째 반복 : {}".format(i)) # 5 4 3 2 1
        for i in temp:
            print("두번째 반복 : {}".format(i)) # 출력 되지 않음
        ```
        -   reversed() 함수의 결과가 제너레이터이기 때문에 한 번 반복하면 비어버림
        -   reversed() 함수와 반복문을 조합할 때는 함수의 결과를 여러 번 활용하지 않고 각 반복문에서 새로운 제너레이터를 생성해야 함
            ```python
            numbers = [1,2,3,4,5]
            for i in reversed(numbers):
                print("첫번째 반복 : {}".format(i)) # 5 4 3 2 1
            for i in reversed(numbers):
                print("두번째 반복 : {}".format(i)) # 5 4 3 2 1
            ```
    -   현재 인덱스가 몇 번째인지 확인하기: `enumerate()`

        ```python
        ex_list = ["요소A", "요소B", "요소C"]
        i = 0
        for item in ex_list:
            print("{}번째 요소 : {}".format(i, item))
            i += 1

        # 또는
        ex_list = ["요소A", "요소B", "요소C"]
        for i in range(len(ex_list)):
            print("{}번째 요소 : {}".format(i, ex_list[i]))

        # 또는 enumerate() 함수 사용
        ex_list = ["요소A", "요소B", "요소C"]
        for i, value in enumerate(ex_list): # enumerate() 함수를 사용하면 for와 in 사이에 반복 변수를 두 개 사용 가능
            print("{}번째 요소 : {}".format(i, value))
        ```

    -   딕셔너리로 쉽게 반복문 작성하기: `items()`

        -   딕셔너리의 items() 함수와 반복문 조합

            ```python
            ex_dict = {
                "키A": "값A",
                "키B": "값B",
                "키C": "값C"
            }
            # 딕셔너리의 items() 함수
            print(ex_dict.items()) # dict_items([('키A', '값A'), ('키B', '값B'), ('키C', '값C')])

            # 반복문과 조합
            for key, element in ex_dict.items():
                print("dictionary[{}] : {}".format(key, element)) # dictionary[키A] : 값A
                                                                  # dictionary[키B] : 값B
                                                                  # dictionary[키C] : 값C
            ```

    -   리스트 안에 for문 사용하기: 리스트 내포

        -   리스트 내포

            ```python
            array = []

            for i in range (0, 20, 2):
                array.append(i * i)
            print(array) # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

            # 위 코드를 리스트 내포로 표현
            array = [i * i for i in range(0, 20, 2)] # 최종 결과(i*i)를 앞에 작성
            print(array) # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
            ```

        -   리스트 내포의 형태
            -   `리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]`
            -   `리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]`
            ```python
            # 한 줄로 입력했을 때 코드가 길어 가독성이 떨어진다면 3줄로 작성해도 무방
            리스트 이름 = [표현식
                for 반복자 in 반복할 수 있는 것
                if 조건문]
            ```
