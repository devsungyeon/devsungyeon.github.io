---
title: "2016년 7급 전산직 데이터베이스 풀이"
strapline: "데이터베이스 풀이"
description: "2016년 7급 전산직 데이터베이스 풀이"
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

# 2016년 7급 전산직 데이터베이스 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 다음은 데이터베이스...

다음은 데이터베이스 안에 있는 어떤 테이블을 보인 것이다. 파일처리 방식과 대비해서 <보기>와 같은 테이블을 이용하는 데이터베이스 방식의 주요 특성으로 옳은 것은?

![2016_7L_1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_1.jpg)

**답 : ④**

- DBS의 자기기술성.



---

## 2. 하나의 데이터베이스...

하나의 데이터베이스 시스탬 내에서 적절한 제어 없이 트랜잭션들을 동시에 실행하였을 경우 여러 문제가 발생할 수 있다. 이를 해결하기 위한 동시성 제어가 올바르게 동작하지 않을 경우 발생할 수 있는 문제점으로 옳지 않은 것은?

![2016_7L_2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_2.jpg)

**답 : ④**

추가로 오손읽기 Dirty Read



---

## 3. 다음 데이터를 순서적으로...

다음 데이터를 순서적으로 삽입하여 B-트리를 구성할 때 루트 노드에 존재하는 키 값은? (단, B-트리의 차수는 3이라고 가정한다.)

![2016_7L_3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_3.jpg)

**답 : ②**





---

## 4. 두 릴레이션 R1(A...

두 릴레이션 R1(A, B, C), R2(B, C, D)를 오른쪽 외부조인(Right Outer Join)을 한 결과에 나타나는 튜플의 수는?

![2016_7L_4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_4.jpg)

**답 : ③**





---

## 5. 다음 두 릴레이션 ...

다음 두 릴레이션 R, S에 대한 조인 결과로 옳지 않은 것은?

![2016_7L_5](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_5.jpg)

**답 : ②**





---

## 6. 도서(도서번호...

도서(<u>도서번호</u>, 도서제목, 출판사명, 발행년도) 테이블에서, 2000년 이후에 10권 이상의 책을 발행한 출판사의 이름을 중복 없이 출력하는 SQL문으로 옳은 것은? (단, 출판사명이 동일한 출판사는 존재하지 않는 것으로 가정한다. 도서번호는 도서 테이블의 기본키이다)

![2016_7L_6](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_6.jpg)

**답 : ④**



## 7. 지연 갱신을 통한...

지연 갱신을 통한 점진적 로깅(incremental logging with deferred updates) 기법을 사용하는 복구 시스템으로 옳은 것은?

![2016_7L_7](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_7.jpg)

**답 : ②**





---

## 8. 데이터베이스에서 동시성...

데이터베이스에서 동시성 제어가 적절하게 이루어지지 않으면서 다음과 같이 두 트랜잭션 T1, T2가 동시에 실행될 때 문제점이 발생할 수 있다. 이 문제점이 발생하지 않을 수 있는 트랜잭션의 격리 수준(isolation level)을 모두 고른 것은?

![2016_7L_8](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_8.jpg)

**답 : ②**



- 무제어 동시공용의 문제점

  - 갱신손실
  - 오손읽기
  - 부정확한 요약문제
  - 반복할 수 없는 읽기 문제

- 독립성 레벨

  - 직렬성 위반 3가지

    - 부정판독
    - 비반복 판독
    - 가상 판독

  - 네가지 종류 트랜잭션 독립성 레벨

    | 독립성 레벨      | 부정판독 | 비반복 판독 | 가상 판독 |
    | ---------------- | -------- | ----------- | --------- |
    | READ UNCOMMITTED | Y        | Y           | Y         |
    | READ COMMITTED   | N        | Y           | Y         |
    | REPEATABLE READ  | N        | N           | Y         |
    | SERIALIABLE      | N        | N           | N         |

    



---

## 9. 다음 ERD(Entity-Relationship Diagram)를...

다음 ERD(Entity-Relationship Diagram)를 구성하는 두 릴레이션 Dept, Emp에 대해 참조무결성 제약조건을 정의하였다고 가정하자. 정의한 참조무결성 제약조건의 영향을 받는 연산들로만 모두 묶은 것은?

![2016_7L_9](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_9.jpg)

**답 : ④**





---

## 10. 데이터베이스는 다양한...

데이터베이스는 다양한 응용을 위해 사용되고 있으며 이를 위해서 새로운 데이터베이스 기술이 등장하였다. 새로운 데이터베이스 기술에 대한 설명으로 옳지 않은 것은?

![2016_7L_10](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_10.jpg)

**답 : ③**

③ ~~공간조인은~~ 주로 지도상의 점, 선, 폴리곤과 이에 대한 속성 데이터를 조인하는 데 사용된다.

==> 속성조인





---

## 11. 데이터 추상화는...

데이터 추상화는 다음 그림과 같이 3단계로 구성된다. 각 단계에 대한 설명으로 옳지 않은 것은?

![2016_7L_11](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_11.jpg)

**답 : ④**

④ 사용자들은 뷰 단계를 통하여 데이터베이스 ~~전반에 걸친 상세 내용~~을 접근한다.

==> 일부에 대한 접근.



---

## 12. 정규화에 대한...

정규화에 대한 설명으로 옳지 않은 것은?

![2016_7L_12](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_12.jpg)

**답 : ①**

① 정규화의 목적은 각 릴레이션에 분산된 종속성을 ~~하나의 릴레이션으로 통합~~하는 것이다.

==> 분리.

통합 ==> 역정규화.





---

## 13. 두 트랜잭션 T1, T2가...

두 트랜잭션 T1, T2가 다음과 같은 트랜잭션 스케줄로 실행될 때, 발생되는 충돌(conflict)로 옳은 것은? (단, R은 읽기연산, W는 쓰기연산에 해당하며, R1(A)는 "트랜잭션 T1이 A를 읽는다", W2(B)는 "트랜잭션 T2가 B에 값을 쓴다"는 의미이다)

![2016_7L_13](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_13.jpg)

**답 : ②**

[read-write conflict](https://en.wikipedia.org/wiki/Read%E2%80%93write_conflict)

[write-read conflict](https://en.wikipedia.org/wiki/Write%E2%80%93read_conflict)

[write-write conflict](https://en.wikipedia.org/wiki/Write%E2%80%93write_conflict)





---

## 14. 다음과 같이 사원과 ...

다음과 같이 사원과 부서 테이블을 이용하는 회사가 직원의 급여를 인상할 때 오류를 방지하기 위해 <설명>과 같은 SQL99 표준에 따른 트리거를 정의하여 사용 중이다. 이를 같은 조건에서 직원들의 급여 인상을 위한 <보기> 의 질의를 수행하였다. 급여 인상의 결과를 보기 위해 질의 "SELECT 사번, 이름, 급여 FROM 사원"을 수행한 결과로 옳은 것은?

![2016_7L_14](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_14.jpg)

**답 : ③**





---

## 15. 검사점(checkpoint) 회복 기법과...

검사점(checkpoint) 회복 기법과 관련하여 트랜잭션의 실행 상태가 다음 그림과 같다고 하자. 데이터 A, B, C, D의 초깃값이 각각 100, 200, 100, 200일 때 T1은 A에 100을 더하고, T2는 B에서 100을 빼고, T3 은 C에 100을 더하고, T4는 D에서 100을 뺀다고 하자. 회복이 수행된 후 A, B, C, D의 값으로 옳은 것은?

![2016_7L_15](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_15.jpg)

**답 : ③**





---

## 16. 고객들 중 꽃을 한번도 ...

고객들 중 꽃을 한번도 구매하지 않은 고객의 고객ID, 이름, 주소를 다음 데이터베이스로부터 검색하려 할 때 옳은 것은? (단, PK는 PRIMARY KEY, FD는 FOREIGN KEY를 의미함)

![2016_7L_16](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_16.jpg)

**답 : ①**

①

②

③

④



---

## 17. 트랜잭션의 교착상태 ...

트랜잭션의 교착상태 방지(deadlock prevention) 프로토콜 중에서 <보기>의 설명을 만족하는 프로토콜은?

![2016_7L_17](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_17.jpg)

**답 : ②**

- 교착 상태 방지 프로토콜
  - 실행 전에 필요한 데이터의 로크
  - 트랜잭션 스케줄링
  - 요구 거절법
  - 타임스탬프를 이용한 교착 상태 방지 기법
    - wait-die 기법
      - 트랜잭션 Ti가 이미 Tj가 로크한 데이터 아이템을 요청할 때 만일 Ti의 시간 스탬프가 Tj의 것보다 작은 경우(즉, Ti가 고참인 경우)에는 Ti는 기다리고 그렇지 않으면 Ti는 복귀(즉, die)하고 다시 시작.
      - 신참(시간 스탬프가 긴) 트랜잭션에게 데이터 아이템 사용 우선권을 부여하는 기법
    - wound-wait 기법
      - 트랜잭션 Ti가 이미 트랜잭션 Tj가 로크한 데이터 아이템을 요청할 때 Ti의 시간 스탬프가 Tj의 것보다 클 경우(즉, Tj가 고참인 경우)에는 기다리고, 그렇지 않으면 Tj는 복귀해서(즉, Ti는 Tj를 상처입힌다) 다시시작.
      - 고참(시간 스탬프가 짧은) 트랜잭션에게 데이터 아이템 사용 우선권을 부여하는 기법.
  - 타임스탬프를 필요로 하지 않는 방법
    - no waiting
      - 트랜잭션이 로크를 획득할 수 없을 경우에는 교착상태가 실제로 발생할 것인지 발생하지 않을 것인지 확인하지 않고 그 트랜잭션을 즉시 철회시키고 일정시간이 경과되면 재시작시킴.
    - cautious waiting
      - Ti가 Tj에서 로크를 건 항목 X가 필요한 경우, Tj가 블로킹된 상태가 아니면(로크가 걸린 다른 항목을 기다리는 상태가 아니면) Ti가 블로킹이 되어 대기를 시작하고, Tj가 블로킹이 된 상태이면 Ti는 철회(abort)됨.



---

## 18. 릴레이션 R(A, B, C, D, E)에...

릴레이션 R(A, B, C, D, E)에 대한 종속성의 집합 F = {A→C, AC→D, D→C, D→E}가 주어졌을 때, 종속성 집합 F의 최소 집합(minimal set)으로 옳은 것은?

![2016_7L_18](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_18.jpg)

**답 : ③**





---

## 19. 학과 등록 테이블이 ...

학과 등록 테이블이 다음과 같을 때, 학과 등록 테이블에 대한 설명으로 옳지 않은 것은? (단, 밑줄은 기본키이다)

![2016_7L_19](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_19.jpg)

**답 : ②**

② 제2 정규형을 ~~만족시킨다.~~

==> 1정규형. 부분함수 종속 존재.







---

## 20. 다음은 데이터로부터의...

다음은 데이터로부터의 지식발견(KDD : Knowledge Discovery from Data)을 위한 단계별 과정이다. 빈칸에 들어갈 말로 옳은 것은?

![2016_7L_20](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2016_7L/2016_7L_20.jpg)

**답 : ①**





