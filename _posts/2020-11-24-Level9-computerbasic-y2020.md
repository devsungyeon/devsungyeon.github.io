---
title: "2020년 9급 전산직 컴퓨터일반 풀이"
strapline: "컴퓨터일반 풀이"
description: "2020년 9급 전산직 컴퓨터일반 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "9Level_computerbasic"
tag:
  - "9급"
  - "컴퓨터일반"
  - "9급공무원"
toc: true
last_modified_at: 2020-11-21
comments: true
---

# 2020년 9급 전산직 컴퓨터일반 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1.  아날로그 신호를 디지털 신호로...

1. 아날로그 신호를 디지털 신호로 변조하기 위한 펄스부호변조(PCM) 과정으로 옳지 않은 것은?

![2020_9L_1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_1.jpg)

**답 : ①**

- PCM(Pulse-code modulation) ; 아날로그 신 호를 디지털 신호로 변조.

​	**Analog → Sampling(표본화) → Quantization(양자화) → Encoding(부호화) → Digital**



---

## 2. DBMS를 사용하는 이점으로...

2. DBMS를 사용하는 이점으로 옳지 않은 것은?

![2020_9L_2](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_2.jpg)

|                     | DBMS                                                         | 파일시스템                                                   |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 중복                | 중복을 **최소화**<br /> ==> 일관성 유지                      |                                                              |
| 공유<br />여러 사람 | O                                                            | X                                                            |
| Data                | <img src="/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2_program+data.png" alt="2_program+data" style="zoom:33%;" /><br />프로그램과 데이터 분리. **독립성** | <img src="/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2_(program+data).png" alt="2_(program+data)" style="zoom: 33%;" /><br />프로그램과 데이터 연결. **종속성** |
| 장점                | 무결성, 보안성                                               | 속도↑                                                        |

**답 : ③**

③ ~~데이터의 중복을 허용~~하여 데이터의 일관성을 유지한다.

​	DBMS는 **데이터의 중복을 최소화**한다.



---

## 3.  CPU 내의 레지스터에 대한...

3. CPU 내의 레지스터에 대한 설명으로 옳지 않은 것은?

![2020_9L_3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_3.jpg)

**답 : ③**

③ Memory Address Register(MAR)

 : 주기억장치(Main Memory)에서 선택될 주소를 기억하는 레지스터

③ IR(Instruction Register)

 : 가장 최근에 인출한 명령어를 보관하는 레지스터

---

![3_CPU_REGISTER_MEMORY](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\3_CPU_REGISTER_MEMORY.png)

- CPU, Memory, 보조기억장치 간 흐름.

---

![3_REGISTER](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\3_REGISTER.png)

---

- Register(기억장치) : CPU 내에서 컴퓨터의 작동에 필요한 데이터와 명령어를 저장.

- PC(Program Counter, 계수기) : **다음에 실행할 명령의 주소**를 기억하는 레지스터
- MAR(Memory Address Register, 주소 레지스터) : 주기억장치(Main Memory)에서 **선택될 주소를 기억**하는 레지스터
- MBR(Memory Buffer Register, 내용 레지스터) : PC 혹은 MAR이 지정하는 주기억장치의 **내용을 임시로 기억**하는 레지스터
- IR(Instruction Register, 명령 레지스터) : 명령 계수기(PC)가 지정한 주소의 명령을 인출하여 명령 실행이 완료될 때까지 명령을 보관하는 레지스터. **가장 최근에 인출한 명령어를 보관**.

- LDA, 등등 코드보는 방법...

- 테이블에서 메모리 주소 계산하는 것


---

## 4. 소프트웨어 개발 프로세스 중...

4. 소프트웨어 개발 프로세스 중 원형(Prototyping) 모델의 단계별 진행 과정을 올바르게 나열한 것은?

![2020_9L_4](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_4.jpg)

**답 : ②**

원형(Prototype) : 우선 만들어 고객의 평가를 받는다.

요구 사항 분석 → **시제품 설계 → 시제품 개발** → 고객의 시제품 평가 → 시제품 정제 → 완제품 생산

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

## 5. 네트워크 토폴로지에 대한...

5. 네트워크 토폴로지에 대한 설명으로 옳지 않은 것은?

![2020_9L_5](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_5.jpg)

**답 : ③**

③ 트리(tree)형 토폴로지는 허브(hub)에 문제가 발생해도 ~~전체 네트워크에 영향을 주지 않는다.~~

​    허브에 문제가 발생하면 **중간 연결고리가 끊어져** 전체 네트워크에 문제가 발생한다.

- 네트워크 토폴로지

| 종류           | 모양                                                         | 장점                                                         | 단점                                                         |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 버스=bus       | ![5_bus](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\5_bus.png) | 설치가 간단<br />비용이 저렴                                 | 장애발견이 어려움<br />중앙 통신선 장애 시 전체 네트워크 문제 발생 |
| 링=ring        | ![5_ring](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\5_ring.png) | 모든 장치가 토큰에 접근 가능<br />순차적인 네트워크<br />컴퓨터 간 연결을 위한 네트워크 서버 불필요 | 한 노드 장애가 전체 망에 문제 발생<br />장치를 추가, 변경 시 네트워크 영향 |
| 트리=계층=tree | ![5_tree](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\5_tree.png) | 제어가 간단<br />네트워크 확장 용이                          | 병목 현상 가능<br />상위 노드에 트래픽 집중되어 병목 현상<br />상위 노드가 장애 발생되면, 하위 네트워크 장애 |
| 스타=성=star   | ![5_star](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\5_star.png) | 장애 발견이 용이<br />Netword 관리가 용이<br />한 노드 장애는 전체 영향 없음 | 중앙 노드 장애 발생시 전체 네트워크 문제 발생<br />많은 양의 케이블을 사용하므로 높은 비용 |
| 메시=mesh      | ![5_mesh](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\5_mesh.png) | 장애에 가장 강함<br />한 경로에 장애가 발생해도 다른 경로로 통신 가능<br /> | 연결선이 가장 많아 가장 높은 비용<br />네트워크 관리 어려움  |



---

## 6. RAID(Redundant Array of Independent...

6. RAID(Redundant Array of Independent Disks) 레벨에 대한 설명으로 옳지 않은 것은?

![2020_9L_6](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_6.jpg)

**답 : ④**

④ RAID 5 구조는 각 디스크에 데이터와 함께 ~~이중 분산 패리티 정보~~를 블록 단위로 분산 저장한다.

  **이중 분산 패리티** 방식은 **RAID 6** 구조에서 사용된다.

- RAID 0 1 2 3 4 5 6 0+1 1+0

| RAID Level | 모양                                                         | 설명                                             | 장점                                                         | 단점                                                         | 디스크 용량 계산                                             |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 0          | ![6_raid_0](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\6_raid_0.png) | 스트라이핑(Striping)<br />최상의 성능            | 데이터 사용 시 I/O를 분할하여 속도 향상                      | 스트라이핑 구 시 기존 데이터를 삭제                          | 최소 디스크 : 2<br />계산식 = 디스크수 * 디스크용량          |
| 1          | ![6_raid_1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\6_raid_1.png) | 미러링(Mirroring)<br />데이터 저장소를 복제      | 한 디스크 장애 시 복제 디스크로 복구 가능<br />높은 가용성   | 디스크 용량이 사용량의 두 배 필요<br />복제 디스크에도 사용해야 되므로 쓰기 속도가 느려짐 | 최소 디스크 : 2<br />계산식 = 디스크수/2 * 디스크용량        |
| 2          | ![6_raid_2](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\6_raid_2.png) | 해밍 코드 ECC를 가진 비트 레벨 스트라이핑        | ECC를 통한 오류 검사 및 수정                                 | ECC를 위한 드라이브가 손상되면 문제 발생                     | 최소 디스크 : 3<br />계산식 = (디스크수-1) * 디스크용량      |
| 3          | ![6_raid_3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\6_raid_3.png) | 전용 패리티를 가진 **바이트** 레벨 스트라이핑    | 높은 가용성                                                  | 전용 패리티 디스크의 병목 현상 발생<br />패리티를 저장한 디스크에 문제가 발생되면 데이터 손실 | 최소 디스크 : 3<br />계산식 = (디스크수-1) * 디스크용량      |
| 4          | ![6_raid_4](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\6_raid_4.png) | 전용 패리티를 이용한 **블록** 레벨 스트라이핑    | 성능 향상<br />높은 결함 허용도<br />3과 동일                | 3과 동일                                                     | 최소 디스크 : 3<br />계산식 = (디스크수-1) * 디스크용량      |
| 5          | ![6_raid_5](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\6_raid_5.png) | 분산 패리티를 가진 **블록** 레벨 스트라이핑      | 전용 패리티 드라이브 사용 **안함!**<br />병목현상을 제거하여 성능 향상<br />높은 가용성 |                                                              | 최소 디스크 : 3<br />계산식 = (디스크수-1) * 디스크용량      |
| 6          | ![6_raid_6](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\6_raid_6.png) | 이중 분산 패리티를 가진 **블록** 레벨 스트라이핑 | 높은 가용성                                                  | 높은 비용                                                    | 최소 디스크 : 4<br />계산식 = (디스크수-2) * 디스크용량      |
| 0+1        | ![6_raid_0+1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\6_raid_0+1.png) | 패리티 없이 이중 스트라이핑하고 미러링           | 결함 허용도<br />가용성                                      | 높은 비용                                                    | 최소 디스크 : 4,6,8<br />계산식 = (디스크수/2) * 디스크용량  |
| 1+0        | ![6_raid_1+0](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\6_raid_1+0.png) | 패리티 없이 미러링하고 스트라이핑                | 높은 결함 허용도<br />성능 우수                              | 높은 비용                                                    | 최소 디스크 : 6,8,10<br />계산식 = (디스크수/2) * 디스크용량 |





---

## 7. 다중 스레드(Multi Thread) 프로그래밍...

7. 다중 스레드(Multi Thread) 프로그래밍의 이점에 대한 설명으로 옳지 않은 것은?

![2020_9L_7](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_7.jpg)

**답 : ④**

④ 다중 스레드는 한 스레드에 문제가 생기더라도 ~~전체 프로세스에 영향을 미치지 않는다.~~

  한 스레드에 문제 발생 시 전체 프로세스에 영향을 미친다.

- Process 안에서 각각의 Thread들이 서로 공유하며 연산한다.
- Process들끼리 데이터를 공유하며 연산한다.

![7_MUTLI_THREAD](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/7_MUTLI_THREAD.png)



---

## 8. OSI(Open Systems Interconnect)...

8. OSI(Open Systems Interconnect) 모델에 대한 설명으로 옳지 않은 것은?

![2020_9L_8](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_8.jpg)

**답 : ①**

① 네트워크 계층은 데이터 전송에 관한 서비스를 제공하는 계층으로 송신 측과 수신 측 사이의 실제적인 ~~연결 설정 및 유지, 오류 복구와 흐름 제어 등을 수행~~한다.

**데이터 링크 계층(Data Link Layer) : 흐름제어기능, 동기화 기능, 오류제어 기능, 순서제어 기능.**

---

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

## 9. 캐시기억장치 교체 알고리즘에 대한...

9. 캐시기억장치 교체 알고리즘에 대한 설명으로 옳지 않은 것은?

![2020_9L_9](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_9.jpg)

**답 : ③**

③ LFU는 캐시 블록마다 참조 횟수를 기록함으로써 ~~가장 많이 참조된 블록을 교체하는 방법~~이다.

  LFU는 **가장 적게 참조된 블록을 교체하는 방법**이다.



- 교체(Replacement) 정책
  1. 최적화 원칙(the principle of optimality)
  2. 무작위 page 교체(random page replacement)
  3. FIFO(First-In First-Out)
  4. SCR(Second Change Replacement)
  5. LRU(Lease Recently Used)
  6. NUR(Not Used Recently)
  7. LFU(Lease Frequence Used)
  8. Working Set
  9. PFF(Page Fault Frequency)



---

## 10. 8진수 123.321을 16진수로...

10. 8진수 123.321을 16진수로 변환한 것은?

![2020_9L_10](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_10.jpg)

**답 : ④**

**8진수 -> 2진수 -> 16진수**

![10_1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/10_1.jpg)



---

## 11.  암호화 기술에 대한 설명으로...

11. 암호화 기술에 대한 설명으로 옳은 것은?

![2020_9L_11](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_11.jpg)

**답 : ②**

① 공개키 암호화는 암호화하거나 복호화하는 데 ~~동일한 키를 사용~~한다.

  암호화키와 복호화키가 다르다.

③ 공개키 암호화의 대표적인 알고리즘에는 ~~데이터 암호화 표준(Data Encryption Standard)~~이 있다.

  공개키 암호화의 대표적인 알고리즘은 RSA, ECC, Elgamal, Rabin이 있다.

④ 비밀키 암호화는 암호화와 복호화 과정에서 ~~서로 다른 키를 사용하는 비대칭 암호화(asymmetric encryption)~~다.

  비밀키 암호화는 암호화키와 복호화키가 동일하다.

|          | 공개키 = 비대칭키                      | 비공개키 = 대칭키 = 비밀키 |
| -------- | -------------------------------------- | -------------------------- |
| 알고리즘 | RSA, ECC, Elgamal, Rabin               | DES, SEED, Rijndael        |
| 설명     | 암호화키 <> 복호화키<br />두 키가 다름 | 암호화키 = 복호화키        |
| 속도     | 느림                                   | 빠름                       |





---

## 12. CPU를 다른 프로세스로 교환하려면...

12. CPU를 다른 프로세스로 교환하려면 이전 프로세스의 상태를 보관하고 새로운 프로세스의 보관된 상태로 복구하는 작업이 필요하다. 이 작업으로 옳은 것은?

![2020_9L_12](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_12.jpg)

**답 : ④**

① 세마포어(Semaphore)

 ; 동시에 리소스에 접근 허용이 접근 허용이 가능한 개수를 가진 counter

 ; 뷰에 상호배제. 임계영역. 프로세스간 임계 침범 하지 못한다.

 ; 뮤텍스와 비슷하나 여러 명이 사용 가능.

② 모니터(Monitor)

 ; 공유 객체, 임계 영역이 코딩된 프로세저, 초기화 코드로 구성된 모듈

 ; 세마포어와 비슷. 세마포어를 사용하면 올바른 프로그램 만드는 것이 어렵다. 

 ; wait 와 signal 연산에서 수행이 어떤 연산에 영향을 미치는 지 파악 어려움.

 ; 세마포어 비해 공유자원에 대한 접근과 해제가 용이.

③ 상호배제(Mutual Exclusion)

 ; 병행성을 보장하기 위한 것으로 어떤 특정한 시점에 하나의 자원에는 하나의 프로세스만 접근할 수 있게 나머지의 접근은 배제시키는 것

④ 문맥교환(Context Switching)

 ; 인터럽트가 발생되었을 때 실행중이던 프로세스가 작업을 멈추었다가 다시 실행될 때 이전 작업을 다시 수행하기 위해 이전 작업 내용과 프로세스의 정보들을 PCB에 저장하는 것

---

## 13. 응용프로그램 제작에 필요한...

13. 응용프로그램 제작에 필요한 개발환경, SKD 등 플랫폼 자체를 서비스 형태로 제공하는 클라우드 컴퓨팅 서비스 모델은?

![2020_9L_13](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_13.jpg)

**답 : ②**

① DNS(Domain Name System)

 ; 호스트의 도메인 이름(www.naver.com)을 호스트의 네트워크 주소(xxx.xxx.xxx.xxx)로 바꾸거나 반대의 변환을 수행하는 것을 도움.

② Paas(Platform as a service)

 ; 서비스를 개발할 수 있는 안정적인 환경(Platform)과 그 환경을 이용하는 응용 프로그램을 개발할 수 있는 API를 제공.

③ Saas(Software as a service)

 ; Cloud 환경에서 동작하는 응용프로그램을 서비스 형태로 제공.

④ IaaS(Infrastructure as a service)

 ; 서버를 운영하기 위한 인프라를 구축하기 위한 서버자원, IP, Network, Storage, 전력 등을 가상의 환경에서 쉽고 편하게 이용할 수 있게 서비스 형태로 제공.



---

## 14. 다음 프로그램의 실행 결과로...

14. 다음 프로그램의 실행 결과로 옳은 것은?

![2020_9L_14](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_14.jpg)

**답 : ④**

```c
#include <stdio.h>
int main(void)
{
    int array[] = {100, 200, 300, 400, 500};
    int *ptr;
    ptr = array;
    /*
    ptr = array
    *ptr = *array = 100
    *(ptr+1) = *(array+1) = 200
    *(ptr+2) = *(array+2) = 300
    *(ptr+3) = *(array+3) = 400
    *(ptr+4) = *(array+4) = 500
    */
    printf("%d\n", *(ptr+3) + 100);
    // *(ptr+3) = 400
    // *(ptr+3) + 100 = 500
}
```



---

## 15. 다음 프로그램은 연결 리스트를...

15. 다음 프로그램은 연결 리스트를 만들기 위한 코드의 일부분이다. 아래 그림과 같이 두 개의 노드 first, second가 연결되었다고 가정하고, 위의 코드를 참조하여 노드 tmp를 노드 first와 노드 second 사이에 삽입하고자 할 때, 프로그램 코드로 옳은 것은?

![2020_9L_15](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_15.jpg)

**답 : ②**

**![15_0](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/15_0.png)**

---

① tmp.link = &first;

![15_1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/15_1.png)

​     first.link = &tmp;

![15_2](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/15_2.png)

---

② tmp.link = first.link;

![15_3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/15_3.png)

​     first.link = &tmp;

![15_4](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/15_4.png)

---

③ tmp.link = &second;

![15_5](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/15_5.png)

​    first.link = second.link;

![15_6](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/15_6.png)

---

④ tmp.link = NULL;

![15_7](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/15_7.png)

​    second.link = &tmp;

![15_8](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/15_8.png)



---

## 16. 다음 C 프로그램의 결과로 옳은...

16. 다음 C 프로그램의 결과로 옳은 것은?

![2020_9L_16](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_16.jpg)

**답 : ①**

~~~c
#include <stdio.h>
int main()
{
    int a, b;
    a = b = 1;
    
    if (a = 2) // a = 2, b = 1
        // "a = 2"는 연산. Error없이 연산이 수행되면 True
        b = a + 1; // a = 2, b = 3
   	else if (a == 1)
        b = b + 1;
    else
        b = 10;
    
    printf("%d, %d\n", a, b);
}
~~~







---

## 17. 다음 이진 트리에 대하여...

17. 다음 이진 트리에 대하여 후위 순회를 하는 경우 다섯 번째 방문하는 노드는?

![2020_9L_17](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_17.jpg)

**답 : ④**

Pre-order(C-L-R) : A-B-D-E-G-C-F

In-order(L-C-R) : D-B-G-E-A-C-F

Post-order(L-R-C) : D-G-E-B-F-C-A

![17_0](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/17_0.gif)

---

## 18. 프세스 스케줄링에 대한 설명으로...

18. 프세스 스케줄링에 대한 설명으로 옳지 않은 것은?

![2020_9L_18](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_18.jpg)

**답 : ①**

① FCFS(First Come First Served) 스케줄링은 ~~비선점 방식~~으로 대화식 시스템에 적합하다.

  FCFC 스케줄링은 **선점 방식**이다.

- 다단계 큐 ; 큐를 여러 개 생성하여 우선순위 없이, 작업별로 분류

- 다단계 피드백 큐 ; 서로 단계들 마다 우선순위를 설정하여, 할당 시간을 부여.

	- 대화형 시스템에 적합




---

## 19. TCP/IP 프로토콜 스택에 대한...

19. TCP/IP 프로토콜 스택에 대한 설명으로 옳은 것은?

![2020_9L_19](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_19.jpg)

**답 : ③**

![8_3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/8_3.jpg)

① ~~데이터링크(datalink) 계층, 전송(transport) 계층, 세션(session) 계층 및 응용(application) 계층~~으로 구성된다.

  **응용계층, 전송계층, 인터넷계층, 네트워크계층** 으로 구성된다.

② ICMP는 ~~데이터링크 계층~~에서 사용 가능한 프로토콜이다.

   ICMP는 **인터넷 계층**에서 사용가능하다.

④ 응용 계층은 ~~데이터가 목적지까지 찾아갈 경로를 설정하기 위해 라우팅(routing) 프로토콜을 운영~~한다.

데이터가 목적지까지 찾아갈 경로를 설정하기 위해 라우팅(routing) 프로토콜을 운영하는 계층은 **인터넷 계층**이다.

| Layer                | 각 계층 Protocol                                             |
| -------------------- | ------------------------------------------------------------ |
| Network Access Layer | 이더넷                                                       |
| Internet Layer       | IP(Internet Protocol)<br />ICMP(Internet Control Message Protocol)<br />IGMP(Internet Group Message Protocol)<br />ARP(Address Resolution Protocol)<br />RARP(Reverse Address Resolution Protocol) |
| Transport Layer      | TCP(Transmission Control Protocol)<br />UDP(User Datagram Protocol)<br />SCTP(Stream Control Transmission Protocol) |
| Application Layer    | FTP(File Transfer Protocol)<br />VSFTP(Very Secure File Transfer Protocol)<br />SNMP(Simple Network Management Protocol)<br />SMTP(Simple Mail Transfer Protocol)<br />HTTP(Hyper Text Transfer Protocol)<br />HTTPs(Hyper Text Transfer Protocol Secure)<br />DNS(Domain Name System) |



---

## 20. 다음 테이블 인스턴스(Instance)들에...

20. 다음 테이블 인스턴스(Instance)들에 대하여 오류 없이 동작하는 SQL(Structured Query Language) 문장은?

![2020_9L_20](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_20.jpg)

**답 : ②**

- UNION ; 중복을 제거
- UNION ALL ; 중복 제거하지 않고 모두 표현.

① SELECT deptno, ~~position~~, AVG(salary) FROM PROFESSOR GROUP BY deptno;

  deptno 로 GROUP BY로 그룹화가 되었는데 position은 그룹 함수로 사용될 수 없고, 이로 인해 error가 발생한다.

③ SELECT grade, COUNT(\*), AVG(height) FROM STUDENT WHERE COUNT(\*) > 2 GROUP BY grade;

  WHERE 절에는 집계 함수를 사용할 수 없다.

④ SELECT name, grade, height FROM STUDENT WHERE height > (SELECT ~~height, grade~~ FROM STUDENT WHERE name = '홍길동');

  서브쿼리에서 height와 grade 가 반환되는데, 반환된 두 값으로 비교를 할 수 없으므로 error 가 발생한다.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyOTczODg4NF19
-->