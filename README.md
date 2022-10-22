# Sparta Coding Club | 웹개발 종합반

### [Notion 노트정리](https://private-carp-369.notion.site/9a162781ca274d6bb0f8b7daaba3d6d0)

</br>
</br>

## 1주차

<details>
<summary>HTML, CSS 기본내용, 부트스트랩</summary>
  
- HTML, CSS의 기본내용에 대해 배움.

- 구글 웹 폰트를 사용함.

- bootstrap 4.0, 5.0을 간단하게 사용해 봄.
  
</details>

<details>
<summary>Javascript</summary>
  
- 모든 브라우저는 HTML + CSS + Javascript로 구성된다.

- console.log에서 간단히 다뤄봄.

- 변수에 대한 이해.

- 리스트와 딕셔너리에 대한 이해.

  - 리스트와 딕셔너리에 대한 이해를 바탕으로 기본적인 조합을 배움.
  
  - 기본 함수에 대한 이해.
  
    - toUpperCase, split, join.
    
  - if, else, if else, AND, OR 조건에 대한 이해.
  
  - 반복문에 대한 간단한 이해.
  
    - 반복문은 주로 리스트와 함께 쓰이며 리스트 내 딕셔너리를 하나씩 출력하는 방법에 대해 배움.
    
    - 또한 조건문을 응용하여 어느 조건에 해당 값을 출력하는 방법에 대해 배움.

</details>

<details>
<summary>1주차 숙제</summary>
  
  - 기획서를 바탕으로 간단한 HTML을 부트스트랩을 이용하여 만들어보기

    ![Untitled](https://user-images.githubusercontent.com/102138834/191512030-81d515a8-1a93-4810-9897-ab360de90869.png)</br>

- 결과

  ![스크린샷 2022-09-20 19 05 43](https://user-images.githubusercontent.com/102138834/191512236-4941b184-7558-4a00-904d-ac34704d5e49.png)

</details>
</br>
</br>

## 2주차

<details>
  <summary>전역변수와 지역변수를 간단히 이해하는 Javascript 홀/짝 클릭</summary>
</br>
<div>
  
  ```javascript
  function hey(){
    let count = 1;
    if (count % 2 == 0) {
        alert('짝수입니다')
    } else {
        alert ('홀수입니다')
    }
    count += 1;
  }
  ```
  
  ```javascript
  let count = 1;
  function hey(){
    if (count % 2 == 0) {
        alert('짝수입니다')
    } else {
        alert ('홀수입니다')
    }
    count += 1;
  }
  ```
  
</div>
</details>

<details>
<summary>jQuery</summary>
  
  - jQuery에 대한 간단한 이해를 바탕으로 간단히 실습.
  - jQuery는 부트스트랩에서 이미 사용중이므로 부트스트랩을 임포트하면 자동으로 jQuery를 쓸 수 있음.
  - backtick을 이용하여 문자 중간에 Javascript 변수를 삽입하는 방법에 대해 배움.
  - 그 외 text, hide, show, val, css, append를 활용하는 법을 배움.
  - jQuery + Javascript의 조합에 대해 배움.
    </br>
    
    ```javascript
    function q1() {
    // 1. input-q1의 입력값을 가져온다.
    // 2. 만약 입력값이 빈칸이면  alert('빈칸입니다!') 띄우기
    // 3. 빈칸이 아니면 alert(입력값) 띄우기

    let txt = $('#input-q1').val();
    if (txt == '') {
        alert('빈칸입니다.')
    } else {
        alert(txt)
    }

    }

    function q2() {
        // 1. input-q2 값을 가져온다.
        // 2. 만약 가져온 값에 @가 있으면 (includes 이용하기 - 구글링!)
        // 3. info.spartacoding@gmail.com -> gmail 만 추출해서 ( .split('@') 을 이용하자!)
        // 4. alert(도메인 값);으로 띄우기
        // 5. 만약 이메일이 아니면 '이메일이 아닙니다.' 라는 얼럿 띄우기

        let txt = $('#input-q2').val();

        if (txt.includes('@')) {
            let domain = txt.split('@')[1].split('.')[0]
            alert(domain)
        } else {
            alert('이메일주소가 아닙니다.')
        }
    }

    function q3() {
        // 1. input-q3 값을 가져온다. let txt = ... q1, q2에서 했던 걸 참고!
        // 2. 가져온 값을 이용해 names-q3에 붙일 태그를 만든다. (let temp_html = `<li>${txt}</li>`) 요렇게!
        // 3. 만들어둔 temp_html을 names-q3에 붙인다.(jQuery의 $('...').append(temp_html)을 이용하면 굿!)

        let txt = $('#input-q3').val();
        let temp_html = `<li>${txt}</li>`
        $('#names-q3').append(temp_html)
    }

    function q3_remove() {
        // 1. names-q3의 내부 태그를 모두 비운다.(jQuery의 $('....').empty()를 이용하면 굿!)

        $('#names-q3').empty()
    }
    ```

</details>

<details>
<summary>Ajax</summary>

- Json과 GET에 대한 간단한 이해.
- 서울시 미세먼지 API를 활용하여 Ajax 통신을 연습함.
- Ajax + jQuery 조합 연습 - 서울시 미세먼지 API를 활용해 미세먼지 수치가 높은 곳을 구분해주기
  </br>

  ```javascript
  function q1() {
    $("#names-q1").empty();
    $.ajax({
      type: "GET",
      url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
      data: {},
      success: function (response) {
        let rows = response["RealtimeCityAir"]["row"];

        for (let i = 0; i < rows.length; i++) {
          let gu_name = rows[i]["MSRSTE_NM"];
          let gu_mise = rows[i]["IDEX_MVL"];

          let temp_html = ``;
          if (gu_mise > 70) {
            temp_html = `<li class="bad">${gu_name} : ${gu_mise}</li>`;
          } else {
            temp_html = `<li>${gu_name} : ${gu_mise}</li>`;
          }
          $("#names-q1").append(temp_html);
        }
      },
    });
  }
  ```

- Ajax + jQuery 조합을 연습 - 서울시 따릉이 API를 활용해 남은 자전거 갯수가 낮은 곳을 구분해주기
  </br>

  ```javascript
  function q1() {
    $("#names-q1").empty();
    $.ajax({
      type: "GET",
      url: "http://spartacodingclub.shop/sparta_api/seoulbike",
      data: {},
      success: function (response) {
        let rows = response["getStationList"]["row"];

        for (let i = 0; i < rows.length; i++) {
          let name = rows[i]["stationName"];
          let rack = rows[i]["rackTotCnt"];
          let bike = rows[i]["parkingBikeTotCnt"];

          let temp_html = ``;
          if (bike < 5) {
            temp_html = `<tr class="urgent">
                                    <td>${name}</td>
                                    <td>${rack}</td>
                                    <td>${bike}</td>
                                </tr>`;
          } else {
            temp_html = `
                                <tr>
                                    <td>${name}</td>
                                    <td>${rack}</td>
                                    <td>${bike}</td>
                                </tr>`;
          }

          $("#names-q1").append(temp_html);
        }
      },
    });
  }
  ```

- Ajax + jQuery 조합을 연습 - 고양이 사진 API를 활용해 랜덤으로 고양이 사진을 불러오기
  </br>
  ```javascript
  function q1() {
  $.ajax({
      type: "GET",
      url: "https://api.thecatapi.com/v1/images/search",
      data: {},
      success: function (response) {
          let imgurl = response[0]['url']
          $('#img-cat').attr('src', imgurl)
          }
    })
  }
  ```
  </details>

<details>
<summary>2주차 숙제</summary>
  
- 1주차에 완성한 쇼핑몰 HTML에 환율 API를 활용해 원달러 환율을 표시한다.

- 페이지 로딩 후 바로 javascript를 실행하여 변동된 환율이 반영되어 나타나도록 한다.
  
  ![스크린샷 2022-09-21 21 12 16](https://user-images.githubusercontent.com/102138834/191522258-c447d396-da78-478f-8fa7-0147d3b58e6c.png)

  </br>
  
  ```javascript
  $(document).ready(function() {
    get_rate();
  });
  ```
  
  ```javascript
  function get_rate(){
    $.ajax({
        type: "GET",
        url: "http://spartacodingclub.shop/sparta_api/rate",
        data: {},
        success: function (response) {
            let now_rate = response['rate'];
            $('#now-rate').text(now_rate);
        }
    })
  }
  ```
  
  ```html
  <div class="item-desc">
      <h1>양키캔들 미드썸머나잇</h1>
      <p class="blue">원달러 환율 : <span id="now-rate"></span></p>
      <span class="price">가격:26,900원/개</span>
      <p>머스크, 세이지, 마호가니코롱</p>
      <p>넓게 트인 여름밤의 시원한 느낌을 담은 향으로 남성들이 선호하는 멋스러운 향.</p>
  </div>
  ```
  
</details>
</br>
</br>

## 3주차

<details>
<summary>Ajax + jQuery 복습 : 나홀로 링크 메모장 완성하기</summary>
  
  - open API에서 데이터를 불러와서 띄워주기
  - 버튼을 통한 메모장 열고 닫기
    </br>
    
    ```javascript
    $(document).ready(function () {
        $('#cards-box').empty();
        listing();
    });

    function listing() {
        $.ajax({
            type: "GET",
            url: "http://spartacodingclub.shop/post",
            data: {},
            success: function (response) {
                let rows = response['articles']
                for (let i = 0; i < rows.length; i++) {
                    let comment = rows[i]['comment']
                    let desc = rows[i]['desc']
                    let image = rows[i]['image']
                    let title = rows[i]['title']
                    let url = rows[i]['url']

                    let temp_html = `<div class="card">
                                        <img class="card-img-top"
                                            src="${image}">
                                        <div class="card-body">
                                            <a href="${url}" class="card-title">${title}</a>
                                            <p class="card-text">${desc}</p>
                                            <p class="card-text comment">${comment}</p>
                                        </div>
                                    </div>`
                    $('#card-box').append(temp_html)
                }
            }
        })
    }

    function openclose() {
        let status = $('#post-box').css('display');
        if (status == 'block') {
            $('#post-box').hide();
            $('#btn-posting-box').text('포스팅 박스 열기');
        } else {
            $('#post-box').show();
            $('#btn-posting-box').text('포스팅 박스 닫기');
        }
    }
    ```

- 결과

  ![스크린샷 2022-09-22 13 19 58](https://user-images.githubusercontent.com/102138834/193493975-358d0566-e876-46ef-9918-e265882ab075.png)


</details>

<details>
<summary>파이썬 시작하기</summary>
<br>

[점프 투 파이썬](https://wikidocs.net/4319)  
  
<details>
<summary>1. 변수</summary>
  
- 변수
  ```python
  a = 3      # 3을 a에 넣는다
  b = a      # a를 b에 넣는다
  a = a + 1  # a+1을 다시 a에 넣는다

  num1 = a*b # a*b의 값을 num1이라는 변수에 넣는다
  num2 = 99 # 99의 값을 num2이라는 변수에 넣는다
  ```

- 기본연산
  ```python
  >>> 1 + 2
  3
  ```
  ```python
  >>> 3 / 2.4
  1.25

  >>> 3 * 9
  27
  ```
  ```python
  >>> a = 1
  >>> b = 2
  >>> a + b
  3
  ```
  
</details>

<details>
<summary>2. 자료형</summary>
  
- 숫자 & 문자형
  ```python
  name = 'bob' # 변수에는 문자열이 들어갈 수도 있고,
  num = 12 # 숫자가 들어갈 수도 있고,

  is_number = True # True 또는 False -> "Boolean"형이 들어갈 수도 있음.
  ```
  
- 리스트 형 (Javascript의 배열형과 동일)
  ```python
  a_list = []
  a_list.append(1)     # 리스트에 값을 넣는다
  a_list.append([2,3]) # 리스트에 [2,3]이라는 리스트를 다시 넣는다

  # a_list의 값은? [1,[2,3]]
  # a_list[0]의 값은? 1
  # a_list[1]의 값은? [2,3]
  # a_list[1][0]의 값은? 2
  ```
  
- Dictionary 형 (Javascript의 dictionary형과 동일)
  ```python
  a_dict = {}
  a_dict = {'name':'bob','age':21}
  a_dict['height'] = 178

  # a_dict의 값은? {'name':'bob','age':21, 'height':178}
  # a_dict['name']의 값은? 'bob'
  # a_dict['age']의 값은? 21
  # a_dict['height']의 값은? 178
  ```
  
- Dictionary 형과 List형의 조합
  ```python
  people = [{'name':'bob','age':20},{'name':'carry','age':38}]

  # people[0]['name']의 값은? 'bob'
  # people[1]['name']의 값은? 'carry'

  person = {'name':'john','age':7}
  people.append(person)

  # people의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
  # people[2]['name']의 값은? 'john'
  ```
</details>
  
<details>
<summary>3. 함수</summary>
  
- 함수의 정의 - 이름은 마음대로 정할 수 있음!
  ```python
  # 수학문제에서
  f(x) = 2*x+3
  y = f(2)
  y의 값은? 7

  # 참고: 자바스크립트에서는
  function f(x) {
    return 2*x+3
  }

  # 파이썬에서
  def f(x):
    return 2*x+3

  y = f(2)
  y의 값은? 7
  ```
  
- 함수의 응용
  ```python
  def sum_all(a,b,c):
	return a+b+c

  def mul(a,b):
    return a*b

  result = sum_all(1,2,3) + mul(10,10)

  # result라는 변수의 값은?
  ```
  
</details>
  
<details>
<summary>4. 조건문</summary>
  
- if / else 로 구성!
  ```python
  def oddeven(num):  # oddeven이라는 이름의 함수를 정의한다. num을 변수로 받는다.
	if num % 2 == 0: # num을 2로 나눈 나머지가 0이면
		 return True   # True (참)을 반환한다.
	else:            # 아니면,
		 return False  # False (거짓)을 반환한다.

  result = oddeven(20)
  # result의 값은 무엇일까요?
  ```
  
  ```python
  def is_adult(age):
	if age > 20:
		print('성인입니다')    # 조건이 참이면 성인입니다를 출력
	else:
		print('청소년이에요')  # 조건이 거짓이면 청소년이에요를 출력

  is_adult(30)
  # 무엇이 출력될까요?
  ```
</details>
  
<details>
<summary>5. 반복문</summary>

- 파이썬에서의 반복문은, 리스트의 요소들을 하나씩 꺼내쓰는 형태. 즉, 무조건 리스트와 함께 쓰임.
  ```python
  fruits = ['사과','배','감','귤']

  for fruit in fruits:
  print(fruit)

  # 사과, 배, 감, 귤 하나씩 꺼내어 찍힙니다.
  ```
  
- 응용 : 과일 개수 세기 함수
  ```python
  fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
  ```
  ```python
  fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

  count = 0
  for fruit in fruits:
    if fruit == '사과':
      count += 1

  print(count)

  # 사과의 개수를 세어 보여줍니다.
  ```
  ```python
  def count_fruits(target):
	count = 0
	for fruit in fruits:
		if fruit == target:
			count += 1
	return count

  subak_count = count_fruits('수박')
  print(subak_count) #수박의 개수

  gam_count = count_fruits('감')
  print(gam_count) #감의 개수
  ```
  
- 딕셔너리의 다른 예제
  ```python
  people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]
  ```
  
  ```python
  people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

  # 모든 사람의 이름과 나이를 출력해봅시다.
  for person in people:
      print(person['name'], person['age'])


  # 이번엔, 반복문과 조건문을 응용한 함수를 만들어봅시다.
  # 이름을 받으면, age를 리턴해주는 함수
  def get_age(myname):
      for person in people:
          if person['name'] == myname:
              return person['age']
      return '해당하는 이름이 없습니다'


  print(get_age('bob'))
  print(get_age('kay'))
  ```

</details>

</details>

<details>
<summary>requests 라이브러리 사용해보기</summary>
  
- requests 라이브러리는 HTTP 호출할 때 거의 표준처럼 사용되는 라이브러리.
- requests 라이브러리는 매우 직관적인 API를 제공하는데 어떤 방식(method)의 HTTP 요청을 하느냐에 따라서 해당하는 이름의 함수를 사용하면 됨.  
  - GET 방식 : requests.get()
  - POST 방식 : requests.post()
  - PUT 방식 : requests.put()
  - DELETE 방식 : requests.delete()
  
- open API에서 데이터를 받아서 requests 라이브러리를 통해 필요한 자료를 출력해보자
  - requests 기본 세팅
  ```python
  import requests # requests 라이브러리 설치 필요

  r = requests.get('url')
  rjson = r.json()
  ```
  
- 서울시 미세먼지 API
  ```python
  http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99
  ```
  
- 미세먼지 70 이상인 곳의 구 이름을 출력
  ```python
  import requests
  
  r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
  rjson = r.json()
  
  gus = rjson['RealtimeCityAir']['row']
  
  for gu in gus:
    gu_name = gu['MSRSTE_NM']
    gu_mise = gu['IDEX_MVL']
    if (gu_mise > 70) :
        print(gu_name, gu_mise)
  ```
    </br>
</details>

<details>
<summary>bs4 라이브러리 사용해보기</summary>

- 웹 스크래핑에 대한 간단한 이해
  ```python
  # 선택자를 사용하는 방법 (copy selector)
  soup.select('태그명')
  soup.select('.클래스명')
  soup.select('#아이디명')

  soup.select('상위태그명 > 하위태그명 > 하위태그명')
  soup.select('상위태그명.클래스명 > 하위태그명.클래스명')

  # 태그와 속성값으로 찾는 방법
  soup.select('태그명[속성="값"]')

  # 한 개만 가져오고 싶은 경우
  soup.select_one('위와 동일')
  ```

- beautifulsoup wikipidia 기본세팅

  ```python
  #!/usr/bin/env python3
  # Anchor extraction from HTML document
  from bs4 import BeautifulSoup
  from urllib.request import urlopen
  with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
      soup = BeautifulSoup(response, 'html.parser')
      for anchor in soup.find_all('a'):
          print(anchor.get('href', '/'))
  ```
  
  - 태그 안의 텍스트를 찍고 싶을 땐 `태그.text`
  
  - 태그 안의 속성을 찍고 싶을 땐 `태그['속성']`
  
- 네이버 영화 크롤링 bs4 기본 세팅

  ```python
  import requests
  from bs4 import BeautifulSoup

  # URL을 읽어서 HTML를 받아오고
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get('',headers=headers)

  # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
  # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
  soup = BeautifulSoup(data.text, 'html.parser')
  ```
  
- 네이버 영화 평점순 순위, title, 평점 스크래핑
  - 코드
  ```python
  import requests
  from bs4 import BeautifulSoup

  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220926',headers=headers)

  soup = BeautifulSoup(data.text, 'html.parser')

  #old_content > table > tbody > tr:nth-child(2) > td.title > div > a

  trs = soup.select('#old_content > table > tbody > tr')

  for tr in trs:
      a_tag = tr.select_one('td.title > div > a')
      if a_tag is not None:
        
	#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
        # img 태그의 alt 속성값을 가져오기
	rank = tr.select_one('td:nth-child(1) > img')['alt']

	# a 태그 사이의 텍스트를 가져오기
        title = a_tag.text

        #old_content > table > tbody > tr:nth-child(2) > td.point
				# td 태그 사이의 텍스트를 가져오기
        score = tr.select_one('td.point').text

        print(rank, title, score)
  ```
  - 결과
  ```
  [Running] python -u "/Users/kimhyukjin/Desktop/prac/prac.py"
  01 탑건: 매버릭 9.77
  02 인생은 뷰티풀: 비타돌체 9.74
  03 클라우스 9.71
  04 할머니의 먼 집 9.62
  05 그린 북 9.60
  06 가버나움 9.59
  07 밥정 9.58
  08 베일리 어게인 9.54
  09 원더 9.53
  10 아일라 9.52
  11 디지몬 어드벤처 라스트 에볼루션 : 인연 9.51
  12 극장판 바이올렛 에버가든 9.50
  13 당갈 9.49
  14 먼 훗날 우리 9.48
  15 포드 V 페라리 9.48
  16 명탐정 코난: 할로윈의 신부 9.47
  17 주전장 9.46
  18 쇼생크 탈출 9.46
  19 터미네이터 2:오리지널 9.45
  20 덕구 9.44
  21 클래식 9.44
  22 라이언 일병 구하기 9.43
  23 장민호 드라마 최종회 9.43
  24 나 홀로 집에 9.43
  25 그대, 고맙소 : 김호중 생애 첫 팬미팅 무비 9.43
  26 월-E 9.42
  27 빽 투 더 퓨쳐 9.42
  28 사운드 오브 뮤직 9.42
  29 보헤미안 랩소디 9.42
  30 포레스트 검프 9.41
  31 글래디에이터 9.41
  32 타이타닉 9.41
  33 가나의 혼인잔치: 언약 9.41
  34 위대한 쇼맨 9.41
  35 인생은 아름다워 9.41
  36 살인의 추억 9.40
  37 매트릭스 9.40
  38 헬프 9.40
  39 센과 치히로의 행방불명 9.40
  40 캐스트 어웨이 9.40
  41 토이 스토리 3 9.39
  42 태극권 9.39
  43 씽2게더 9.39
  44 쉰들러 리스트 9.39
  45 헌터 킬러 9.39
  46 히든 피겨스 9.39
  47 반지의 제왕: 왕의 귀환 9.38
  48 어벤져스: 엔드게임 9.38
  49 죽은 시인의 사회 9.38
  50 집으로... 9.38

  [Done] exited with code=0 in 0.273 seconds
  ```
</details>

<details>
<summary>mongoDB 사용해보기</summary>

- insert / find / find / find_one / update / delete `summary`

  ```python
  # insert
  doc = {'name':'bobby','age':21}
  db.users.insert_one(doc)

  # find
  same_ages = list(db.users.find({'age':21},{'_id':False}))

  # find_one
  user = db.users.find_one({'name':'bobby'})

  # update
  db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

  # delete
  db.users.delete_one({'name':'bobby'})
  ```

- 웹 스크래핑 영화 정보 DB에 넣기
  ```python
  import requests
  from bs4 import BeautifulSoup

  from pymongo import MongoClient
  client = MongoClient('localhost', 27017)
  db = client.dbsparta

  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220926',headers=headers)

  soup = BeautifulSoup(data.text, 'html.parser')

  #old_content > table > tbody > tr:nth-child(2) > td.title > div > a

  trs = soup.select('#old_content > table > tbody > tr')

  for tr in trs:
      a_tag = tr.select_one('td.title > div > a')
      if a_tag is not None:
          #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
          rank = tr.select_one('td:nth-child(1) > img')['alt']
          title = a_tag.text
          #old_content > table > tbody > tr:nth-child(2) > td.point
          score = tr.select_one('td.point').text

          doc = {
              'rank':rank,
              'title':title,
              'score':score
          }

          db.movies.insert_one(doc)
  ```

- 웹 스크래핑한 영화 정보 이용해보기
  - 영화 '매트릭스'의 평점 가져오기 (O)
    ```python
    matrix = db.movies.find_one({'title':'매트릭스'},{'_id':False})
    print(matrix['score'])
    ```
  - 영화 '매트릭스'의 평점과 같은 평점의 영화제목 가져오기 (X)
    ```python
    same_movies = list(db.movies.find({'score':'9.41'},{'_id':False}))

    print(same_movies)
    ```
    - 수정 코드
      ```python
      same_movies = list(db.movies.find({'score':'9.41'},{'_id':False}))
      
      for same in same_movies:
      print(same['title'])
      ```
      
    - 결과
      ```python
      [Running] python -u "/Users/kimhyukjin/Desktop/web_development/3week/db_Quiz.py"
      포레스트 검프
      글래디에이터
      타이타닉
      가나의 혼인잔치: 언약
      위대한 쇼맨
      인생은 아름다워
      매트릭스
      
      [Done] exited with code=0 in 0.612 seconds
      ```
      
    - 위에 `""`으로 표시된 것은 문자 '9.41'이고 아래 `##`으로 표시된 것은 숫자 9.41이다.
    
    - 그래서 score를 바꿀때 앞에 str(0)을 써주거나 '0'으로 써야 하고 물론 작성한 코드도 부족했지만 위 내용처럼 문자와 숫자가 구분되지 않아서 매트릭스만 출력되었던 부분도 이러한 이유가 있는 것 같다.
    
    - 또한 list로 받은 `same_movies`를 for문을 돌려서 title만 뽑아내야 한다.
    
  - 영화 '매트릭스'의 평점을 0으로 바꾸기 (O)
    ```python
    db.movies.update_one({'title':'매트릭스'},{'$set':{'score':'0'}})
    ```
    
</details>

<details>
<summary>3주차 숙제</summary>

- 지니뮤직 사이트에서 순위 / 곡 제목 / 가수 스크래핑하기
  ```
  https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1
  ```

- `strip()`함수 사용하기

- python 문자열 인덱싱과 슬라이싱

- 코드
  ```python
  import requests
  from bs4 import BeautifulSoup
  
  from pymongo import MongoClient
  client = MongoClient('localhost', 27017)
  db = client.dbsparta
  
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get('https://www.genie.co.kr/chart/top200?ditc=W&rtm=N',headers=headers)
  
  soup = BeautifulSoup(data.text, 'html.parser')
  
  trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
  
  for tr in trs:
      rank = tr.select_one('td.number').text[0:2].strip()
      title = tr.select_one('td.info > a.title.ellipsis').text.strip()
      artist = tr.select_one('td.info > a.artist.ellipsis').text
      print(rank, title, artist)
  ```
- 결과
  ```
  [Running] python -u "/Users/kimhyukjin/Desktop/web_development/3week/3week_homework.py"
  1 After LIKE IVE (아이브)
  2 새삥 (Prod. by ZICO) (Feat. 호미들) 지코 (ZICO)
  3 Shut Down BLACKPINK
  4 Pink Venom BLACKPINK
  5 Attention NewJeans
  6 Hype boy NewJeans
  7 LOVE DIVE IVE (아이브)
  8 그때 그 순간 그대로 (그그그) WSG워너비 (가야G)
  9 FOREVER 1 소녀시대 (GIRLS' GENERATION)
  10 Cookie NewJeans
  11 보고싶었어 WSG워너비 (4FIRE)
  12 LAW (Prod. by Czaer) 비비 (BIBI) & 윤미래
  13 TOMBOY (여자)아이들
  14 Monologue 테이 (Tei)
  15 그라데이션 10CM
  16 사랑인가 봐 멜로망스 (MeloMance)
  17 SNEAKERS ITZY (있지)
  18 나의 X에게 경서
  19 That's Hilarious Charlie Puth
  20 That That (Prod. & Feat. SUGA of BTS) 싸이 (Psy)
  21 내가 아니라도 주호
  22 ELEVEN IVE (아이브)
  23 사랑은 늘 도망가 임영웅
  24 정이라고 하자 (Feat. 10CM) BIG Naughty (서동현)
  25 도깨비불 (Illusion) aespa
  26 내 기쁨은 너가 벤틀리를 끄는 거야 김승민
  27 다정히 내 이름을 부르면 경서예지 & 전건호
  28 POP! 나연 (TWICE)
  29 취중고백 김민석 (멜로망스)
  30 Love story 볼빨간사춘기
  31 해요 (2022) #안녕
  32 LOVE me BE'O (비오)
  33 봄여름가을겨울 (Still Life) BIGBANG (빅뱅)
  34 Stay The Kid LAROI & Justin Bieber
  35 신호등 이무진
  36 FEARLESS LE SSERAFIM (르세라핌)
  37 너의 모든 순간 성시경
  38 strawberry moon 아이유 (IU)
  39 우리들의 블루스 임영웅
  40 새벽에 걸려온 너의 전화는 한동근
  41 MY BAG (여자)아이들
  42 바보에게 바보가 (웹툰 '연애의 발견' X 이석훈) 이석훈
  43 사랑한다고 말해줘 탑현
  44 Loving You Girl (Feat. Hkeem) Peder Elias
  45 Bad Habits Ed Sheeran
  46 듣고 싶을까 MSG워너비 (M.O.M)
  47 밤하늘의 별을 (2020) 경서
  48 Feel My Rhythm Red Velvet (레드벨벳)
  49 Next Level aespa
  50 Talk that Talk TWICE (트와이스)
  
  [Done] exited with code=0 in 0.694 seconds
  ```

</details>
</br>
</br>

## 4주차

<details>
<summary>Flask 시작하기</summary>

- render_template

  - flask 프레임워크의 Jinja2 템플릿엔진을 사용하여 render_template()함수를 이용하여 HTML을 렌더링해보자
  
    ```python
    from flask import Flask, render_template, request, jsonify
    app = Flask(__name__)
    ```
  
- Flask API GET, POST 연습해보기 

  - GET
  
    ```python
    @app.route('/test', methods=['GET'])
    def test_get():
      title_receive = request.args.get('title_give')
      print(title_receive)
      return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
    ```
  
    ```javascript
    $.ajax({
      type: "GET",
      url: "/test?title_give=봄날은간다",
      data: {},
      success: function(response){
         console.log(response)
      }
    })
    ```
  
  - POST
  
    ```python
    @app.route('/test', methods=['POST'])
    def test_post():
      title_receive = request.form['title_give']
      print(title_receive)
      return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
    ```
    
    ```javascript
    $.ajax({
      type: "POST",
      url: "/test",
      data: { title_give:'수리남' },
      success: function(response){
         console.log(response)
      }
    })
    ```
    
</details>

<details>
<summary>'책 리뷰' 미니 프로젝트</summary>

- 들어가기 전

  - Flask를 통해서 개발 순서를 머릿속으로 익히고 배운다.
  
    - 클라이언트와 서버가 잘 연결되어 있는지 확인하기
    
    - 서버 만들기
    
    - 클라이언트 만들기
    
    - 완성 확인하기
    
  - POST, GET 연습을 통해 코드를 익힌다.
  
    - 데이터를 받아서 보내주는 연습과 Json형식으로 GET 리턴하는 연습을 익힌다.
    
  - Ajax와 jQuery의 조합에 대한 사용법을 숙지한다.
  
    - title, author, review의 데이터를 받아서 db에 insert하고
    
    - 모든 데이터를 find, HTML에 append.
  
  <details>
  <summary>index.html</summary>
    <br>
    
	```html
	<!DOCTYPE html>
	<html lang="ko">

	<head>
	<!-- Webpage Title -->
	<title>Flask 책리뷰 연습하기</title>

	<!-- Required meta tags -->
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
	integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

	<!-- JS -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
	integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
	crossorigin="anonymous"></script>

	<!-- 구글폰트 -->
	<link href="https://fonts.googleapis.com/css?family=Do+Hyeon&display=swap" rel="stylesheet">

	<script type="text/javascript">

	$(document).ready(function () {
	    showReview();
	});

	// 리뷰 저장하기
	function makeReview() {
	    // #id에 해당하는 .val() value값을 let 변수명으로 받아라
	    let title = $('#title').val()
	    let author = $('#author').val()
	    let review = $('#bookReview').val()

	    // 위에서 받은 변수들을 ajax post로 받은 데이터들을 받아서 서버에 보내줘라.
	    $.ajax({
		type: "POST",
		url: "/review",
		data: { title_give: title, author_give: author, review_give: review },
		success: function (response) {
		    alert(response["msg"]);
		    window.location.reload();
		}
	    })
	}

	// 리뷰 띄워주기
	function showReview() {
	    $.ajax({
		type: "GET",
		url: "/review",
		data: {},
		success: function (response) {
		    // reviews에 서버에서 보낸 all_review를 받아내고
		    let reviews = response['all_reviews']

		    // 반복문을 돌려서 모든 데이터를 변수 지정해서 꺼낸 다음에
		    for (let i = 0; i < reviews.length; i++) {
			let title = reviews[i]['title']
			let author = reviews[i]['author']
			let review = reviews[i]['review']

			// html에 append한다.
			let temp_html = `<tr>
					    <td>${title}</td>
					    <td>${author}</td>
					    <td>${review}</td>
					</tr>`

			$('#reviews-box').append(temp_html)
		    }
		}
	    })
	}
	</script>

	<style type="text/css">
	* {
	    font-family: "Do Hyeon", sans-serif;
	}

	h1,
	h5 {
	    display: inline;
	}

	.wrap {
	    margin: auto;
	    width: 100%;
	}

	.main-image {
	    width: 800px;
	    height: 600px;
	    margin: auto;
	}

	.info {
	    margin: 20px auto 20px auto;
	    width: 500px;
	}

	.review-btn {
	    text-align: center;
	}

	.reviews {
	    margin: 70px auto 70px auto;
	    width: 800px;
	}

	.title {
	    width: 200px;
	}

	.author {
	    width: 100px;
	}

	.review-content {
	    width: 700px;
	}
	</style>
	</head>

	<body>
	<div class="container">
	<div class="main-image">
	    <img src="https://previews.123rf.com/images/maxxyustas/maxxyustas1511/maxxyustas151100002/47858355-education-concept-books-and-textbooks-on-the-bookshelf-3d.jpg"
		class="img-fluid" alt="Responsive image">
	</div>
	<div class="info">
	    <h1>읽은 책에 대해 리뷰를 남겨보자.</h1>
	    <p>내가 읽은 책의 제목과 그 책의 저자, 나의 개인적인 리뷰를 남기는 공간</p>
	    <div class="input-group mb-3">
		<div class="input-group-prepend">
		    <span class="input-group-text">책제목</span>
		</div>
		<input type="text" class="form-control" id="title">
	    </div>
	    <div class="input-group mb-3">
		<div class="input-group-prepend">
		    <span class="input-group-text">저자</span>
		</div>
		<input type="text" class="form-control" id="author">
	    </div>
	    <div class="input-group mb-3">
		<div class="input-group-prepend">
		    <span class="input-group-text">리뷰</span>
		</div>
		<textarea class="form-control" id="bookReview" cols="30" rows="5"
		    placeholder="140자까지 입력할 수 있습니다."></textarea>
	    </div>
	    <div class="review-btn">
		<button onclick="makeReview()" type="button" class="btn btn-primary">리뷰 작성하기</button>
	    </div>
	</div>
	<div class="reviews">
	    <table class="table">
		<thead>
		    <tr>
			<th scope="col" class="title">책 제목</th>
			<th scope="col" class="author">저자</th>
			<th scope="col" class="review-content">리뷰</th>
		    </tr>
		</thead>
		<tbody id="reviews-box">
		</tbody>
	    </table>
	</div>
	</div>
	</body>

	</html>
	```

  </details>
  
  <details>
  <summary>app.py</summary>
    <br>
    
	```python
	from flask import Flask, render_template, jsonify, request
	app = Flask(__name__)


	# mongoDB
	from pymongo import MongoClient
	client = MongoClient('localhost', 27017)
	db = client.bookreview


	## HTML을 주는 부분
	@app.route('/')
	def home():
	    return render_template('index.html')


	## API 역할을 하는 부분
	@app.route('/review', methods=['POST'])
	def write_review():
	    title_receive = request.form['title_give']
	    author_receive = request.form['author_give']
	    review_receive = request.form['review_give']

	    ## 딕셔너리를 하나 만들고
	    doc = {
		'title': title_receive,
		'author': author_receive,
		'review': review_receive
	    }

	    # bookreview collection 으로 insert 해라.
	    db.bookreview.insert_one(doc)

	    return jsonify({'msg': '리뷰를 남겼습니다'})


	@app.route('/review', methods=['GET'])
	def read_reviews():
	    # db bookreview에서 모든 데이터를 find하고 reviews에 담고
	    reviews = list(db.bookreview.find({}, {'_id':False}))

	    # json형식으로 reviews를 all reviews로 return한다.
	    return jsonify({'all_reviews': reviews})


	if __name__ == '__main__':
	    app.run('0.0.0.0', port=5001, debug=True)
	```
  
  </details>
  
  <details>
  <summary>홈페이지 사진</summary>
    <br>
    
    ![스크린샷 2022-10-11 20 58 16](https://user-images.githubusercontent.com/102138834/195085350-6bc16a9d-26a5-4ac2-b6da-6d142f2cb2c2.png)
    
  
  </details>
  
  <details>
  <summary>DB</summary>
    <br>
    
    <img width="596" alt="스크린샷 2022-10-11 20 58 38" src="https://user-images.githubusercontent.com/102138834/195085515-d2d854c5-4ba1-41af-8c5c-cd3fedc83726.png">

  
  </details>

</details>

<details>
<summary>'영화 링크 메모장' 미니 프로젝트</summary>

- 들어가기 전

  - meta tag 스크롤링을 통한 데이터를 DB에 저장하고 이를 활용해 나만의 영화 리뷰 메모장을 만든다.
  
    - meta tag 스크롤링하는 beautifulsoup의 새로운 크롤링 방식에 대해 익힌다.
  
  - Flask를 통해서 개발 순서를 머릿속으로 익히고 배운다.
  
    - 클라이언트와 서버가 잘 연결되어 있는지 확인하기
    
    - 서버 만들기
    
    - 클라이언트 만들기
    
    - 완성 확인하기
    
  - POST, GET 연습을 통해 코드를 익힌다.
  
    - 데이터를 받아서 보내주는 연습과 Json형식으로 GET 리턴하는 연습을 익힌다.
    
  - Ajax와 jQuery의 조합에 대한 사용법을 숙지한다.
  
    - 스크롤링한 데이터를 받아서 db에 insert하고
    
    - 모든 데이터를 find, HTML에 append.
    
  <details>
  <summary>index.html</summary>
    <br>
    
	```html
	<!Doctype html>
	<html lang="ko">

	<head>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
		integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

	    <!-- JS -->
	    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
		integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
		crossorigin="anonymous"></script>

	    <!-- 구글폰트 -->
	    <link href="https://fonts.googleapis.com/css?family=Stylish&display=swap" rel="stylesheet">


	    <title>영화리뷰 메모장</title>

	    <!-- style -->
	    <style type="text/css">
		* {
		    font-family: "Stylish", sans-serif;
		}

		.wrap {
		    width: 900px;
		    margin: auto;
		}

		.comment {
		    color: blue;
		    font-weight: bold;
		}

		#post-box {
		    width: 500px;
		    margin: 20px auto;
		    padding: 50px;
		    border: black solid;
		    border-radius: 5px;
		}
	    </style>
	    <script>
		$(document).ready(function () {
		    showArticles();
		});

		function openClose() {
		    if ($("#post-box").css("display") == "block") {
			$("#post-box").hide();
			$("#btn-post-box").text("포스팅 작성하기");
		    } else {
			$("#post-box").show();
			$("#btn-post-box").text("포스팅 박스 닫기");
		    }
		}

		function postArticle() {
		    let url = $('#post-url').val()
		    let comment = $('#post-comment').val()

		    $.ajax({
			type: "POST",
			url: "/memo",
			data: {url_give:url, comment_give:comment},
			success: function (response) { // 성공하면
			    alert(response["msg"]);
			    window.location.reload()
			}
		    })
		}

		function showArticles() {
		    $.ajax({
			type: "GET",
			url: "/memo?sample_give=샘플데이터",
			data: {},
			success: function (response) {
			    let articles = response['all_articles']

			    for (let i = 0; i < articles.length; i++) {
				let title = articles[i]['title']
				let image = articles[i]['image']
				let url = articles[i]['url']
				let desc = articles[i]['desc']
				let comment = articles[i]['comment']

				let temp_html = `<div class="card">
						    <img class="card-img-top"
							src="${image}"
							alt="Card image cap">
						    <div class="card-body">
							<a target="_blank" href="${url}" class="card-title">${title}</a>
							<p class="card-text">${desc}</p>
							<p class="card-text comment">${comment}</p>
						    </div>
						</div>`

				$('#cards-box').append(temp_html)
			    }
			}
		    })
		}
	    </script>

	</head>

	<body>
	    <div class="wrap">
		<div class="jumbotron">
		    <h1 class="display-4">NAVER 영화 링크 메모장!</h1>
		    <p class="lead">재밌게 본 영화의 NAVER 링크를 저장해두고, 기록할 수 있는 나만의 영화리뷰 공간</p>
		    <hr class="my-4">
		    <p class="lead">
			<button onclick="openClose()" id="btn-post-box" type="button" class="btn btn-primary">포스팅 작성하기
			</button>
		    </p>
		</div>
		<div id="post-box" class="form-post" style="display:none">
		    <div>
			<div class="form-group">
			    <label for="post-url">아티클 URL</label>
			    <input id="post-url" class="form-control" placeholder="">
			</div>
			<div class="form-group">
			    <label for="post-comment">간단 코멘트</label>
			    <textarea id="post-comment" class="form-control" rows="2"></textarea>
			</div>
			<button type="button" class="btn btn-primary" onclick="postArticle()">기사저장</button>
		    </div>
		</div>
		<div id="cards-box" class="card-columns">
		</div>
	    </div>
	</body>

	</html>
	```
  
  </details>
  
  <details>
  <summary>app.py</summary>
    <br>

	```python
	from flask import Flask, render_template, jsonify, request
	app = Flask(__name__)

	import requests
	from bs4 import BeautifulSoup

	from pymongo import MongoClient
	client = MongoClient('localhost', 27017)
	db = client.linkmemo


	## HTML을 주는 부분
	@app.route('/')
	def home():
	    return render_template('index.html')


	@app.route('/memo', methods=['GET'])
	def listing():
	    articles = list(db.linkmemo.find({}, {'_id':False}))
	    return jsonify({'all_articles':articles})


	## API 역할을 하는 부분
	@app.route('/memo', methods=['POST'])
	def saving():
	    url_receive = request.form['url_give']
	    comment_receive = request.form['comment_give']

	    # data에 url receive를 받기 때문에 아래와 같이 따로 써 줄 필요가 없다.
	    # url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=81888' 탑건 메버릭 url

	    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
	    data = requests.get(url_receive, headers=headers)

	    soup = BeautifulSoup(data.text, 'html.parser')

	    og_title = soup.select_one('meta[property="og:title"]')['content']
	    og_image = soup.select_one('meta[property="og:image"]')['content']
	    og_description = soup.select_one('meta[property="og:description"]')['content']

	    doc = {
		'title':og_title,
		'image':og_image,
		'desc':og_description,
		'url':url_receive,
		'comment':comment_receive
	    }

	    db.linkmemo.insert_one(doc)

	    return jsonify({'msg':'포스팅을 완료하였습니다'})


	if __name__ == '__main__':
	    app.run('0.0.0.0',port=5001,debug=True)
	```
  
  </details>


</details>



<details>
<summary>4주차 숙제</summary>

- 1주차에 완성한 쇼핑몰에 두 가지 기능을 추가해서 완성하기

  - 정보를 입력 후 주문하기를 클릭하면 주문 목록에 데이터가 추가
  
  - 페이지 로딩 후 하단에 주문자 목록이 자동으로 보여지도록
  
  <details>
  <summary>index.html</summary>
    <br>
    
	```html
	<!doctype html>
	<html lang="en">

	<head>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
		integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

	    <!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
		integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
		crossorigin="anonymous"></script>
	    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
		integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
		crossorigin="anonymous"></script>

	    <title>스파르타코딩클럽 | 부트스트랩 연습하기</title>

	    <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">

	    <style>
		* {
		    font-family: 'Jua', sans-serif;
		}

		.item-img {
		    width: 500px;
		    height: 300px;

		    margin: 30px auto 30px auto;
		    background-image: url("https://t1.daumcdn.net/liveboard/nts/5bcccfbd33da4865817b9c606b6b852e.JPG");
		    background-position: center;
		    background-size: cover;
		}

		.price {
		    font-size: 20px;
		}

		.item-desc {
		    width: 500px;
		    margin: 20px auto 20px auto;
		}

		.item-order {
		    width: 500px;
		    margin: 20px auto 70px auto;
		}

		.btn-order {
		    margin: auto;
		    width: 100px;

		    display: block;
		}

		.wrap {
		    width: 700px;
		    margin: auto;
		}

		.rate {
		    color: blue;
		}
	    </style>

	    <script>
		$(document).ready(function () {
		    get_rate();
		    listing();
		});

		function listing() {
		    $.ajax({
			type: "GET",
			url: "/order",
			data: {},
			success: function (response) {
			    if (response["result"] == "success") {
				let orders = response['orders'];
				for (let i = 0; i < orders.length; i++) {
				    let name = orders[i]['name'];
				    let count = orders[i]['count'];
				    let address = orders[i]['address'];
				    let phone = orders[i]['phone'];

				    let temp_html = `<tr>
							<th scope="row">${name}</th>
							<td>${count}</td>
							<td>${address}</td>
							<td>${phone}</td>
						    </tr>`
				    $('#orders-box').append(temp_html)
				}
			    }
			}
		    })
		}

		function get_rate() {
		    $.ajax({
			type: "GET",
			url: "https://api.manana.kr/exchange/rate.json",
			data: {},
			success: function (response) {
			    let now_rate = response[1]['rate'];
			    $('#now-rate').text(now_rate);
			}
		    })
		}

		function order() {
		    let name = $('#order-name').val();
		    let count = $('#order-count').val();
		    let address = $('#order-address').val();
		    let phone = $('#order-phone').val();

		    $.ajax({
			type: "POST",
			url: "/order",
			data: { name_give: name, count_give: count, address_give: address, phone_give: phone },
			success: function (response) {
			    if (response["result"] == "success") {
				alert(response["msg"]);
				window.location.reload();
			    }
			}
		    })
		}
	    </script>
	</head>

	<body>
	    <div class="wrap">
		<div class="item-img"></div>
		<div class="item-desc">
		    <h1>양키캔들 미드썸머나잇</h1>
		    <p class="blue">원달러 환율 : <span id="now-rate"></span></p>
		    <span class="price">가격:26,900원/개</span>
		    <p>머스크, 세이지, 마호가니코롱</p>
		    <p>넓게 트인 여름밤의 시원한 느낌을 담은 향으로 남성들이 선호하는 멋스러운 향.</p>
		</div>
		<div class="item-order">
		    <div class="input-group mb-3">
			<div class="input-group-prepend">
			    <span class="input-group-text">주문자이름</span>
			</div>
			<input type="text" id="order-name" class="form-control" aria-label="Default"
			    aria-describedby="inputGroup-sizing-default">
		    </div>
		    <div class="input-group mb-3">
			<div class="input-group-prepend">
			    <label class="input-group-text" for="inputGroupSelect01">수량</label>
			</div>
			<select class="custom-select" id="order-count">
			    <option selected>-- 수량을 선택하세요 --</option>
			    <option value="1">1</option>
			    <option value="2">2</option>
			    <option value="3">3</option>
			    <option value="4">4</option>
			    <option value="5">5</option>
			    <option value="6">6</option>
			    <option value="7">7</option>
			</select>
		    </div>
		    <div class="input-group mb-3">
			<div class="input-group-prepend">
			    <span class="input-group-text">주소</span>
			</div>
			<input id="order-address" type="text" class="form-control" aria-label="Default"
			    aria-describedby="inputGroup-sizing-default">
		    </div>
		    <div class="input-group mb-3">
			<div class="input-group-prepend">
			    <span class="input-group-text">전화번호</span>
			</div>
			<input id="order-phone" type="text" class="form-control" aria-label="Default"
			    aria-describedby="inputGroup-sizing-default">
		    </div>
		    <button type="button" onclick="order()" class="btn btn-primary btn-order">주문하기</button>
		</div>
		<table class="table">
		    <thead>
			<tr>
			    <th scope="col">이름</th>
			    <th scope="col">수량</th>
			    <th scope="col">주소</th>
			    <th scope="col">전화번호</th>
			</tr>
		    </thead>
		    <tbody id="orders-box">
		    </tbody>
		</table>
	    </div>
	</body>

	</html>
	```
  
  </details>
  
  <details>
  <summary>app.py</summary>
    <br>

	```python
	from flask import Flask, render_template, jsonify, request

	app = Flask(__name__)

	from pymongo import MongoClient

	client = MongoClient('localhost', 27017)
	db = client.dbhomework


	## HTML 화면 보여주기
	@app.route('/')
	def homework():
	    return render_template('index.html')


	# 주문하기(POST) API
	@app.route('/order', methods=['POST'])
	def save_order():
	    name_receive = request.form['name_give']
	    count_receive = request.form['count_give']
	    address_receive = request.form['address_give']
	    phone_receive = request.form['phone_give']

	    doc = {
		'name': name_receive,
		'count': count_receive,
		'address': address_receive,
		'phone': phone_receive
	    }
	    db.orders.insert_one(doc)

	    return jsonify({'result': 'success', 'msg': '주문 완료!'})


	# 주문 목록보기(Read) API
	@app.route('/order', methods=['GET'])
	def view_orders():
	    orders = list(db.orders.find({}, {'_id': False}))
	    return jsonify({'result': 'success', 'orders': orders})


	if __name__ == '__main__':
	    app.run('0.0.0.0', port=5001, debug=True)
	```
  </details>
  
  <details>
  <summary>홈페이지</summary>
    <br>
    
    ![스크린샷 2022-10-11 22 27 48](https://user-images.githubusercontent.com/102138834/195104810-09756398-8d62-4375-8d34-3b8b291aa2e3.png)

  
  </details>
  
  <details>
  <summary>DB</summary>
    <br>
  
    <img width="823" alt="스크린샷 2022-10-11 22 30 59" src="https://user-images.githubusercontent.com/102138834/195104826-f9a9b8c6-37c4-4ff7-b334-ce75413bf2fa.png">

  
  </details>

</details>
</br>
</br>

## 5주차

<details>
<summary>'my favorite movie star' 미니 프로젝트</summary>

- 영화인들의 정보를 스크롤링하여 나만의 영화인 홈페이지이다. 좋아요 순으로 정렬하고 영화인을 삭제할 수 있다.

- 들어가기 전

  - Ajax와 jQuery의 조합에 대한 Read, Update, Delete를 배운다.
  
  - Flask를 통해서 개발 순서를 머릿속으로 익히고 배운다.
  
    - 클라이언트와 서버가 잘 연결되어 있는지 확인하기
    
    - 서버 만들기
    
    - 클라이언트 만들기
    
    - 완성 확인하기
    
  - POST, GET 연습을 통해 코드를 익힌다.
  
    - 데이터를 받아서 보내주는 연습과 Json형식으로 GET 리턴하는 연습을 익힌다.
  
  </br>  
  <details>
  <summary>만들 API</summary>
  
    - Read : 데이터 정보 전체 조회
    
    - Update : 좋아요 기능
  
    - Delete : 배우의 데이터 삭제
  
  </details>

  <details>
  <summary>배우 데이터 적립을 위한 스크롤링</summary>
  
    - 영화배우와 영화, 이미지, url, 최근작품, 좋아요의 데이터를 스크롤링해서 mongoDB에 넣는다.
    
        ```python
		import requests
		from bs4 import BeautifulSoup

		from pymongo import MongoClient

		client = MongoClient('localhost', 27017)
		db = client.mystar

		# DB에 저장할 영화인들의 출처 url을 가져옵니다.
		def get_urls():
		    headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
		    data = requests.get('https://movie.naver.com/movie/sdb/rank/rpeople.nhn', headers=headers)

		    soup = BeautifulSoup(data.text, 'html.parser')

		    trs = soup.select('#old_content > table > tbody > tr')

		    urls = []
		    for tr in trs:
			a = tr.select_one('td.title > a')
			if a is not None:
			    base_url = 'https://movie.naver.com/'
			    url = base_url + a['href']
			    urls.append(url)

		    return urls

		# 출처 url로부터 영화인들의 사진, 이름, 최근작 정보를 가져오고 mystar 콜렉션에 저장합니다.
		def insert_star(url):
		    headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
		    data = requests.get(url, headers=headers)

		    soup = BeautifulSoup(data.text, 'html.parser')

		    name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
		    img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
		    recent_work = soup.select_one(
			'#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text

		    doc = {
			'name': name,
			'img_url': img_url,
			'recent': recent_work,
			'url': url,
			'like': 0
		    }

		    db.mystar.insert_one(doc)
		    print('완료!', name)

		# 기존 mystar 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
		def insert_all():
		    db.mystar.drop()  # mystar 콜렉션을 모두 지워줍니다.
		    urls = get_urls()
		    for url in urls:
			insert_star(url)

		### 실행하기
		insert_all()
        ```

  </details>
  
  <details>
  <summary>app.py</summary>

    - sort함수를 사용해 좋아요 순으로 정렬하고, 좋아요 버튼 클릭시 데이터를 수정하는 방법에 대해 배움.
  
      ```python
		from pymongo import MongoClient

		from flask import Flask, render_template, jsonify, request

		app = Flask(__name__)

		client = MongoClient('localhost', 27017)
		db = client.mystar


		# HTML 화면 보여주기
		@app.route('/')
		def home():
		    return render_template('index.html')


		# API 역할을 하는 부분
		# GET
		@app.route('/api/list', methods=['GET'])
		def show_stars():
		    movie_star = list(db.mystar.find({}, {'_id':False}).sort('like',-1))
		    # sort : pymongo에서 데이터를 정렬해서 데이터를 뽑아줌.
		    return jsonify({'movie_stars': movie_star})


		@app.route('/api/like', methods=['POST'])
		def like_star():
		    name_receive = request.form['name_give']
		    # 이름을 받아오고

		    target_star = db.mystar.find_one({'name': name_receive})
		    current_like = target_star['like']
		    # 받아온 이름에서 맞는 target_star 하나를 찾아주고 그 target_star의 like를 current_like로 받는다.

		    new_like = current_like + 1
		    # 찾은 target_star의 current_like를 하나 올려서 new_like로 받고

		    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})
		    # db에 POST하는데 name이 위에서 받아온 name_receive인 것의 like를 new_like로 바꾼다.

		    return jsonify({'msg': '좋아요!'})


		@app.route('/api/delete', methods=['POST'])
		def delete_star():
		    name_receive = request.form['name_give']

		    db.mystar.delete_one({'name':name_receive})

		    return jsonify({'msg': '영화인을 삭제했습니다.'})


		if __name__ == '__main__':
		    app.run('0.0.0.0', port=5001, debug=True)
      ```
  
  </details>

  <details>
  <summary>index.html</summary>

    - Ajax, jQuery
  
      ```html
		<!DOCTYPE html>
		<html lang="ko">

		<head>
		    <meta charset="UTF-8" />
		    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
		    <title>My Favorite movie star</title>
		    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
		    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.0/css/bulma.min.css" />
		    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
		    <style>
			.center {
			    text-align: center;
			}

			.star-list {
			    width: 500px;
			    margin: 20px auto 0 auto;
			}

			.star-name {
			    display: inline-block;
			}

			.star-name:hover {
			    text-decoration: underline;
			}

			.card {
			    margin-bottom: 15px;
			}
		    </style>
		    <script>
			$(document).ready(function () {
			    showStar();
			});

			function showStar() {
			    $.ajax({
				type: 'GET',
				url: '/api/list?sample_give=샘플데이터',
				data: {},
				success: function (response) {
				    let mystars = response['movie_stars']
				    for (let i = 0; i < mystars.length; i++) {
					let name = mystars[i]['name']
					let img_url = mystars[i]['img_url']
					let recent = mystars[i]['recent']
					let url = mystars[i]['url']
					let like = mystars[i]['like']

					let temp_html = `<div class="card">
							    <div class="card-content">
								<div class="media">
								    <div class="media-left">
									<figure class="image is-48x48">
									    <img src="${img_url}"
										alt="Placeholder image" />
									</figure>
								    </div>
								    <div class="media-content">
									<a href="${url}" target="_blank" class="star-name title is-4">${name} (좋아요: ${like})</a>
									<p class="subtitle is-6">최신작 : ${recent}</p>
								    </div>
								</div>
							    </div>
							    <footer class="card-footer">
								<a href="#" onclick="likeStar('${name}')" class="card-footer-item has-text-info">
								    좋아요
								    <span class="icon">
									<i class="fas fa-thumbs-up"></i>
								    </span>
								</a>
								<a href="#" onclick="deleteStar('${name}')" class="card-footer-item has-text-danger">
								    삭제
								    <span class="icon">
									<i class="fas fa-ban"></i>
								    </span>
								</a>
							    </footer>
							</div>`
					$('#star-box').append(temp_html)
				    }
				}
			    });
			}

			function likeStar(name) {
			    $.ajax({
				type: 'POST',
				url: '/api/like',
				data: { name_give:name },
				success: function (response) {
				    // 좋아요 메세지를 띄워주고 윈도우를 reload한다.
				    alert(response['msg']);
				    window.location.reload()
				}
			    });
			}

			function deleteStar(name) {
			    $.ajax({
				type: 'POST',
				url: '/api/delete',
				data: { name_give:name },
				// 가져갈 데이터는 name_give이고 name이라는 변수 가져가라.
				success: function (response) {
				    alert(response['msg']);
				    window.location.reload()
				}
			    });
			}

		    </script>
		</head>

		<body>
		    <section class="hero is-warning">
			<div class="hero-body">
			    <div class="container center">
				<h1 class="title">
				    My Favorite movie star
				</h1>
				<h2 class="subtitle">
				    영화인 랭킹
				</h2>
			    </div>
			</div>
		    </section>
		    <div class="star-list" id="star-box">
		    </div>
		</body>

		</html>
      ```
  
  </details>

  <details>
  <summary>결과물 확인하기</summary>
  
    - 데이터 불러오기
  
      ![스크린샷 2022-10-12 21 06 59](https://user-images.githubusercontent.com/102138834/196372458-1ffa9227-c7c0-4408-a978-01994e7ae27f.png)

    - 좋아요 기능
    
      ![스크린샷 2022-10-17 21 58 02](https://user-images.githubusercontent.com/102138834/196372698-3327bef4-369a-40f9-974e-c55ee88b6dd0.png)

    - 영화인 리스트 삭제
    
      ![스크린샷 2022-10-17 22 06 29](https://user-images.githubusercontent.com/102138834/196372793-9fd37b3c-8ba8-4051-a039-05add296470c.png)

      ![스크린샷 2022-10-17 22 06 37](https://user-images.githubusercontent.com/102138834/196372833-c237c452-4856-4b50-af24-d9a9a6f90021.png)

  
  </details>

</details>

<details>
<summary>AWS EC2 서버 구매하고 세팅하기</summary>

</details>


<details>
<summary>gavia 도메인 설정</summary>

</details>


</br>
</br>

## 미니프로젝트

- 웹개발 종합반 SUMMARY

  - flask API

  - Mongo DB Atlas & Robo 3T

  - Ajax + jQuery
  
  - AWS EC2
  
  - bs4 Scrolling


<details>
<summary>'화성땅 공동구매' 미니프로젝트</summary>

- 화성땅을 공동구매하려는 사람들의 구매 명단을 작성한다. 이름, 주소, 원하는 평수를 선택할 수 있다.

- 들어가기 전

  - Ajax와 jQuery의 조합에 대한 Create, Read를 익힌다.
  
  - Flask를 통해서 개발 순서를 머릿속으로 익히고 배운다.
  
    - 클라이언트와 서버가 잘 연결되어 있는지 확인하기
    
    - 서버 만들기
    
    - 클라이언트 만들기
    
    - 완성 확인하기
    
  - POST, GET 연습을 통해 코드를 익힌다.
  
    - 데이터를 받아서 보내주는 연습과 Json형식으로 GET 리턴하는 연습을 익힌다.
    
  - mongo DB Atlas의 사용법에 대해 간단히 익힌다.
  
  </br>  
  <details>
  <summary>만들 API</summary>
  
    - Create : 구매자 이름, 주소, 평수 데이터를 받는다.
    
    - Read : 구매자의 모든 데이터를 불러온다.
  
  </details>
  
  <details>
  <summary>index.html</summary>
  	</br>
	
	```html
	<script>
	$(document).ready(function () {
	    show_order();
	});

	function show_order() {
	    $.ajax({
		type: 'GET',
		url: '/mars',
		data: {},
		success: function (response) {
		    let rows = response['orders']

		    for (let i =0; i < rows.length; i++) {
			let name = rows[i]['name']
			let address = rows[i]['address']
			let size = rows[i]['size']

			let temp_html = `<tr>
					    <td>${name}</td>
					    <td>${address}</td>
					    <td>${size}</td>
					</tr>`

			$('#order-box').append(temp_html)
		    }
		}
	    });
	}

	function save_order() {
	    // jQuery로 받아서
	    let name = $('#name').val()
	    let address = $('#address').val()
	    let size = $('#size').val()

	    // 데이터를 보낸다.
	    $.ajax({
		type: 'POST',
		url: '/mars',
		data: { name_give:name, address_give:address, size_give:size },
		success: function (response) {
		    alert(response['msg'])
		    window.location.reload()
		}
	    });
	}
	</script>
	```
  
  </details>


  <details>
  <summary>app.py</summary>
  	</br>
	
	```python
	from flask import Flask, render_template, request, jsonify
	from pymongo import MongoClient
	import certifi

	ca = certifi.where()

	# mongo db Atlas
	client = MongoClient('', tlsCAFile=ca)
	db = client.sparta

	app = Flask(__name__)

	@app.route('/')
	def home():
	    return render_template('index.html')

	# 주문 저장하기
	@app.route("/mars", methods=["POST"])
	def web_mars_post():
	    name_receive = request.form['name_give']
	    address_receive = request.form['address_give']
	    size_receive = request.form['size_give']

	    doc = {
		'name':name_receive,
		'address':address_receive,
		'size':size_receive
	    }

	    db.mars.insert_one(doc)

	    return jsonify({'msg': '주문 완료!'})

	# 주문 보여주기
	@app.route("/mars", methods=["GET"])
	def web_mars_get():
	    order_list = list(db.mars.find({}, {'_id':False}))
	    return jsonify({'orders':order_list})

	if __name__ == '__main__':
	    app.run('0.0.0.0', port=5000, debug=True)
	```

  </details>
  
  <details>
  <summary>홈페이지</summary>
  </br>
  
	![스크린샷 2022-10-22 13 58 58](https://user-images.githubusercontent.com/102138834/197327673-a1800ed4-1619-4612-8633-51280c03ad1a.png)
  
  </details>
</details>


<details>
<summary>'스파르타피디아' 미니프로젝트</summary>

- 영화 링크를 입력하면 meta태그를 스크래핑해서 나만의 영화 리뷰 페이지를 만든다.

- 들어가기 전

  - Ajax와 jQuery의 조합에 대한 복습 반복 연습.
  
  - Flask를 통해서 개발 순서 반복 연습.
    
  - CR 반복 연습.
  
    - 데이터를 받아서 보내주는 연습과 Json형식으로 GET 리턴하는 연습을 익힌다.
    
  - .repeat 에 대한 사용
  
  - mongo DB Atlas의 사용법에 대해 간단히 익힌다.
  
  </br>  
  <details>
  <summary>만들 API</summary>
  
    - Create : meta태그 스크래핑 된 데이터들을 POST.
    
    - Read : 모든 포스팅 정보를 GET.
  
  </details>
  
  <details>
  <summary>index.html</summary>
	</br>

	```html
	<script>
	$(document).ready(function () {
	    listing();
	});

	function listing() {
	    $.ajax({
		type: 'GET',
		url: '/movie',
		data: {},
		success: function (response) {
		    let rows = response['movies']

		    for (let i = 0; i < rows.length; i++) {
			let title = rows[i]['title']
			let comment = rows[i]['comment']
			let desc = rows[i]['desc']
			let star = rows[i]['star']
			let image = rows[i]['image']

			let star_image = '⭐️'.repeat(star)

			let temp_html = `<div class="col">
					    <div class="card h-100">
						<img src="${image}"
						    class="card-img-top">
						<div class="card-body">
						    <h5 class="card-title">${title}</h5>
						    <p class="card-text">${desc}</p>
						    <p>${star_image}</p>
						    <p class="mycomment">${comment}</p>
						</div>
					    </div>
					</div>`
			$('#cards-box').append(temp_html)
		    }
		}
	    })
	}

	function posting() {
	    let url = $('#url').val()
	    let star = $('#star').val()
	    let comment = $('#comment').val()

	    $.ajax({
		type: 'POST',
		url: '/movie',
		data: { url_give:url, star_give:star, comment_give:comment },
		success: function (response) {
		    alert(response['msg'])
		    window.location.reload()
		}
	    });
	}

	function open_box() {
	    $('#post-box').show()
	}
	function close_box() {
	    $('#post-box').hide()
	}
	</script>
	```
  
  </details>
  
  
  <details>
  <summary>app.py</summary>
	</br>

	```python
	from flask import Flask, render_template, request, jsonify
	from bs4 import BeautifulSoup
	import requests
	from bs4 import BeautifulSoup
	from pymongo import MongoClient
	import certifi

	ca = certifi.where()

	# mongo db Atlas
	client = MongoClient('', tlsCAFile=ca)
	db = client.sparta

	app = Flask(__name__)

	@app.route('/')
	def home():
	    return render_template('index.html')

	# 포스팅 기록하기
	@app.route("/movie", methods=["POST"])
	def movie_post():
	    url_receive = request.form['url_give']
	    star_receive = request.form['star_give']
	    comment_receive = request.form['comment_give']

	    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
	    data = requests.get(url_receive,headers=headers)

	    soup = BeautifulSoup(data.text, 'html.parser')

	    title = soup.select_one('meta[property="og:title"]')['content']
	    image = soup.select_one('meta[property="og:image"]')['content']
	    desc = soup.select_one('meta[property="og:description"]')['content']

	    doc = {
		'title':title,
		'image':image,
		'desc':desc,
		'star':star_receive,
		'comment':comment_receive
	    }
	    db.movies.insert_one(doc)

	    return jsonify({'msg':'포스팅 완료!'})

	# 포스팅 불러오기
	@app.route("/movie", methods=["GET"])
	def movie_get():
	    movie_list = list(db.movies.find({}, {'_id':False}))
	    return jsonify({'movies':movie_list})

	if __name__ == '__main__':
	    app.run('0.0.0.0', port=5000, debug=True)
	```
  
  </details>
  
  <details>
  <summary>홈페이지</summary>
	</br>
  
	![스크린샷 2022-10-22 15 04 37](https://user-images.githubusercontent.com/102138834/197328089-38e32526-7faa-42c9-b2fa-84c485c18705.png)

  
  </details>

</details>


<details>
<summary>'팬명록' 미니프로젝트</summary>

- 좋아하는 가수의 단순 응원댓글 페이지

- 들어가기 전

  - Ajax와 jQuery의 조합에 대한 복습 반복 연습.
  
  - Flask를 통해서 개발 순서 반복 연습.
    
  - CR 반복 연습.
  
    - 데이터를 받아서 보내주는 연습과 Json형식으로 GET 리턴하는 연습을 익힌다.
    
  - mongo DB Atlas의 사용법에 대해 간단히 익힌다.
  
  </br>  
  <details>
  <summary>만들 API</summary>
  
    - Create : mongoDB Atlas에 데이터들을 POST.
    
    - Read : 모든 응원 댓글 정보를 GET.
  
  </details>
  
  <details>
  <summary>index.html</summary>
	</br>

	```html
	<script>
	$(document).ready(function(){
	    set_temp()
	    show_comment()
	});

	// 온도 API 불러와서 띄워주기
	function set_temp(){
	    $.ajax({
		type: "GET",
		url: "http://spartacodingclub.shop/sparta_api/weather/seoul",
		data: {},
		success: function (response) {
		    $('#temp').text(response['temp'])
		}
	    })
	}

	// 댓글 저장하기
	function save_comment() {
	    let name = $('#name').val()
	    let comment = $('#comment').val()

	    $.ajax({
		type: "POST",
		url: "/fanboard",
		data: {'name_give':name, 'comment_give':comment},
		success: function (response) {
		    alert(response["msg"])
		    window.location.reload()
		}
	    });
	}

	// 전체 댓글 보여주기
	function show_comment() {
	    $('#comment-list').empty()
	    $.ajax({
		type: "GET",
		url: "/fanboard",
		data: {},
		success: function (response) {
		    let rows = response['comments']
		    for (let i = 0; i < rows.length; i++) {
			let name = rows[i]['name']
			let comment = rows[i]['comment']

			let temp_html = `<div class="card">
					    <div class="card-body">
						<blockquote class="blockquote mb-0">
						    <p>${comment}</p>
						    <footer class="blockquote-footer">${name}</footer>
						</blockquote>
					    </div>
					</div>`
			$('#comment-list').append(temp_html)
		    }
		}
	    });
	}
	</script>
	```
  </details>
  
  <details>
  <summary>app.py</summary>
	</br>
	
	```python
	from flask import Flask, render_template, request, jsonify
	from pymongo import MongoClient
	import certifi

	ca = certifi.where()

	# mongo db Atlas
	client = MongoClient('', tlsCAFile=ca)
	db = client.sparta

	app = Flask(__name__)

	@app.route('/')
	def home():
	    return render_template('index.html')

	# 댓글 저장하기
	@app.route("/fanboard", methods=["POST"])
	def homework_post():
	    name_receive = request.form["name_give"]
	    comment_receive = request.form["comment_give"]

	    doc = {
		'name': name_receive,
		'comment': comment_receive
	    }

	    db.fanboard.insert_one(doc)
	    return jsonify({'msg':'응원완료!'})

	# 전체 댓글 보여주기
	@app.route("/fanboard", methods=["GET"])
	def homework_get():
	    comment_list = list(db.fanboard.find({},{'_id':False}))
	    return jsonify({'comments':comment_list})


	if __name__ == '__main__':
	    app.run('0.0.0.0', port=5000, debug=True)
	```
  
  </details>
  
  <details>
  <summary>홈페이지</summary>
	</br>

	![스크린샷 2022-10-22 15 33 48](https://user-images.githubusercontent.com/102138834/197331684-14049590-0cba-4a67-b2fd-968b124b1d71.png)
  
  </details>

</details>

<details>
<summary>'To do list' 미니프로젝트</summary>

- 간단한 To Do List 페이지 만들기

- 들어가기 전

  - Ajax와 jQuery의 조합에 대한 복습 반복 연습.
  
  - Flask를 통해서 개발 순서 반복 연습.
    
  - CRU 반복 연습.
  
    - 데이터를 받아서 보내주는 연습과 Json형식으로 GET 리턴하는 연습을 익힌다.
    
  - mongo DB Atlas의 사용법에 대해 간단히 익힌다.
  
  </br>  
  <details>
  <summary>만들 API</summary>
  
    - Create : mongoDB Atlas에 To do 데이터들을 POST. (리스트 기록하기)
    
    - Read : 모든 To Do List를 GET. (리스트 띄워주기)
    
    - Update : To Do List에 대한 완료처리 (리스트 완료처리)
  
  </details>

  <details>
  <summary>index.html</summary>
	</br>

	```html
	<script>
	$(document).ready(function () {
	    show_todo();
	});

	// to do list 보여주기
	function show_todo(){
	    $.ajax({
		type: "GET",
		url: "/todo",
		data: {},
		success: function (response) {
		    let rows = response['todos']

		    for (let i = 0; i < rows.length; i++) {
			let todo = rows[i]['todo']
			let num = rows[i]['num']
			let done = rows[i]['done']

			let temp_html = ``
			if (done == 0) {
			    temp_html = `<li>
					    <h2>✅ ${todo}</h2>
					    <button onclick="done_todo(${num})" type="button" class="btn btn-outline-primary">완료!</button>
					</li>`
			} else {
			    temp_html = `<li>
					    <h2 class="done">✅ ${todo}</h2>
					</li>`
			}
			$('#todo-list').append(temp_html)
		    }
		}
	    });
	}

	// to do list 기록하기
	function save_todo(){
	    let todo = $('#todo').val()

	    $.ajax({
		type: "POST",
		url: "/todo",
		data: {todo_give:todo},
		success: function (response) {
		    alert(response["msg"])
		    window.location.reload()
		}
	    });
	}

	// 완료 된 to do list 체크하기
	function done_todo(num){
	    $.ajax({
		type: "POST",
		url: "/todo/done",
		data: {num_give:num},
		success: function (response) {
		    alert(response["msg"])
		    window.location.reload()
		}
	    });
	}
	</script>
	```
  
  </details>

  <details>
  <summary>app.py</summary>
	</br>

	```python
	from flask import Flask, render_template, request, jsonify
	from pymongo import MongoClient
	import certifi

	ca = certifi.where()

	# mongo db Atlas
	client = MongoClient('', tlsCAFile=ca)
	db = client.sparta

	app = Flask(__name__)

	@app.route('/')
	def home():
	    return render_template('index.html')

	# to do list 기록하기
	@app.route("/todo", methods=["POST"])
	def todo_post():
	    todo_receive = request.form['todo_give']

	    # todo_list에 모든 데이터를 받은다음에
	    todo_list = list(db.todo.find({}, {'_id':False}))
	    # 받은 길이의 순서대로 +1을 해서 num을 매겨준다.
	    count = len(todo_list) + 1

	    doc = {
		'num' : count,
		'todo' : todo_receive,
		'done' : 0
	    }

	    db.todo.insert_one(doc)

	    return jsonify({'msg': 'to do list 등록 완료!'})

	# 완료 to do list 체크하기
	@app.route("/todo/done", methods=["POST"])
	def todo_done():
	    num_receive = request.form['num_give']
	    db.todo.update_one({'num': int(num_receive)}, {'$set': {'done':1}})
	    return jsonify({'msg': 'to do 완료!'})



	# to do list 띄워주기
	@app.route("/todo", methods=["GET"])
	def todo_get():
	    todo_list = list(db.todo.find({}, {'_id':False}))
	    return jsonify({'todos':todo_list})

	if __name__ == '__main__':
	    app.run('0.0.0.0', port=5000, debug=True)
	```
  
  </details>
  
  <details>
  <summary>홈페이지</summary>
	</br>

	![스크린샷 2022-10-22 16 09 46](https://user-images.githubusercontent.com/102138834/197331950-29598b30-82a5-4cbe-8d7d-d15c18c74f28.png)

	![스크린샷 2022-10-22 16 20 47](https://user-images.githubusercontent.com/102138834/197331956-ecb1a04b-f7c0-4ec9-83ec-9aa7d9873284.png)

  
  </details>

</details>


</br>
</br>
</br>

<details>
<summary>웹개발 종합반 - 이범규 튜터님</summary>
</br>

![image](https://user-images.githubusercontent.com/102138834/197332515-29e3d491-d1e3-4610-aea4-d16fc64cc6e9.png)

</br>

</details>
