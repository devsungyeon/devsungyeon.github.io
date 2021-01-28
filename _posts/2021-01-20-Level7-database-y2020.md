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



## 1. 관계 데이터 모델의 키와 제약...

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

## 2. 릴레이션 스키마의 표현은...

2. 릴레이션 스키마의 표현은 릴레이션명(속성명1:도메인1, 속성명2:도메인2, ..., 속성명n:도메인n)이다. 이 표현을 따르는 릴레이션 스키마 A(a:int, x:int, c:int)와 B(b:int, x:int, d:int)에 대한 관계대수식 ??와 동등한 관계대수식은? 

![2020_7L_2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_2.jpg)

**답 : ④**

a>10의 비교연산은 A 테이블에만 속한 속성으로 비교를 하므로, 우선 실행하여 A릴레이션의 튜플의 수를 줄일 수 있다.



---

## 3. 스키마가 사원(<u>사원번호</u>...

3. 스키마가 사원(<u>사원번호</u>, 직급, 보너스)인 사원 테이블의 인스턴스가 <보기 1>과 같을 때, <보기 2>의 ㄱ, ㄴ에 들어갈 말로 옳게 짝 지은 것은?
		

![2020_7L_3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_3.jpg)

**답 : ③**

ㄱ.
사원번호 --> 직급
직급 --> 보너스

따라서, 이행적 함수 종속을 가진다.

ㄴ.
1 항상 도메인. 도메인은 원자값
2 부분 함수 종속 제거
3 이행적 함수 종속 제거
4 결정자는 항상 후보키
5 다치 종속 제거
6 조인 종속 제거


---

## 4. 데이터베이스 시스템에서 ...

4. 데이터베이스 시스템에서 데이터 저장 요구량이 빠르게 증가하고 있어서 많은 수의 디스크가 요구된다. 다수의 디스크 드라이브를 사용하여 저장 용량을 늘리고 읽기와 쓰기를 병렬로 수행하기도 하며, 디스크의 고장에 대비하기 위해 RAID(Redundant Arrays of Independent Disks)를 구성하여 활용한다. 이와 같은 RAID에서 1 TByte 디스크 드라이브 6개를 이용하여 RAID를 구성할 때, 구성된 RAID의 저장 용량이 가장 작은 구성 방법은?

![2020_7L_4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_4.jpg)

**답 : ②**

Mirroring이 가장 저장 용량이 작다.

①

②

③

④



---

## 5. 다음은 산업통계 테이블...

5. 다음은 산업통계 테이블이다. 이 테이블을 대상으로 아래 결과를 출력하고자 한다. 이를 위한 SQL 질의문은?

![2020_7L_5](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_5.jpg)

**답 : ③**

SQL 실행결과를 보면,
대분류에서 각 산업 부분 별로 종사수가 가장 많은 튜플을 출력하였다.

①

②

③

④



---

## 6. 버킷 용량 C = 2 인 버킷...

6. 버킷 용량 C = 2 인 버킷들의 주소 공간이 0 ~ (N-1)인 해시에서 키를 K로 하는 해시 함수 h(K) = K mod N 이고, N 값은 5이다. 이때 일련의 K 값들이 3, 5, 7, 9, 11, 13, 18, 14 순서로 삽입된 후 4번 버킷의 값은? (단, 버킷에서의 충돌은 충돌 발생 버킷 주소 i에 대하여 (i+1)mod N을 통해 지정하는 선형탐색 개방 주소법을 이용하여 해결한다)

![2020_7L_6](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_6.jpg)

**답 : ④**

선형탐색 개방 주소법 : 버킷에 데이터가 존재하여 충돌이 발생할 경우, 순차적으로 다음 버킷을 확인하여 빈 버킷을 찾아 데이터를 삽입한다.

①

②

③

④



## 7. 다음 트랜잭션 스케줄의...

7. 다음 트랜잭션 스케줄의 선행그래프(precedence graph)로 옳은 것은? (단, ti는 시간단위, Tj는 트랜잭션, R(A)는 A항목 읽기, W(A)는 A항목 쓰기를 나타낸다)

![2020_7L_7](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_7.jpg)

**답 : ①**

각 트랜잭션에서 다른 트랜잭션으로의 충돌이 발생했는지 확인하여 그래프를 그린다.
충돌
Read - Write 충돌
Write - Read 충돌
Write - Write 충돌

①

②

③

④



---

## 8. 다음 SQL 구문에 대한...

8. 다음 SQL 구문에 대한 설명으로 옳지 않은 것은? 

![2020_7L_8](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_8.jpg)

**답 : ①**

① 명시된 이벤트가 발생할 때마다 DBMS가 자동적으로 수행하는 구문이다.

 ==> Trigger에 대한 설명이다.

- CREATE ASSERTION ; 제약조건에 위배되는 연산을 수행하지 못하게 함.

- CREATE TRIGGER ; 제약조건을 위배하는 경우 동작.





---

## 9. XML Schema와 DTD에 대한...

9. XML Schema와 DTD에 대한 비교 중 옳지 않은 것으로만 묶은 것은?

![2020_7L_9](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_9.jpg)

**답 : ③**

①

②

③

④



---

## 10. 즉시 갱신(Immediate Update...

10. 즉시 갱신(Immediate Update) 전략을 이용하는 회복 시스템에서 <보기 1>의 로그 레코드 형식으로 <보기 2>의 로그 레코드가 형성되어 있다. 복구는 REDO 단계 실행 후 UNDO 단계를 실행한다. 이 시스템에서 복구 절차에 대한 설명으로 옳지 않은 것으로만 묶은 것은?

![2020_7L_10](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_10.jpg)

**답 : ②**

ㄴ. T0의 rollback을 처리하기 위하여 생성된 <T0, C, 300>, <T0, A, 100>은 복구과정에서 UNDO 단계 연산이 된다.



ㅁ. REDO 단계에서는 REDO 연산에 따른 로그 레코드를 로그에 기록한다.



- 지연갱신(Redo)
  - 트랜잭션이 commit될 때까지 갱신 내용을 디스크에 저장하지 않고 **지연.**
  - 트랜잭션 실행 중, 갱신된 내용을 주기억장치의 버퍼에 기록한다.
  - 트랜잭션이 commit하면 버퍼의 내용을 디스크로 저장하도록 OS에 요청.
  - 만약 트랜잭션 수행 도중에 Error 발생, 디스크 갱신을 하지 않았으므로, Undo연산이 필요 없다. **즉, 로그에는 이전값이 필요 없다.**
  - commit이 로그에 정상적으로 적혀있더라도 디스크에 저장되지 않았을 경우에 대비하여 Redo연산만 수행한다.
- 즉시갱신(Undo/Redo)
  - 트랜잭션이 **commit할 때마다** OS에 디스크 저장을 요구
  - 장애가 발생하여 재가동된다면 완료되지 못한 트랜잭션에 대해서 Undo연산으로 값을 되돌려야 한다.
  - 디스크의 반영 사실을 확인할 수 없으므로 Redo연산이 필요하다.
  - 갱신에 관한 **로그 레코드에 이전값, 이후값이 모두 저장.**



---

## 11. 데이터베이스에 대한 ...

11. 데이터베이스에 대한 설명으로 옳지 않은 것은?

![2020_7L_11](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_11.jpg)

**답 : ②**

② 데이터 중복성이란 한 시스템 내에 내용이 같은 데이터가 중복 저장 관리되는 것을 의미하며, 경제성 문제는 발생하나 ~~보안성은 향상된다.~~
 ==> 데이터가 중복되면 필요 용량이 늘어나게 되므로, 경제성 문제가 발생한다.
 ==> 하지만 동일 데이터가 여러 곳에 존재하게 되므로 보안성 문제도 발생한다.




---

## 12. 트랜잭션의 특성에 대한...

12. 트랜잭션의 특성에 대한 설명으로 옳지 않은 것은?

![2020_7L_12](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_12.jpg)

**답 : ④**

④ S은행 계좌에서 K은행 계좌로 이체하는 트랜잭션을 수행하는 동안 다른 트랜잭션이 관여할 수 없으나 ~~참조할 수는 있다.~~
 ==> 트랜잭션 수행 중에는 다른 트랜잭션의 영향을 받지 않는다. ==> Isolation

Atomicity(원자성) ; Commit or Rollback
Consistency(일관성) ; 트랜잭션이 실행을 성공적으로 완료하면 언제나 일관성있는 데이터베이스 상태로 유지.
Isolation(고립성) ; 트랜잭션을 수행 시 다른 트랜잭션의 연산 작업이 끼어들지 않도록 보장.
Durability(영속성, 지속성) ; 성공적으로 수행된 트랜잭션은 영원히 반영.


① ==> Atomicity

② ==> Durability

③ ==> Consistency


---

## 13. 다음의 사원 테이블에 대한...

13. 다음의 사원 테이블에 대한 SQL 질의문의 결과는? (단, 열 A, B는 모두 INTEGER 타입이고, 값이 표시되어 있지 않은 열은 NULL이다.)

![2020_7L_13](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_13.jpg)

**답 : ①**

①

②

③

④



---

## 14. 다음은 트랜잭션의 수행...

14. 다음은 트랜잭션의 수행 중에 장애가 발생할 경우의 회복(Recovery) 기법을 적용하여 트랜잭션의 상태를 복구시키는 사례이다. 로그는 그대로 기록을 유지하면서, 회복 관리자가 정하는 일정한 시간 간격으로 검사점을 생성하는 Checkpoint 회복기법을 적용하는 경우에 트랜잭션들의 상태를 설명한 것으로 옳지 않은 것은?

![2020_7L_14](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_14.jpg)

**답 : ②**

①

②

③

④



---

## 15. 다음은 테이블을 생성하는...

15. 다음은 테이블을 생성하는 SQL 구문이다. 이 테이블에 대한 연산을 설명하는 것으로 옳지 않은 것은?

![2020_7L_15](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_15.jpg)

**답 : ②**

①

②

③

④



---

## 16. 두 트랜잭션 스케줄...

16. 두 트랜잭션 스케줄 s1, s2에 대하여, s1의 비연쇄(Cascadeless) 스케줄 여부와 s2의 s1에 대한 뷰 동치 여부로 옳게 짝지어진 것은? (단, ri, wi, ci는 각각 트랜잭션 Ti의 읽기, 쓰기, 완료 연산을 의미한다)

![2020_7L_16](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_16.jpg)

**답 : ②**

①

②

③

④



---

## 17. 다음 시스템 카탈로그...

17. 다음 시스템 카탈로그(System Catalog)에 대한 설명으로 옳은 것으로만 묶은 것은?

![2020_7L_17](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_17.jpg)

**답 : ③**

①

②

③

④



---

## 18. 다음은 제품 데이터베이스의...

18. 다음은 제품 데이터베이스의 스키마 다이어그램과 인스턴스를 나타낸 것이다. 데이터베이스를 구성하는 이 두 테이블을 대상으로 아래 결과를 출력하고자 한다. 이를 위한 SQL 질의문은?

![2020_7L_18](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_18.jpg)

**답 : ③**

①

②

③

④



---

## 19. 다음 데이터베이스...

19. 다음 데이터베이스 시스템의 질의최적화에 대한 설명으로 옳지 않은 것으로만 묶은 것은?

![2020_7L_19](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_19.jpg)

**답 : ③**

①

②

③

④



---

## 20. 트랜잭션 고립 수준...

20. 트랜잭션 고립 수준 중 REPEATABLE READ 모드에서 발생할 수 있는 문제를 모두 고르면?

![2020_7L_20](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_20.jpg)

**답 : ①**

①

②

③

④
