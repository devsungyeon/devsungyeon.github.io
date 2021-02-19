---
title: "Software Engineering Summary"
strapline: "Software"
description: "Software 정리"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "Software_engineering"
tag:
  - "소프트웨어공학"
  - "소공"
  - "소공 요약"
toc: true
last_modified_at: 2021-02-12
comments: true
---

# Software 정리

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"

## Top

## PART 01 소프트웨어공학의 개념

  - SDLC ; 타당성 조사 - 계획 - 사용자 요구파악 - 분석 - 설계 - 구현 - 시험 - 유지보수

---
### 1. 소프트웨어의 개념
---
- 생산성 향상
- 품질향상
- 재사용 가능한 소프트웨어 개발
    - System의 5대 구성요소 ; Input, Process(Transformation), Output, Control, Feedback
    O = P(I)
    Input -> Process(Transformation) -> Output
- 방법론
    
    | 구분 | 구조적 방법론 | 정보공학 방법론 | 객체지향 방법론 |
    | --- | --- | --- | --- |
    | = | 프로세스 중심 방법론<br>= 자료흐름방법론<br>= 절차식 방법론 | 자료중심 방법론 |  |
    | 중점 | Process 중심 | Data 중심 | 객체 중심 |
    | 생명주기 | Top-down | Top-down | Bottom-up |

[to the Top](#Top)

---
### 2. 소프트웨어의 개념

[to the Top](#Top)

---
### 3. 소프트웨어의 위기

  - Brooks Raw ; 인력을 추가로 투입하더라도 오히려 프로젝트 시간은 지연될 수 있다.
  
[to the Top](#Top)

---
### 4. 소프트웨어 개발 프로세스 모형

- SDLC ; 타당성 조사 - 계획 - 사용자 요구파악 - 분석 - 설계 - 구현 - 시험 - 유지보수
  - 소프트웨어 개발 프로세스 모형

| 구분     | 설명                   | 장점                         | 단점                         |
|--------|----------------------|----------------------------|----------------------------|
| 폭포수    | 산출물 명확. <br>**문서와 결과물 도출에 중점**               | 가시성이 좋음. 소규모 적합            | 신규 프로젝트 부적합. <br>새로운 요구 반영 어려움 |
| 프로토타이핑 | 견본품. <br>신속한 원형화         | 폭포수의 전 단계로 올라갈 수 없는 점을 보완. | 관리, 통제가 어렵다.               |
| 나선형    | 폭포수, 원형의 장점을 취합. <br>점진적 | 대규모 시스템 적합                 | 초기 위험 분석 오류 시, 실패 가능성      |
| V-모형 | 분석과 설계는 왼편. 테스팅과 유지보수는 오른편. <br>**작업과 결과의 검증에 초점**  | 테스트 단계에서 오류 발견 시 되돌아갈 수 있음 |  |
| 점증적 모형 | 선형순차 + 프로토타입 결합 | 중요,기초 기능을 우선 개발. <br>확장하는 형태. 점증적(추가) & 반복적(보완)<br>신규 프로젝트 적합 | 관리 문제<br>검증 문제<br>계약 문제<br>유지보수 문제 |
| UP(Unified Process) 모형 | UML. 객체 지향 분석 및 설계를 지원하기 위한 Diagram<br>Usecase Diagram<br>점증적 반복<br>가. 개 념 정립(도입, Inception) ; 개략적 파악<br>나. 전개(정련, Elaboration) ; 비전 구체화. 아키텍처 프레임워크 설정<br>다. 구축(Construction) ; 구현 및 설치 준비. 문서를 User에게 인도하기 위해 **준비**<br>라. 전환(전이, Transition) ; **인도**. 테스트, 설치, 다음 반복 단계를 준비 | 사용자 요구 즉시 파악 가능 |  |
| 신속한 소프트웨어 개발 모형 | 신속하게 개발하여 새로운 도전과 기회에 반응하기 위함. |  중첩된 반복적인 프로세스.<br>설계 문서 최소화 |  |


- 신속한 소프트웨어 개발 모형

1) 애자일(agile) 기법
    - 문서화 < 구현 < 시험
    - 문제점
        - 대규모에는 부적합. 중소규모에 적합
        - 시스템 개발에 필요한 시간에 대해 비용을 지불
    - 원리
        
| 원리           | 설명                                       |
|--------------|------------------------------------------|
| 고객 참여        | 고객은 개발 프로세스 전체에 긴밀하게 참여                  |
| 점증적인 인도      | 점증적으로 인도                                 |
| 사람은 프로세스가 아님 | 규정된 프로세스 없이 자신들의 작업 방식으로 개발. (프로세스보다 사람) |
| 변경을 수용       | 변경들을 수용할 수 있도록 설계                        |
| 단순성의 유지      | 모두 단순성에 초점                               |


2) XP(eXtreme Programming) 모형 
    - **의사소통, 단순함, 피드백, 용기, 존중. '고객에게 최고의 가치를 가장 빨리'**
    - 경량 방법론
    - 고객의 참여를 극한 수준까지 유도.
    - 스토리 카드. ; 고객의 요구 요약. (요구분석서, CRC 카드)
    - **시험 우선 개발** ; 코드보다 시험을 먼저 작성

3)  d

[to the Top](#Top)

---


## PART 02 소프트웨어 프로젝트 관리

### 1. 프로젝트 범위

- 3P ; People, Process, Problem
- 4P ; People, Process, Product, Project
- Brooks Law ; 스케줄 지연에 대해 추가 인력을 투입이 오히려 악화될 수 있다.
- PMBOK(Project Management Body of Knowledge, 프로젝트관리지식체계)
    - 프로세스 그룹 ; 시작, 기획, 실행, 통제, 종료
    - 지식 영역 10개 항목 ; 통합, 범위, 시간, 원가, 품질, 인력자원, 의사소통, 위험, 조달, 이해관리자
        - 통합관리
        - 범위관리
        - 시간관리
        - 원가관리
        - 품질관리
        - 인력자원관리
        - 의사소통관리
        - 위험관리
        - 조달관리
        - 이해관리자관리

[to the Top](#Top)

---

### 2. 비용 계획

[to the Top](#Top)

---

### 3. 일정 계획

[to the Top](#Top)

---

### 4. 조직 계획

[to the Top](#Top)

---

### 5. 위험 분석 및 관리

[to the Top](#Top)

---

### 6. 개발 계획서

[to the Top](#Top)

---


## PART 03 소프트웨어 품질보증과 품질관리

### 1.품질보증의 개념

[to the Top](#Top)

---

### 2. 품질 관리 시스템

[to the Top](#Top)

---

### 3. 제품 품질

[to the Top](#Top)

---

### 4. 프로세스 품질

[to the Top](#Top)

---

### 5. 소프트웨어 품질 관리

[to the Top](#Top)

---

### 6. 소프트웨어 매트릭스 & 신뢰성

[to the Top](#Top)

---


## PART 04 소프트웨어 형상관리

### 1. 형상관리의 개념

[to the Top](#Top)

---

### 2. 형상관리를 지원하는 도구

[to the Top](#Top)

---

## PART 05 소프트웨어 요구사항 분석

### 1. 요구사항 분석의 개념

[to the Top](#Top)

---

### 2. 구조적 분석 기법

[to the Top](#Top)

---

### 3. 자료구조 지향 분석 기법

[to the Top](#Top)

---

### 4. 요구 사항의 명세화

[to the Top](#Top)

---

## PART 06 소프트웨어 설계

### 1. 설계의 개념

[to the Top](#Top)

---

### 2. 설계의 원리

[to the Top](#Top)

---

### 3. 설계 표기법

[to the Top](#Top)

---

### 4. 사용자 인터페이스 설계

[to the Top](#Top)

---




## PART 07 객체지향 패러다임

### 1. 객체지향의 개념

[to the Top](#Top)

---

### 2. 객체지향 개발 단계

## PART 08 UML & Design Pattern

### 1. UML의 개념

[to the Top](#Top)

---

### 2. UML의 다이어그램

[to the Top](#Top)

---

### 3. Design Pattern

[to the Top](#Top)

---



## PART 09 구현(Implementation)

### 1. 프로그래밍의 개념

[to the Top](#Top)

---

### 2. 코딩과 주석

[to the Top](#Top)

---



## PART 10 소프트웨어의 시험과 디버깅

### 1. 시험의 개념

[to the Top](#Top)

---

### 2. 시험 기법

[to the Top](#Top)

---

### 3. 소프트웨어 검사 전략

[to the Top](#Top)

---

### 4. 자동 검사 도구

[to the Top](#Top)

---

### 5. 프로그램 디버깅

[to the Top](#Top)

---



## PART 11 소프트웨어 유지보수

### 1. 유지보수의 개념

[to the Top](#Top)

---

### 2. 소프트웨어의 진화

[to the Top](#Top)

---



## PART 12 소프트웨어 재공학

### 1. 소프트웨어의 재사용

[to the Top](#Top)

---

### 2. 소프트웨어 재공학

[to the Top](#Top)

---

### 3. CASE의 개념

[to the Top](#Top)

---



## PART 13 클라이언트/서버 소프트웨어공학

### 1.클라이언트/서버의 아키텍처

[to the Top](#Top)

---



## PART 14 정형적 방법

### 1.정형적 방법의 개념

[to the Top](#Top)

---



## PART 15 최신 소프트웨어공학

### 1. MDA 프레임워크

[to the Top](#Top)

---

### 2. 웹서비스와 SCA

[to the Top](#Top)

---

### 3. 컴포넌트 기반 소프트웨어공학

[to the Top](#Top)

---

### 4. 관점지향 프로그래밍

[to the Top](#Top)

---

### 5. 보안공학

[to the Top](#Top)

---


































<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMwMDUwNDgyNCwtOTM3OTI4OTA4XX0=
-->