# 2025-03-25

## Chap07 모듈

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

-   모듈 내부에 변수와 함수를 넣어 모듈을 만들 수 있음
-   `__name__ == "__main__"`

    -   `__name__`은 Python에서 현재 모듈의 이름을 담고 있는 특별한 변수
    -   모듈이 직접 실행될 때는 `"__main__"`이라는 값을 가지고, 다른 모듈에서 import될 때는 해당 모듈의 파일명(확장자 제외)을 값으로 가짐
    -   이를 통해 모듈이 직접 실행되는지 아니면 다른 모듈에서 import되는지 구분할 수 있음
    -   프로그램의 진입점을 엔트리 포인트(entry point) 또는 메인(main)이라고 부름
    -   활용 예시

        ```python
        # test_module.py 파일
        PI = 3.141592

        def number_input():
            output = input("숫자를 입력해주세요: ")
            return float(output)

        def get_circumference(radius):
            return 2 * PI * radius

        def get_circle_area(radius):
            return PI * radius * radius

        # 이 파일을 직접 실행할 때만 아래 코드가 실행됨
        # 다른 파일에서 import할 때는 실행되지 않음
        if __name__ == "__main__":
            radius = number_input()
            print(f"원의 둘레: {get_circumference(radius)}")
            print(f"원의 넓이: {get_circle_area(radius)}")
        ```

-   패키지

    -   pip : Python Package Index
        -   패키지 관리 시스템
        -   패키지는 모듈을 모아놓은 것

-   `__init__.py`

    -   패키지로 인식되게 하는 파일로, 해당 디렉토리가 패키지임을 Python에게 알려줌
    -   Python 3.3부터는 없어도 패키지로 인식 됨

-   텍스트 데이터

    -   텍스트 데이터는 문자열로 표현되는 데이터
    -   인코딩

-   바이너리 데이터

    -   바이너리 데이터는 이진 데이터로 표현되는 데이터
    -

-   인코딩 / 디코딩
    -   인코딩 : 문자나 기호를 컴퓨터가 이해할 수 있는 형태(바이트 등)로 변환하는 과정
    -   디코딩 : 인코딩된 데이터를 원래의 형태(사람이 읽을 수 있는 문자 등)로 변환하는 과정
    -   대표적인 인코딩 방식: ASCII, UTF-8, UTF-16, EUC-KR 등
    -   인터넷의 이미지 저장
        ```python
        from urllib import request
        response = request.urlopen("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
        output = response.read()
        print(output)
        # 바이너리 모드로 파일 열기
        file = open("google.png", "wb") # 바이너리 모드로 파일 열기, wb대신 w를 사용하면 텍스트 모드로 열리게 되어 바이너리 데이터를 쓸 때 인코딩 오류가 발생함
        file.write(output)
        file.close()
        ```

---

## Chap08 클래스

### 8.1 클래스의 기본

-   C를 제외한 대부분의 프로그래밍 언어는 객체 지향 프로그래밍 언어(Object-Oriented Programming Language)
-   클래스 기반의 객체 지향 프로그래밍 언어
-   클래스(class)라는 것을 기반으로 객체(object)를 만들고, 객체를 우선으로 프로그램을 구성하는 프로그래밍

-   객체

    > -   추상화
    >
    > 프로그램에서 필요한 요소만을 사용해서 객체를 표현하는 것

    -   객체 예시

        ```python
        student = [
            {"name": "홍길동", "korean" : 87, "english" : 95, "math" : 75, "science" : 83},
            {"name": "이영희", "korean" : 95, "english" : 90, "math" : 85, "science" : 78},
            {"name": "박철수", "korean" : 75, "english" : 90, "math" : 80, "science" : 95},
        ]

        print("이름", "총점", "평균", sep="\t")
        for student in students:
            score_sum = student["korean"] + student["english"] + student["math"] + student["science"]
            score_average = score_sum / 4
            print(student["name"], score_sum, score_average, sep="\t")
        ```

    -   딕셔너리로 학생을 표현하고 리스트로 묶어 학생 정보를 표현
    -   이처럼 여러 가지 속성을 가질 수 있는 대상을 객체(object)라고 함 (현재 코드에서는 학생이 객체)
    -   객체 예시 2

        ```python
        def create_student(name, korean, english, math, science):
            return {
                "name": name,
                "korean": korean,
                "english": english,
                "math": math,
                "science": science
            }

        students = [
            create_student("홍길동", 87, 95, 75, 83),
            create_student("이영희", 95, 90, 85, 78),
            create_student("박철수", 75, 90, 80, 95),
        ]

        print("이름", "총점", "평균", sep="\t")
        for student in students:
            score_sum = student["korean"] + student["english"] + student["math"] + student["science"]
            score_average = score_sum / 4
            print(student["name"], score_sum, score_average, sep="\t")
        ```

    -   객체 예시 3

        ```python
        def create_student(name, korean, english, math, science):
            return {
                "name": name,
                "korean": korean,
                "english": english,
                "math": math,
                "science": science
            }

        def student_get_sum(student):
            return student["korean"] + student["english"] + student["math"] + student["science"]

        def student_get_average(student):
            return student_get_sum(student) / 4

        def student_to_string(student):
            return "{}\t{}\t{}".format(
                student["name"],
                student_get_sum(student),
                student_get_average(student)
            )

        students = [
            create_student("홍길동", 87, 95, 75, 83),
            create_student("이영희", 95, 90, 85, 78),
            create_student("박철수", 75, 90, 80, 95),
        ]

        print("이름", "총점", "평균", sep="\t")
        for student in students:
            print(student_to_string(student))
        ```

    -   위 처럼 객체와 관련된 코드를 분리할 수 있게 하는 것이 객체 지향 프로그래밍의 핵심
    -   이를 위해 클래스(class)라는 구조를 사용

    -   클래스 예시

        ```python
        class Student:
            pass

        student = Student()

        student = [
            Student(),
            Student(),
            Student(),
        ]
        ```

    -   만들어진 클래스는 클래스 이름과 같은 함수(생성자)를 사용해서 객체를 만듦
    -   `인스턴스 이름(변수 이름) = 클래스 이름()` 형식으로 사용
    -   클래스 이름은 대문자로 시작하는 것이 관례
    -   클래스를 기반으로 만들어진 객체를 인스턴스(instance)라고 함

-   생성자

    -   클래스 이름과 같은 함수를 생성자(constructor)라고 함
        ```python
        class 클래스 이름:
            def __init__(self, 매개변수1, 매개변수2, ...):
                pass
        ```
    -   클래스 내부의 함수는 첫 번째 매개변수로 반드시 self를 지정해야 함
    -   self는 자기 자신을 나타내는 딕셔너리라고 생각하면 됨
    -   다만, self가 가지고 있는 속성과 기능에 접근할 떄는 `self.<식별자>` 형식으로 접근
        > self는 키워드가 아니라 단순한 식별자이므로, 변수 이름으로 활용해도 됨  
        > 그러나 거의 모든 프로그래머가 self를 사용하므로, 기본 규칙을 따르는 것이 좋음
    -   예시

        ```python
        class Student:
            def __init__(self, name, korean, english, math, science):
                self.name = name
                self.korean = korean
                self.english = english
                self.math = math
                self.science = science

            students = [
                Student("홍길동", 87, 95, 75, 83),
                Student("이영희", 95, 90, 85, 78),
                Student("박철수", 75, 90, 80, 95),
            ]

            # 인스턴스 속성에 접근
            students[0].name
            students[0].korean
            students[0].english
            students[0].math
            students[0].science
        ```

    -   생성자(constructor) <> 소멸자(destructor)
        -   인스턴스가 생성될 때 호출되는 함수 : 생성자
        -   인스턴스가 소멸될 때 호출되는 함수 : 소멸자
        -   생성자와 소멸자는 각각 `__init__()`과 `__del__(self)` 형식으로 사용
        -   소멸자는 잘 사용하지 않음

-   메소드

    -   클래스가 가지고 있는 함수
    -   메소드 선언 방식
        ```python
        class 클래스 이름:
            def 메소드 이름(self, 매개변수1, 매개변수2, ...):
                pass
        ```

    > C#, Java 등의 언어에서는 클래스의 함수를 '메소드'라고 부를 정도로 메소드라는 용어를 많이 사용함  
    > 파이썬에서는 메소드라는 용어를 사용하지 않고, 함수(function)라는 용어를 사용함  
    > 멤버 함수(member function), 인스턴스 함수(instance function) 등의 용어를 더 많이 사용함

    -   클래스 내부에 함수(메소드) 선언 예시

        ```python
        class Student:
            def __init__(self, name, korean, english, math, science):
                self.name = name
                self.korean = korean
                self.english = english
                self.math = math
                self.science = science

            def get_sum(self):
                return self.korean + self.english + self.math + self.science

            def get_average(self):
                return self.get_sum() / 4

            def to_string(self):
                return "{}\t{}\t{}".format(
                    self.name,
                    self.get_sum(),
                    self.get_average()
                )

            students = [
                Student("홍길동", 87, 95, 75, 83),
                Student("이영희", 95, 90, 85, 78),
                Student("박철수", 75, 90, 80, 95),
            ]

            print("이름", "총점", "평균", sep="\t")
            for student in students:
                print(student.to_string())
        ```

### 8.2 클래스의 추가적인 구문

-   클래스를 사용하는 것은 속성과 기능을 가진 객체를 만들겠다는 것
-   어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스를 만드는 상속
-   상속 관계에 따라서 객체가 어떤 클래스를 기반으로 만들었는지 확인할 수 있게 해주는 isinstance() 함수
-   파이썬이 기본적으로 제공하는 str() 함수 혹은 연산자를 사용해서 클래스의 특정 함수를 호출할 수 있게 해주는 기능 등

-   어떤 클래스의 인스턴스인지 확인

    -   `isinstance()` 함수는 첫 번째 매개변수에 객체(인스턴스), 두 번째 매개 변수에 클래스를 입력
    -   `isinstance(인스턴스, 클래스)` 형식으로 사용
        -   이 때, 인스턴스가 해당 클래스를 기반으로 만들어졌다면 True, 아니면 False를 반환
    -   단순한 인스턴스 확인이라면 `type(인스턴스) == 클래스` 형식으로 사용해도 됨

        -   다만, 상속을 사용할 때 다르게 동작함

        ```python
        # isinstance() 함수와 type() 함수의 차이 예시
        class Animal:
            pass

        class Dog(Animal):  # Animal을 상속받는 Dog 클래스
            pass

        dog = Dog()  # Dog 클래스의 인스턴스 생성

        # isinstance() 함수는 상속 관계를 고려함
        print(isinstance(dog, Dog))     # True: dog는 Dog의 인스턴스
        print(isinstance(dog, Animal))  # True: dog는 Animal을 상속받은 Dog의 인스턴스

        # type() 함수는 정확한 클래스만 확인함
        print(type(dog) == Dog)     # True: dog의 타입은 Dog
        print(type(dog) == Animal)  # False: dog의 타입은 Animal이 아니라 Dog

        # 따라서 상속 관계를 고려해야 할 때는 isinstance()를 사용하는 것이 적합함
        ```

-   클래스를 생성하고 리스트 내부에 객체들을 넣음, 반복을 적용했을 떄, 요소가 Student 클래스의 인스턴스인지, Teacher 클래서의 인스턴스인지 확인하고, 각각의 대상이 가지고 있는 적절한 함수를 호출하는 예제
-   isinstance()함수를 사용하면 하나의 리스트로 여러 종류의 데이터를 다룰 수 있음

    ```python
    class Student:
        def study(self):
            print("공부를 합니다.")

    class Teacher:
        def teach(self):
            print("학생을 가르칩니다.")

    classroom = [Student(), Student(), Teacher(), Student(), Studnet()]

    for person in classroom:
        if isinstance(person, Student):
            person.study()
        elif isinstance(person, Teacher):
            person.teach()
    ```

-   특수한 이름의 메소드 - `__str__()` 메소드 - 객체를 문자열로 변환할 수 있음
    | 이름 | 영어 | 설명 |
    |------|------|------|
    | eq | equal | 객체가 같은지 비교할 때 호출되는 메소드 |
    | ne | not equal | 객체가 다른지 비교할 때 호출되는 메소드 |
    | gt | greater than | 객체가 큰지 비교할 때 호출되는 메소드 |
    | ge | greater than or equal | 객체가 크거나 같은지 비교할 때 호출되는 메소드 |
    | lt | less than | 객체가 작은지 비교할 때 호출되는 메소드 |
    | le | less than or equal | 객체가 작거나 같은지 비교할 때 호출되는 메소드 |

-   학생 성적 관리 예시: [compare_func.py](../implementations/compare_func.py)

-   예외 처리

    -   ==, !=, >, >=, <, <= 를 사용하면 비교 연산자가 아닌 메소드를 호출하게 됨
    -   비교할 때 사용되는 자료형을 한정하고 싶다면 자료형을 한정하고 이외의 자료형을 사용할 때 예외를 발생시키는 방법을 사용할 수 있음

-   클래스 변수와 메소드

    -   인스터스가 속성과 기능을 가질 수도 있지만, 클래스가 속성(변수)과 기능(함수)을 가질 수도 있음
    -   클래스 변수

        ```python

        # 선언
        class 클래스 이름:
            클래스 변수 = 값

        # 접근
        클래스 이름.클래스 변수
        ```

    -   예시

        ```python
        class Student:
            count = 0

            def __init__(self, name, korean, english, math, science):
                self.name = name
                self.korean = korean
                self.english = english
                self.math = math
                self.science = science

                # 클래스 변수 설정
                Student.count += 1
                print("{}번째 학생이 생성되었습니다.".format(Student.count))

        students = [
            Student("홍길동", 87, 95, 75, 83),
            Student("이영희", 95, 90, 85, 78),
            Student("박철수", 75, 90, 80, 95),
        ]

        print()
        print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))
        ```

    -   클래스 함수

        ```python
        class 클래스 이름:
            @classmethod
            def 클래스 함수 이름(cls, 매개변수1, 매개변수2, ...): # cls는 클래스 자신을 가리키는 매개변수
                pass
        ```

        -   클래스 함수의 첫 번째 매개변수에는 클래스 자체가 들어가는데, 일반적으로 cls라는 이름의 변수로 선언
        -   호출 : `클래스 이름.클래스 함수 이름(매개변수1, 매개변수2, ...)`

        ```python
        class Student:
            count = 0
            students = []

            @classmethod
            def print(cls): # Student 클래스에 print() 함수를 추가
                print("--- 학생 목록 ---")
                print("이름\t총점\t평균")
                for student in cls.students: # Student.students 라고 해도 되지만, 매개변수로 받은 cls를 활용
                    print(str(student))
                print("---")

            def __init__(self, name, korean, english, math, science):
                self.name = name
                self.korean = korean
                self.english = english
                self.math = math
                self.science = science

                Student.count += 1
                Student.students.append(self)

            def get_sum(self):
                return self.korean + self.english + self.math + self.science

            def get_average(self):
                return self.get_sum() / 4

            def __str__(self):
                return "{}\t{}\t{}".format(
                    self.name,
                    self.get_sum(),
                    self.get_average()
                )

        Student("홍길동", 87, 95, 75, 83)
        Student("이영희", 95, 90, 85, 78)
        Student("박철수", 75, 90, 80, 95)

        Student.print()
        ```

-   가비지 컬렉터

    -   `가비지 컬렉터(Garbage Collector)`는 더 이상 사용되지 않는 메모리를 자동으로 해제하는 시스템
    -   `스왑(Swap)`은 메모리가 부족할 때 디스크 공간을 임시 메모리로 사용하는 기술

-   프라이빗 변수와 게터/세터

    -   프라이빗 변수
        -   클래스 내부의 변수를 외부에서 접근하지 못하도록 할 떄 인스턴스 변수 이름을 `__<변수 이름>` 형태로 선언
        -   `__`를 변수 이름 앞에 붙이면 클래스 내부에서만 접근 가능한 변수가 됨
    -   게터 / 세터 (Getter / Setter)
        -   게터(Getter)는 프라이빗 변수의 값을 읽는 메소드
        -   세터(Setter)는 프라이빗 변수의 값을 설정하는 메소드
    -   데코레이터를 사용한 게터/세터
        -   변수 이름과 같은 함수를 정의하고 `@property`와 `@<게터 함수 이름>.setter`를 사용

-   상속 (inheritance)

    -   상속은 기존 클래스의 기능을 물려받아 새로운 클래스를 만드는 기법
    -   상속을 통해 코드 재사용성을 높이고 유지보수가 용이해짐
    -   부모 클래스(또는 슈퍼 클래스)의 속성과 메소드를 자식 클래스(또는 서브 클래스)가 물려받음
    -   파이썬에서는 `class 자식클래스(부모클래스):` 형태로 상속을 구현
    -   자식 클래스에서 부모 클래스의 메소드를 재정의하는 것을 메소드 오버라이딩(Overriding)이라고 함
    -   부모 클래스의 메소드를 호출할 때는 `super().메소드명()` 형태로 사용

    -   다중 상속(Multiple Inheritance)

        -   파이썬은 여러 부모 클래스로부터 상속받을 수 있는 다중 상속을 지원
        -   `class 자식클래스(부모클래스1, 부모클래스2, ...):` 형태로 구현
        -   다중 상속 시 메소드 해석 순서(MRO, Method Resolution Order)를 따름
        -   동일한 이름의 메소드가 여러 부모 클래스에 존재할 경우, 클래스 선언 시 먼저 명시된 부모 클래스의 메소드가 우선 적용됨
        -   다중 상속은 복잡성을 증가시킬 수 있으므로 신중하게 사용해야 함

    -   예시
        ```python
        # 부모 클래스 정의
        class Animal:
            def __init__(self, name):
                self.name = name

            def speak(self):
                return "동물이 소리를 냅니다."

            def introduce(self):
                return f"저는 {self.name}입니다."

        # 자식 클래스 정의 - Animal 클래스 상속
        class Dog(Animal):
            def speak(self):  # 메소드 오버라이딩
                return "멍멍!"

        class Cat(Animal):
            def speak(self):  # 메소드 오버라이딩
                return "야옹!"

            def introduce(self):
                # 부모 클래스의 메소드 호출
                parent_intro = super().introduce()
                return f"{parent_intro} 그리고 저는 고양이입니다."

        # 객체 생성 및 사용
        animal = Animal("동물")
        dog = Dog("바둑이")
        cat = Cat("나비")

        print(animal.speak())  # 출력: 동물이 소리를 냅니다.
        print(dog.speak())     # 출력: 멍멍!
        print(cat.speak())     # 출력: 야옹!

        print(animal.introduce())  # 출력: 저는 동물입니다.
        print(dog.introduce())     # 출력: 저는 바둑이입니다.
        print(cat.introduce())     # 출력: 저는 나비입니다. 그리고 저는 고양이입니다.
        ```
    -   예외 클래스 만들기

        ```python
        class CustomException(Exception):
            def __init__(self, message="사용자 정의 예외가 발생했습니다."):
                self.message = message
                super().__init__(self.message)

            def __str__(self):
                return self.message

        try:
            raise CustomException("사용자 정의 예외 메시지")
        except CustomException as e:
            print(e)
        ```

    -   부모에 정의되어 있는 함수를 자식에서 다시 정의하는 것을 `재정의` 또는 `오버라이드(override)`라고 함
