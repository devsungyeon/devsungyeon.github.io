---
title: "2020년 7급 전산직 소프트웨어공학 풀이"
strapline: "소프트웨어공학 풀이"
description: "2020년 7급 전산직 소프트웨어공학 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "7Level_softwareengdatabase"
tag:
  - "7급"
  - "소프트웨어공학"
  - "7급공무원"
toc: true
last_modified_at: 2021-02-24
comments: true
---

# 2020년 7급 전산직 소프트웨어공학 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 다음 설명에 ...

다음 설명에 해당하는 소프트웨어 개발 프로세서 방법은?


![2020_7L_1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_1.jpg)

**답 : ④**

- SDLC ; 타당성 조사 - 계획 - 사용자 요구파악 - 분석 - 설계 - 구현 - 시험 - 유지보수
  - 소프트웨어 개발 프로세스 모형

| 구분                        | 설명                                                         | 장점                                                         | 단점                                                 |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------- |
| 폭포수                      | 산출물 명확. <br>**문서와 결과물 도출에 중점**               | 가시성이 좋음. 소규모 적합                                   | 신규 프로젝트 부적합. <br>새로운 요구 반영 어려움    |
| 프로토타이핑                | 견본품. <br>신속한 원형화                                    | 폭포수의 전 단계로 올라갈 수 없는 점을 보완.                 | 관리, 통제가 어렵다.                                 |
| 나선형                      | 폭포수, 원형의 장점을 취합. <br>점진적                       | 대규모 시스템 적합                                           | 초기 위험 분석 오류 시, 실패 가능성                  |
| V-모형                      | 분석과 설계는 왼편. 테스팅과 유지보수는 오른편. <br>**작업과 결과의 검증에 초점** | 테스트 단계에서 오류 발견 시 되돌아갈 수 있음                |                                                      |
| 점증적 모형                 | 선형순차 + 프로토타입 결합                                   | 중요,기초 기능을 우선 개발. <br>확장하는 형태. 점증적(추가) & 반복적(보완)<br>신규 프로젝트 적합 | 관리 문제<br>검증 문제<br>계약 문제<br>유지보수 문제 |
| UP(Unified Process) 모형    | UML. 객체 지향 분석 및 설계를 지원하기 위한 Diagram<br>Usecase Diagram<br>점증적 반복<br>가. 개 념 정립(도입, Inception) ; 개략적 파악<br>나. 전개(정련, Elaboration) ; 비전 구체화. 아키텍처 프레임워크 설정<br>다. 구축(Construction) ; 구현 및 설치 준비. 문서를 User에게 인도하기 위해 **준비**<br>라. 전환(전이, Transition) ; **인도**. 테스트, 설치, 다음 반복 단계를 준비 | 사용자 요구 즉시 파악 가능                                   |                                                      |
| 신속한 소프트웨어 개발 모형 | 신속하게 개발하여 새로운 도전과 기회에 반응하기 위함.        | 중첩된 반복적인 프로세스.<br>설계 문서 최소화                |                                                      |


- 신속한 소프트웨어 개발 모형

1) 애자일(agile) 기법

    - 문서화 < 구현 < 시험
        - 문제점
        - 대규모에는 부적합. 중소규모에 적합
        - 시스템 개발에 필요한 시간에 대해 비용을 지불
        - 원리
        

| 원리                   | 설명                                                         |
| ---------------------- | ------------------------------------------------------------ |
| 고객 참여              | 고객은 개발 프로세스 전체에 긴밀하게 참여                    |
| 점증적인 인도          | 점증적으로 인도                                              |
| 사람은 프로세스가 아님 | 규정된 프로세스 없이 자신들의 작업 방식으로 개발. (프로세스보다 사람) |
| 변경을 수용            | 변경들을 수용할 수 있도록 설계                               |
| 단순성의 유지          | 모두 단순성에 초점                                           |



2) XP(eXtreme Programming) 모형 

    - **의사소통, 단순함, 피드백, 용기, 존중. '고객에게 최고의 가치를 가장 빨리'**
        - 경량 방법론
        - 고객의 **참여를 극한 수준까지 유도.**
        - 스토리 카드. ; 고객의 요구 요약. (요구분석서, CRC 카드)
        - **시험 우선 개발** ; 코드보다 시험을 먼저 작성
        - 중요 키워드 ; 점증적, 소규모 릴리즈, 시험개발우선, 짝 프로그래밍 등.
        - XP의 프로세스 ; 계획 - 설계 - 코딩 - 테스팅



3) 스크럼(Scrum)

- 30일마다 동작가능한 제품을 제공하는 **스프린트(Sprint)** 2~4주기 제품 생산
  - 스크럼 ; 매일 이루어지는 스크럼 팀의 회의. 매일 짧은 회의(15분)
  - 스프린트 ; 개발에서 이루어지는 반복



4) TDD 테스트 주도 개발(Test-driven development)

- **테스팅과 코드 개발을 중첩**시키는 개발 방법론.
- JUnit과 같은 자동화된 테스트 프레임워크 필수적.
- **신규** 개발에 가치. (기존x)
- 장점
  - 코드 커버리지 ; 모든 코드의 일부는 하나의 연관된 테스트가 있어야 함. 초기 결함 발견.
  - 회귀 테스팅 ; 테스트 스위트(test suite)가 점증적 개발. 변경이 새로운 버그를 초래하지 않았는지 회귀 테스트 항상 실행
    - 테스트 스위트(test suite) ; 테스트 케이스들을 하나록 묶은 것.
  - 단순화된 디버깅 ; 디버깅 도구 사용 불필요.
  - 시스템 문서화



5) RAD(Rapid Application Development)

- 4세대 언어로부터 진화.
- 매우 짧은 개발 주기. 
- 컴포넌트 기반으로 개발. **재사용이 가능한 컴포넌트의 개발을 중요시.**



6) 컴포넌트 기반 개발(CBD ; Component-based Development)

- 데이터와 그 데이터를 조작하는 연산을 하나로 묶는 클래스화. 재사용



cf) 애자일 UP(Agile Unified Process ; AUP)

- inception, elaboration, contruction, transition을 채택.





---

## 2. 클래스(Class) ...

클래스(Class) 다이어그램에 대한 설명으로 옳지 않은 것은?

![2020_7L_2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_2.jpg)

**답 : ③**

③ 오퍼레이션이나 처리 과정이 수행되는 동안 일어나는 일들을 단계적으로 표현하고자 할 때 사용하는 다이어그램이다.

==> 액티비티 다이어그램에 대한 설명.



- 클래스 다이어그램 ; 시스템의 구조를 나타낼 때 사용. 객체, 클래스, 속성, 오퍼레이션 및 연관관계를 이용하여 시스템이 갖는 정적인 정보들의 관계를 설명.

  - 집합(Aggregation)

    - 구성요소(부분)이 없어도 전체 개념이 존재할 수 있다.
    - 구성요소는 하나 이상의 집합들에 소속될 수 있다.
    - ◇
    - ![uml_aggregation](/assets/images/SwengSummary/uml_aggregation.png)

  - 복합(Composition)

    - 구성요소가 없다면 전체 개념이 존재하지 않음
    - ◆
    - ![uml_composition](/assets/images/SwengSummary/uml_composition.png)

  - 일반화 Generalization

    - 빈 삼각형이 붙은 실선. 구체적. 수직적. Is-a

      

- 순서 다이어그램 Sequence Diagram 순차도

  - 객체들 간의 메시지 교환을 시각화

  - 객체들 사이에 보내지는 메시지의 상호작용을 보여줌.

  - 순서적 = 시간적

    

- 커뮤니케이션 다이어그램 = communication diagram = collaboration diagram.

  - 객체들 사이의 조직=관계을 강조
  - **객체간**의 연결 관계



- 상태 다이어그램 = State diagram = 상태도
  - 단일 객체가 갖는 여러 상태와 상태 사이의 전환을 이용하여 동작을 나타냄
  - Finite state machine 모습을 확장
  - 시작상태 ● 는 반드시 하나만 존재, 
  - 종료상태 ⊙ 는 0개 이상 존재



- 액티비티 다이어그램 = 활동 다이어그램 = 활동도 ; 오퍼레이션이나 처리 과정이 수행되는 동안 일어나는 일들을 단계적으로 표현.
  - 병렬 액티비티.
  - 시스템을 화이트박스로 보고 수행한 기능모델.



- 복합 구조 다이어그램 composite structure diagram

  - 아키텍처 다이어그램
  - 트리구조.
  - 내부구조를 명시적 중첩시켜 표현

  

- 배치 다이어그램 (사용자 환경)

  - sw 와 hw component 사이의 물리적인 관계를 파악하기 위한 diagram



---

## 3. 사용자 인터페이스를...

사용자 인터페이스를 설계할 때 고려 사항이 아닌 것은?



![2020_7L_3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_3.jpg)

**답 : ①**

① 소프트웨어 내부 모듈 사이의 인터페이스를 정의하거나 ~~외부 시스템 사이의 인터페이스를 정의한다.~~

- 사용자 인터페이스 종류
  - 그래픽 사용자 인터페이스 GUI
  - 웹 인터페이스
  - 명령어 인터페이스 CUI
  - 텍스트 사용자 인터페이스
- 인터페이스 설계의 3가지 영역
  - 소프트웨어 모듈간의 인터페이스 설계. PL
  - 소프트웨어와 정보의 다른 비인간 생산자와 소비자(즉, 다른 외부개체) 간의 인터페이스 설계. DC
  - 인간과 컴퓨터간의 인터페이스 설계. SE



---

## 4. 소프트웨어 개발...

소프트웨어 개발 단계에 따른 테스트의 순서는?



![2020_7L_4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_4.jpg)

**답 : ②**





---

## 5. ISO의 소프트웨어 ...

ISO의 소프트웨어 프로세스 평가를 위한 국제 표준인 SPICE에 대한 설명이다. 이에 해당하는 프로세스 범주는?



![2020_7L_5](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_5.jpg)

**답 : ②**

- ISO/IEC 12207
  - 프로세스 중심
  - 기본 생명주기 프로세스 ; 획득, 공급, 개발, 운영, 유지보수
  - 지원 생명주기 프로세스 ; 문서화, 품질보증, 형상관리, 검증, 확인, 문제해결, 합동검토, 감사
  - 조직 생명주기 프로세스 ; 기반구조, 관리, 개선, 훈련
- CMM ; 생산하는 **능력을 정량화**
  - 프로세스 성숙단계 5단계
    - 초기 ; 예측불가
    - 반복 ; 문서화 가능
    - 정의 ; 표준화, 일관된 프로세스
    - 관리 ; 정량적 관리평가, 예층 가능한 프로세스
    - 최적화 ; 개선되는 프로세스
- SPICE(ISO/IEC 15504) ; 최저점을 대표점수로 산정
  - 프레세스 수행능력 - 6단계로 나누어 평가
    - Lv0 : 불완전 ; 실패. 결과물 없음.
    - Lv1 : 수행 ; 목적. 성취는 없음.
    - Lv2 : 관리 ; 문서화 단계.
    - Lv3 : 확립 ; 표준 프로세스.
    - Lv4 : 예측 ; 정량적 이해, 수행 예측
    - Lv5 : 최적화 ; 지속적 프로세스 감시 및 개선. 현재 및 미래 경영목표에 효과적인 적응.
  - 프로세스 영역 
    - 고객공급자 프로세스 ; 발주, 공급자 선정, 고객인수, 요구사항 도출, 공급, 운영 등
    - 엔지니어링 프로세스 ; 요구분석, 설계 및 구현, 통합 및 시험 등.
    - 지원 프로세스 ; 문서화, 형상관리, 품질보증, 검증, 확인, 검토 등.
    - 관리 프로세스 ; 프로젝트관리, 품질관리, 위험관리 등.
    - 조직 프로세스 ; 프로세스 정의, 심사, 개선, 인적자원 관리, 기반구조, 측정, 재사용 등
- CMMi
  - CMM + SPICE
  - 성숙도 단계
    - 실행되지 않음 not performed 0단계
    - 실행됨 performed 1단계
    - 관리됨 managed 2단계
    - 정의됨 defined 3단계
    - 정량적으로 관리됨 quantitatively managed 4단계
    - 최적화됨 optimizing 5단계





| Level                  | Focus                                  | Process Areas                                                |
| ---------------------- | -------------------------------------- | ------------------------------------------------------------ |
| Performed              |                                        |                                                              |
| Managed                | Basic<br>Project<br/>Management        | Requirements management<br/>Project planning<br/>Project monitoring and control<br/>Supplier agreement management<br/>Measurement and analysis<br/>Process and product quality assurance<br/>Configuration management |
| Defined                | Process<br/>standardization            | Requirements development<br/>Technical solution<br/>Product integration<br/>Verification<br/>Validation<br/>Organizational process focus<br/>Organizational process definition<br/>Organizational training<br/>Integrated project management<br/>Integrated supplier management<br/>Risk management<br/>Decision analysis and resolution<br/>Organizational environment for integration<br/>Integrated teaming |
| Quantitatively managed | Quantitative<br/>management            | Organizational process Performance<br/>Quantitative project management |
| Optimizing             | Continuous<br/>process<br/>improvement | Organizational innovation and deployment<br/>Causal analysis and resolution |





---

## 6. 다음은 UML2.0...

다음은 UML2.0 다이어그램에 대한 내용이다. <보기 1>과 <보기 2>를 바르게 연결한 것은?



![2020_7L_6](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_6.jpg)

**답 : ②**

[JI-DUM UML 2.0](http://jidum.com/jidums/view.do?jidumId=961)

- UML 2.0
  - UML의 확장.
  - 객체지향, 컴포넌트 뿐만 아니라 SOA, MDA, 리얼타입, 워크플로우 시스템에 대한 지원 강화.
  - 요구사항 획득으로부터 마지막 테스트까지 모두 지원하는 표기법으로 진화
  - 분석/설계와 실제 구현 간의 차이를 극복.



- **다이아그램 변경 사항**
  - Composite Structure Diagram : **단계화된 구조를** 통해 classifier내 요소간 관계 표현
  - Interaction Overview Diagram : 시퀀스들의 workflow를 보여주기 위해 서로 다른 시퀀스들 간의 activity 흐름 표현
  - Communication Diagram : collaboration을 지칭하는 용어 변경
  - Timing Diagram : 시간 흐름 관점에서 객체 상태 변이, 상호작용을 가시화

![img](http://www.jidum.com/upload/ckeditor/2016/10/20161020095545502.png)



| Diagram                            | 내용                                                      | 비고                  |
| ---------------------------------- | --------------------------------------------------------- | --------------------- |
| Class                              | 클래스와 클래스 간의 관계를 기술                          | UML 1                 |
| Component                          | 컴포넌트의 구조와 연관관계를 기술                         | UML 1                 |
| Object                             | 특정 시점의 객체의 Snapshot을 기술                        | unofficially in UML 1 |
| Composite Structure (Architecture) | - 하나의 클래스의 실행 시의 내부 구조를 기술- CBD 지원    | New to UML2           |
| Deployment                         | 시스템의 물리적인 배치를 기술                             | UML 1                 |
| Package                            | 시스템의 컴파일시의 **계층적인** 구조를 기술              | unofficially in UML 1 |
| Activity                           | 절차적이고 병렬적인 행위를 기술                           | UML 1                 |
| Use Case                           | 사용자가 상호작용하는 시스템의 모습을 기술                | UML 1                 |
| State machine                      | 객체의 상태에 따른 작업과 Event에 따른 상태의 변화를 기술 | UML 1 (State)         |
| Sequence                           | 객체들간의 상호작용을 순서에 초점을 맞춰 기술             | UML 1                 |
| InteractionOverview                | Sequence와 Activity Diagram의 결합                        | New toUML2            |
| Communication(Collaboration)       | 객체들간의 상호작용을 연결에 초점을 맞춰 기술             | UML 1                 |
| Timing                             | 객체들간의 상호작용을 시간 제약에 초점을 맞춰 기술        | New to UML2           |





## 7. 다음 파이썬(Python)...

다음 파이썬(Python) 코드에 적용된 디자인 패턴은?



![2020_7L_7](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_7.jpg)

**답 : ④**

① [Interpreter Pattern](http://jidum.com/jidums/view.do?jidumId=1000)

② [Strategy Pattern](http://jidum.com/jidums/view.do?jidumId=1009)

③ [Memento Pattern](http://jidum.com/jidums/view.do?jidumId=1005)

④ [Command Pattern](http://jidum.com/jidums/view.do?jidumId=999)



---

## 8. 비기능적 요구사항에...

비기능적 요구사항에 해당하는 것은?



![2020_7L_8](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_8.jpg)

**답 : ③**





---

## 9. 형상 관리 요소...

형상 관리 요소 및 절체에 대한 설명으로 옳지 않은 것은?



![2020_7L_9](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_9.jpg)

**답 : ③**

③ ~~형상은~~ 대상 시스템을 분석하여 높은 수준의 추상화된 정보를 추출하는 작업이다.

==> 역공학 reverse engineering ; 소스 코드를 분석하여 설계 문서를 추출.



---

## 10. 다음 설명에 ...

다음 설명에 해당하는 스크럼(Scrum) 관련 활동은?



![2020_7L_10](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_10.jpg)

**답 : ①**

- 스프린트 ; 2~4주기 혹은 30일 마다 동작 가능한 제품을 제공.

① 스프린트 회고 ; 개선할 수 있는 최고의 기회. 회고의 주제 = '다음 스프린트를 더 잘하기 위해 무엇을 할 수 있을 것인가?'

② 스프린트 리뷰 = 스프린트 검토 ; 고객에게 진행된 스프린트 결과를 데모하고, 여기서 고객의 피드백을 정리하여 다음 스프린트에 적용하는 것을 말한다.

③ 일일 스크럼 미팅 ; 날마다 15분 정도의 회의.

④ 릴리스 계획



---

## 11. 객체지향 설계가 ...

객체지향 설계가 갖는 특징으로 옳지 않은 것은?



![2020_7L_11](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_11.jpg)

**답 : ②**

② 객체지향 설계는 ~~하나의 커다란 작업을 여러 개의 작은 작업으로 분할하고, 분할된 각각의 소작업을 함수(모듈)로 구현하는 것이다.~~

==> 상향식. 데이터에서 출발하여 데이터에 연관된 기능을 파악.

==> 하향식 ; 구조적 분석 기법.





---

## 12. 소프트웨어 설계 시...

소프트웨어 설계 시 고려해야 하는 결합도가 낮은 것부터 순서대로 바르게 나열한 것은?



![2020_7L_12](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_12.jpg)

**답 : ④**





---

## 13. 소프트웨어 개발 단계를 ...

소프트웨어 개발 단계를 시간의 흐름에 따라 네 개의 범주(도입, 상세, 구축, 이행)로 나누고, 각 범주에는 요구사항 도출부터 설계, 구현, 평가까지의 개발 생명주기가 포함되어 있는 방법론은?




![2020_7L_13](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_13.jpg)

**답 : ②**

- 소프트웨어 개발 프로세스 모형

| 구분                        | 설명                                                         | 장점                                                         | 단점                                                 |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------- |
| 폭포수                      | 산출물 명확. <br>**문서와 결과물 도출에 중점**               | 가시성이 좋음. 소규모 적합                                   | 신규 프로젝트 부적합. <br>새로운 요구 반영 어려움    |
| 프로토타이핑                | 견본품. <br>신속한 원형화                                    | 폭포수의 전 단계로 올라갈 수 없는 점을 보완.                 | 관리, 통제가 어렵다.                                 |
| 나선형                      | 폭포수, 원형의 장점을 취합. <br>점진적                       | 대규모 시스템 적합                                           | 초기 위험 분석 오류 시, 실패 가능성                  |
| V-모형                      | 분석과 설계는 왼편. 테스팅과 유지보수는 오른편. <br>**작업과 결과의 검증에 초점** | 테스트 단계에서 오류 발견 시 되돌아갈 수 있음                |                                                      |
| 점증적 모형                 | 선형순차 + 프로토타입 결합                                   | 중요,기초 기능을 우선 개발. <br>확장하는 형태. 점증적(추가) & 반복적(보완)<br>신규 프로젝트 적합 | 관리 문제<br>검증 문제<br>계약 문제<br>유지보수 문제 |
| UP(Unified Process) 모형    | UML. 객체 지향 분석 및 설계를 지원하기 위한 Diagram<br>Usecase Diagram<br>점증적 반복<br>가. 개 념 정립(도입, Inception) ; 개략적 파악<br>나. 전개(정련, Elaboration) ; 비전 구체화. 아키텍처 프레임워크 설정<br>다. 구축(Construction) ; 구현 및 설치 준비. 문서를 User에게 인도하기 위해 **준비**<br>라. 전환(전이, Transition) ; **인도**. 테스트, 설치, 다음 반복 단계를 준비 | 사용자 요구 즉시 파악 가능                                   |                                                      |
| 신속한 소프트웨어 개발 모형 | 신속하게 개발하여 새로운 도전과 기회에 반응하기 위함.        | 중첩된 반복적인 프로세스.<br>설계 문서 최소화                |                                                      |





---

## 14. 빈칸에 들어갈 내용을...

빈칸에 들어갈 내용을 순서대로 바르게 나열한 것은?



![2020_7L_14](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_14.jpg)

**답 : ④**

- 상위 - 드라이버
- 하위 - 스텁



---

## 15. 다음 코드 변환에 ...

다음 코드 변환에 대한 리팩토링 기법에 맞는 최적의 작업은?



![2020_7L_15](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_15.jpg)

**답 : ②**

- 객체지향의 개념

  - 객체 ; 데이터와 수행되는 함수들을 가진 작은 소프트웨어 모듈

  - 속성 ; 객체들이 가지고 있는 데이터 값을 단위별로 정의한 것.

  - 메서드(Method) ; 객체가 어떻게 동작하는지를 규정하고 속성의 값을 변경.

  - 클래스 ; 객체의 타입(Object Type)을 말하며, 객체들이 갖는 속성과 적용연산을 정의하는 템플릿

  - 가상 혹은 추상 클래스(Abstract Class)

    - 서브 클래스들의 공통 특성을 하나의 슈퍼 클래스로 추출하기 위한 목적으로 생성된 클래스.
    - 재사용 부품을 이용하여 확장할 수 있는 개념
    - 일반 클래스와 달리 생성할 목적을 가지고 있지 않으며 생성할 수도 없다.

  - 인터페이스 ; 함수들의 시그니처만 명세하고, 함수의 구현은 전혀 존재하지 않는다.

  - 다형성 ; 한 함수가 여러 클래스들에 정의되어 있는 현상

    - 다중성 = 다양성
    - 동일한 메시지가 다른 객체에 보내지더라도 수신 객체는 자기 자신의 고유한 방법만으로 행동
    - 같은 이름의 메서드를 다른 클래스에서 호출 가능 = 동적바인딩(dynamic binding)에 의해 이루어짐

  - 상속성 ; 기존 클래스들의 속성과 오퍼레이션을 상속.

  - 오버로딩 vs 오버라이딩

    |      | 오버로딩 overloading       | 오버라이딩 overriding |
    | ---- | -------------------------- | --------------------- |
    | 설명 | 중복정의                   | 재정의                |
    | 비고 | 변수 타입 또는 개수가 다름 | 같음                  |

  

  - 캡슐화 ; 정보은닉 Information Hiding

  - 객체지향 프로그래밍의 장단점
    - 장점 ; 재사용성, 선언형 명세 설계, 신뢰성, 유지보수 용이성, 신속한 설계, 설계 독립성, 프로그래밍 개발 용이성, 대량의 분산처리 지원
    - 단점 ; 정형화된 분석 및 설계 방법이 없다. 실행 시 처리(interface) 시간 지연. (다형성, 상속, 오버로딩, 다중 상속) 등은 유지보수 어려움.

  





---

## 16. McCall의 소프트웨어...

McCall의 소프트웨어 품질 요소에 대한 설명으로 옳지 않은 것은?

![2020_7L_16](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_16.jpg)

**답 : ③**

③ 이식성 = 다른 다양한 환경에서 운영될 수 있는지.

상호운용성 - 다른 소프트웨어와 정보를 교환할 수 있는 정도.



- McCall의 sw 품질요인
  - 제품 운영
    - 정확성 ; 사용자의 요구정도를 충족시키는 정도
    - 신뢰성 ; 요구된 기능을 계속적으로 수행할 수 있는 정도 → 사용자, 발주자, 유지보수자가 공통으로 관심을 보이는 항목
    - 용이성 ; 쉽게 배울 수 있고 사용할 수 있는 정도
    - 무결성 ; 허용되지 않은 사용이나 자료의 변경을 제어하는 정도
    - 효율성 ; 최소의(주어진) 시간과 기억용량을 소비하여 요구되는 기능을 수행할 수 있는 정도 → 사용자, 발주자가 공통으로 관심을 보이는 항목
  - 제품 개조
    - 유지보수성 ; 오류가 발견되었을 때 쉽게 교정되는 정도
    - 유연성(융통성) ; 기능의 추가나 다른 환경에서 적응하기 위해 쉽게 수정될 수 있는 정도
    - 시험성 ; 쉽고 철저하게 시험될 수 있는 정도
  - 제품 전이
    - 이식성 ; 여러 하드웨어, 운영체제 환경에서도 운용 가능하도록 쉽게 수정될 수 있는 정도
    - 재사용성 ; 전체나 일부가 다른 응용 목적으로 사용될 수 있는 정도
    - 상호운영성 ; 다른 소프트웨어와 정보를 교환할 수 있는 정도.

  

---

## 17. 객체지향의 개념에서...

객체지향의 개념에서 다형성(Polymorphism)의 주요 설명으로 옳지 않은 것은?



![2020_7L_17](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_17.jpg)

**답 : ①**

① 속성과 관련된 오프레이션을 클래스 안에 묶어서 하나로 취급한다.

==> 캡슐화



---

## 18. T. McCabe의...

T. McCabe의 순환 복잡도(Cyclomatic Complexity)에 대한 설명으로 옳지 않은 것은?



![2020_7L_18](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_18.jpg)

**답 : ①**

① 사이클로매틱 수는 ~~각 모듈에 대한 제어도(fan-out)를 이용하여 측정한다.~~

==> 의사결정수 와 조건수를 이용하여 측정한다.

각 모듈에 대한 제어도(fan-out)를 이용 ==> 구조화.

- 구조화
  - 소프트웨어 전체 구조와 그 구조가 시스템에 개념적인 무결성을 제공하는 방법.
  - 프로그램 구조는 모듈의 계층적 구성, 제어계층구조 암시, 구조도에 의해 표현.
    - 깊이 Depth ; 제어 수준의 개수
    - 너비 Width ; 제어의 전체적인 폭
    - 제어도 Fan-out ; 한 모듈이 호출하는 하위 모듈의 수
    - 공유도 Fan-in ; 한 모듈을 호출하는 상위 모듈의 수





---

## 19. <표1>과 같이 ...

표1과 같이 기능항목에 대한 복잡도가 주어지고, 입력은 10개, 출력은 5개, 질의는 8개, 파일은 28개, 응용인터페이스는 4개이며, 복잡도는 단순이다. 개발팀의 생산성은 주당 60 기능점수로 구현된다. 표2를 참조하여 프로젝트를 수행하기 위한 노력을 추정한 값은?



![2020_7L_19](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_19.jpg)



**답 : ④**



- TCF ; Technical Complexity Factor 기술복잡도

- TCF = 0.65 + 0.01 * **총영향도**( sum 가중치 * 인자)

- FP = UFP * TCF

  - UFP Unadjusted Function Point ; 조정 전 기능점수

- TCF = 0.65 + 0.01 * 25 (5+2+2+3+2+2+2+2+3+2) = 0.9

- FP = UFP * TCF = 222 * 0.9 = 199.8

- MM = 199.8 / 60 = 3.33




---








## 20. 원인-결과 그래프...

원인-결과 그래프 기법으로 테스트 케이스를 구하고자 한다. 문제에 대한 원인과 결과가 다음과 같을 때, 제한조건을 포함한 그래프는?



![2020_7L_20](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/2020_7L_20.jpg)


**답 : ③**



- 제약(Constraints)
  - E exclusive ; 원인1과 원인2 중 많아야 하나가(at most one) 참이 될 수 있음을 의미한다. 즉, 두 원인이 동시에 참일 수 없다.
  - I Inclusive ; 원인1, 원인2, 또는 원인3 중 적어도 하나는 (at least one) 참이어야 함을 나타낸다. 즉, 모두가 동시에 거짓일 수는 없다.
  - O one and only one ; 원인1과 원인2 중 오로지 하나만 참이어야 함을 나타낸다.
  - R Requires ; 원인1일 참이려면 원인2도 반드시 참이어야 함을 나타낸다. 즉, 원인1이 참이면서 원인2가 거짓인 경우는 불가능하다.



(1열 A or B) && (2열 #) ==> '출입가능'

~(1열 A or B) ==> '출입가능'

(1열 A or B) && ~(2열 #) ==> '출입가능'

A ; 부장

B ; 사원



![20-1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2020_7L/20-1.jpg)

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg5MDE5MDU5XX0=
-->