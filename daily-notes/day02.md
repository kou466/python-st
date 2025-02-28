# 2025-02-28

## Chap03 조건문

- Boolean
    - True / False

    - 비교 연산자
        - ==
        - !=
        - >
        - <
        - >=
        - <=

        - 문자열에도 비교 연산자 사용 가능
            - 사전순으로 비교

- 논리 연산자
    - and
        - 조건 중 하나라도 False이면 False
    - or
        - 조건 중 하나라도 True이면 True
    - not
        - True -> False
        - False -> True

- 조건문
    - if
    - elif
    - else

    - if 조건문의 매개변수에 Boolean 타입이 아닌 값을 넣으면 자동으로 Boolean 타입으로 변환
    - False로 변환되는 값은 0, 0.0, None, 빈 컨테이너(빈 문자열, 빈 리스트, 빈 딕셔너리, 빈 튜플, 빈 세트 등)

- pass 키워드
    - 아무것도 하지 않음
    - 조건문의 매개변수에 들어가는 코드 블록을 작성할 때 사용
    - 예시

```python
if 조건문:
    pass
elif 조건문:
    pass
else:
    pass
```

> ### raise NotImplementedError
> - 아직 구현되지 않은 기능을 작성할 때 사용  
> - 조건문의 코드블록 내부에 사용 가능
