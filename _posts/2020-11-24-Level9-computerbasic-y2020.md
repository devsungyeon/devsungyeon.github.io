---
 v ntitle: "2020년 9급 전산직 컴퓨터일반 풀이"
strapline: "컴퓨터일반 풀이"
description: "2020년 9급 전산직 컴퓨터일반 풀이"
header:
 overlay_image: c:/GitHub/devsungyeon.github.io/assets/images/bright.jpg
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

![2020_9L_1](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_1.jpg)

**답 : ①**

- PCM(Pulse-code modulation) ; 아날로그 신호를 디지털 신호로 변조.

​	**Analog → Sampling(표본화) → Quantization(양자화) → Encoding(부호화) → Digital**



---

## 2. DBMS를 사용하는 이점으로...

2. DBMS를 사용하는 이점으로 옳지 않은 것은?

![2020_9L_2](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_2.jpg)

|                     | DBMS                                                         | 파일시스템                                                   |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 중복                | 중복을 **최소화**<br /> ==> 일관성 유지                      |                                                              |
| 공유<br />여러 사람 | O                                                            | X                                                            |
| Data                | <img src="c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2_program+data.png" alt="2_program+data" style="zoom:33%;" /><br />프로그램과 데이터 분리. **독립성** | <img src="c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2_(program+data).png" alt="2_(program+data)" style="zoom: 33%;" /><br />프로그램과 데이터 연결. **종속성** |
| 장점                | 무결성, 보안성                                               | 속도↑                                                        |

**답 : ③**

③ ~~데이터의 중복을 허용~~하여 데이터의 일관성을 유지한다.

​	DBMS는 **데이터의 중복을 최소화**한다.



---

## 3.  CPU 내의 레지스터에 대한...

3. CPU 내의 레지스터에 대한 설명으로 옳지 않은 것은?

![2020_9L_3](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_3.jpg)

**답 : ③**

③ Memory Address Register(MAR)

 : 주기억장치(Main Memory)에서 선택될 주소를 기억하는 레지스터

③ IR(Instruction Register)

 : 가장 최근에 인출한 명령어를 보관하는 레지스터

---

![3_CPU_REGISTER_MEMORY](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\3_CPU_REGISTER_MEMORY.png)

- CPU, Memory, 보조기억장치 간 흐름.

---

![3_REGISTER](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\3_REGISTER.png)

---

- Register(기억장치) : CPU 내에서 컴퓨터의 작동에 필요한 데이터와 명령어를 저장.

- PC(Program Counter, 계수기) : **다음에 실행할 명령의 주소**를 기억하는 레지스터
- MAR(Memory Address Register, 주소 레지스터) : 주기억장치(Main Memory)에서 **선택될 주소를 기억**하는 레지스터
- MBR(Memory Buffer Register, 내용 레지스터) : PC 혹은 MAR이 지정하는 주기억장치의 **내용을 임시로 기억**하는 레지스터
- IR(Instruction Register, 명령 레지스터) : 명령 계수기(PC)가 지정한 주소의 명령을 인출하여 명령 실행이 완료될 때까지 명령을 보관하는 레지스터. **가장 최근에 인출한 명령어를 보관**.

---

## 4. 소프트웨어 개발 프로세스 중...

4. 소프트웨어 개발 프로세스 중 원형(Prototyping) 모델의 단계별 진행 과정을 올바르게 나열한 것은?

![2020_9L_4](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_4.jpg)

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

![2020_9L_5](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_5.jpg)

**답 : ③**

③ 트리(tree)형 토폴로지는 허브(hub)에 문제가 발생해도 ~~전체 네트워크에 영향을 주지 않는다.~~

​    허브에 문제가 발생하면 **중간 연결고리가 끊어져** 전체 네트워크에 문제가 발생한다.

- 네트워크 토폴로지

| 종류           | 모양                                                         | 장점                                                         | 단점                                                         |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 버스=bus       | ![5_bus](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\5_bus.png) | 설치가 간단<br />비용이 저렴                                 | 장애발견이 어려움<br />중앙 통신선 장애 시 전체 네트워크 문제 발생 |
| 링=ring        | ![5_ring](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\5_ring.png) | 모든 장치가 토큰에 접근 가능<br />순차적인 네트워크<br />컴퓨터 간 연결을 위한 네트워크 서버 불필요 | 한 노드 장애가 전체 망에 문제 발생<br />장치를 추가, 변경 시 네트워크 영향 |
| 트리=계층=tree | ![5_tree](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\5_tree.png) | 제어가 간단<br />네트워크 확장 용이                          | 병목 현상 가능<br />상위 노드에 트래픽 집중되어 병목 현상<br />상위 노드가 장애 발생되면, 하위 네트워크 장애 |
| 스타=성=star   | ![5_star](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\5_star.png) | 장애 발견이 용이<br />Netword 관리가 용이<br />한 노드 장애는 전체 영향 없음 | 중앙 노드 장애 발생시 전체 네트워크 문제 발생<br />많은 양의 케이블을 사용하므로 높은 비용 |
| 메시=mesh      | ![5_mesh](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\5_mesh.png) | 장애에 가장 강함<br />한 경로에 장애가 발생해도 다른 경로로 통신 가능<br /> | 연결선이 가장 많아 가장 높은 비용<br />네트워크 관리 어려움  |



---

## 6. RAID(Redundant Array of Independent...

6. RAID(Redundant Array of Independent Disks) 레벨에 대한 설명으로 옳지 않은 것은?

![2020_9L_6](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_6.jpg)

**답 : ④**

④ RAID 5 구조는 각 디스크에 데이터와 함께 ~~이중 분산 패리티 정보~~를 블록 단위로 분산 저장한다.

  **이중 분산 패리티** 방식은 **RAID 6** 구조에서 사용된다.

- RAID 0 1 2 3 4 5 6 0+1 1+0

| RAID Level | 모양                                                         | 설명                                             | 장점                                                         | 단점                                                         | 디스크 용량 계산                                             |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 0          | ![6_raid_0](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\6_raid_0.png) | 스트라이핑(Striping)<br />최상의 성능            | 데이터 사용 시 I/O를 분할하여 속도 향상                      | 스트라이핑 구 시 기존 데이터를 삭제                          | 최소 디스크 : 2<br />계산식 = 디스크수 * 디스크용량          |
| 1          | ![6_raid_1](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\6_raid_1.png) | 미러링(Mirroring)<br />데이터 저장소를 복제      | 한 디스크 장애 시 복제 디스크로 복구 가능<br />높은 가용성   | 디스크 용량이 사용량의 두 배 필요<br />복제 디스크에도 사용해야 되므로 쓰기 속도가 느려짐 | 최소 디스크 : 2<br />계산식 = 디스크수/2 * 디스크용량        |
| 2          | ![6_raid_2](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\6_raid_2.png) | 해밍 코드 ECC를 가진 비트 레벨 스트라이핑        | ECC를 통한 오류 검사 및 수정                                 | ECC를 위한 드라이브가 손상되면 문제 발생                     | 최소 디스크 : 3<br />계산식 = (디스크수-1) * 디스크용량      |
| 3          | ![6_raid_3](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\6_raid_3.png) | 전용 패리티를 가진 **바이트** 레벨 스트라이핑    | 높은 가용성                                                  | 전용 패리티 디스크의 병목 현상 발생<br />패리티를 저장한 디스크에 문제가 발생되면 데이터 손실 | 최소 디스크 : 3<br />계산식 = (디스크수-1) * 디스크용량      |
| 4          | ![6_raid_4](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\6_raid_4.png) | 전용 패리티를 이용한 **블록** 레벨 스트라이핑    | 성능 향상<br />높은 결함 허용도<br />3과 동일                | 3과 동일                                                     | 최소 디스크 : 3<br />계산식 = (디스크수-1) * 디스크용량      |
| 5          | ![6_raid_5](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\6_raid_5.png) | 분산 패리티를 가진 **블록** 레벨 스트라이핑      | 전용 패리티 드라이브 사용 **안함!**<br />병목현상을 제거하여 성능 향상<br />높은 가용성 |                                                              | 최소 디스크 : 3<br />계산식 = (디스크수-1) * 디스크용량      |
| 6          | ![6_raid_6](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\6_raid_6.png) | 이중 분산 패리티를 가진 **블록** 레벨 스트라이핑 | 높은 가용성                                                  | 높은 비용                                                    | 최소 디스크 : 4<br />계산식 = (디스크수-2) * 디스크용량      |
| 0+1        | ![6_raid_0+1](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\6_raid_0+1.png) | 패리티 없이 이중 스트라이핑하고 미러링           | 결함 허용도<br />가용성                                      | 높은 비용                                                    | 최소 디스크 : 4,6,8<br />계산식 = (디스크수/2) * 디스크용량  |
| 1+0        | ![6_raid_1+0](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2020_9L\6_raid_1+0.png) | 패리티 없이 미러링하고 스트라이핑                | 높은 결함 허용도<br />성능 우수                              | 높은 비용                                                    | 최소 디스크 : 6,8,10<br />계산식 = (디스크수/2) * 디스크용량 |





---

## 7. 다중 스레드(Multi Thread) 프로그래밍...

7. 다중 스레드(Multi Thread) 프로그래밍의 이점에 대한 설명으로 옳지 않은 것은?

![2020_9L_7](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_7.jpg)

**답 : ④**

④ 다중 스레드는 한 스레드에 문제가 생기더라도 ~~전체 프로세스에 영향을 미치지 않는다.~~

  한 스레드에 문제 발생 시 전체 프로세스에 영향을 미친다.





---

## 8. OSI(Open Systems Interconnect)...

8. OSI(Open Systems Interconnect) 모델에 대한 설명으로 옳지 않은 것은?

![2020_9L_8](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_8.jpg)

**답 : ①**

---

## 9. 캐시기억장치 교체 알고리즘에 대한...

9. 캐시기억장치 교체 알고리즘에 대한 설명으로 옳지 않은 것은?

![2020_9L_9](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_9.jpg)

**답 : ③**

---

## 10. 8진수 123.321을 16진수로...

10. 8진수 123.321을 16진수로 변환한 것은?

![2020_9L_10](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_10.jpg)

**답 : ④**

---

## 11.  암호화 기술에 대한 설명으로...

11. 암호화 기술에 대한 설명으로 옳은 것은?

![2020_9L_11](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_11.jpg)

**답 : ②**

---

## 12. CPU를 다른 프로세스로 교환하려면...

12. CPU를 다른 프로세스로 교환하려면 이전 프로세스의 상태를 보관하고 새로운 프로세스의 보관된 상태로 복구하는 작업이 필요하다. 이 작업으로 옳은 것은?

![2020_9L_12](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_12.jpg)

**답 : ④**

---

## 13. 응용프로그램 제작에 필요한...

13. 응용프로그램 제작에 필요한 개발환경, SKD 등 플랫폼 자체를 서비스 형태로 제공하는 클라우드 컴퓨팅 서비스 모델은?

![2020_9L_13](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_13.jpg)

**답 : ②**



---

## 14. 다음 프로그램의 실행 결과로...

14. 다음 프로그램의 실행 결과로 옳은 것은?

![2020_9L_14](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_14.jpg)

**답 : ④**



---

## 15. 다음 프로그램은 연결 리스트를...

15. 다음 프로그램은 연결 리스트를 만들기 위한 코드의 일부분이다. 아래 그림과 같이 두 개의 노드 first, second가 연결되었다고 가정하고, 위의 코드를 참조하여 노드 tmp를 노드 first와 노드 second 사이에 삽입하고자 할 때, 프로그램 코드로 옳은 것은?

![2020_9L_15](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_15.jpg)

**답 : ②**



---

## 16. 다음 C 프로그램의 결과로 옳은...

16. 다음 C 프로그램의 결과로 옳은 것은?

![2020_9L_16](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_16.jpg)

**답 : ①**



---

## 17. 다음 이진 트리에 대하여...

17. 다음 이진 트리에 대하여 후위 순회를 하는 경우 다섯 번째 방문하는 노드는?

![2020_9L_17](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_17.jpg)

**답 : ④**



---

## 18. 프세스 스케줄링에 대한 설명으로...

18. 프세스 스케줄링에 대한 설명으로 옳지 않은 것은?

![2020_9L_18](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_18.jpg)

**답 : ①**







---

## 19. TCP/IP 프로토콜 스택에 대한...

19. TCP/IP 프로토콜 스택에 대한 설명으로 옳은 것은?

![2020_9L_19](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_19.jpg)

**답 : ③**



---

## 20. 다음 테이블 인스턴스(Instance)들에...

20. 다음 테이블 인스턴스(Instance)들에 대하여 오류 없이 동작하는 SQL(Structured Query Language) 문장은?

![2020_9L_20](c:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/2020_9L_20.jpg)

**답 : ③**







