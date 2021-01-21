---
title: "2020년 7급 전산직 데이터베이스 풀이"
strapline: "데이터베이스 풀이"
description: "2020년 7급 전산직 데이터베이스 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "7Level_database"
tag:
  - "7급"
  - "데이터베이스"
  - "7급공무원"
toc: true
last_modified_at: 2021-01-20
comments: true
---

# 2020년 7급 전산직 데이터베이스 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 

1. 관계 데이터 모델의 키와 제약 조건에 대한 설명으로 옳은 것만을 모두 고르면?

![2020_7L_1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_1.jpg)

**답 : ③ **

ㄱ. R(<u>A, B</u>, C) 릴레이션에서 기본키가 복합키 (A, B)이고 B가 외래키라면, 참조 무결성에 의해 B는 ~~널값을 가질 수 있다.~~

 ==> 기본키는 절대 널값을 가질 수 없다.

ㄹ. 대체키와 외래키는 유일성과 최소성을 ~~모두 만족해야 한다.~~

 ==> 대체키는 유일성과 최소성 모두 만족

 ==> 외래키는 **참조되는 테이블**에서는 **기본키**로서 유일성과 최소성을 만족.

​        하지만 **참조하는 테이블**에서는 유일성이 만족하지 않을 수 있다.

유일성 : 하나의 키 값으로 하나의 튜플을 유일하게 식별할 수 있어야 하는 것.

최소성 : 키를 구성하는 속성 하나를 제거하면 유일하게 식별할 수 없도록 꼭 필요한 최소의 속성으로 구성되어야 함.

- 슈퍼키, 후보키, 기본키, 대체키, 외래키

| 구분   | 유일성 | 최소성 | Remark                                                       |
| ------ | ------ | ------ | ------------------------------------------------------------ |
| 슈퍼키 | O      | X      | 유일성만 만족하면 슈퍼키가 될 수 있다.                       |
| 후보키 | O      | O      | 유일성과 최소성을 모두 만족<BR/>기본키 + 대체키              |
| 기본키 | O      | O      | 후보키 중 하나를 선택.                                       |
| 대체키 | O      | O      | 후보키 중 기본키를 제외한 나머지 키                          |
| 외래키 | -      | -      | 다른 테이블의 데이터를 참조할 때, 다른 테이블의 기본키를 참조하는 테이블의 외래키로 삼는다. |





---

## 2. 

2. 

![2020_7L_2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_2.jpg)

**답 : **

①

②

③

④



---

## 3. 

3. 

![2020_7L_3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_3.jpg)

**답 : **

①

②

③

④



---

## 4. 

4. 

![2020_7L_4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_4.jpg)

**답 : ④**

①

②

③

④



---

## 5. 

5. 

![2020_7L_5](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_5.jpg)

**답 : **

①

②

③

④



---

## 6. 

6. 

![2020_7L_6](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_6.jpg)

**답 : **

①

②

③

④



## 7. 

7. 

![2020_7L_7](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_7.jpg)

**답 : **

①

②

③

④



---

## 8. 

8. 

![2020_7L_8](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_8.jpg)

**답 : **

①

②

③

④



---

## 9. 

9. 

![2020_7L_9](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_9.jpg)

**답 : ①**

①

②

③

④



---

## 10. 

10. 

![2020_7L_10](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_10.jpg)

**답 : **

①

②

③

④



---

## 11. 

11. 

![2020_7L_11](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_11.jpg)

**답 : **

①

②

③

④



---

## 12. 

12. 

![2020_7L_12](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_12.jpg)

**답 : **

①

②

③

④



---

## 13. 

13. 

![2020_7L_13](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_13.jpg)

**답 : **

①

②

③

④



---

## 14. 

14. 

![2020_7L_14](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_14.jpg)

**답 : **

①

②

③

④



---

## 15. 

15. 

![2020_7L_15](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_15.jpg)

**답 : **

①

②

③

④



---

## 16. 

16. 

![2020_7L_16](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_16.jpg)

**답 : **

①

②

③

④



---

## 17. 

17. 

![2020_7L_17](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_17.jpg)

**답 : **

①

②

③

④



---

## 18. 

18. 

![2020_7L_18](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_18.jpg)

**답 : **

①

②

③

④



---

## 19. 

19. 

![2020_7L_19](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_19.jpg)

**답 : **

①

②

③

④



---

## 20. 

20. 

![2020_7L_20](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_20.jpg)

**답 : **

①

②

③

④