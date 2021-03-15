---
title: "2016년 7급 전산직 소프트웨어공학 풀이"
strapline: "소프트웨어공학 풀이"
description: "2016년 7급 전산직 소프트웨어공학 풀이"
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

# 2016년 7급 전산직 소프트웨어공학 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 객체지향 시스템 테스트의...

1. 객체지향 시스템 테스트의 설명으로 옳지 않은 것은?

  ![2016_7L_1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_1.jpg)

**답 : ①**

① 클래스에 대한 테스트 시 필요로 하는 객체 상태를 고려하지 않는다.

==> 상태 기반 테스팅은 객체지향 테스팅의 한 종류.

- 객체지향 시스템 테스팅 ; 오브젝트 상태에 중점을 둠. 오브젝트의 오퍼레이션이 실행될 때, 오브젝트 상태가 일관성을 유지하는지를 체크.

  

- 객체지향
  - 객체지향 구성
    - 객체 + 클래스
  - 객체지향 기본 원칙
    - 캡슐화 ; 데이터와 데이터를 처리하는 함수를 하나로 묶음
    - 정보은닉 ; 다른 객체에게 자신의 정보를 숨기고 자신의 연산만을 통하여 접근을 허용
    - 추상화 ; 불필요한 부분을 생략하고 객체의 속성중 가장 중요한 것에만 중점. 모델화
    - 상속성 ; 이미 정의된 상위 클래스의 모든 속성과 연산을 하위 클래스가 물려받는 것.
    - 다형성 ; 객체가 연산 수행 시, 하나의 메시지에 대해 각 객체가 가지고 있는 고유한 방법으로 응답할 수 있는 능력
  - 객체지향 기법의 생명주기
    - OOA object oriented analysis 객체지향분석
      - 사용자의 **요구사항을 분석**하여 요구된 문제와 관련된 모든 클래스, 이와 연관된 속성과 연산 그들간의 관계 등을 정의하여 모델링.
    - OOD object oriented design 객체지향설계
      - OOA를 사용하여 생성한 여러가지 분석 모델을 설계 모델로 변환하는 작업. 시스템 설계와 객체 설계를 수행
    - OOP object oriented programming 객체지향구현
      - 설계단계에서 생성한 설계 모델과 명세서를 근거로, 코딩하는 단계
    - OOT object oriented test 객체지향시험
      - 클래스 테스트 ; 구조적 기법에서의 단위 테스트와 같은 개념으로 가장 작은 단위.
      - 통합테스트 ; 객체를 몇 개 결합하여 하나의 시스템으로 완성시키는 과정에서의 검사.
        - 스레드 기반 테스트 ; 시스템에 대한 하나의 입력이나 이벤트에 응답하는 데 요구되는 클래스들을 통합하는 것. 각각의 스레드가 통합되고 개별적으로 테스트
        - 사용 기반 테스트 ; 독립 클래스르 테스트한 후 독립 클래스를 사용하는 다음 계층의 종속 클래스를 테스트
      - 확인 테스트 ; 사용자의 요구사항에 대한 만족 여부 검사
      - 시스템 테스트 ; 모든 요소들이 적합하게 통합되고 올바른 기능을 수행하는 지 검사



---

## 2. 소프트웨어 재사용에 ...

소프트웨어 재사용에 대한 설명으로 옳지 않은 것은?

![2016_7L_2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_2.jpg)

**답 : ③**

③ 소프트웨어 재사용은 기존의 소프트웨어를 활용하므로 수정하거나 이해하기 위한 ~~추가의 노력이 들지 않는다.~~

==> 소프트웨어 시스템과 컴포넌트는 특수한 재사용 가능 개체이다. 새로운 상황에 맞게 수정하는데 비용이 많이 든다.







---

## 3. 형상관리에 대한 ...

형상관리에 대한 설명으로 옳은 것은?

![2016_7L_3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_3.jpg)

**답 : ④**

① 컴포넌트 기반의 소프트웨어 개발 프로젝트에서는 형상관리가 ~~필요하지 않다~~.

② 베이스라인은 ~~단위 테스트를 통과한 원시 코드의 집합을 의미한다~~.

==> 기준선은 명세와 제품 전체를 포함한다.

③ ISO 9000에서는 ~~형상관리에 대한 언급이 없으나~~ CMMI에서는 형상관리 프로세스를 요구한다.

- ISO 9000은 기업의 품질 경영 시스템의 개발에 사용될 수 있는 국제 표준의 집합.

- CMMI

| Level                  | Focus                                  | Process Areas                                                |
| ---------------------- | -------------------------------------- | ------------------------------------------------------------ |
| Performed              |                                        |                                                              |
| Managed                | Basic<br>Project<br/>Management        | Requirements management<br/>Project planning<br/>Project monitoring and control<br/>Supplier agreement management<br/>Measurement and analysis<br/>Process and product quality assurance<br/>Configuration management |
| Defined                | Process<br/>standardization            | Requirements development<br/>Technical solution<br/>Product integration<br/>Verification<br/>Validation<br/>Organizational process focus<br/>Organizational process definition<br/>Organizational training<br/>Integrated project management<br/>Integrated supplier management<br/>Risk management<br/>Decision analysis and resolution<br/>Organizational environment for integration<br/>Integrated teaming |
| Quantitatively managed | Quantitative<br/>management            | Organizational process Performance<br/>Quantitative project management |
| Optimizing             | Continuous<br/>process<br/>improvement | Organizational innovation and deployment<br/>Causal analysis and resolution |







---

## 4. 다음에서 설명하는 ...

다음에서 설명하는 CMMI의 성숙도 단계에 해당하는 것은?

![2016_7L_4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_4.jpg)

**답 : ④**



---

## 5. 인수 테스트(acceptance test)에...

인수 테스트(acceptance test)에 대한 설명으로 옳지 않은 것은?

![2016_7L_5](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_5.jpg)

**답 : ②**

② 알파 테스트는 ~~선택된 사용자가 사용자 환경에서 수행하는 인수 테스트이다~~.

- 알파 테스트 ; 선택된 사용자가 개발자 환경에서 수행하는 인수 테스트
- 베타 테스트 ; 선택된 사용자가 사용자 환경에서 수행하는 인수 테스트



---

## 6. McCabe의 순환복잡도...

McCabe의 순환복잡도(CC : Cyclometic Complexity)에 대한 설명으로 옳지 않은 것은?

![2016_7L_6](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_6.jpg)

**답 : ③**

③ 프로그램의 ~~모든 경로를 최소 한 번 이상 실행하도록~~ 테스트하기 위한 입력의 개수에 해당한다.

- 경로 검증 기준(path coverage) ; 모든 경로를 최소 한번 이상 실행하도록 하는 테스트 기준.



- McCabe의 소프트웨어 복잡도
  - sw복잡도는 문제의 복잡도, 프로그램 구조의 복잡도, 데이터 복잡도로 세분화
  - 프로그램 구조의 복잡도는 McCabe의 순환적 복잡도 이용.
  - CC cyclomatic Complexity = 의사결정수 + 조건수 + 1= P + 1 = E - N + 2





## 7. COCOMO Ⅱ 의 ...

COCOMO Ⅱ 의 서브모델이 아닌 것은?

![2016_7L_7](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_7.jpg)

**답 : ②**

- COCOMO 모델

  - 정적 단일 변수 모델

  - Boehm이 제안한 원시 프로그램의 규모에 의한 비용예측 모형

  - **수학적 산정기법이지만 비정형모델**

    | 유형                    | 설명                    |
    | ----------------------- | ----------------------- |
    | Organic, 유기적, 조직형 | 50KDSI, 5만 라인 이하   |
    | semidetached, 반 내장형 | 300KDSI, 30만 라인 이하 |
    | embedded, 내장형        | 300KDSI, 30만 라인 이상 |

    | 비용추정 단계 및 적용변수 구체화 정도에 따른 분류 | 설명                                                         |
    | ------------------------------------------------- | ------------------------------------------------------------ |
    | Basic COCOMO                                      | 원시코드 라인 수만으로 비용 계산                             |
    | Intermediate COCOMO                               | 4가지 특성의 15가지 요인을 가미하여 곱한 가중치 계수<br>ㄱ. 제품의 속성<br>ㄴ. 컴퓨터의 속성<br/>ㄷ. 개발요원의 속성<br/>ㄹ. 프로젝트의 속성 |
    | Detailed COCOMO                                   | 노력승수 = 개발 공정별 노력승수 * 개발 공정별 가중치         |



- COCOMO Ⅱ
  - 재사용, 요구분석, 요구변경을 반영할 수 있다.
  - 소프트웨어 개발 프로젝트가 진행된 정도에 따라 세 가지 다른 모델을 제시
    - 1단계 ; Application composition model. 어플리케이션 결합(응용 합성) 단계로 객체점수 혹은 어플리케이션 점수라 부르는 규모척도 이용. 프로토타입을 만드는 단계
    - 2단계 ; Early design model. 초기 설계단계로 대안이 되는 자세한 구조와 기능을 탐구. 기능점수 방법을 채택
    - 3단계 ; Post-Architecture model. FP와 LOC를 규모척도로 이용.
  - 서브모델의 종류
    - 응용 결합 모델 ; 프로토타입 개발을 추정하기 위한 모델
    - 초기 설계 모델 ; 기능 점수에 기초
    - 포스트 아키텍처 보델 ; 비용산정을 위한 표준 공식을 이용(LOC, FP)
    - 재사용 모델 ; 재사용 가능한 컴포넌트와 혹은 설계나 프로그램 변환 도구가 자동적으로 생성하는 프로그램 코드의 통합에 필요한 노력을 계산하는 데 이용.



---

## 8. 객체지향 설계 중 ...

객체지향 설계 중 "클라이언트는 자신이 사용하지 않는 메서드에 의존 관계를 맺으면 안 된다." 라는 설계 원칙으로 옳은 것은?

![2016_7L_8](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_8.jpg)

**답 : ④**

- SRP Single Responsibility Principle 단일 책임의 원리
  - 하나의 클래스는 하나의 책임만. 세분화
- OCP Open-Closed Principle 개방-폐쇄의 원리
  - **확장에 열림, 변경에 닫힘**
  - OPEN : **수직관계 Is-a** 에는 열림
  - CLOSE : **수평관계 has-a**에는 유연, 즉 영향을 받지 않아야 한다
- LSP Liskov Substitution Principle 리스코프 치환의 원리
  - 자식 타입들은 부모 타입들이 사용되는 곳에 대체.
  - **즉, 부모 클래스가 사용되는 곳에 자식 클래스로 치환하더라도 문제가 없어야 한다.**
  - 상위 클래스는 파생 클래스로 대체 가능해야 한다.
- ISP Interface Segregation Principle 인터페이스 분리의 원리
  - 서로 다른 성격의 인터페이스는 명백히 분리. 하나x, 다수의 인터페이스
- DIP Dependency Inversion Principle 의존 관계 역전의 원리
  - 추상클래스는 파생클래스를 참조해서는 안되며, 파생클래스나 추상클래스는 오직 추상클래스만을 참조.
  - 상속성과 관계
  - 추상 = 부모, 파생 = 자식



---

## 9. 소프트웨어 품질에 ...

소프트웨어 품질에 대한 설명으로 옳지 않은 것은?

![2016_7L_9](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_9.jpg)

**답 : ③**

③ 인스펙션(inspection) - 체크리스트를 가지고 ~~본인이~~ 개발한 코드와 산출물 등을 검토하는 것

- 인스펙션 - 워크스루를 구조적이고 체계적으로 발전시킨 공식적인 검토회의. 개발자뿐 아니라 사회자나 검열관, 관리자 등이 참여.



---

## 10. 요구사항 품질 속성에...

요구사항 품질 속성에 대한 설명으로 옳지 않은 것은?

![2016_7L_10](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_10.jpg)

**답 : ③**

③ 완전성(completeness) - 요구사항을 바로 구현할 수 있도록 자료구조나 알고리즘이 명시되어야 한다.

- 요구 분석 명세서 평가 기준
  - 무결성correctness과 완벽성completeness ; 사용자의 요구를 오류 없이 완벽하게 반영하고 있어야 한다.
  - 일관성consistency ; 요구 분석서 안에 서로 모순되는 부분이 없어야 한다.
  - 명확성unambiguous ; 요구 분석서는 모호한 점이 없도록 간결하고 명쾌하게 써야한다.
  - 기능성function ; 어떻게보다 무엇에 관점을 두고 기술. ==> 어떻게 등은 설계 단계에서 다룸.
  - 검증 가능성verifiable ; 요구 분석이 사용자의 요구 분석을 만족시키고 있는지, 개발된 시스템이 요구 분석에 기술된 내용과 일치하는지 검증.
  - 추적 가능성traceable ; 요구 분석 명세서의 내용은 장, 절, 문단으로 나뉘어 체계적으로 정리되어야 한다. 설계서, 사용자 지침서 등, 후에 작성될 문서에서 인용하거나 특정 내용을 변경하기 위하여 찾기 쉽도록 하기 위한 것이다.



---

## 11. 통합 프로세스 모델...

통합 프로세스 모델(UP : Unified Process)의 특징을 설명한 것으로 옳지 않은 것은?

![2016_7L_11](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_11.jpg)

**답 : ④**

④ 위험 관리는 포함되어 있지 않다.

==> UP는 계속적인 반복과정을 통해 위험 관리가 가능하다.

- UP
  - 유스케이스 기반, 아키텍처 중심, 반복적이고 점진적.
  - UML. 객체 지향 분석 및 설계를 지원하기 위한 Diagram
  - Usecase Diagram
  - 점증적 반복
    - 가. 개 념 정립(도입, Inception) ; 개략적 파악
    - 나. 전개(정련, Elaboration) ; 비전 구체화. 아키텍처 프레임워크 설정
    - 다. 구축(Construction) ; 구현 및 설치 준비. 문서를 User에게 인도하기 위해 **준비**
    - 라. 전환(전이, Transition) ; **인도**. 테스트, 설치, 다음 반복 단계를 준비



---

## 12. 소프트웨어 테스트에...

소프트웨어 테스트에 대한 설명으로 옳지 않은 것은?

![2016_7L_12](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_12.jpg)

**답 : ④**

④ 블랙 박스 테스트(black box test)는 입력 값에 대한 예상 출력 값을 정해 놓고 그대로 결과가 나오는지 ~~원시 코드를 보며~~ 확인한다.



---

## 13. 요구분석명세서를 작성할...

요구분석명세서를 작성할 때 고려해야 할 사항으로 옳지 않은 것은?

![2016_7L_13](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_13.jpg)

**답 : ①**

① 시스템의 기능을 ~~구현하는 방법에~~ 대하여 중점적으로 기술한다.

==> 요구분석명세서는 어떻게가 아닌 무엇을 고려한다.





---

## 14. 소프트웨어 유지보수의...

소프트웨어 유지보수의 형태에 대한 설명으로 옳지 않은 것은?

![2016_7L_14](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_14.jpg)

**답 : ③**

③ 적응 유지보수(adaptive maintenance)는 ~~개발 과정에서 바로 잡지 못한 오류를 유지보수 단계에서 해결하는 것이다~~.

==> 수정 유지보수에 대한 설명이다.



- 유지보수 형태
  - 완전 유지보수 perfective
    - 새로운 기능을 추가하고 기존의 소프트웨어 기능을 개선(enhancement)
  - 적응 유지보수 adaptive
    - 새로운 운영체제, **하드웨어** 환경으로 이식(porting)
  - 수정 유지보수 corrective
    - 하자의 원인을 찾아 문제를 해결하는 것으로, After service
  - 예방 유지보수 preventive
    - 기존의 소프트웨어 구조를 변형시키는 것(restructuring) - 재구조화(개조)



---

## 15. 허가받지 않은 사용자가...

허가받지 않은 사용자가 데이터 접근을 통해 변경을 시도했을 때 보호할 수 있는지 정도를 나타내는 품질 특성에 해당하는 것은?

![2016_7L_15](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_15.jpg)

**답 : ①**





---

## 16. 애자일(agile) 선언문에...

애자일(agile) 선언문에 대한 설명으로 옳지 않은 것은?

![2016_7L_16](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_16.jpg)

**답 : ③**





---

## 17. 다음에서 설명하는 ...

다음에서 설명하는 디자인 패턴에 해당하는 것은?

![2016_7L_17](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_17.jpg)

**답 : ②**

| 분류 | 종류      | 사용목적                                              |
| ---- | --------- | ----------------------------------------------------- |
| 구조 | Bridge    | 인터페이스와 구현의 명확한 분리                       |
| 구조 | Adapter   | 기존 모듈 재사용을 위한 인터페이스 변경               |
| 구조 | Composite | 객체간의 부분전체 관계 형성 및 관리, 재귀적 합성 이용 |
| 구조 | Facade    | 서브시스템에 대한 통합된 인터페이스를 제공            |





---

## 18. 비기능 요구사항에 ...

비기능 요구사항에 대한 설명으로 옳지 않은 것은?

![2016_7L_18](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_18.jpg)

**답 : ④**

④ 시스템이 제공해야 하는 서비스와 시스템이 특정 입력에 대해 어떻게 반응하는지, 시스템이 특정 상황에서 어떻게 동작해야 하는지에 관한 사항이다.

==> 기능 요구사항에 대한 설명.



---

## 19. 객체지향 개념에 대한...

객체지향 개념에 대한 설명으로 옳지 않은 것은?

![2016_7L_19](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_19.jpg)

**답 : ②**

② 전체 객체에 전속되어 독립된 객체로 존재할 수 없는 부분 객체도 있는데 이와 같은 관계를 특별히 ~~집합 관계(aggregation relationship)~~라고 한다.

==> 복합(composition) 관계라고 한다.

- 집합 관계 ; 구성요소(부분)가 업성도 전체 개념이 존재할 수 있다. 예. 부서원이 없어도 부서는 남아 있을 수 있다.
  - 구성요소는 하나 이상의 전체 집합에 소속될 수 있다.



- UML 다이어그램 내용.







---

## 20. 유스케이스 다이어그램에서 ...

유스케이스 다이어그램에서 A 유스케이스를 수행하는 도중에 특정 조건을 만족하면 B 유스케이스를 수행한다. A 유스케이스와 B 유스케이스 간의 관계로 옳은 것은?

![2016_7L_20](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/2016_7L_20.jpg)

**답 : ④**



- Usecase 다이어그램에서 사용되는 관계
  - 확장관계 ; 새로운 흐름 추가나 확장. ![20-1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/20-1.png)
  - 통신관계 ; ![20-2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/20-2.png)
  - 일반화관계 ; ![20-3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/20-3.png)
  - 이용(포함 = 의존)관계 ; 하나의 유스케이스를 수행할 때 다른 유스케이스의 행동을 포함. 하나의 진행과정으로 사용.![20-4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2016_7L/20-4.png)