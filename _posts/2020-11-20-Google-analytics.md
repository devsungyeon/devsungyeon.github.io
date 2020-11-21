---
title: "[구글 애널리틱스] 추적 ID UA- 코드 만들기 GA4"
strapline: "Google Analytics"
description: "Google Analytics 추적 ID 만들기"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "Github Blog"
tag:
  - "Github Blog"
  - "Google Analytics"
toc: true
last_modified_at: 2020-11-20
comments: true
---



# 추적 코드(ID) UA-xxxxxxxx-x 만들기

Google Analytics 버전 4(GA4)가 출시되었다.

웹, iOS Android 등에서 접속되는 모든 부분을 분석 용으로 사용이 가능하다.



![image-20201121104904273](/assets/images/image-20201121104904273.png)



GA4가 출시되며, 여러 추적을 단일 속성으로 통합하여 기능을 제공하지만, **추적ID(Tracking ID)**가 **측정ID**로 바뀌며 **G-xxxxxxxxxx(측정 ID)**로 변경되었으며 **UA-xxxxxxx-x(추적 ID)** 코드를 찾기가 쉽지 않은 어려움을 겪었다.

아래는 **Google Analytics 사용방법**과 **측정 ID**와 **추적 ID(UA- 로 시작하는 ..)**를 만드는 방법에 대해 설명하였다.

## 1 Google Analytics 시작하기

필자는 크롬을 사용하였고, Google 계정에 로그인한 상태이다.

![image-20201121105311252](/assets/images/image-20201121105311252.png)

구글에 **google analytics**을 검색하고, **Google Analytics** 클릭.

![image-20201121105625675](/assets/images/image-20201121105625675.png)

**측정 시작** 클릭

![image-20201121105800090](/assets/images/image-20201121105800090.png)

**계정 이름(필수)** 입력 후, **다음** 클릭

![image-20201121105911544](/assets/images/image-20201121105911544.png)

**속성 이름** 입력 (선택사항 : 시간대 및 통화 변경)



### ### UA- 추적 코드 생성! ###

고급 옵션 보기 클릭

![image-20201121110155673](/assets/images/image-20201121110155673.png)

**유니버설 애널리틱스 속성 만들기** 클릭

![image-20201121110305827](/assets/images/image-20201121110305827.png)

웹사이트 URL에 __.github.io 또는 주소 URL 입력.

![image-20201121110421120](/assets/images/image-20201121110421120.png)

**Google 애널리틱스 4 속성과 유니버설 애널리틱스 속성 둘 다 만들기** 클릭 후 다음.

![image-20201121110517760](/assets/images/image-20201121110517760.png)

비지니스 정보는 상황에 맞게 선택 후 **만들기** 클릭

![image-20201121110815149](/assets/images/image-20201121110815149.png)

**서비스 약관 계약** 동의 후 **동의함** 클릭.

![image-20201121110858116](/assets/images/image-20201121110858116.png)

완료 후 **측정 ID(G-)** 를 확인할 수 있다.



## 2 측정 ID G- 찾기

관리 항목에서도 **측정 ID**를 찾을 수 있다.

![image-20201121111144281](/assets/images/image-20201121111144281.png)

좌측 상단에 애널리틱스 옆 **모든 계정**을 클릭

![image-20201121111239839](/assets/images/image-20201121111239839.png)

**test-GA4(GA4항목)** 클릭

![image-20201121111611179](/assets/images/image-20201121111611179.png)

좌측 하단 **>** 클릭

![image-20201121111646640](/assets/images/image-20201121111646640.png)

**관리** 클릭.

![image-20201121111912878](/assets/images/image-20201121111912878.png)

**데이터 스트림** 클릭

![image-20201121111936959](/assets/images/image-20201121111936959.png)

본인이 만든 **스트림** 클릭

![image-20201121111958660](/assets/images/image-20201121111958660.png)

**측정 ID(G-)** 를 확인할 수 있다.



## 3 추적 ID(Tracking ID) UA- 찾기

![image-20201121111144281](/assets/images/image-20201121111144281.png)

좌측 상단에 애널리틱스 옆 **모든 계정**을 클릭

![image-20201121111239839](/assets/images/image-20201121111239839.png)

UA- 항목에서 바로 **추적ID(Tracking ID)인 UA-코드**를 확인할 수 있다.

![image-20201121111333845](/assets/images/image-20201121111333845.png)

혹은 **UA 속성**에서 **속성 보기**로 들어가 **열기**를 클릭 후,

**관리**에서도 확인할 수 있다. 

![image-20201121111611179](/assets/images/image-20201121111611179.png)

좌측 하단 **>** 클릭

![image-20201121111646640](/assets/images/image-20201121111646640.png)

**관리** 클릭.

![image-20201121111717261](C:\Users\LSY\AppData\Roaming\Typora\typora-user-images\image-20201121111717261.png)

가운데 속성에서 **추적ID(UA-)** 를 확인할 수 있다.

혹은 **추적 정보** 탭을 클릭하면 아래와 같은 **추적 코드**에 들어가서도 확인이 가능하다.

![image-20201121112715341](/assets/images/image-20201121112715341.png)



궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"