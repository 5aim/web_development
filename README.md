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


##  2주차
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
      $('#names-q1').empty()
      $.ajax({
          type: "GET",
          url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
          data: {},
          success: function (response) {
              let rows = response['RealtimeCityAir']['row']

              for (let i = 0; i < rows.length; i++) {
                  let gu_name = rows[i]['MSRSTE_NM']
                  let gu_mise = rows[i]['IDEX_MVL']

                  let temp_html = ``
                  if (gu_mise > 70) {
                      temp_html = `<li class="bad">${gu_name} : ${gu_mise}</li>`
                  } else {
                      temp_html = `<li>${gu_name} : ${gu_mise}</li>`
                  }
                  $('#names-q1').append(temp_html)
              }
          }
      })
    }
  - Ajax + jQuery 조합을 연습 - 서울시 따릉이 API를 활용해 남은 자전거 갯수가 낮은 곳을 구분해주기
    </br>
    
    ```javascript
      function q1() {
      $('#names-q1').empty()
      $.ajax({
          type: "GET",
          url: "http://spartacodingclub.shop/sparta_api/seoulbike",
          data: {},
          success: function (response) {
              let rows = response['getStationList']['row']

              for (let i = 0; i < rows.length; i++) {
                  let name = rows[i]['stationName']
                  let rack = rows[i]['rackTotCnt']
                  let bike = rows[i]['parkingBikeTotCnt']

                  let temp_html = ``
                  if (bike < 5) {
                      temp_html = `<tr class="urgent">
                                      <td>${name}</td>
                                      <td>${rack}</td>
                                      <td>${bike}</td>
                                  </tr>`
                  } else {
                      temp_html = `
                                  <tr>
                                      <td>${name}</td>
                                      <td>${rack}</td>
                                      <td>${bike}</td>
                                  </tr>`
                  }

                  $('#names-q1').append(temp_html)
              }
          }
      })
    }
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
