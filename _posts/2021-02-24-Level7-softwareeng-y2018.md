---
title: "2018년 7급 전산직 소프트웨어공학데이터베이스 풀이"
strapline: "소프트웨어공학데이터베이스 풀이"
description: "2018년 7급 전산직 소프트웨어공학데이터베이스 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "7Level_softwareengdatabase"
tag:
  - "7급"
  - "소프트웨어공학데이터베이스"
  - "7급공무원"
toc: true
last_modified_at: 2021-02-24
comments: true
---

# 20189년 7급 전산직 소프트웨어공학데이터베이스 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 소프트웨어 개발 프로세스...

1. 소프트웨어 개발 프로세스 모델 중 폭포수(waterfall) 모델에 대한 설명으로 옳지 않은 것은?

1. 
![2018_7L_1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_1.jpg)


**답 : ④**

④ 소프트웨어 요구사항의 ~~변경이 많은 경우에 적합~~한 모델이다. ==> V-모형 or 애자일

- 폭포수 모델(waterfall) = 선형 순차 모델 ; 순차모델이기에 변경 시, 전 단계로 되돌아갈 수 없다.
  - 산출물이 명확, 문서와 결과물 도출에 중점.
  - 장 ; 가시성이 좋음, 소규모 적합
  - 단 ; 신규 프로젝트 부적합, 새로운 요구 반영 어려움.




---

## 2. 소프트웨어 통합 프로세스(UP)...

2. 
소프트웨어 통합 프로세스(UP) 모델의 구체화 단계(elaboration phase)에서 하는 주요 활동으로 옳지 않은 것은?①

②

③

④



---

## 2. 

2. 
![2018_7L_2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_2.jpg)


**답 : ①**

- UP(Unified Process) 모형 ; UML 방법과 도구를 위한 프레임워크로 설계된 **"유스케이스(use-case driven) 기반, 아키텍처 중심(architecture centric), 반복적(iterative)이고 점진적(incremental)"** 소프트웨어 프로세스를 위한 필요성에 대두.
  - 점증적 반복 incremental and iterative
  - UP의 개발 단계
    - 개념 정립, 도입, Inception
    - 전개, 정련, Elaboration
    - 구축, Construction
    - 전환, 전이, Transition
    - =-=-
    - 개념 정립, 도입, Inception
      - 시스템에 대한 비지니스 케이스를 설정(확립)하는 것이 목표.
      - 개력적으로 파악.
      - 대력적인 틀(framework)만 잡은 구조
    - **전개, 정련, Elaboration**
      - **비전을 구체화, 개발 범위를 확정**
      - **시스템의 뼈대(Framework)를 확립.**
      - **아키텍처 프레임워크를 설정.**
      - **아키텍처 설계, 요구사항 분석, 중대한 위험 요소 식별 및 해결**
    - 구축, Construction
      - 구현하고 설치를 준비
      - 시스템의 설계와, 프로그래밍, 시험을 하는 단계
      - 관련 문서가 사용자에게 인도되기 위해 준비.
    - 전환, 전이, Transition
      - 테스트, 설치, 다음 반복 단계



---

## 3. 기능점수(FP)를 계산하기...

3. 
기능점수(FP)를 계산하기 위해 고려할 대상으로 옳지 않은 것은?①

②

③

④



---

## 3. 

3. 
![2018_7L_3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_3.jpg)


**답 : ④**

- 기능점수(Function Point) ; 소프트웨어의 각 기능에 대하여 가중치를 부여하여 요인별 가중치를 합산하여 소프트웨어의 규모나 복잡도, 난이도를 산출하는 모형.
  - **라인수(LOC)에 영향 없다.**
  - EI External Input ; 외부로부터 입력을 카운트
  - EO External Output ; 외부로 출력을 카운트
  - EQ ; External inQuiry ; 외부 조회를 카운트
  - ILF ; Internal Logical File ; 시스템에 존재하는 사용자 데이터 및 제어 정보의 그룹을 카운트
  - EIF ; External Interface File ; sw system 사이에 전달되거나 공유된 파일을 카운트



---

## 4. 그림과 같이 관찰대상(Subject)의...

4. 
그림과 같이 관찰대상(Subject)의 데이터(A ~ D)에 변화가 발생하면 이 변화를 탐지하여 여러 가지 방식으로 사용자에게 디스플레이하는 프로그램을 작성하고자 한다. 이 프로그램에 적용할 수 있는 디자인 패턴은?①

②

③

④



---

## 4. 

4. 
![2018_7L_4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_4.jpg)


**답 : ④**

==> **하나의 데이터 소스로부터 여러 View**를 보여주고 있으므로 Observer 패턴에 해당한다.

① Decorator ; 덧칠. 객체의 기능을 동적으로 추가 제거

② Flyweight ; 가벼움. 작은 객체들의 공유

③ Mediator ; 중재=조정. M:N 객체 관계를 M:1로 단순화. 객체들 간의 상호작용을 객체로 캡슐화.



| 대분류        | 종류                    | 사용 목적                                                    |
| ------------- | ----------------------- | ------------------------------------------------------------ |
| 객체 사용     | Factory Methode         | 대행 함수(위임)를 통한 객체 생성, 인스턴스 생성 결정은 서브클래스 |
| 객체 사용     | Abstract Factory        | 제품군(product family)별 객체 생성                           |
| 객체 사용     | Singleton               | 클래스 인스턴스가 하나만 만들어지고 그 인스턴스의 전역접근   |
| 객체 사용     | Prototype               | 복제를 통한 객체 생성                                        |
| 객체 사용     | Builder                 | 부분 생성을 통한 전체 객체 생성                              |
| **구조 개선** | Adapter                 | 기존 모듈 재사용을 위한 인터페이스 변경                      |
| **구조 개선** | Facade                  | 서브시스템에 대한 통합된 인터페이스를 제공                   |
| **구조 개선** | Bridge                  | 인터페이스와 구현의 명확한 분리                              |
| **구조 개선** | Composite               | 객체간의 부분전체 관계 형성 및 관리, 재귀적 합성 이용        |
| **구조 개선** | Decorator               | 객체의 기능을 동적으로 추가삭제                              |
| **구조 개선** | Flyweight               | 작은 객체들의 공유                                           |
| **구조 개선** | Proxy                   | 대체(대리자) 객체를 통한 작업 수행                           |
| 행위 개선     | Interpreter             | 간단한 문법에 기반한 검증작업 및 작업처리                    |
| 행위 개선     | Template Method         | 상위클래스에서 기본 골격을 결정, 하위클래스에서 구체적 내용 정의 |
| 행위 개선     | Command                 | 요청을 객체로 캡슐화. 수행할 작업의 일반화를 통한 조작       |
| 행위 개선     | Iterator                | 동일 자료형의 여러 객체 순차 접근                            |
| 행위 개선     | Mediator                | 객체들 간의 상호작용을 객체로 캡슐화, M:N 객체 관계를 M:1로 단순화 |
| 행위 개선     | Memento                 | 객체의 이전 상태 복원 또는 보관                              |
| 행위 개선     | Observer                | One source Multiple Use                                      |
| 행위 개선     | State                   | 객체 상태 추가시 행위 수행의 원활한 변경                     |
| 행위 개선     | Strategy                | 동일 목정의 여러 알고리즘 중 선택해서 적용                   |
| 행위 개선     | Visitor                 | 오퍼레이션이 처리할 요소의 클래스를 변경하지 않고도 새로운 오퍼레이션을 정의, 구문트리 파싱 시 트리를 이루는 모든 노드를 방문하여 작업 |
| 행위 개선     | Chain of Responsibility | 수행 기능 객체군까지 요청 전파.                              |





---

## 5. CMMI 모델의 정의 단계...

5. 
CMMI 모델의 정의 단계(defined level)에 해당하는 프로세스 영역으로 옳지 않은 것은?①

②

③

④



---

## 5. 

5. 
![2018_7L_5](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_5.jpg)


**답 : ④**

- CMMi(Capability Maturity Model integration)
  - 



| Level                  | Focus                                  | Process Areas                                                |
| ---------------------- | -------------------------------------- | ------------------------------------------------------------ |
| Performed              |                                        |                                                              |
| Managed                | Basic<br>Project<br/>Management        | Requirements management<br/>Project planning<br/>Project monitoring and control<br/>Supplier agreement management<br/>Measurement and analysis<br/>Process and product quality assurance<br/>Configuration management |
| Defined                | Process<br/>standardization            | Requirements development<br/>Technical solution<br/>Product integration<br/>Verification<br/>Validation<br/>Organizational process focus<br/>Organizational process definition<br/>Organizational training<br/>Integrated project management<br/>Integrated supplier management<br/>Risk management<br/>Decision analysis and resolution<br/>Organizational environment for integration<br/>Integrated teaming |
| Quantitatively managed | Quantitative<br/>management            | Organizational process Performance<br/>Quantitative project management |
| Optimizing             | Continuous<br/>process<br/>improvement | Organizational innovation and deployment<br/>Causal analysis and resolution |



---

## 6. PMBOK의 프로젝트 ...

6. 
PMBOK의 프로젝트 위험 관리 프로세스에 대한 설명으로 옳지 않은 것은?①

②

③

④



---

## 6. 

6. 
![2018_7L_6](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_6.jpg)


**답 : ③**

①

②

③ 위험 식별은 ~~도출된 위험들이 미치는 영향이  얼마나 큰지, 얼마나 자주 발생하는지 등을 분석하는 프로세스이다.~~

- 위험 식별 ; 무엇이 위험인지 파악하고 찾아내는 프로세스.
- 정량적 위험 분석 ; 도출된 위험들이 미치는 영향이  얼마나 큰지, 얼마나 자주 발생하는지 등을 분석하는 프로세스



- PMBOK 설명

https://m.blog.naver.com/PostView.nhn?blogId=yingbbang&logNo=221591267108&proxyReferer=https:%2F%2Fwww.google.com%2F



## 7. 대학교 학사관리시스템...

7. 
대학교 학사관리시스템의 기능적 요구사항으로 옳지 않은 것은?

④



## 7. 

7. 
![2018_7L_7](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_7.jpg)


**답 : ④**

④ 시스템 장애로 인한 정지시간이 1년에 10시간을 넘지 않아야 한다. ==> 성능 요구사항에 해당.

- 기능 요구사항 ; 목표 시스템이 반드시 수행해야 하거나 목표 시스템을 이용하여 사용자가 반드시 수행할 수 있어야 하는 기능(동작)에 대하여 기술
  - 작성 내용 ; 어플리케이션 및 세부 기능 명칭, 기능의 세부내용, 기능 입출력 정보와 유형, 기능의 수행 평가 및 테스트 방법 등을 작성. 필요 시 오류 처리, 복구 방안 등도 포함하여 명시
  - 상세화 수준. Level4 단위까지 세분화
    - L1 ; 단위업무 시스템
    - L2 ; 주요 업무 기능
    - L3 ; 세부 기능
    - L4 ; 세부 기능의 활동
  - 기능 요구사항 도출 ; 기능 요구사항을 토대로 사업규모(기능점수), 사업기간 등을 산정.
    - 1단계 ; 사용자 요건 도출
    - 2단계 ; 요구사항 상세화 정의
    - 3단계 ; 기능점수 산출 절차로 진행
- 성능 요구사항 ; 목표 시스템의 일부 기능이 달성해야 하는 최고 또는 최저 능력을 명시한 것으로 시스템이 어떠한 기능을 수행할 때 소요되는 시간이나 처리량, 자원 사용치 등에 대한 요구사항을 기술
  - 작성 내용 ; 목표 시스템의 처리속도, 처리량, 시간, 동적정적 용량, 가용성 등. 성능에 대한 요구사항을 기술
  - 상세화. 
    - 요구 사항 작성 시, 작성 항목 별로 목표 값, 목표 값 측정 환경 및 조건, 예외 사항을 기술하며, 목표 값은 검증 가능하고 정량적으로 기술하는 것이 중요.

①

②

file:///C:/Users/LSY/Downloads/2018%EB%85%84+%EA%B3%B5%EA%B3%B5SW%EC%82%AC%EC%97%85+%EC%A0%9C%EC%95%88%EC%9A%94%EC%B2%AD%EC%84%9C+%EC%9E%91%EC%84%B1%EC%9D%84+%EC%9C%84%ED%95%9C+%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD+%EC%83%81%EC%84%B8%ED%99%94+%EC%8B%A4%EB%AC%B4%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8-20181015.pdf③

④



---

## 8. 애자일 프로세스...

8. 
애자일 프로세스 모델에 해당하지 않는 것은?

8. 
![2018_7L_8](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_8.jpg)


**답 : ②**

②



- 애자일 프로세스 모델
  - XP
  - 스크럼
  - TDD
  - RAD
  - CBD
  - 소프트웨어 프로토타이핑 모형
  - 4세대 기법
  - ASD
  - DSDM
  - Crystal
  - FDD
  - LSD Lean sw dev
  - AM 애자일 모델링
  - 애자일 UP = AUP①

②

③

④



---

## 9. 익스트림 프로그래밍의...

9. 
익스트림 프로그래밍의 테스팅에 대한 설명으로 옳지 않은 것은?

9. 
![2018_7L_9](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_9.jpg)


**답 : ③**

③ 프로그램을 큰 단위로 나누어 ~~릴리스 직전~~ 테스트를 수행한다.

==> **코딩 전,** 단위 테스트 케이스를 생성하고 이후 인수 테스트가 이루어진다.

**시험 우선 개발.**①

②

③

④



---

## 10. 유스케이스에 대한 ...

10. 
유스케이스에 대한 설명으로 옳은 것만을 모두 고르면?

10. 
![2018_7L_10](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_10.jpg)


**답 : ②**

ㄱ. ~~개발자~~의 관점에서 요구사항을 정의한다.

==> 사용자의 관점

ㄷ. 유스케이스 명세서에는 비기능적 요구사항을 ~~기술해서는 안 된다~~.

==> 기능적 비기능적 요구사항을 모두 기술 가능.



- 유스케이스
  - 액터, 유스케이스, 시나리오, 관계



---

## 11. 다음 설명에 해당하는...

11. 
다음 설명에 해당하는 테스팅은?①

②

③

④



---

## 11. 

11. 
![2018_7L_11](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_11.jpg)


**답 : ③**

==> 부하로 인해 테스트

① 보안 테스팅 ; 인가받지 않은 내부 혹은 외부의 액세스로부터 시스템이 어떻게 스스로를 방어하는지에 대해 테스트

② 회귀 테스팅 ; 시스템의 변화에 따른 영향을 파악하기 위한 테스팅

④ 조합 테스팅 ; 잠재적 조합 요소의 거대한 양을 처리하기 위한 테스트케이스를 선정하는데, 도움을 주는 통계적 테스트 기법. 3가지 입력 ==> 3<sup>3</sup>= 27가지 결과
①

②

③

④



---

## 12. <보기 1>의 디자인 패턴...

12. <보기 1>의 디자인 패턴 분류와 <보기 2>의 디자인 패턴을 바르게 연결한 것은?

12. 
![2018_7L_12](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_12.jpg)


**답 : ②**

①

②

③

④



---

## 13. 응집도를 강한 것 부터...

13. 
응집도를 강한 것 부터 순서대로 나열할 때, ㄱ~ㄹ에 들어갈 용어를 바르게 연결한 것은?

13. 
![2018_7L_13](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_13.jpg)


**답 : ③**

결합도 ; **(좋음)**(약) 자 - 스 - 제 - 외 - 공 - 내 (강)**(나쁨)**

응집도 ; **(나쁨)**(약) 우 - 논 - 시 - 절 - 정 - 순 - 기 (강)**(좋음)**



---

## 14. 다음 코드와 부합하는...

14. 
다음 코드와 부합하는 클래스 간의 관계로 옳은 것은?①

②

③

④



---

## 14. 

14. 
![2018_7L_14](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_14.jpg)


**답 : ①**

①

②

③

④



---

## 15. UML 시퀀스(sequence)...

15. 
UML 시퀀스(sequence) 다이어그램의 구성요소로  옳지 않은 것은?

15. 
![2018_7L_15](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_15.jpg)


**답 : ①**

- 시퀀스 다이어그램 = 순서 다이어그램 = 순차도
  - 구성요소 ; 생명선, 메시지
  - 복합 부분(복합 프래그먼트) ; 객체의 연결, 처리내용



---

## 16. 역공학(reverse engineering)...

16. 
역공학(reverse engineering) 프로세스에 대한 설명으로 옳지 않은 것은?①

②

③

④



---

## 16. 

16. 
![2018_7L_16](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_16.jpg)


**답 : ①**

① 코드 난독화를 수행하면 ~~역공학을 쉽게 할 수 있다.~~

==> 난독화를 통해 역공학을 어렵게 만든다.



---

## 17. 다음 설명에 해당하는 ...

17. 
다음 설명에 해당하는 것은?

②

③

④



---

## 17. 

17. 
![2018_7L_17](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_17.jpg)


**답 : ③**

① 컴포넌트 ; 실제 동작하고 있는 개체 / 활동중인 독립적인 단위

모듈 ; 가장 첫 번째 그리고 가장 맨 앞에 위치하는 구현이 된 단위

② 웹서비스 ; 네트워크 상에서 서로 다른 종류의 컴퓨터들 간에 상호작용을 하기 위한 소프트웨어 시스템

cf) 기존 분산 컴퓨팅 기술 ; COBRA, DCOM, RMI

④ 클래스 라이브러리 ; 공통 중간 언어(CLI ; common Intermediate language)를 포함한 모든 닷넷 프레임워크의 언어에서 사용 가능한 표준 라이브러리.



---

## 18. CRC 카드에 대한 ...

18. 
CRC 카드에 대한 설명으로 옳은 것만을 모두 고르면?

②

③

④



---

## 18. 

18. 
![2018_7L_18](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_18.jpg)


**답 : ②**

ㄱ. 클래스의 연산에 대한 상세 알고리즘 설계를 위해 이용되는 도구이다.

==> 보기 설명은 설계의 개념이며, 컴포넌트 수준 설계에 해당.

- 설계의 유형(기술적 시각)
  - 데이터(클래스) 설계
  - 구조 설계
  - 인터페이스 설계
  - 컴포넌트 수준 설계
  - 배치 수준 설계

CRC ; 객체지향 **분석** 단계에서 클래스 모델링을 위해 사용.

ㄹ. 카드의 상단에 클래스 이름, 왼쪽 열에 ~~협력자~~, 오른쪽 열에 ~~클래스 책임을~~ 나열한다.

==> 왼쪽 열에 클래스 책임, 오른쪽 열에 협력자를 나열한다.



---

## 19. 테스팅에서 프로그램의...

19. 
테스팅에서 프로그램의 실제 실행결과가 올바른 결과인지를 판단하는 메커니즘은?①

②

③

④



---

## 19. 

19. 
![2018_7L_19](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_19.jpg)


**답 : ③**

① 테스트 하니스 ; 시스템의 일부 기능만 시험하기 위하여 소프트웨어를 변경하는 것.

② 테스트 적합성 기준 ; 테스트를 선정 또는 생성하는 기준.

③ 테스트 오라클 ; 테스트의 예상 결과를 작성.

④ 테스트 종료 기준 ; 

- 테스트 종료 기준
  - 정해진 테스트 일정이 지나면 테스트 종료
  - 모든 테스트 케이스를 실행하여도 더 이상 결함이 발견되지 않으면 테스트 종료



---

## 20. 다음 표는 프로젝트를...

20. 
다음 표는 프로젝트를 수행하는 데 필요한 작업, 소요 기간, 선행 작업을 나타낸 것이다. 작업 T5를 담당한 개발자가 이직하여 대체 인력을 확보하였으나 대체 인력의 교육에 15일이 소요되어, 작업 T5는 소요기간이 35일로 변경되었다. 프로젝트를 완료하기까지 필요한 최소 소요 기간은 개발자가 이직 전보다 얼마나 증가하는가?

②

③

④



---

## 20. 

20. 
![2018_7L_20](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2018_7L/2018_7L_20.jpg)


**답 : ①**

- CP

  - 개발자 이직 전 ; T1 T2 T4 T7 T8 ; 65일
  - 개발자 이직 후 ; T3 T5 T6 = 70일

  **5일 증가.**①

②

③

④
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ0MjI5MDAyMiwtMzM0MDg1OTgyXX0=
-->