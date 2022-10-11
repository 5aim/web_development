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
