# BeautifulSoup 모듈 사용 예시

# 기존 코드는 html 파서를 사용하나, 오류가 발생하여 xml 파서를 사용하는 코드로 변경함

# from urllib import request
# from bs4 import BeautifulSoup

# # 웹 페이지 열기
# response = request.urlopen("http://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20250320.xml")

# soup = BeautifulSoup(response, "html.parser")

# for location in soup.select("location"):
#     print("도시 : ", location.select_one("city").string)
#     print("날씨 : ", location.select_one("wf").string)
#     print("최저기온 : ", location.select_one("tmn").string)
#     print("최고기온 : ", location.select_one("tmx").string)
#     print()

# 책에서 예시로 사용한 코드는 rss 중기 예보를 가져옴. 그러나 아래 사유에 따라 단기 및 중기 예보를 가져오는 것이 불가능해져, 장기전망을 가져오는 코드로 변경함 (ai 활용)

# □ 중단시기: 2025. 03. 31. (월) 10:00 이후 / 생산부서의 일정에 따라 예정보다 빨라질 수 있습니다.
# □ 중단서비스: 단기예보(1, 3시간 간격), 중기예보
# □ 중단사유: 개선된 단기예보 데이터 제공(‘24.11.28.)에 따라 RSS 서비스 종료
#   ○ 기존 RSS로 표출되던 데이터 생산 중단으로 기존 형식으로 제공 불가
# □ 대체서비스: 기상청 API허브 (https://apihub.kma.go.kr) > 예특보 > 단·중기예보

# XML 파서를 사용하는 코드
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4.element import Tag  # BeautifulSoup의 Tag 클래스 import

url = "http://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20250320.xml"

# 웹 페이지 열기
with urlopen(url) as response:
    xml_data = response.read()

# XML 파서 사용 (lxml 필요)
soup = BeautifulSoup(xml_data, "lxml-xml")  # XML 문서에는 XML 파서 사용

# 디버깅: XML 구조 확인
# print("루트 태그 존재:", soup is not None)
# print("첫 번째 태그 존재:", soup.find() is not None)

# find: 지정된 태그 이름과 일치하는 첫 번째 요소를 찾음
weather_forecast = soup.find("weather_forecast")
# print("weather_forecast 타입:", type(weather_forecast))

# 오류가 발생하던 이전 코드
# if weather_forecast and hasattr(weather_forecast, 'find_all'):
#     weeks = weather_forecast.find_all("week")

# isinstance: 객체가 특정 클래스의 인스턴스인지 확인 (예: Tag 타입인지)
if weather_forecast and isinstance(weather_forecast, Tag):
    # find_all: 지정된 태그 이름과 일치하는 모든 요소를 찾음
    weeks = weather_forecast.find_all("week")
    for week in weeks:
        # lambda와 endswith 조합: 특정 접미사로 끝나는 태그 이름 찾기
        period_tag = week.find(lambda tag: tag.name.endswith("_period"))
        review_tag = week.find(lambda tag: tag.name.endswith("_weather_review"))

        if period_tag and review_tag:
            # get_text: 태그의 텍스트 내용만 추출 (strip=True로 앞뒤 공백 제거)
            period = period_tag.get_text(strip=True)
            # replace: 문자열 대체 (여기서는 <br> 태그를 줄바꿈으로 변환)
            review = review_tag.get_text(strip=True).replace("<br>", "\n")

            print(f"기간: {period}")
            print(f"날씨 리뷰: {review}\n")

        else:
            print("기간 또는 날씨 리뷰 태그가 없습니다.")


# print("Location 태그 존재 여부:", bool(soup.find("location")))
# print("전체 태그 목록 샘플:", [tag.name for tag in soup.find_all()][:20])
