---
title: "2014년 9급 전산직 컴퓨터일반 풀이"
strapline: "컴퓨터일반 풀이"
description: "2014년 9급 전산직 컴퓨터일반 풀이"
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

# 2014년 9급 전산직 컴퓨터일반 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1.  데이터베이스에서 ...

 데이터베이스에서 트랜잭션(transaction)이 가져야 할 ACID 특성으로 옳지 않은 것은?


![2014_9L_1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_1.jpg)

**답 : ④**

- ACID
  - Atomicity 원자성
    - 트랜잭션은 완전하게 끝나거나 수행하지 않아야 한다.
  - Consistency 일관성
    - 트랜잭션 실행 이전과 이후 일관성이 유지.
  - Isolation 고립성
    - 동시에 실행되는 transaction은 서로를 방해하지 않아야 하며, 실행 단계에 있는 트랜잭션은 다른 트랜잭션이 볼 수 없어야 한다.
  - Durability 지속성=영속성
    -  트랜잭션이 발생하고 나서 반영된 내용은 이후의 어떤 문제가 발생하더라도 손실되지 않아야 한다.





---

## 2. 운영체제에 대한 ...

운영체제에 대한 설명으로 옳은 것만을 모두 고르면?


![2014_9L_2](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_2.jpg)

**답 : ③**

ㄴ. ~~스풀링(spooling)~~은 CPU와 입출력 장치의 속도 차이를 줄이기 위해 주기억장치의 일부분을 버퍼처럼 사용하는 것이다.

==> 캐시(Cache)

- 스풀링(spooling) ; 버퍼링의 일종. 주변장치와 중앙처리장치의 처리속도 차이에 의한 대기시간을 줄이기 위해 사용하는 기법.

ㄷ. RR robin은 선점 방식이다.





---

## 3. 열거된 메모리들을 ...

열거된 메모리들을 처리 속도가 빠른 순서대로 바르게 나열한 것은?


![2014_9L_3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_3.jpg)

**답 : ②**





---

## 4. 8진수 (56.13...

8진수 (56.13)<sub>8</sub>을 16진수로 변환한 값은?


![2014_9L_4](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_4.jpg)

**답 : ②**

56.13<sub>8</sub>

= 101 110.001 011<sub>2</sub>

= 0010 1110.0010 1100<sub>2</sub>

= 2E.2C<sub>16</sub>



---

## 5. OSI 7계층 중 종점...

OSI 7계층 중 종점 호스트 사이의 데이터 전송을 다루는 계층으로서 종점 간의 연결 관리, 오류 제어와 흐름 제어 등을 수행하는 계층은?


![2014_9L_5](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_5.jpg)

**답 : ①**

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

## 6. 데이터 통신 시스템에서...

데이터 통신 시스템에서 발생하는 에러를 제어하는 방식으로 송신측이 오류를 검출할 수 있을 정도의 부가적인 정보를 프레임에 참가하여 전송하고 수신측이 오류 검출 시 재전송을 요구하는 방식은?


![2014_9L_6](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_6.jpg)

**답 : ①**

- ARQ Automatic Repeat reQuest
    - 통신회선에서 착오가 발생하면 수신측은 착오의 발생을 송신측에 알리고, 송신측은 착오가 발생한 block을 재전송하는 방식으로 검출 후 재전송.
    - 정지 조회 ARQ(stop-and-wait ARQ)방식
    - 연속적 ARQ(Continuous ARQ)방식
        - 반송 N블록 ARQ(Go-back-N ARQ)
        - 선별 재송 ARQ(Selective ARQ)
    - 적응적 ARQ(Adaptive ARQ)방식
- FEC Forward Error Correction
    - 데이터 전송 과정에서 발생한 오류를 검출하고 재전송 요구 없이 스스로 수정하는 기능
    - 송신측에서 오류 검출을 위한 부가 정보를 추가해 전송하고, 수신측이 이 부가 정보를 이용해 오류를 발견하고 수정
    - 재전송 요구가 없어 역채널이 필요없고, 연속적인 데이터 흐름이 가능하다. 그러나 전송 효율이 떨어진다.
    - 검출과 수정을 위한 방식
        - 해밍 코드, 상승 코드
- BEC(Backward Error Correction, 후진 오류 수정)
    - 데이터 전송 과정에서 오류가 발생하면 송신 측에 재전송을 요구하는 방식이다.
    - 검출 방식
        - 패리티 검사, CRC, 블록 합
    - 오류 제어
        - ARQ(자동 반복 요청)
- 순회 부호 cyclic code
- 해밍 부호 Hamming code
    - 데이터 비트에 체크비트를 추가하여, 오류를 검사 확인 및 정정



---

## 7. 3개의 페이지 프레임으로...

3개의 페이지 프레임으로 구성된 기억장치에서 다음과 같은 순서대로 페이지 요청이 일어날 때, 페이지 교체 알고리즘으로 LFU(Least Frequently Used)를 사용한다면 몇 번의 페이지 부재가 발생하는가? (단, 초기 페이지 프레임은 비어있다고 가정한다)


![2014_9L_7](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_7.jpg)

**답 : ②**

|      | 2    | 3    | 1    | 2    | 1    | 2    | 4    | 2    | 1    | 3    | 2    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 부재 | O    | O    | O    |      |      |      | O    |      |      | O    |      |
| p1   | 2    | 2    | 2    |      |      |      | 2    |      |      | 2    |      |
| p2   |      | 3    | 3    |      |      |      | 4    |      |      | 3    |      |
| p3   |      |      | 1    |      |      |      | 1    |      |      | 1    |      |



---

## 8. 관계형 데이터베이스의...

관계형 데이터베이스의 표준 질의어인 SQL(Structured Query Language)에서 CREATE TABLE문에 대한 설명으로 옳지 않은 것은?


![2014_9L_8](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_8.jpg)

**답 : ④**

④ CHECK절은 무결성 제약 조건으로 반드시 UPDATE 키워드와 함께 사용한다.
==> WITH CHECK OPTION 절을 사용한 뷰에서 INSERT와 UPDATE를 수행하면 Error가 발생한다.


---

## 9. 데이터 전송 방식 ...

데이터 전송 방식 중에서 한 번에 한 문자 데이터를 전송하며 시작 비트(start-bit)와 정지 비트(stop-bit)를 사용하는 전송 방식은?


![2014_9L_9](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_9.jpg)

**답 : ①**

- 비동기식 전송 방식
  - 데이터를 전송할 때 하나의 글자를 나타내는 부호의 전후에 스타트비트와 스탑비트를 넣어서 블록의 동기화를 취해주는 방식.
  - =start-stop 전송 방식
  - 비트열을 전송하지 않을 때는 송수신기의 회선은 휴지상태(idle, 항상 1)로 있다가 데이터 전송시에 ST 상태(0)를 전송하여 수신 혹은 타임슬랏의 1/2시간 동안 0 상태를 유지함을 감지하여 데이터 수신을 준비한다.
- 동기식 전송 방식
  - 두대의 송수신 시스템이 통신 시에 시차가 있을 경우 보내온 데이터의 잘못 해석할 가능성을 막기 위해 양방향 시차를 맞추어 수신자가 정확히 수신할 수 있는 기술.
  - 데이터블럭 전후에 특정한 제어 정보를 삽입. 데이터블럭과 전후의 제어정보를 합쳐서 프레임이라고 한다.
- 아날로그 전송 방식
  - 연속적 데이터 전송. 대표적 예는 전화기
- 병렬 전송 방식
  - 직렬 전송은 하나의 전송 매체를 통하여 한 비트씩 순서적으로 전송하는 방법이며, 병렬전송에 비해 느리지만 구축 비용이 적게 들어 장거리 전송에 사용
  - 병렬 전송은 한번에 보내는 N개의 선을 이용하여 동시에 전송하는 방법. 전송속도는 빠르지만, 구축비용이 많이 들어 단거리 전송에 사용.



---

## 10. 다음 C 프로그램의...

다음 C 프로그램의 출력 결과로 옳은 것은?


![2014_9L_10](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_10.jpg)

**답 : ①**





---

## 11. 정렬 알고리즘 중에서...

정렬 알고리즘 중에서 시간 복잡도가 나머지 셋과 다른 것은?


![2014_9L_11](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_11.jpg)

**답 : ③**



- 안정적 ; 동일한 값들은 순서 유지
- 제자리 ; 주어진 공간 외, 추가적인 공간 사용 X

| Name | Best          | Average               | Worst         | 안정적 | 제자리 |
| ---- | ------------- | --------------------- | ------------- | ------ | ------ |
| 선택 | n<sup>2</sup> | n<sup>2</sup>         | n<sup>2</sup> | △      | O      |
| 거품 | n             | n<sup>2</sup>         | n<sup>2</sup> | O      | O      |
| 삽입 | n             | n<sup>2</sup>         | n<sup>2</sup> | O      | O      |
| 쉘   |               | n (log n)<sup>2</sup> | n<sup>2</sup> | △      | O      |
| 퀵   | n log n       | n log n               | n<sup>2</sup> | X      | O      |
| 합병 | n log n       | n log n               | n log n       | O      | X      |
| 힙   | n log n       | n log n               | n log n       | X      | O      |
| 기수 |               | k(n+q)                | n<sup>2</sup> |        |        |



---

## 12. 데이터 전송 중에...

데이터 전송 중에 발생하는 에러를 검출하는 방식으로 옳지 않은 것은?


![2014_9L_12](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_12.jpg)

**답 : ④**

- 패리티 parity 검사 방식

  - 전송 비트에 1비트의 검사비트인 패리티비트를 추가하여 오류 검출이 가능.

- 검사합 checksum 방식

  - 중복 검사의 한 형태, 오류 정정을 통해 공간(전자 통신)이나 시간(기억 장치)속에서 송신된 자료의 무결성을 보호하는 단순한 방법

- CRC 방식

  - cyclic redundancy check
  - 네트워크 등을 통하여 데이터를 전송할 때 전송한 데이터에 오류가 있는지를 확인하기 위한 체크값을 결정하는 방식

- BCD 부호 방식

  - binary coded decimal. 이진화 십진법 = 8421코드

  - BCD코드는 10진수 자리수마다 1:1매칭해서 2진수로 변환하는 것. 

  - 0~9까지만 4비트로 표현하고 10부터는 상위로 비트를 올림.

    | 10진수 | Binary    | BCD 코드      |
    | ------ | --------- | ------------- |
    | 0      | 0000 0000 | 0000 0000     |
    | 1      | 0000 0001 | 0000 0001     |
    | 2      | 0000 0010 | 0000 0010     |
    | 3      | 0000 0011 | 0000 0011     |
    | 4      | 0000 0100 | 0000 0100     |
    | 5      | 0000 0101 | 0000 0101     |
    | 6      | 0000 0110 | 0000 0110     |
    | 7      | 0000 0111 | 0000 0111     |
    | 8      | 0000 1000 | 0000 1000     |
    | 9      | 0000 1001 | 0000 1001     |
    | 10     | 0000 1010 | **0001 0000** |
    | 11     | 0000 1011 | **0001 0001** |
    | 12     | 0000 1100 | **0001 0010** |
    | 13     | 0000 1101 | **0001 0011** |
    | 14     | 0000 1110 | **0001 0100** |
    | 15     | 0000 1111 | **0001 0101** |

    



---

## 13. 다음 전위(prefix) 표기...

다음 전위(prefix) 표기 수식을 중위(infix) 표기 수식으로 바꾼 것으로 옳은 것은? (단, 수식에서 연산자는 +, *, /이며 피연산자는 A, B, C, D이다)


![2014_9L_13](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_13.jpg)

**답 : ③**





---

## 14. 프로그램의 내부구조나...

프로그램의 내부구조나 알고리즘을 보지 않고, 요구사항 명세서에 기술되어 있는 소프트웨어 기능을 토대로 실시하는 테스트는?


![2014_9L_14](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_14.jpg)

**답 : ②**

- 구조 테스트
  - 소프트웨어가 어떻게 구성되었는가에 대한 정보. 즉, 코드와 디자인의 테스트케이스를 유도하는데 사용.
- 경로 테스트
  - 화이트 박스 테스트 예제 및 검증기준
  - 문장검증 경로 ; 모든 문장이 한번씩 수행되도록 검증 하는 기준.
  - 분기 검증 기준 ; 경로에서 나타나는 모든 분기점 파악
  - 경로 검증 기준 ; 모든 경로에 대해 테스트를 수행
  - 조건 검증 기준 ; if else, or 등 조건문 테스트.



---

## 15. 객체 지향 언어에서 ...

객체 지향 언어에서 클래스 A와 클래스 B는 상속관계에 있다. A는 부모 클래스, B는 자식 클래스라고 할 때 클래스 A에서 정의돈 메서드(method)와 원형이 동일한 메서드를 클래스 B에서 기능을 추가하거나 변형하여 다시 정의하는 것을 무엇이라고 하는가?


![2014_9L_15](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_15.jpg)

**답 : ④**

- 추상 클래스
  - 클래스 구현부 내부에 추상 메서드가 하나 이상 포함되거나 abstract로 정의된 경우.
  - 추상 클래스는 new 연산자를 사용하여 객체를 생성할 수 없다.
  - 추상 클래스는 새로운 일반 클래스를 위한 부모 클래스의 용도로만 사용된다.
- 인터페이스
  - 모든 메서드가 추상 메서드인 경우.
  - 추상 클래스보다 한단계 더 추상화된 클래스.
- 오버로딩 overloading ; 중복정의
- 오버라이딩 overriding ; 재정의



---

## 16. 인터넷 관련 용어에...

인터넷 관련 용어에 대한 설명으로 옳지 않은 것은?


![2014_9L_16](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_16.jpg)

**답 : ④**

④ 웹 캐시(web cache)는 웹 서버가 사용자의 컴퓨터에 저장하는 방문 기록과 같은 작은 임시 파일로 이를 이용하여 ~~웹 서버는 사용자를 식별, 인증하고 사용자별 맞춤 정보를 제공할 수도 있지만~~ 개인 정보 침해의 소지가 있다.

==> 쿠키에 대한 설명.



---

## 17. 운영체제의 디스크...

운영체제의 디스크 스케줄링 기법에 대한 설명으로 옳은 것은?


![2014_9L_17](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_17.jpg)

**답 : ③**

① ~~FCFS(First-Come-First-Served)는~~ 현재의 판독/기록 헤드위치에서 대기 큐 내 요구들 중 탐색 시간이 가장 짧은 것을 선택하여 처리하는 기법이다.

==> SSTF

② N-Step-SCAN은 대기 큐 내에서 디스크 암(disk arm)이 외부 실린더에서 내부 실린더로 움직이는 방향에 있는 요구들만을 처리하는 기법이다.

==> N-Step-SCAN ; 헤드가 한쪽 방향으로 이동해 나가면서 요청에 의해서 들어온 것만 서비스하다가 다시 반대쪽으로 오면서 이전에 도착했던 요청들을 서비스하는 기법.

④ SSTF(Shortest-Seek-Time-First)는 각 요구 처리에 대한 응답 시간을 항상 공평하게 하는 기법이다.



---

## 18. 멀티미디어 기술에...

멀티미디어 기술에 대한 설명으로 옳지 않은 것은?


![2014_9L_18](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_18.jpg)

**답 : ②**

② RLE(Run-Lenght Encoding)는 ~~손실 압축 기법~~으로 압축되는 데이터에 동일한 값이 연속하여 나타나는 긴 열이 있을 경우 자주 사용한다.

==> 무손실 압축 방법

==> 허프만코드와 유사.



---

## 19. JAVA 클래스 D의 ...

JAVA 클래스 D의 main()함수 내에서 컴파일하거나 실행하는 데 에러가 발생하지 않는 명령어는?


![2014_9L_19](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_19.jpg)

**답 : ③**

- 추상클래스에는 파생클래스만이 대체 가능.





---

## 20. 유비쿼터스 컴퓨팅 ...

유비쿼터스 컴퓨팅 환경과 관련된 기술에 대한 설명으로 옳지 않은 것은?


![2014_9L_20](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_20.jpg)

**답 : ③**

③ 텔레매틱스(telematics)는 증강현실(augmented reality)이 확장된 개념으로 사용자가 실세계 위에 가상세계의 정보를 겹쳐 볼 수 있도록 구현한 기술이다.

XR ; 증강현실(augmented reality)이 확장된 개념으로 사용자가 실세계 위에 가상세계의 정보를 겹쳐 볼 수 있도록 구현한 기술.

텔레매틱스 = 통신 telecommunication과 정보과학 informatics의 합성어. 무선음성데이터통신과 인공위성을 이용한 GPS를 기반으로 자동차에서 주고 받는 기술.

� 가능.





---

## 20. 유비쿼터스 컴퓨팅 ...

유비쿼터스 컴퓨팅 환경과 관련된 기술에 대한 설명으로 옳지 않은 것은?


![2014_9L_20](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2014_9L/2014_9L_20.jpg)

**답 : ③**

③ 텔레매틱스(telematics)는 증강현실(augmented reality)이 확장된 개념으로 사용자가 실세계 위에 가상세계의 정보를 겹쳐 볼 수 있도록 구현한 기술이다.

XR ; 증강현실(augmented reality)이 확장된 개념으로 사용자가 실세계 위에 가상세계의 정보를 겹쳐 볼 수 있도록 구현한 기술.

텔레매틱스 = 통신 telecommunication과 정보과학 informatics의 합성어. 무선음성데이터통신과 인공위성을 이용한 GPS를 기반으로 자동차에서 주고 받는 기술.

