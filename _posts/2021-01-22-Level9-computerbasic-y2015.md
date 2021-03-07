---
title: "2015년 9급 전산직 컴퓨터일반 풀이"
strapline: "컴퓨터일반 풀이"
description: "2015년 9급 전산직 컴퓨터일반 풀이"
header:
 overlay_image: /assets/images/bright.jpg
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

![2015_9L_1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_1.jpg)

**답 : ①**

① 스프레드시트 

- 표 형식으로 데이터의 조직, 분석, 저장을 가능케 하는 상호작용의 컴퓨터 애플리케이션.
- 경리, 회계 등의 계산을 위해 사용되는 표 형식의 계산용지나, 계산용지를 컴퓨터에서 사용할 수 있게 구현한 표 계산 프로그램을 의미.



---

## 2. OSI 7계층 중 ...

OSI 7계층 중 브리지(bridge)가 복수의 LAN을 결합하기 위해 동작하는 계층은?


![2015_9L_2](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_2.jpg)

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


![2015_9L_3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_3.jpg)

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


![2015_9L_4](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_4.jpg)

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


![2015_9L_5](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_5.jpg)

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


![2015_9L_6](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_6.jpg)

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


![2015_9L_7](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_7.jpg)

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


![2015_9L_8](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_8.jpg)

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


![2015_9L_9](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_9.jpg)

**답 : ①**

① ~~CSMA/CD 방식은~~ CSMA 방식에 충돌 검출 기법을 추가한 것으로 IEEE 802.11b의 MAC 방식으로 사용된다.

==> CSMA/CA 방식.



- 통신망의 종류

- 근거리 통신망 LAN

  - Local Area Network. 사무실, 빌딩, 공장 등 제한된 지역에서 정보처리장치를 연결하기 위하여 최적화되고 신뢰성 있는 통신채널을 제공하는 네트워크.

  - 경로선택이 필요없어(항상 일정 경로) 네트워크 제어가 쉽다.

  - 전송매체에 의한 분류

    - 평형 케이블 Twisted Pair ; 가격 저렴. 전기적잡음에 약함. 대역폭이 좁음. PC용이나 소규모 LAN. 10Base-T
    - 동축 케이블 Coaxial Cable ; 가격 비교적 저렴. 10Base5, 10Base2, 10Broad36
    - 광 케이블 Optical Fiber ; 가장 넓은 대역폭. 고속통신이 가능. 접속에 어려움. 10Base-F

  - LAN 통신구조

    - 하위 2개 계층 사용. 물리계층. 데이터링크계층
    - 물리계층
    - 데이터링크 계층 ; MAC 계층과 논리 링크 제어 계층으로 분류.
      - MAC Media Access Control 매체 접근 제어 계층
      - IEEE 802.2 : 논리링크제어LLC 계층의 이행에 대한 표준 프로토콜
      - IEEE 802.3 : 이더넷 표준. CSMA/CD 엑세스 제어 방식 사용.
      - IEEE 802.4 : 토큰버스 액세스 제어 방식 사용.
      - IEEE 802.5 : 토큰링 액세스 제어 방식 사용.
      - IEEE 802.6 : 도시권 통신망(MAN) 규격으로 이중 버스 구조.
      - IEEE 802.11 : Wi-Fi라고도 하며, 무선 LAN 규격으로써 CSMA/CA 액세스 제어 방식을 사용.
      - IEEE 802.11b : 최소 전송속도 11Mbps. 실제 6-7Mbps
      - IEEE 802.11a : 5GHz 대역. 54Mbps
      - IEEE 802.11g : 2.4GHz. 54Mbps
      - IEEE 802.11n : 2.4GHz & 5GHz, 600Mbps
      - IEEE 802.11i : Wi-Fi의 암호화 국제표준. 802.11의 WEP(Wired Equivalent Privacy)는 최초 무선 암호화 방식이지만, 암호화 키 값이 고장되어 있어 쉽게 크랙당할 우려가 있어, WEP를 보완한 WPA(Wi-Fi Protected Access) 무선암호화 방식을 사용.
      - IEEE 802.15 : 소규모 무선랜 기술(블루투스, WPAN) ; 가정용 무선랜 = bluetooth.

  - 매체 접근 제어방식 MAC, Media Access Control

    - 경쟁 방식 ; ALOHA, CSMA, CSMA/CD, CSMA/CA

    - 비경쟁 방식 ; Token Passing(Token Ring, Token Bus)

    - ALOHA ; 하와이 대학. 반송파 감지기능이 없으며, 충돌 감지 기능이 없다. 충돌이 일어나면 일정시간 후에 재전송

    - CSMA ; 반송파 감지 다중 접속 Carrier Sense Multiple Access

      - 반송파를 감지하여 회선 사용 가능 여부를 판단, 접속을 개시하거나 대기하는 다중접속방식
      - 데이터 프레임을 송신하기에 앞서 타인의 반송파가 없으면 즉시 프레임을 보내고, 반송파가 검출되면 적당한 시간만큼 기다린 다음 다시 시도.
      - 충돌  감지 기능이 없으며, 충돌이 발생하면 임의의 시간 동안 대기한 후에 전송 채널을 감지하는 과정을 다시 반복.

    - CSMA/CD

      - 반송파 감지 다중 접근/충돌 탐지(Carrier Sense Multiple Access With Collision Detection)
      - 두개 이상의 노드가 동시에 전송을 시작하면 전송 중인 프레임은 충돌이 발생하며, 노드가 충돌을 감지하면 보내던 데이터 프레임의 전송을 중단.

    - CSMA/CA

      - 반송파 감지 다중 접근/충돌 회피(Carrier Sense Multiple Access/Collision Avoidance)
      - 무선 LAN(Wi-Fi)
      - 충돌을 대비하여 예비(확인) 신호를 전송. 예비신호가 충돌없이 전송된 것을 확인하면 데이터를 보낸다.

    - 토큰 패싱

      |         | 반송파 감지 | 충돌 감지  |
      | ------- | ----------- | ---------- |
      | ALOHA   | X           | X          |
      | CSMA    | O           | X          |
      | CSMA/CD | O           | O          |
      | CSMA/CA | O           | 필요 없음. |

      

      | Network          | 데이터 속도 | 매체 접근 방법 | 신호방식                     | 오류제어 |
      | ---------------- | ----------- | -------------- | ---------------------------- | -------- |
      | Ethernet         | 10 Mbps     | CSMA/CD        | Manchester(디지털 부호 체계) | No       |
      | Fast Ethernet    | 100 Mbps    | CSMA/CD        | Several                      | No       |
      | Gigabit Ethernet | 1 Gbps      | CSMA/CD        | Several                      | No       |
      | Token Ring       | 4/16 Mbps   | Token Ring     | Differential Manchester      | Yes      |
      | FDDI             | 100 Mbps    | Token Ring     | 4B/5B, NRZ-I                 | Yes      |

  



---

## 10. 다음은 C언어로 내림차순...

다음은 C언어로 내림차순 버블정렬 알고리즘을 구현한 함수이다. ㄱ에 들어갈 if문의 조건으로 올바른 것은? (단, size는 1차원 배열인 value의 크기이다)


![2015_9L_10](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_10.jpg)

**답 : ④**





---

## 11. 객체지향 기법을 ...

객체지향 기법을 지원하지 않는 프로그래밍 언어는?


![2015_9L_11](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_11.jpg)

**답 : ①**

- LISP
  - 함수형 언어.

- 객체지향 언어
  - 시뮬라 Simula 67
  - 스몰토크
  - 비주얼 베이직 닷넷
  - 오브젝티브-C
  - C++
  - C#
  - 자바
  - 객체지향 파스칼
  - 델파이
  - 파이썬
  - 펄
  - 루비
  - 액션스크립트
  - ASP
  - 스위프트



---

## 12. 관계형 모델(relational...

관계형 모델(relational model)의 릴레이션(relation)에 대한 설명으로 옳지 않은 것은?


![2015_9L_12](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_12.jpg)

**답 : ④**

④ 한 릴레이션의 속성들은 ~~고정된~~ 순서를 갖는다.

==> 순서에 영향을 받지 않는다.



---

## 13. 컴퓨터 버스에 ...

컴퓨터 버스에 대한 설명으로 옳지 않은 것은?


![2015_9L_13](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_13.jpg)

**답 : ①**

① 주소 정보를 전달하는 주소 버스(address bus), 데이터 전송을 위한 데이터 버스(data bus), 그리고 ~~명령어 전달을 위한 명령어 버스(instruction bus)~~로 구성된다.

- 버스
  - 데이터 버스 ; 시스템 모듈들 간의 데이터 이동 경로를 제공
  - 주소 버스 ; 데이터의 근원지나 목적지의 일정한 메모리 주소를 전달.
  - 제어 버스 ; 데이터 버스와 주소 버스를 제어하기 위해 사용.
- 동기식 버스 vs 비동기식 버스
  - 동기식 버스
    - 정해진 시간에 데이터를 전송하는 방법. 
    - 장 ; 논리회로가 간단. 단 ; 느린 장비도 정해진 clock에 맞춰야 함.
  - 비동기식 버스
    - 서로 데이터를 주고 받을 준비가 되어있는지 확인하는 핸드쉐이킹 프로토콜을 사용하여 수신측에서 준비가 되었으면 바로 전송.
    - 장 ; 시간 낭비가 적다. 단 ; 회로 구성이 복잡. 핸드쉐이킹하는 과장이 필요해 속도가 느림.
- PCIe
  - 버스의 특징이 공용 선이라는 것인데 이 특징 덕분에 한 쪽이 데이터 선을 점령하면 다른 쪽에서는 신호 중첩을 유발시킬 수 있어서 사용을 하면 안된다. 이 점을 보완하기 위해 점대점 상호연결방식이 등장하였다.
  - QPI Quick Path Interconnect
    - 다른 구성요소와 직접 연결하는 점대점 상호방식 중 하나로 레이어로 구성된 프로토콜 구조이므로 물리적으로 연결되어 있는 부분부터 오류의 존재 여부를 점검하는 등 각각의 레이어에서 하는 일이 구분되어 있다. 고속, 고효율의 패킷 기반의 전송방식을 사용하며 인텔의 i7 데스크톱 프로세서 이후로 사용되어지는 방식이다.
  - PCIe Peripheral Component Interconnect Express
    - 버스를 1대1로 연결해서 택시로 만들었다. 높은 용량 덕분에 기가이더넷과 같은 빠른 데이터 속도의 I/O 디바이스를 지원하는데 사용되어지며 각각의 버스마다 독립적인 데이터 흐름을 제공하여 많이 사용되어 진다. 또한 핀수가 적고 물리적 면적이 작으며 상세한 오류검출 및 보고구조 등의 장점을 가지고 있다. 최근엔 I/O 가상화도 지원한다.



---

## 14. 다음 이진 트리...

다음 이진 트리(binary tree)의 노드들을 후위 순회(post-order traversal)한 경로를 나타낸 것은?


![2015_9L_14](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_14.jpg)

**답 : ②**





---

## 15. 프로토콜에 대한...

프로토콜에 대한 설명으로 옳지 않은 것은?


![2015_9L_15](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_15.jpg)

**답 : ①**

① ARP는 ~~데이터 링크 계층의 프로토콜로 MAC 주소에 대해 해당 IP 주소를 반환해준다.~~

==>  전송계층

==> ARP ; IP -> MAC

==> RARP ; MAC -> IP







---

## 16. 비결정적 유한 오토마타...

비결정적 유한 오토마타(non-deterministic finite automata)에 대한 설명으로 옳지 않은 것은?


![2015_9L_16](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_16.jpg)

**답 : ④**

④ 모든 문맥 자유 언어(context-free language)를 인식한다.

==> 문맥 자유 문법으로 생성. pushdown automata에 의해 인식.





---

## 17. 클라우드 컴퓨팅...

클라우드 컴퓨팅 서비스 모델과 이에 대한 설명이 바르게 짝지어진 것은?


![2015_9L_17](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_17.jpg)

**답 : ③**





---

## 18. 다음 C 언어로...

다음 C 언어로 작성된 프로그램의 실행 결과에서 세 번째 줄에 출력되는 것은?


![2015_9L_18](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_18.jpg)

**답 : ③**

func(5) : 120

func(3) : 6

func(1) : 1



---

## 19. 서브넷 마스크(subnet...

서브넷 마스크(subnet mask)를 255.255.255.224로 하여 한 개의 C클래스 주소 영역을 동일한 크기의 8개 하위 네트워크로 나누었다. 분할된 네트워크에서 브로드캐스트를 위한 IP 주소의 오른쪽 8비트에 해당하는 값으로 옳은 것은?


![2015_9L_19](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_19.jpg)

**답 : ③**

IPv4 ; 32bit

IPv6 ; 128bit

- 클래스의 분류
  - class A ; 0~       00000000     0.0.0.0 ~ 127.255.255.255
  - class B ; 10~     10000000 128.0.0.0 ~ 191.255.255.255
  - class C ; 110~   11000000 192.0.0.0 ~ 223.255.255.255
  - class D ; 1110~ 11100000 224.0.0.0 ~ 239.255.255.255
  - class E ; 1111~ 11110000  240.0.0.0 ~ 255.255.255.255
- IPv4의 전송방법에 따른 분류
  - 유니캐스트 1:1 ; 특정인에게 전송
  - 멀티캐스트 1:N ; 특정 다수인에게 전송
  - 브로드캐스트 1:ALL ; 불특정 다수인에게 전송 ==> IPv6에서는 Broadcast가 Multicast로 바뀜.

- Subnetting

  - 서브넷 마스크에서 1로 표현된 부분은 네트워크, 0인 부분은 호스트를 나타낸다.
  - 클래스 C의 디폴트 서브넷 마스크 ; 255.255.255.0
  - 클래스 B의 디폴트 서브넷 마스크 ; 255.255.0.0
  - 클래스 A의 디폴트 서브넷 마스크 ; 255.0.0.0
  - 호스트 주소 부분이 모두 0인 경우는 서브넷 주소 자체를 의미. 
  - 호스트 주소 부분이 모두 1인 경우는 브로드캐스트 주소를 의미.

- 예. B클래스 주소에서 호스트 주소 8비트를 서브네팅 하는 경우.

  - B클래스. 디폴트 서브넷 마스크 255.255.0.0. 2<sup>16</sup>개의 네트워크로 구분하여. 2<sup>16</sup> - 2개(네트워크, 브로드캐스트)의 호스트를 가진 2<sup>16</sup>개의 네트워크.
  - B클래스. 서브넷 마스크 255.255.255.0. 2<sup>24</sup>개의 네트워크로 구분하여. 2<sup>8</sup> - 2개(네트워크, 브로드캐스트)의 호스트를 가진 2<sup>24</sup>개의 네트워크.

- 슈퍼네팅.supernetting. 

  - 서브네팅의 반대 개념. 부족한 IP를 효율적으로 사용하기 위해 여러 개의 C 클래스 주소를 하나의 네트워크로 구성하는 방식.
  - 예. 8개의 연속된 C클래스 주소를 하나로 묶는 경우.
    - 3비트의 네트워크 주소가 추가로 필요. 슈퍼넷 마스크 ; 255.255.248.0 = 11111111.11111111.11111000.00000000
    - 0의 갯수인 11개. 11비트를 호스트 주소로 사용.2<sup>11</sup>개의 호스트 가능.

- CIDR Classless Inter-Domain Routing

  - A, B, C 클래스 별로 IP 주소를 구분하지 않고 네트워크 주소 범위를 자유롭게 지정할 수 있도록 함.
  - 예. 220.66.32.0/21    21 ; 상위 21비트가 네트워크 주소. 하위 11비트는 호스트 주소.
  - 예. 네트워크 주소 203.252.48.0에서부터 203.252.55.0까지 8개의 네트워크 주소를 CIDR을 이용하여 표현한 경우
    - 48은 이진수로 0011 0000, 55는 0011 0111
    - 네트워크 주소 하위 3비트만 다르고 나머지 비트는 동일.
    - 203.252.48.0/21로 표기. 8개의 네트워크 주소를 한꺼번에 표현.

- IP 알리어스 IP Alias

  - 하나의 NIC Network Interface Card에 여러 개의 IP 주소를 할당하는 것.

- 예.

  - 210.100.100.3 --> C클래스에 속함.

  - 서브네팅이 없으면 디폴트 서브넷 마스크 255.255.255.0

  - IP주소 AND 서브넷마스크 = 네트워크 주소

    |               | 10진수 표현   | 2진수 표현                                    |
    | ------------- | ------------- | --------------------------------------------- |
    | IP주소        | 210.100.100.3 | 1101 0010   0110 0100   0110 0100   0000 0011 |
    | 서브넷마스크  | 255.255.255.0 | 1111 1111   1111 1111   1111 1111   0000 0000 |
    | 네트워크 주소 | 210.100.100.0 | 1101 0010   0110 0100   0110 0100   0000 0000 |

  - 해당 네트워크를 3개의 작은 서브 네트워크로 나누려 한다.

  - 2<sup>1</sup> < 3 < 2<sup>2</sup>   따라서 최소한 2비트의 서브넷 마스크가 필요. 

  - ==> 네트워크 부분의 2비트가 추가로 필요. (디폴트는 16비트를 주소로, 8비트를 호스트로 사용.)

  - 따라서 255.255.255.192의 서비넷 마스크를 적용

    |               | 10진수 표현     | 2진수 표현                                    |
    | ------------- | --------------- | --------------------------------------------- |
    | IP주소        | 210.100.100.3   | 1101 0010   0110 0100   0110 0100   0000 0011 |
    | 서브넷마스크  | 255.255.255.192 | 1111 1111   1111 1111   1111 1111   1100 0000 |
    | 네트워크 주소 | 210.100.100.0   | 1101 0010   0110 0100   0110 0100   0000 0000 |

  - 새로운 서브넷마스크로 서브넷팅한 결과로 아래와 같이 총 4개의 서브넷을 얻을 수 있어 기존의 3개의 서브넷의 요구사항을 만족한다.

    |         | 네트워크 주소   | 사용가능한 호스트 범위            | 브로드캐스트 주소 |
    | ------- | --------------- | --------------------------------- | ----------------- |
    | 서브넷1 | 210.100.100.0   | 210.100.100.1 ~ 210.100.100.62    | 210.100.100.63    |
    | 서브넷2 | 210.100.100.64  | 210.100.100.65 ~ 210.100.100.126  | 210.100.100.127   |
    | 서브넷3 | 210.100.100.128 | 210.100.100.129 ~ 210.100.100.190 | 210.100.100.191   |
    | 서브넷4 | 210.100.100.192 | 210.100.100.193 ~ 210.100.100.254 | 210.100.100.255   |

- 예.
  - IP가 203.10.24.27. 서브넷마스크 255.255.255.240,   네트워크의 호스트 범위와 브로드캐스트 주소는?
  - 호스트 : 203.10.24.17 ~ 203.10.24.30    브로드캐스트 : 203.10.24.31
- 예.
  - 클래스 B주소를가지고 서브넷 마스크 255.255.255.240으로 서브넷을 만들었을 때, 나오는 서브넷의 수와 호스트 수는?
  - 서브넷의 수 : 2<sup>12</sup> = 4096    한 서브넷의 호스트 수 : 14



---

## 20. 연결리스트(linked...

연결리스트(linked list)의 'preNode' 노드와 그 다음 노드 사이에 새로운 'newNode' 노드를 삽입하기 위해 빈 칸 ㄱ에 들어갈 명령문으로 옳은 것은?


![2015_9L_20](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2015_9L/2015_9L_20.jpg)

**답 : ②**