---
title: "2015년 9급 전산직 컴퓨터일반 풀이"
strapline: "컴퓨터일반 풀이"
description: "2015년 9급 전산직 컴퓨터일반 풀이"
header:
 overlay_image: C:/GitHub/devsungyeon.github.io/assets/images/bright.jpg
categories:
  - "9Level_computerbasic"
tag:
  - "9급"
  - "컴퓨터일반"
  - "9급공무원"
toc: true
last_modified_at: 2020-12-05
comments: true
---

# 2015년 9급 전산직 컴퓨터일반 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 시스템 소프트웨어에...

시스템 소프트웨어에 포함되지 않는 것은?

![2015_9L_1](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_1.jpg)

**답 : ①**

① 스프레드시트 

- 표 형식으로 데이터의 조직, 분석, 저장을 가능케 하는 상호작용의 컴퓨터 애플리케이션.
- 경리, 회계 등의 계산을 위해 사용되는 표 형식의 계산용지나, 계산용지를 컴퓨터에서 사용할 수 있게 구현한 표 계산 프로그램을 의미.



---

## 2. OSI 7계층 중 ...

OSI 7계층 중 브리지(bridge)가 복수의 LAN을 결합하기 위해 동작하는 계층은?


![2015_9L_2](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_2.jpg)

**답 : ②**

- OSI vs TCP/IP

![8_3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/8_3.jpg)

1. OSI 7 Layer
   - 네트워크 통신을 다루는 OSI 표준. 개방시스템 상호연결(OSI) 모델
   - 개방시스템(Open System) ; 기반구조와 관계없이 시스템간의 통신을 제공
   - 계층구조, 데이터의 움직임 파악 가능, 트러블슈팅 용이, 호환성
2. TCP/IP
   - 인터넷에서 컴퓨터들이 서로 정보를 주고받는데 쓰이는 통신규약(프로토콜)
   - 하드웨어, 운영체제, 접속매체에 관계없이 동작할 수 있는 개방성.
3. OSI 7 Layer vs TCP/IP
   - 두 모델 모두 계층형
   - TCP/IP는 인터넷 개발 이후 계속 표준화되어 신뢰성이 우수. OSI 7 Layer는 구현되는 예가 없어 신뢰성 저하.
   - OSI 7 Layer : 장비 개발과 통신 자체를 어떻게 표준으로 잡을지 사용
   - TCP/IP : 실질적인 통신 자체에 사용

---

- OSI 7 Layer

![8_5](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/8_5.jpg)

| Layer | 명칭             | 설명                                                         | 전송 단위 | 장비           | 프로토콜             |
| ----- | ---------------- | ------------------------------------------------------------ | --------- | -------------- | -------------------- |
| 1     | 물리 계층        | 물리적 전송 매체와 전송 신호 방식을 정의.                    | Bit       | Repeater, Hub  | DHCP, DNS, FTP, HTTP |
| 2     | 데이터 링크 계층 | 흐름 제어 기능(송신 측과 수신 측의 속도 차이 해결)<br />프레임의 동기화 기능<br />오류제어 기능<br />순서제어 기능 | Frame     | Bridge, switch | JPEG, MPEG, SMB, AFP |
| 3     | 네트워크 계층    | 네트워크 연결을 관리, 데이터의 교환 및 중계 기능<br />경로 설정(Routing), 데이터 교환 및 중계, 트래픽 제어, 패킷 정보 전송 | Packet    | Router         | SSH, TLS             |
| 4     | 전송 계층        | 종단 시스템(End-to-End) 간에 투명한 데이터 전송을 가능하게 함<br />주소 설정, 다중화, 오류제어, 흐름제어기능<br />TCP(신뢰성), UDP(비신뢰성) | Segment   | Gateway        | TCP, UDP, ARP        |
| 5     | 세션 계층        | 세션을 구축하고 관리.<br />송,수신 측 간의 동기를 위해 체크섬. | Message   |                | IP, ICMP, IGMP       |
| 6     | 표현 계층        | 서로 다른 데이터 표현을 갖는 시스템 간의 상호 접속을 위함.<br />코드 변환, 데이터 암호화, 데이터 압축, 정보 형식 변환 | Message   |                | MAC, PPP             |
| 7     | 응용 계층        | 사용자가 OSI 환경에 접근할 수 있도록 서비스 제공.            | Message   |                | Ethernet, RS-232C    |

---

- TCP/IP

| Layer                | 각 계층 Protocol                                             |
| -------------------- | ------------------------------------------------------------ |
| Network Access Layer | 이더넷                                                       |
| Internet Layer       | IP(Internet Protocol)<br />ICMP(Internet Control Message Protocol)<br />IGMP(Internet Group Message Protocol)<br />ARP(Address Resolution Protocol)<br />RARP(Reverse Address Resolution Protocol) |
| Transport Layer      | TCP(Transmission Control Protocol)<br />UDP(User Datagram Protocol)<br />SCTP(Stream Control Transmission Protocol) |
| Application Layer    | FTP(File Transfer Protocol)<br />VSFTP(Very Secure File Transfer Protocol)<br />SNMP(Simple Network Management Protocol)<br />SMTP(Simple Mail Transfer Protocol)<br />HTTP(Hyper Text Transfer Protocol)<br />HTTPs(Hyper Text Transfer Protocol Secure)<br />DNS(Domain Name System) |



- 각 계층별 대표적 프로토콜

| 계층                      | 프로토콜                                                     |
| ------------------------- | ------------------------------------------------------------ |
| 7 Application 응용계층    | HTTP, SMTP, SNMP, FTP, Telnet, SSH & Scp, NFS, RTSP          |
| 6 Presentation 표현계층   | JPEG, MPEG, XDR, ASN.1, SMB, AFP                             |
| 5 Session 세션계층        | TLS, SSH, ISO 8327 / CCITT X.225, RPC, NetBIOS, AppleTalk    |
| 4 Transport 전송계층      | TCP, UDP, RTP, SCTP, SPX, AppleTalk                          |
| 3 Network 네트워크계층    | IP, ICMP, IGMP, X.25, CLNP, ARP, RARP, BGP, OSPF, RIP, IPX, DDP |
| 2 Datalink 데이터링크계층 | Ethernet, Token Rin, PPP, HDLC, Frame relay, ISDN, ATM, 무선랜, FDDI |
| 1 Physical 물리계층       | 전선, 전파, 광섬유, 동축케이블, 도파관, PSTN, Repeater, DSU, CSU, Modem |





---

## 3. 데이터베이스 설계 ...

데이터베이스 설계 과정에서 목표 DBMS의 구현 데이터 모델로 표현한 데이터베이스 스키마가 도출되는 단계는?


![2015_9L_3](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_3.jpg)

**답 : ③**

③

- 개념적 ; 현실 세계의 실체를 데이터베이스로 저장하기 위해서 개념 세계의 개체로 구체화 하는 과정.
  - ER model 객체-관계 모델
    - 개체 ; 사각형
    - 관계 ; 다이아몬드
    - 타원 ; 개체 또는 관계의 속성.
- 논리적 ; DBMS가 이해할 수 있는 논리적인 데이터 구조로 변환
  - 관계형 데이터모델
  - 네트워크형 데이터모델
  - 계층형 데이터모델
- 물리적 ; 논리적 데이터 구조를 컴퓨터에 저장하도록 물리적 데이터 구조로 변환하는 과정.



- 데이터베이스 설계 시 고려사항
  - 데이터의 일관성 consistency
  - 효율성 efficiency
  - 회복 recovery
  - 무결성 integrity
  - 보안 Security
  - 확장성 expansibility



- 데이터베이스 설계 순서
  - 요구사항 분석 - 개념적 설계 - 논리적 설계(논리적 설계 이후 스키마 도출) - 물리적 설계 - 구현.



---

## 4. 객체지향 프로그래밍의 ...

객체지향 프로그래밍의 특징 중 상속 관계에서 상위 클래스에 정의된 메소드(method) 호출에 대해 각 하위 클래스가 가지고 있는 고유한 방법으로 응답할 수 있도록 유연성을 제공하는 것은?


![2015_9L_4](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_4.jpg)

**답 : ③**

① 재사용성 reusability

- 기존 시스템에 추가적인 기능을 덧붙이거나 수정하여, 기존 시스템을 그래도 사용할 수 있는 능력.

② 추상화 abstraction

- 복잡한 자료, 모듈, 시스템 등으로부터 핵심적인 개념 또는 기능을 간추려 내는 것.

③ 다형성 polymorphism

- 프로그래밍 언어의 자료형 체계의 성질을 나타내는 것. 프로그램 언어의 각 요소들(상수, 변수, 식, 오브젝트, 함수, 메소드 등)이 다양한 자료형(type)에 속하는 것이 허가되는 성질을 가리킨다.

④ 캡슐화 encapsulation

- 객체의 속성(data fields)과 행위(메서드, methods)를 하나로 묶고, 실제 구현 내용 일부를 외부에 감추어 은닉한다.



---

## 5. 다음은 캐시 기억장치를...

다음은 캐시 기억장치를 사상(mapping) 방식 기준으로 분류한 것이다. 캐시 블록은 4개 이상이고 사상 방식을 제외한 모든 조건이 동일하다고 가정할 때, 평균적으로 캐시 적중률(hit ratio)이 높은 것에서 낮은 것 순으로 바르게 나열한 것은?


![2015_9L_5](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_5.jpg)

**답 : ②**

- 캐시 기억장치의 사상 Mapping
  - 캐시 기억장치와 주기억장치 사이에서 정보를 옮기는 것을 사상.
  - 직접 사상 Direct Mapping
  - 연관 사상 Associate Mapping = 완전연관 사상
  - 집합 연관 사상 Set Associate Mapping



- 직접 사상 Direct Mapping

  - 메인메모리의 데이터 블록이 지정된 캐시라인에만 들어갈 수 있음.
  - 워드 ; 하나의 번지에서 저장되는 데이터의 단위.
  - 블럭 ; 4워드면 캐시 한 라인도 4워드.
  - 라인 ; 캐시기억장치 각 슬롯에 저장되는 데이터 값.

- 연관 사상 Associate Mapping

  - 메인메모리의 데이터 블록이 아무 캐시라인에나 들어갈 수 있음.

- 집합 연관 사상 Set Associate Mapping

  - 메인메모리의 데이터 블록이 복수의 캐시라인을 묶은 지정된 세트에만 들어갈 수 있음.

    | 매핑 방식                 | 캐시 적중 성능                                               |
    | ------------------------- | ------------------------------------------------------------ |
    | 직접매핑 캐시             | 가장 간단하고 가장 빠른 적중검사<br>실패율이 높아 가장 나쁜 성능 |
    | 2-방향 세트연관 캐시      | 2-way                                                        |
    | 4-방향 세트연관 캐시      | 4-way                                                        |
    | n-방향 세트연관 캐시(n>4) | 8-way, 16-way etc..                                          |
    | 완전연관 캐시             | 가장 복잡하지만 가장 낮은 실패율<br>가장 좋은 성능           |

    



---

## 6. 다음 논리회로의 ...

다음 논리회로의 부울식으로 옳은 것은?


![2015_9L_6](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_6.jpg)

**답 : ③**

(AC')' + BC

= A' + C + BC

= A' + C



① F = AC' + BC

② F(A, B, C) = ∑m(0, 1, 2, 3, 6, 7) = m0+m1+m2+m3+m6+m7 = A' + B

④ F = (A' + B' + C)(A + B' + C') = M6*M3 = m0+m1+m2+m4+m5+m7 = A'C' + AC + B'



- 최소항 Minterm의 합(OR)
- 최대항 Maxterm의 곱(AND)

|      |      |      | 최소항   |      | 최대항       |      |
| ---- | ---- | ---- | -------- | ---- | ------------ | ---- |
| x    | y    | z    | 항       | 표현 | 항           | 표현 |
| 0    | 0    | 0    | x' y' z' | m0   | x + y + z    | M0   |
| 0    | 0    | 1    | x' y' z  | m1   | x + y + z'   | M1   |
| 0    | 1    | 0    | x' y z'  | m2   | x + y' + z   | M2   |
| 0    | 1    | 1    | x' y z   | m3   | x + y' + z'  | M3   |
| 1    | 0    | 0    | x y' z'  | m4   | x' + y + z   | M4   |
| 1    | 0    | 1    | x y' z   | m5   | x' + y + z'  | M5   |
| 1    | 1    | 0    | x y z'   | m6   | x' + y' + z  | M6   |
| 1    | 1    | 1    | x y z    | m7   | x' + y' + z' | M7   |





## 7. 소프트웨어 개발 ...

소프트웨어 개발 프로세스 모델 중 하나인 나선형 모델(spiral model)에 대한 설명으로 옳지 않은 것은?


![2015_9L_7](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_7.jpg)

**답 : ④**

④ 관리가 복잡하여 대규모 시스템의 소프트웨어 개발에는 ~~적합하지 않다.~~

==> 적합하다.

==> 폭포수 모델이 소규모 시스템 개발에 적합하다.



- 소프트웨어 생명주기 모형

| 생명주기 모형                                         | 정의                                                         | 장점                                                         | 단점                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 폭포수 모형<br />=Waterfall Model<br />=선형순차 모형 | 체계적인 원리<br />단계별 결과물이 명확히 나옴<br />적용사례 많음<br />가장 오래되었고 널리 사용 | **기존 시스템**을 보완하는 데 적합<br />**소규모 시스템** 개발에 적합 | **신규 시스템 개발에는 부적합**<br />**문서화**에 치중<br />병행되거나 이전 단계로 이동이 불가<br />검출되지 않은 실수가 큰 손실<br />개발 중 새로운 요구 반영 어려움 |
| 프로토타이핑 모형<br />=Prototyping<br />원형 모형    | 모델을 사전에 만듦.<br />개발자가 사용자의 요구 파악         | 초기에 **사용자의 의도 파악** 용이                           | 견본품의 폐기가 가능<br />사용자는 견본품을 실제품으로 착각<br />기능이 제한적<br />낮은 신뢰성 |
| 나선형 모형<br />=Spiral Model                        | 폭포수 모형과 원형 모형을 결합<br />1~4 과정을 반복적으로 수행<br />1. 계획<br />2. 위험분석<br />3. 공학<br />4. 사용자평가 | **대규모 시스템** 개발에 적합<br />개발 시 생기는 위험을 최소화<br />위험성 평가에 크게 의존<br /> | 계속적인 변경은 소프트웨어의 구조를 훼손                     |
| V-모형<br />V-Diagram                                 | 폭포수 모델의 변형<br />작업과 결과의 검증에 초점<br />분석과 설계단계는 왼편(개발)<br />테스팅과 유지보수단계는 오른편(검증) | 오류발견 시, 이전 단계로 이동 가능<br />신뢰성이 높은 분야에 적합 |                                                              |
| 익스트림 프로그래밍<br />=XP, eXtreme Programming     | 애자일 기법 중 하나로 점증적 방법 변형<br />고객의 참여를 극한까지 유도<br />코드 작성 전, 업무에 대한 시험 준비<br />**시험 우선 개발** | 점증적인 시험 개발<br />사용자 참여<br />**자동화**된 시험 장치의 사용 |                                                              |
| UP(Unified Process) 모형                              | 유즈케이스(usecase, 사용사례) 기반<br />구조중심<br />반복적이고 점증적<br />개발단계<br />1. 개념 정립(도입, Inception)<br />2. 전개(정련, Elaboration)<br />3. 구축(Construction)<br />4. 전환(전이, Transition) |                                                              |                                                              |
| 스크럼(Scrum)                                         | 솔루션에 포함할 기능에 대한 우선순위 부여<br />개발주기는 30일<br />날마다 15분 회의<br />항상 팀 단위로 생각<br />구분 없는 열린 공간. 원활한 의사소통 |                                                              |                                                              |



---

## 8. 다음 표는 단일 CPU에...

다음 표는 단일 CPU에 진입한 프로세스의 도착 시간과 처리하는 데 필요한 실행 시간을 나타낸 것이다. 프로세스 간 문맥 교환에 따른 오버헤드는 무시한다고 할 때, SRT(Shortest Remaining Time) 스케줄링 알고리즘을 사용한 경우 네 프로세스의 평균 반환시간(turnaround time)은?


![2015_9L_8](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_8.jpg)

**답 : ②**

| 프로세스 | 도착시간 | 실행시간 | 0-2  | Rem  | 2-4  | Rem  | 4-5  | Rem  | 5-7  | Rem  | 7-11 | Rem  | 11-17 | Rem  | 작업완료 | 반환시간 |
| -------- | -------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----- | ---- | -------- | -------- |
| P1       | 0        | 8        | P1   | 6    |      | 6    |      | 6    |      | 6    |      | 6    | P1    | 0    | 17       | 17       |
| P2       | 2        | 4        |      | 4    | P2   | 2    |      | 2    | P2   | 0    |      |      |       |      | 7        | 5        |
| P3       | 4        | 1        |      |      |      | 1    | P3   | 0    |      |      |      |      |       |      | 5        | 1        |
| P4       | 6        | 4        |      |      |      |      |      |      |      | 4    | P4   | 0    |       |      | 11       | 5        |

평균 반환시간 = (17+5+1+5)/4 = 28/4 = 7



---

## 9. 이더넷(Ethernet)의 ...

이더넷(Ethernet)의 매체 접근 제어(MAC) 방식인 CSMA/CD에 대한 설명으로 옳지 않은 것은?


![2015_9L_9](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_9.jpg)

**답 : ①**

① CSMA/CD 방식은 CSMA 방식에 충돌 검출 기법을 추가한 것으로 IEEE 802.11b의 MAC 방식으로 사용된다.





---

## 10. 다음은 C언어로 내림차순...

다음은 C언어로 내림차순 버블정렬 알고리즘을 구현한 함수이다. ㄱ에 들어갈 if문의 조건으로 올바른 것은? (단, size는 1차원 배열인 value의 크기이다)


![2015_9L_10](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_10.jpg)

**답 : ④**

①

②

③

④



---

## 11. 객체지향 기법을 ...

객체지향 기법을 지원하지 않는 프로그래밍 언어는?


![2015_9L_11](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_11.jpg)

**답 : ①**

①

②

③

④



---

## 12. 관계형 모델(relational...

관계형 모델(relational model)의 릴레이션(relation)에 대한 설명으로 옳지 않은 것은?


![2015_9L_12](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_12.jpg)

**답 : ④**

①

②

③

④



---

## 13. 컴퓨터 버스에 ...

컴퓨터 버스에 대한 설명으로 옳지 않은 것은?


![2015_9L_13](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_13.jpg)

**답 : ①**

①

②

③

④



---

## 14. 다음 이진 트리...

다음 이진 트리(binary tree)의 노드들을 후위 순회(post-order traversal)한 경로를 나타낸 것은?


![2015_9L_14](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_14.jpg)

**답 : ②**

①

②

③

④



---

## 15. 프로토콜에 대한...

프로토콜에 대한 설명으로 옳지 않은 것은?


![2015_9L_15](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_15.jpg)

**답 : ①**

①

②

③

④



---

## 16. 비결정적 유한 오토마타...

비결정적 유한 오토마타(non-deterministic finite automata)에 대한 설명으로 옳지 않은 것은?


![2015_9L_16](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_16.jpg)

**답 : ④**

①

②

③

④



---

## 17. 클라우드 컴퓨팅...

클라우드 컴퓨팅 서비스 모델과 이에 대한 설명이 바르게 짝지어진 것은?


![2015_9L_17](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_17.jpg)

**답 : ③**

①

②

③

④



---

## 18. 다음 C 언어로...

다음 C 언어로 작성된 프로그램의 실행 결과에서 세 번째 줄에 출력되는 것은?


![2015_9L_18](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_18.jpg)

**답 : ③**

①

②

③

④



---

## 19. 서브넷 마스크(subnet...

서브넷 마스크(subnet mask)를 255.255.255.224로 하여 한 개의 C클래스 주소 영역을 동일한 크기의 8개 하위 네트워크로 나누었다. 분할된 네트워크에서 브로드캐스트를 위한 IP 주소의 오른쪽 8비트에 해당하는 값으로 옳은 것은?


![2015_9L_19](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_19.jpg)

**답 : ③**

①

②

③

④



---

## 20. 연결리스트(linked...

연결리스트(linked list)의 'preNode' 노드와 그 다음 노드 사이에 새로운 'newNode' 노드를 삽입하기 위해 빈 칸 ㄱ에 들어갈 명령문으로 옳은 것은?


![2015_9L_20](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_20.jpg)

**답 : ②**

①

②

③

④