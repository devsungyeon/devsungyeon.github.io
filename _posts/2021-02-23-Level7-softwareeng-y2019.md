---
title: "2019년 7급 전산직 소프트웨어공학 풀이"
strapline: "소프트웨어공학 풀이"
description: "2019년 7급 전산직 소프트웨어공학 풀이"
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

# 2019년 7급 전산직 소프트웨어공학 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 애자일 선언문은...

애자일 선언문은 애자일 방법론이 추구하고 있는 가치를 요약하고 있다. 애자일 선언문의 내용으로 옳은 것은?



![2019_7L_1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_1.jpg)

**답 : ①**





---

## 2. 다음에서 설명하는...

다음에서 설명하는 아키텍처는?



![2019_7L_2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_2.jpg)

**답 : ④**

- 피어-투-피어(peer-to-peer) 아키텍처
  - 다수의 단말간에 통신할 때의 아키텍처 중 하나로, 대등한 사람이 서로 통신하는 것을 특징하는 통신방식 통신모델 또는 통신 기술의 한 분야.
  - P2P 응용 범위 ; P2P 데이터 전송, P2P 전화, P2P 게시판, P2P 방송 ( TV, 라디오 ) , P2P 그룹웨어, P2P 분산 파일 시스템, P2P - SIP, P2P - DNS , P2P - 가상 네트워크, P2P 지진 정보
  - 장점
    - 높은 확장성
    - 저가
  - 단점
    - 통신 상태 특정 곤란성 ; P2P 방식으로 통신하는 단말의 존재와 연결 경로를 가정 할 수 없이 항상 상대의 존재와 그 연결 경로를 확인할 필요
    - 통신 경로에 의한 통신 속도의 제한.
- 저장소(repository) 아키텍처
  - 중앙자료구조(Central Data Structure)와 독립된 컴포넌트(Component)로 구성된 아키텍처.
  - 큰 데이터의 이동 및 공유에 적합, 컴포넌트간의 통신은 이루어지지 않음.
  - 장점
    - 대량의 데이터를 저장하는데 효과적
    - 컴포넌트의 추가 삭제가 편리
    - 중앙 집중화를 통해 데이터 관리가 용이, 보안적인 측면이 뛰어남
  - 단점
    - 저장소에 오류가 생기면 시스템 전체에 문제 발생
    - 데이터 분산이 어려움.
- 마스터-슬레이브(master-slave) 아키텍처 = 클라이언트/서버 구조
  - 클라이언트와 서버로 나뉘는 아키텍쳐.
  - 하나의 서버에 다수의 클라이언트가 접속하는 일대다 관계로 구성
  - 서버는 하나의 중앙 서버 또는 분산된 여러 서버가 존재할 수 있음.
  - 특징
    - 새로운 서버의 추가 및 업그레이드가 용이
    - 데이터가 서버에 집주오디어 데이터 관리가 용이, 보안적인 측면이 뛰어남
    - 서버에 네트워크 트래픽과 데이터가 집중되어 처리 비용이 급증할 수 있음.
- 마이크로서비스(microservice) 아키텍처
  - 마이크로서비스
    - 소프트웨어가 잘 정의된 API를 통해 통신하는 소규모의 독립적인 서비스
    - 대규모 소프트웨어 프로젝트를 마이크로 단위의 모듈로 분리하여 loosely-coupled한 구조로 만들고 API를 통해 서로 통신

[Microservice Arch](https://medium.com/giljae/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98-microservices-architecture-%EC%9D%98-%EC%9E%A5%EC%A0%90%EA%B3%BC-%EB%8B%A8%EC%A0%90-7c45615cfe1a)

- MVC 구조

  - 상호작용 애플리케이션을 모델, 뷰, 컨트롤러의 세개의 컴포넌트로 구성하는 아키텍처로 유저 인터페이스와 비지니스 로직들을 서로 분리하여 개발하는 방법.

  - 장점

    - 동일한 모델에 대해 다양한 뷰를 제공
    - 효율적인 모듈화가 가능
    - 모델과 뷰의 구분으로 사용자 인터페이스에 대한 요구 사항을 적용시키는데 용이

  - 단점

    - 간단한 애플리케이션에 적용하기에는 복잡

    - 모델이 자주 변경되는 경우 업데이트 요청이 많아 뷰의 갱신이 따라가지 못함.

      | 모델     | - 애플리케이션의 핵심 기능을 포함<br>- 상태 변화 시 컨틀로러와 뷰에 전달 |
      | -------- | ------------------------------------------------------------ |
      | 뷰       | - 정보 표시를 관리<br>- 결과물 생성을 위해 모델로부터 정보를 수신 |
      | 컨트롤러 | - 사용자로부터 입력을 받아 모델과 뷰에 명령을 전달<br>- 모델에 명령을 전달해 상태를 변경하고, 뷰에 명령을 보내 표시 방법을 변경 |

- 파이퍼 필터 구조

  - 데이터의 흐름을 점진적으로 처리하는 시스템을 위한 아키텍처
  - 프로세싱을 위한 시스템이 각 필터에 캡슐화되어 있으며, 데이터는 인접 필터 사이의 파이프를 통해 전달되는 형태
    - 각 필터들은 상호 독립적, 앞 뒤의 필터에 대한 정보를 알 수 없음.
    - 모든 데이터의 처리 순서는 파이프 구조와 각각의 필터를 통해 조정 가능한 이벤트에 의해 통제됨.
  - 장점
    - 설계자는 몇 개의 필터들을 간단히 조합하여 시스템의 입출력 행위를 이해
    - 새로운 필터를 기존의 구조에 추가하거나 통합하는 것이 가능
    - 각 필터의 독립적인 구조로 인해 다양한 시스템에 적용할 수 있는 재사용성을 가짐
    - 각 필터들의 독립적인 수행이 가능해 동시 수행(Concurrency)으로 효율 증진을 노릴 수 있음.
    - 응답성(throughput)이나 데드락(deadlock)과 같은 특수한 분석을 지원
      - 응답성(throughput) ; 지정된 시간동안 처리할 수 있는 데이터의 양
      - 데드락(Deadlock) ; 둘 이상의 프로세스가 자원의 한계로 인해 처리되지 못하고 대기해 있는 상태
  - 단점
    - 상태 정보를 공유하는데 유연하지 못함
    - 각 필터 간 공통된 특성이 적어 각 필터가 전송받은 데이터를 다시 파싱(parsing)해야 하는 경우가 발생할 수 있음.
      - 파싱(parsing) ; 입력 데이터를 시스템 구조에 맞게 분석 및 해부하는 과정



---

## 3. 다음은 무엇에...

다음은 무엇에 사용되는 도구인가?



![2019_7L_3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_3.jpg)

**답 : ④**

- 버전 관리
  - CVS(Concurrent Versions System, 동시 버전 시스템)
  - Subversion
  - Git

- 프로젝트 관리
  - MS Project
  - Jira
  - Trello
  - Smartsheet
- 소프트웨어 설계
  - AgileJ StructureViews ?
- 소프트웨어 테스팅
  - JUnit
  - Mockito
  - JMeter



---

## 4. CMMI 프로세스...

CMMI 프로세스 성숙도 수준(maturity level) 중 관리(Managed) 단계의 특징으로만 묶은 것은?



![2019_7L_4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_4.jpg)

**답 : ①**

ㄷ - Defined

ㄹ - Optimizing



| Level                  | Focus                                  | Process Areas                                                |
| ---------------------- | -------------------------------------- | ------------------------------------------------------------ |
| Performed              |                                        |                                                              |
| Managed                | Basic<br>Project<br/>Management        | Requirements management<br/>Project planning<br/>Project monitoring and control<br/>Supplier agreement management<br/>Measurement and analysis<br/>Process and product quality assurance<br/>Configuration management |
| Defined                | Process<br/>standardization            | Requirements development<br/>Technical solution<br/>Product integration<br/>Verification<br/>Validation<br/>Organizational process focus<br/>Organizational process definition<br/>Organizational training<br/>Integrated project management<br/>Integrated supplier management<br/>Risk management<br/>Decision analysis and resolution<br/>Organizational environment for integration<br/>Integrated teaming |
| Quantitatively managed | Quantitative<br/>management            | Organizational process Performance<br/>Quantitative project management |
| Optimizing             | Continuous<br/>process<br/>improvement | Organizational innovation and deployment<br/>Causal analysis and resolution |





---

## 5. 그림과 같이 서비스 ...

그림과 같이 서비스 구현 클래스의 a(), b() 연산을 사용하는 클라이언트 클래스가 서비스 구현 클래스에 직접 의존하는 관계에서 클라이언트 클래스가 서비스 인터페이스에 의존하고 서비스 구현 클래스는 서비스 인터페이스를 구현하는 것으로 설계를 변경하였다. 다음 중 이와 가장 관련이 깊은 SOLID 설계 원칙은?



![2019_7L_5](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_5.jpg)

**답 : ③**

[UML 화살표](https://lktprogrammer.tistory.com/32)

- 객체지향 설계의 원리
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

## 6. 어떤 웹 서비스...

어떤 웹 서비스 시스템은 다음과 같은 특징을 가지고 있다. 이 시스템과 관련하여 ISO/IEC 9126 품질 특성 중에서 개선할 필요가 있는 것은?



![2019_7L_6](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_6.jpg)

**답 : ②**





## 7. 스크럼(Scrum)의...

스크럼(Scrum)의 제품 백로그(product backlog)에 대한 설명으로 옳지 않은 것은?



![2019_7L_7](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_7.jpg)

**답 : ③**

③ 제품 백로그에 있는 업무의 우선순위를 결정한 후에는 ~~변경하지 않는다.~~

==> 각 스프린트 진입시 제품 백로그 목록으로부터 항목을 선정하고, 스프린트 수행동안 해당 백로그를 보다 구체적으로 상세화하여 기능에 반영한다. 이 과정에서 시장의 요구, 고객가치에 따라 우선순위가 조정되거나 항목이 추가, 삭제될 수 있다.

[제품 백로그](https://engineering-skcc.github.io/agile-quickguide/Agile-QuickGuide04-%EC%A0%9C%ED%92%88%EB%B0%B1%EB%A1%9C%EA%B7%B8%EB%8F%84%EC%B6%9C/)

- 제품 백로그 ; 스크럼 팀이 해결해야 하는 "해야 할 일(to do)"에 대한 목록이다. 그 목록의 내용은 소프트웨어에 대한 특징, 소프트웨어 요구사항, 사용자 스토리에 대한 정의 또는 아키텍처 정의나 사용자 문서와 같이 추가적으로 필요한 업무에 대한 설명일 수도 있다.



---

## 8. 개발자 A는 <명세>에...

개발자 A는 <명세>에 따라 <코드>를 작성한 후 테스팅을 수행하였다. A는 100% 문장 커버리지를 달성하면서 동시에 프로그램의 오류를 발견할 수 있었다. A가 사용한 테스트 입력은? (단, 단축 연산(short-circuit evaluation)은 수행하지 않는다.)



![2019_7L_8](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_8.jpg)

**답 : ①**

- 화이트박스 테스트 검증 기준
  - 문장 검증 기준, statement coverage, 노드/문장 커버리지
    - 모든 문장이 적어도 한 번씩 수행
  - 분기 검증 기준, branch coverage, 간선/분기 커버리지
    - 마름모로 표시된 모든 각 분기점들의 참과 거짓을 적어도 한 번 이상 실행.
    - 분기 커버리지를 만족하면 문장 커버리지 만족
  - 경로 검증 기준, path coverage, 경로 커버리지
    - 수행 가능한 **모든 경로**를 검사.
  - 조건 검증 기준(condition coverage, 조건 커버리지
    - if나 while문 안에 있는 조건식을 자세히 조사
    - 조건문의 **모든 조건식을 만족하는 경우**와 **만족하지 않는 경우**를 테스트



---

## 9. <그림> 은 <보기>에서...

<그림> 은 <보기>에서 기술하고 있는 병원 진료 시스템의 일부 명세에 해당하는 유스케이스 다이어그램이다. <그림>에서 '사용자'와 '보호자', '사용자'와 '환자' 사이에 들어갈 관계와 '진료예약'과 '로그인', '진료예약취소'와 '로그인' 사이에 들어갈 관계로 옳은 것은? (단, A, B, C, D는 다이어그램의 구성 요소가 아니며 관계의 방향을 지시한다)



![2019_7L_9](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_9.jpg)

**답 : ①**

[Usecase Diagram include and extend](https://googry.tistory.com/2)

- 포함 Include
  - 하나의 유스케이스가 다른 유스케이스의 실행을 전제로 할 때 형성.
  - 기능을 포함하는 유스케이스 ---<<include>>---> 기능에 포함되는 유스케이스
  - 글 등록 ---<<include>>--> 로그인
- 확장 Extend
  - 확장 대상 유스케이스를 수행 할 때 특정 조건에 따라 확장 기능 유스케이스를 수행하는 경우 적용.
  - 확장 대상 유스케이스 <---<<extend>>--- 확장 기능 유스케이스
  - 글을 등록한다 <---<<extend>>--- 파일을 첨부한다.
  - "글을 등록한다" 기능을 수행할 때 "파일을 첨부한다" 기능을 선택적으로 수행 할 수 있다.



---

## 10. 다음은 어떤 시스템의...

다음은 어떤 시스템의 유지보수를 위한 요구사항의 일부이다. 아래 요구사항에 따라 수행한 유지보수 활동이 기존 기능에 영향을 끼쳤는지 알아보기 위해 수행하는 테스팅은?



![2019_7L_10](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_10.jpg)

**답 : ①**





---

## NN 11. 다음 클래스 ...

다음 클래스 다이어그램으로 표현한 설계에서 사용한 디자인 패턴은?



![2019_7L_11](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_11.jpg)

**답 : ②**









---

## 12. 어떤 소프트웨어의 ...

어떤 소프트웨어의 고장 간 평균 시간(MTBF; Mean Time Between Failures)이 2,500시간이고 평균 수리 시간(MTTR; Mean Tiem To Repair)이 100시간일 때 평균 가동 시간(MTTF; Mean Time To Failure)과 가용성(availability)은? (단, 소수점 이하에서 반올림한다)



![2019_7L_12](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_12.jpg)

**답 : ②**

MTBF =  = MTTR + MTTF

MTTF = 2500 - 100 = 2500

Availability = MTTF / MTBF = 2500 / 2600 * 100% = 96%



---

## 13. 형상관리의 형상 제어...

형상관리의 형상 제어(configuration control) 활동에서 수행하는 작업으로만 묶은 것은?



![2019_7L_13](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_13.jpg)

**답 : ②**

ㄱ - 형상 식별

ㄹ - 형상 감사

- 형상관리의 기능(활동)
  - 형상 식별
    - 소프트웨어 형상 항목들을 관리하고 제어하기 위해서 각 항목들은 객체지향 방법으로 각기 이름이 붙여지고 조직되어 진다.
    - 형상관리 대상인 SCI(형상 항목 Software Configuration Item)들은 tree구조(계층구조)로 구분하고 관리 목록 번호 부여.
    - 조직 구조 명료. 수정 용이. 변경 발생 시 추적 용이
  - 버전 제어
    - sw 프로세스가 진행되는 동안 생성되는 형상객체들의 다른 비전들을 관리하기 위해 절차와 툴들을 결합
    - 프로시저와 도구 결합
  - 형상 제어
    - SCI의 변경요구를 검토 승인. 현재의 베이스라인(기준선)에 적절히 반영할 수 있도록 통제.
    - 형상통제 위원회(Configuration Control Board)의 구성이 필요. CCB는 변경 요청자와 작업 수행자로 구성.
    - CCB는 각 베이스 라인의 승인 및 변경 승인 여부를 결정.
  - 형상 감사
    - 수정된 SCI나 기준선이 미리 정해진 요구사항과 일치하는지를 검사.
    - 소프트웨어 베이스라인의 무결성을 평가하여 공식적으로 승인.
    - 검증(Verification) 및 확인(Validation)
      - 검증(Verification) ; 개발자 입장. 명세서 대상
      - 확인(Validation) ; 사용자 입장. 요구기능 대상
  - 형상 상태 보고
    - 소프트웨어 형상 및 변경관리의 식별 통제 감사 기능의 수행 결과를 기록하고 데이터베이스에 의한 관리를 하며 보고서를 작성.



---

## 14. 다음은 리팩토링 ...

다음은 리팩토링 전후의 코드 변화이다. 적용된 리팩토링 기법에 해당하는 것은?



![2019_7L_14](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_14.jpg)

**답 : ③**







---

## 15. 소프트웨어 테스팅...

소프트웨어 테스팅 문서에 관한 국제 표준은?



![2019_7L_15](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_15.jpg)

**답 : ③**

- ISO/IEC 9899 ; C언어 표준.
- IEEE 828 ; SCMP – 소프트웨어 설정 관리 계획
- IEEE 829 ; 소프트웨어 시험을 위한 '8가지 정의된 단계'를 규정한 [IEEE](https://ko.wikipedia.org/wiki/IEEE) 표준
  - SQAP – 소프트웨어 품질 보증 계획 IEEE 730
  - SCMP – 소프트웨어 설정 관리 계획 IEEE 828
  - STD – 소프트웨어 테스트 문서 IEEE 829
  - SRS – 소프트웨어 요구 사양 IEEE 830
  - SVVP – 소프트웨어 유효성 검증 계획 IEEE 1012sdfs
  - SDD – 소프트웨어 설계 기술 IEEE 1016
  - SPMP – 소프트웨어 프로젝트 관리 계획 IEEE 1058
  - SUD – 소프트웨어 사용자 문서 IEEE 1063
- IEEE 1042 ; 형상 관리 표준 중 하나.



- **Configuration Management Standards**

  \- ISO 10007

  \- BS 15000/ISO 20000/ITIL

  \- IEEE 828

  \- IEEE 1042

  \- IEEE 1044

  \- EIA 649

  \- ECSS-M-040

  \- J-STD-016

  \- ESA PSS-05-09

  \- US/ISO 12207

  

- **Software Testing Standards**

  \- ISO 9000

  \- BS-7925

  \- IEEE 829

  \- IEEE 1028

  \- IEEE 810 + IEEE 1044

  \- ISO 9126

  \- IEEE/ISO 12207

  \- IEEE/ISO 15288

  

- **Requirements Handing Standards**

  \- ISO 9000

  \- ISO 9126

  \- ISO/IEC 12119

  \- IEEE 610

  \- IEEE 830

  \- IEEE 1220



---

## 16. 다음은 두 정수를...

다음은 두 정수를 입력받아 큰 값을 출력하는 프로그램이다. 이 프로그램에서 caller 함수와 max 함수 간의 결합도와 max 함수의 응집도를 바르게 나열한 것은?




![2019_7L_16](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_16.jpg)

**답 : ④**



- 응집도 ; 한 모듈 내에 있는 구성요소들의 기능적 관련성

| 우연적, 동시적  | 논리적           | 시간적, 임시적 | 절차적    | 정보적, 교환적, 통신적                 | 순차적                     | 기능적, 함수적 |
| --------------- | ---------------- | -------------- | --------- | -------------------------------------- | -------------------------- | -------------- |
| 약함            | <                | <              | <         | <                                      | <                          | 강함           |
| 안좋음          | <                | <              | <         | <                                      | <                          | 좋음           |
| 한 모듈 내 존재 | 논리적으로 유사. |                | 특정 순서 | 동일 입력 출력을 사용해 다른 기능 수행 | 한 출력이 다른 원소의 입력 | 단일 기능 수행 |

- 결합도 ; 모듈간의 상호 의존도

| 자료                    | 스탬프       | 제어 | 외부            | 공통                        | 내용   |
| ----------------------- | ------------ | ---- | --------------- | --------------------------- | ------ |
| 약                      | <            | <    | <               | <                           | 강     |
| 좋음                    | >            | >    | >               | >                           | 안좋음 |
| 매개변수, call by value | 배열, 구조체 |      | 외부변수 extern | 전역변수, call by reference | 종속.  |







---

## 17. 다음 용어에 대한...

다음 용어에 대한 설명으로 옳은 것은?



![2019_7L_17](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_17.jpg)

**답 : ④**

① 사용자 스토리 ; 사용자 입장에서 요구사항에 대한 내용을 표현

- 백로그
  - 사용자 관점의 사용자 스토리를 개발자 용으로 변경

② 베이스라인은 공식적인 회의를 통하여 시스템 변경이 이루어져야 한다.

③ 기능점수는 각 기능에 대해 가중치를 부여하여 요인별 가중치를 합산하여 규모, 복잡도, 난이도를 산출.





---

## 18. <명세>는 어떤 과목의...

<명세>는 어떤 과목의 통과 여부를 결정하는 프로그램에 대한 명세이다. <코드>의 프로그램은 <명세>에 따라 작성하였지만 오류가 있다. <코드>의 오류를 검출할 수 있는 테스팅 기법과 테스트 입력을 바르게 짝지은 것은?



![2019_7L_18](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_18.jpg)

**답 : ①**

- 동등 분할 = 등가 분할 기법
  - 테스트 아이템의 입력 또는 출력이 여러 영역(Patition)으로 구분되는 경우에 적용
  - 동일한 영역 내에서는 어떠한 값을 선택해도 항상 같은 결과를 기대할 수 있다는 것을 전제로 함(테스팅이 가정하에 실행됨)
  - 실무에서는 잘 활용되지 않는다. 테스트 강도 약함.



---

## 19. 유스케이스 분석 ...

유스케이스 분석 기법에서는 유스케이스를 바탕으로 세 가지 유형의 클래스들을 도출한다. 다음 중에서 이에 해당하지 않는 클래스 유형은?



![2019_7L_19](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_19.jpg)

**답 : ③**

- 클래스를 도출하는 방법으로서 유스케이스 분석기법을 사용할 수 있다.
- 유스케이스(Use-case)는 객체지향 방법론 및 컴포넌트 기반 방법론(CBD, Component-Based Development)에서 시스템에 대한 요구사항을 정의할때 일반적으로 사용되는 개념이다.
- 개발자는 우선 시스템이 제공할 기능을 유스케이스 단위로 정의한다.
- 예를 들어 현금 자동 인출기 시스템의 경우에는 입금, 출금, 이체, 조회 등이 유스케이스가 될 수 있다.
- 개발자가 이 유스케이스를 분석하여 몇몇 유형의 도출하는 방법이 일반적으로 사용되며, 이 방법을 유스케이스 분석 기법이라고 부른다.
- 유스케이스 분석기법은 각 유스케이스의 내용을 분석하여 다음과 같은 세가지 유형의 클래스를 도출하려고 노력한다.
  - 경계클래스(boundary class)
    - 개발할 시스템과 시스템 외부와의 연결, 즉 인터페이스 역할을 하는 클래스들을 경계클래스
  - 실체클래스(entity class)
    - 실체클래스는 영속적인 정보(시스템의 수행이 종료되어도 그 값이 유지되어야 하는 정보_와 그 정보에 대한 조작 기능을 제공하는 클래스
  - 제어클래스(control class)
    - 제어 클래스는 시스템이 제공할 유스케이스의 제어 로직 및 비즈니스 로직을 제공하는 클래스

 





---

## 20. 다음 Java 코드의...

다음 Java 코드의 MyEmplyeeService, EmplyeeService, EmployeeDao, Employee 클래스를 UML 클래스 다이어그램으로 표현하였을 때 클래스 다이어그램에 나타나지 않는 관계는? (단, MyEmployeeService, EmployeeService, EmployeeDao, Employee 클래스는 이 외 다른 클래스와 아무 관계가 없다)



![2019_7L_20](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2019_7L/2019_7L_20.jpg)


**답 : ④**

Relationships(관계)

| 종류                  | 설명                                                         |
| --------------------- | ------------------------------------------------------------ |
| Dependency 의존       | 한쪽의 변화가 다른 쪽에 영향을 줄 수 있다. 화살표 시작점을 위해서 화살표 향한 쪽을 행함.  주문 --> 상품. **점선 속이 찬 화살표** |
| Association 연관      | 참조 관계. 연관이 있음을 나타냄. **실선**                    |
| Generalization 일반화 | 두 클래스가 일반화-특수화 관계. 상속을 표현. 화살표 시작점이 화살표 도착점의 특성을 상속.   토끼 --> 동물. **실선 빈 화살표** |
| Realization 실체화    | 구체화. Use case - Collaboration, Interface - class. **점선 빈 화살표.** 건물 --> 청사진 |

