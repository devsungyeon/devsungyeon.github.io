---
title: "2017년 7급 전산직 데이터베이스 풀이"
strapline: "데이터베이스 풀이"
description: "2017년 7급 전산직 데이터베이스 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "7Level_database"
tag:
  - "7급"
  - "데이터베이스"
  - "7급공무원"
toc: true
last_modified_at: 2020-12-05
comments: true
---

# 2017년 7급 전산직 데이터베이스 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 데이터베이스 관리...


데이터베이스 관리 시스템(DBMS)의 역할에 대한 설명으로 옳지 않은 것은?


![2017_7L_1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_1.jpg)


**답 : ①**

① ~~데이터 조작어(DML)~~로 스키마의 구조를 기술하여 시스템 카탈로그(혹은 데이터 사전)에 저장한 후 필요할 때 활용된다.


==> DCL







---

## 2. 관계형 데이터...


관계형 데이터베이스에 대한 설명으로 옳지 않은 것만을 모두 고른 것은?


![2017_7L_2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_2.jpg)


**답 : ③**

ㄱ. 기본키 속성이 복합 속성인 경우 그 속성의 일부 요소 속성에서 널(NULL) 값을 가질 수 있다.

==> 기본키는 null 키가 될 수 없다.

ㄴ. 슈퍼키는 후보키가 되기 위한 필요충분조건이다.

- 슈퍼키는 유일성만을 만족.

- 후보키는 유일성과 최소성을 만족.

슈퍼키 > 후보키 > 대체키 > 기본키

ㄷ. 릴레이션 R이 릴레이션 S를 참조하는 경우 R의 외래키가 S의 기본키가 아닌 후보키 중 하나를 참조해야 한다.

==> 참조하는 경우 외래키는 반드시 참조되는 기본키를 참조해야 한다.





---

## 3. 




![2017_7L_3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_3.jpg)


**답 : **

①

②

③

④



---

## 4. 


![2017_7L_4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_4.jpg)


**답 : ④**

①

②

③

④ ==> 기본키 제약조건 위배.



---

## 5. 


![2017_7L_5](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_5.jpg)


**답 : ③**

[인덱싱, 해싱](https://hyolo.tistory.com/58)

- 인덱싱

	- 순서 인덱싱 ; B* 트리 인덱스
		
		- 검색 키가 순서대로 저장

		- 밀집 인덱스 ; 모든 레코드에 대해 인덱스 엔트리(검색 키와 포인터 쌍)를 유지

		- 희소 인덱스 ; 소수의 인덱스 엔트리만 유지.

	- 해시 인덱싱

		- 검색키가 버킷들에 해시 함수를 이용하여 분산 저장.

② [ p/2 ] 내림

④ 전체 학생 수에 영향



---

## 6. 


![2017_7L_6](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_6.jpg)


**답 : **









## 7. 


![2017_7L_7](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_7.jpg)


**답 : ④**

④ 

[db설계 및 개체관계모델 - 확장된 개체-관계 특성](https://m.blog.naver.com/PostView.nhn?blogId=nkind&logNo=110086303571&proxyReferer=https:%2F%2Fwww.google.com%2F)

- Disjoint Overlap

- 분리 disjoint

	- 분리 제약조건에서는 하나의 개체는 단지 하나의 하위 개체 집합에만 속해야 한다. 여러 개의 개체 집합에 속할 수 없다.

- 중첩 overlap 

	- 중첩 일반화에서 동일한 개체가 단일 일반화의 하나 이상의 하위 개체 집합에 속할 수 있다.



---

## 8. 


![2017_7L_8](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_8.jpg)


**답 : ①**

- DBMS의 캐시관리 방식

① no-steal 방식에서는 회복 과정 중 UNDO와 REDO 연산의 수행이 모두 필요하다.

==> undo 불필요.

- 캐시 관리 방식

	- steal / no-steal

		- no-steal ; 지연. 트랜잭션이 완료하기 전까지 트랜잭션의 갱신한 캐쉬 페이지가 디스크에 기록하지 않는 방식

		- steal ; 에잇 -> 즉시. 트랜잭션이 완료되기 전에 갱신된 페이지를 디스크에 기록할 수 있는 방식

	- force / no-force

		- force ; 트랜잭션이 완료될 때 트랜잭션이 갱신한 모든 페이지를 디스크에 반영하는 방식

		- no-force ; 트랜잭션이 완료될 때 강제적으로 갱신된 모든 페이지를 디스크에 반영하지 않는 방식

	- 전형적인 데이터베이스 시스템은 steal/no-force 방식을 사용
		
		- steal ; 모든 갱신된 페이지를 주기적 장치에 저장할 필요가 없으므로 대용량의 저장 장치가 필요 없음

		- no-force ; 갱신된 페이지가 계속 버퍼에 존재하여 I/O 비용을 제거






---

## 9. 


![2017_7L_9](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_9.jpg)


**답 : **

①

②

③

④



---

## 10. 


![2017_7L_10](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_10.jpg)


**답 : **

①

②

③

④



---

## 11. 


![2017_7L_11](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_11.jpg)


**답 : **

①

②

③

④



---

## 12. 


![2017_7L_12](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_12.jpg)


**답 : **

①

②

③

④



---

## 13. 


![2017_7L_13](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_13.jpg)


**답 : **

①

②

③

④



---

## 14. 


![2017_7L_14](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_14.jpg)


**답 : **

①

②

③

④



---

## 15. 


![2017_7L_15](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_15.jpg)


**답 : ①**

①

MMDB ; T-tree 사용. 디스크에 저장된 데이터를 접근하는 방법인 B-tree 계열과는 달리 모든 데이터가 메모리에 존재하도록 하는 Indexing 기술.

디스크 기반 DB ; B-tree 사용



---

## 16. 


![2017_7L_16](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_16.jpg)


**답 : **

①

②

③

④



---

## 17. 


![2017_7L_17](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_17.jpg)


**답 : **

④ 2pl 의 경우 unlock 이후 lock 수행이 불가.


|     | X | S | IS | SIX | IX |
|-----|---|---|----|-----|----|
| X   |   |   |    |     |    |
| S   |   | T | T  |     |    |
| IS  |   | T | T  | T   | T  |
| SIX |   |   | T  |     |    |
| IX  |   |   | T  |     | T  |




---

## 18. 


![2017_7L_18](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_18.jpg)


**답 : **

①

②

③

④



---

## 19. 


![2017_7L_19](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_19.jpg)


**답 : ③**

- ARIE

	- 복구 중 로깅

	- WAL 사용

	- UNDO 중 로깅 ; UNDO를 할 때에도 로깅을 함으로써 회복을 수행하는 도중에 실패하여 회복을 다시 시작할 때에 이미 완료된 UNDO연산은 반복하지 않음.



---

## 20. 


![2017_7L_20](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2017_7L/2017_7L_20.jpg)


**답 : **

①

②

③

④