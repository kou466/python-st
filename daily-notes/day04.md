# 2025-03-25

## Chap7 모듈

### 7.1 표준 모듈

-   표준 모듈
    -   파이썬에 기본적으로 내장되어 있는 모듈
-   외부 모듈
    -   다른 사람들이 만들어서 공개한 모듈
-   모듈을 가져올 떄 사용하는 import 구문

    -   `import 모듈명`

-   모듈 사용의 기본 : math 모듈

    -   `import math`
    -   `math.pi`
    -   모듈 문서
        -   https://docs.python.org/3/library/index.html

-   from 구문

    -   `from 모듈명 import 사용할 변수 또는 함수`
    -   변수 또는 함수는 여러 개의 변수 / 함수를 입력할 수 있음

-   as 구문

    -   `import 모듈명 as 사용하고 싶은 식별자`
    -   모듈명이 길거나 복잡할 때 사용
        ```python
        import math as m
        print(m.pi)
        ```

-   random 모듈

    -   랜덤한 값을 생성할 떄 사용하는 모듈
    -   `import random`
    -   `random.random()` : 0부터 1 사이의 랜덤한 실수 생성
    -   https://docs.python.org/3/library/random.html

-   sys 모듈

    -   시스템과 관련된 정보를 가지고 있는 모듈
    -   `import sys`
    -   `sys.argv` : 명령줄에서 Python 스크립트 실행 시 전달된 인자들의 리스트
    -   `sys.getwindowsversion` : Windows 버전 정보를 반환하는 함수
    -   `sys.copyright` : Python 저작권 정보를 담고 있는 문자열
    -   `sys.version` : Python 인터프리터의 버전 정보를 담고 있는 문자열
    -   `sys.exit()` : 프로그램 종료

-   os 모듈

    -   운영체제와 관련된 기능을 가진 모듈
    -   `import os`
    -   `os.getcwd()` : 현재 작업 디렉토리 반환
    -   `os.mkdir(path)` : 디렉토리 생성
    -   `os.rmdir(path)` : 디렉토리 삭제
    -   `os.remove(path)` : 파일 삭제
    -   `os.system(command)` : 운영체제 명령어 실행

    -   파일 제거 시, remove()함수와 unlink()함수의 차이
        -   os.remove()와 os.unlink()는 기능적으로 동일함 (실제로 같은 함수)
        -   둘 다 파일을 삭제하는 기능을 수행
        -   차이점은 이름만 다를 뿐, 내부적으로는 같은 함수를 호출함
        -   UNIX 시스템에서는 파일 삭제를 'unlinking'이라고 표현하는 전통에서 unlink라는 이름이 유래됨

    > os.system() 함수는 명령어를 실행하는데, `rm -rf /` 와 같은 명령어를 실행하면 디렉토리 안의 모든 파일을 삭제할 수 있음  
    > 이런 명령어를 실행하면 악의적인 사용자가 시스템을 손상시킬 수 있음  
    > 따라서 os.system() 함수를 사용할 때는 실행할 명령어를 신중하게 검토해야 함

-   datetime 모듈

    -   date(날짜), time (시간)과 관련된 모듈
    -   `now.strftime("%Y-%m-%d %H:%M:%S")` : 날짜와 시간을 문자열로 변환
    -   strftime() 함수를 사용하면 시간을 형식에 맞춰 출력할 수 있음
        -   단, 한국어등의 문자는 매개변수에 넣을 수 없음
        -   이를 보완하고자 다음 형식으로 사용할 수 있음
            -   `"{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second)`
            -   `now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초"))`
                -   `(*"년월일시분초")`처럼 문자열, 리스트 등 앞에 `*`를 붙이면 요소 하나하나가 매개변수로 지정됨
    -   `timedelta()` 함수는 특정한 시간의 이전 또는 이후를 구할 수 있음
    -   1년 후, 2년 후 등을 구할 때에는 `replace()` 함수를 사용해서 날짜 값을 교체하는 것이 일반적

-   time 모듈

    -   시간과 관련된 기능을 다룸
    -   `time.sleep()` 함수는 특정 시간동안 코드 진행을 정지할 떄 사용하는 함수
        -   매개변수에는 정지하고 싶은 시간을 초 단위로 입력

-   urllib 모듈

    -   URL을 다루는 라이브러리
        ```python
        import urllib import request
        response = request.urlopen("https://www.google.com")
        print(response.read())
        ```
    -   urlopen()함수는 URL 주소의 페이지를 열어주는 함수
    -   read() 함수는 해당 웹 페이지에 있는 내용을 읽어서 가져옴
        -   이때, 실행 결과는 문자열이 아니라 바이너리 데이터(binary data)를 반환

-   operator.itemgetter() 함수
    -   operator.itemgetter() 함수는 객체의 특정 인덱스나 키를 기준으로 정렬할 때 사용
    -   `from operator import itemgetter`로 임포트
    -   주로 리스트나 딕셔너리를 정렬할 때 사용됨
    -   예시:
        ```python
        students = [
            {"이름": "홍길동", "점수": 90},
            {"이름": "김철수", "점수": 85},
            {"이름": "이영희", "점수": 95}
        ]
        # 점수를 기준으로 정렬
        sorted_students = sorted(students, key=itemgetter("점수"))
        ```
    -   여러 필드를 기준으로 정렬할 때도 유용함: `itemgetter("필드1", "필드2")`
    -   리스트나 튜플의 경우 인덱스로 접근: `itemgetter(0, 1)`

### 7.2 외부 모듈

-   외부 모듈을 사용하기 위해서는 모듈을 설치해야 함
-   모듈 설치 방법
    -   pip 설치
        -   `pip install 모듈명`
-   BeautifulSoup 모듈
    -   웹 페이지를 파싱하고 원하는 데이터를 추출하는 모듈
    -   사용 예시: [bs_weather.py](../implementations/bs_weather.py)
        -   XML 파서를 사용하여 기상청 장기전망 데이터를 가져오는 예제
        -   기존 RSS 서비스가 2025.03.31부터 중단되어 장기전망 데이터로 대체
-   Flask 모듈

    -   웹 애플리케이션을 개발하는 모듈
    -   일반적으로 Python으로 웹 개발을 할 떄는, Django 또는 Flask를 사용함
    -   사용 예시: [flask_web_server.py](../implementations/flask_web_server.py)

-   라이브러리, 프레임워크

    -   라이브러리와 프레임워크의 차이점

    | 구분                  | 설명                                            |
    | --------------------- | ----------------------------------------------- |
    | 라이브러리(library)   | 정상적인 제어를 하는 모듈                       |
    | 프레임워크(framework) | 제어 역전(Inversion of Control)이 발생하는 모듈 |

    -   제어 역전

        -   프로그램의 흐름을 개발자가 제어하는 것이 아니라, 프레임워크가 제어하는 것
        -   제어 역전의 여부로 라이브러리와 프레임워크를 구분

    -   라이브러리
        -   개발자가 모듈의 기능을 호출하는 형태의 모듈
    -   프레임워크
        -   모듈이 개발자가 작성한 코드를 호출하는 형태의 모듈

-   데코레이터
    -   함수 데코레이터 / 클래스 데코레이터
    -   함수 데코레이터는 함수의 기능을 변경하거나 확장하는 데 사용되는 기능
        ```python
        # 함수 데코레이터 사용 예시
        def decorator(func):
            def wrapper(*args, **kwargs):
                print("함수 실행 전")
                result = func(*args, **kwargs)
                print("함수 실행 후")
                return result
            return wrapper
        ```
    -   데코레이터를 사용하면 functools 모듈을 사용할 수 있음
    -   함수 데코레이터를 사용할 때, 매개변수 등을 전달할 수 있어 반복되는 구문이 많아질 때 코드의 가독성이 높아짐
        ```python
        from functools import wraps
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs): # 가변 매개변수와 키워드 가변 매개변수를 사용한 예제
                print("함수 실행 전")
                result = func(*args, **kwargs)
                print("함수 실행 후")
                return result
        ```
        > @기호 > 어노테이션과는 완전히 다른 기능임

### 7.3 모듈 만들기

- 