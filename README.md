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
  
</details>
