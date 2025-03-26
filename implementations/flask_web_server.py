# flask 테스트 예제

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "<h1>Hello, World!</h1>"


# bs_weather.py 와 동일하게 기상청의 rss 개선으로 인해 책의 기존 코드는 사용이 불가능하여 장기 예보로 수정함

# bs scraping 예제
from flask import Flask
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4.element import Tag

app = Flask(__name__)

@app.route("/")
def hello():
    target = urlopen(
        "http://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20250320.xml"
    )
    soup = BeautifulSoup(target, "lxml-xml")
    
    output = "<h1>기상청 장기 예보</h1>"
    
    weather_forecast = soup.find("weather_forecast")
    
    if weather_forecast and isinstance(weather_forecast, Tag):
        weeks = weather_forecast.find_all("week")
        for week in weeks:
            period_tag = week.find(lambda tag: tag.name.endswith("_period"))
            review_tag = week.find(lambda tag: tag.name.endswith("_weather_review"))

            if period_tag and review_tag:
                period = period_tag.get_text(strip=True)
                # <br> 태그는 HTML에서 그대로 사용할 수 있으므로 변환하지 않음
                review = review_tag.get_text(strip=True)
                
                output += f"<h2>기간: {period}</h2>"
                output += f"<p>{review}</p>"
            else:
                output += "<p>기간 또는 날씨 리뷰 태그가 없습니다.</p>"
    else:
        output += "<p>날씨 정보를 가져올 수 없습니다.</p>"
        
    return output

if __name__ == "__main__":
    app.run(debug=True)
