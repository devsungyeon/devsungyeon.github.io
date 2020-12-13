---
title: "2017년 9급 전산직 컴퓨터일반 풀이"
strapline: "컴퓨터일반 풀이"
description: "2017년 9급 전산직 컴퓨터일반 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "9Level_computerbasic"
tag:
  - "9급"
  - "컴퓨터일반"
  - "9급공무원"
toc: true
last_modified_at: 2020-12-13
comments: true
---

# 2017년 9급 전산직 컴퓨터일반 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 컴퓨터 구조에 대한 ...

1. 컴퓨터 구조에 대한 설명으로 옳지 않은 것은?

![2017_9L_1](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_1.jpg)

**답 : ③**

③ CISC 구조는 RISC구조에 비해 ~~명령어 종류가 적고 고정 명령어 형식을 취한다.~~

==> CISC 구조는 명령어 종류가 많고 가변 명령어 형식을 취한다.

| Abbreviation | CISC                                                         | RISC                                                         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Means        | Complex Instruction Set Computer                             | Reduced Instruction Set Computer                             |
| 명령어 형식  | 가변 길이 명령어 사용<br />==> 각각의 명령어가 프로세싱 성능을 극대화<br />==> 명령어 해석이 어렵고, 제어장치가 복잡. | 고정 길이 명령어 사용<br />==> 신속한 프로세싱 달성을 위함<br />==> 명령어 해석이 쉽고, 제어장치도 간단. |
| 특징         | 비교적 적은 명령어로 프로그램 실행.                          | 명령어가 작고 단순. 많은 수의 명령어가 조합됨.               |

- EISC(Extendable Instruction Set Computer)
  - CISC + RISC
  - RISC의 간결성과 CISC 확장성을 동시에 가짐.
  - 확장 레지스터와 확장 플래그를 도입하여 operand 길이를 필요한 만큼 확장 가능함.





---

## 2. 중앙처리장치 내의 레지스터 중...

2. 중앙처리장치 내의 레지스터 중 PC(program counter), IR(instruction register), MAR(memory address register), AC(accumulator)와 다음 설명이 옳게 짝지어진 것은?

![2017_9L_2](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_2.jpg)

**답 : ④**

![2-1](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2-1.png)

- PC : 다음에 인출할 명령어의 주소를 보관.
- MAR : CPU가 메모리에 접근하기 위해 참조하려는 명령어의 주소 혹은 데이터의 주소를 보관.
- MBR : PC 혹은 MAR이 지정하는 주기억장치의 **내용을 임시로 기억**하는 레지스터
- AC : 명령어 실행 시 필요한 데이터를 일시적으로 보관.
- IR : 가장 최근에 인출한 명령어를 보관.



---

## 3. 트랜잭션이 정상적으로...

3. 트랜잭션이 정상적으로 완료(commit)되거나, 중단(abort)되었을 때 롤백(rollback)되어야 하는 트랜잭션의 성질은?

![2017_9L_3](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_3.jpg)

**답 : ①**

### ▣ ACID

① 원자성(atomicity)

- 반드시 완료되거나 혹은 실패(취소)
- Commit(완료, 성공)와 Rollback(복귀, 실패)
- 트랜잭션과 관련된 작업들이 부분작으로 실행되다가 중단되지 않는 것을 보장

② 일관성(consistency)

- 트랜잭션이 실행을 완료하면 언제나 일관성 있는 데이터베이스 상태로 유지.

③ 격리성(isolation) : 고립성. 

- 트랜잭션을 수행 시 다른 트랜잭션의 연산 작업이 끼어들지 못하도록 보장.
- 중간 단계의 연산 데이터를 볼 수 없음.

④ 영속성(durability)

- 성공적으로 수행된 트랜잭션은 영원히 반영되어야 함.



---

## 4. 다음의 설명과 무선 PAN...

4. 다음의 설명과 무선 PAN 기술이 옳게 짝지어진 것은?

![2017_9L_4](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_4.jpg)

**답 : ①**



---

## 5. 디스크 헤드의 위치가 55이고...

5. 디스크 헤드의 위치가 55이고 0의 방향으로 이동할 때, C-SCAN 기법으로 디스크 대기 큐 25, 30, 47, 50, 63, 75, 100을 처리한다면 제일 마지막에 서비스 받는 트랙은?

![2017_9L_5](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_5.jpg)

**답 : ②**

- C-SCAN(Circular Scan)
  - 디스크가 원형으로 되어있는 형태를 가진다고 생각한다.
  - 0~100까지의 큐가 있을 때, 55번에서 **100방향으로 이동**한다면, 100번까지 이동후에 0번으로 이동하여 **100방향**으로 다시 탐색한다.

| 디스크 | 25   | 30   | 47   | 50   | 63   | 75   | 100  |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 순서   | 4    | 3    | 2    | 1    | 7    | 6    | 5    |

- FCFS(First Come First Served)

  | 디스크 | 25   | 30   | 47   | 50   | 63   | 75   | 100  |
  | ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
  | 순서   | 1    | 2    | 3    | 4    | 5    | 6    | 7    |

- SSTF(Shortest Seek Time First)

  - 현재 위치에서 탐색 거리가 가장 짧은 요청 트랙을 먼저 서비스.

  | 디스크 | 25   | 30   | 47   | 50   | 63   | 75   | 100  |
  | ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
  | 순서   | 4    | 3    | 2    | 1    | 5    | 6    | 7    |

- SCAN

  - 이동 방향에서 가장 짧은 거리에 있는 요청을 먼저 서비스
  - 끝지점에 도달 후, 진행 방향이 변경된다.

  | 디스크 | 25   | 30   | 47   | 50   | 63   | 75   | 100  |
  | ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
  | 순서   | 4    | 3    | 2    | 1    | 5    | 6    | 7    |

  



---

## 6. 컴퓨터 시스템 구성요소...

6. 컴퓨터 시스템 구성요소 사이의 데이터 흐름과 제어 흐름에 대한 설명으로 옳은 것은?

![2017_9L_6](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_6.jpg)

**답 : ④**

- 제이 흐름 ; 제어장치에서 연관된 흐름은 모두 제어 흐름이다.
- 데이터 흐름 ; 제어 흐름 이외의 흐름.



## 7. 수식의 결과가 거짓...

7. 수식의 결과가 거짓(false)인 것은?

![2017_9L_7](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_7.jpg)

**답 : ②**

![7-1](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\7-1.png)

① 20D<sub>(16)</sub> > 524<sub>(10)</sub> : True

- 20D<sub>(16)</sub> = 2 * 16<sup>2</sup> + 13 = 2 * 256 + 13 = 512 + 13 = 525<sub>(10)</sub>

② 0.125<sub>(10)</sub> = 0.011<sub>(2)</sub> : False

- 0.011<sub>(2)</sub> = 0.01<sub>(2)</sub> + 0.001<sub>(2)</sub> = 0.25<sub>(10)</sub> + 0.125<sub>(10)</sub> = 0.375<sub>(10)</sub>

③ 10<sub>(8)</sub> = 1000<sub>(2)</sub> : True

- 10<sub>(8)</sub> = 8<sub>(10)</sub> = 1000<sub>(2)</sub>

④ 0.1<sub>(10)</sub> < 0.1<sub>(2)</sub> : True

- 0.1<sub>(2)</sub> = 0.5<sub>(10)</sub>



---

## 8. '인터넷 서점'에 대한 ...

8. '인터넷 서점'에 대한 유스케이스 다이어그램에서 '회원등록' 유스케이스를 수행하기 위해서는 '실명확인' 유스케이스가 반드시 선행되어야 한다면 이들의 관계는?

![2017_9L_8](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_8.jpg)

**답 : ③**

==> **"반드시 선행되어야 한다"**에서 포함 관계임을 파악할 수 있다.



### UML 유스케이스 다이어그램 - Usecase Diagram

---

- 시스템과 사용자의 상호작용을 다이어그램으로 표현한 것으로 사용자의 관점에서 시스템의 서비스 혹은 기능 및 그와 관련한 외부 요소를 보여주는 것.
- 사용자가 시스템 냉부에 있는 기능 중에 어떤 기능을 사용할 수 있는지 나타내며 유스케이스 다이어그램을 사용함으로써 고객과 개발자가 요구사항에 대한 의견을 조율할 수 있다.

- 구성요소 : 시스템(System), 액터(Actor), 유스케이스(Usecase), 관계(Relation)

  - 시스템(System) ; 만들고자 하는 프로그램

  - 액터(Actor) ; 시스템의 외부에서 시스템과 상호작용을 하는 사람 혹은 시스템

  - 유스케이스(Usecase) ; 사용자 입장에서 바라본 시스템의 기능

  - 관계(Relation) ; 액터와 유스케이스 사이의 의미있는 관계

    - 연관(Association) ; 유스케이스와 액터간의 상호작용이 있음을 표현

    - 의존(Dependency)

      - 포함(Include) ; 하나의 유스케이스가 다른 유스케이스의 실행을 전제로 할 때 형성되는 관계

        ==> 포함되는 유스케이스는 포함하는 유스케이스를 실행하기 위해 **반드시** 먼저 실행되어야 하는 경우.

      - 확장(Extend) ; 확장 기능 유스케이스와 확장 대상 유스케이스 사이에 형성되는 관계

    - 일반화(Generalization) ; 유사한 유스케이스 또는 액터를 모아 추상화한 유스케이스 또는 액터와 연결시켜 그룹을 만들어 이해도를 높이기 위한 관계

출처

https://googry.tistory.com/2



---

## 9. 노드 A, B, C를 가지는 이중...

9. 노드 A, B, C를 가지는 이중 연결 리스트에서 노드 B를 삭제하기 위한 의사코드(pseudo code)로 옳지 않은 것은? (단, 노드 B의 메모리는 해제하지 않는다)

![2017_9L_9](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_9.jpg)

**답 : ④**

A->next = A->next->next;

![9-1](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\9-1.png)



A->next->next->prev = B->prev;

//A->next->next->prev ; 오류 발생. A->next->next ; null

![9-2](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\9-2.png)



---

## 10. 이동 애드혹 네트워크(MANET)에...

10. 이동 애드혹 네트워크(MANET)에 대한 설명으로 옳지 않은 것은?

![2017_9L_10](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_10.jpg)

**답 : ④**

④ 동적인 네트워크 토폴로지를 효율적으로 구성하기 위해 ~~액세스 포인트(AP)와 괕은 중재자를 필요로 한다.~~

==> 이동 애드훅 네트워크는 기지국이나 무선 접속점과 같은 인프라스트럭처가 없는 환경에서 **디바이스끼리 연결**해서 이용하는 통신망을 의미한다.

==> 주로 기지국이 설치되기 힘든 곳이나 전쟁, 재난상황 등에 이용된다.



---

## 11. 공개키 암호화 방법을 사용하여...

11. 공개키 암호화 방법을 사용하여 철수가 영희에게 메시지를 보내는 것에 대한 설명으로 옳지 않은 것은?

![2017_9L_11](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_11.jpg)

**답 : ③**

③ 철수는 ~~자신의 공개키~~를 사용하여 평문을 암호화한다.

==> 철수는 **상대(수신인)의 공개키**를 사용하여 평문을 암호화한다.

|           | 개인키로 암호화                          | 공개키로 암호화                   |
| --------- | ---------------------------------------- | --------------------------------- |
| 사용 유형 | **인증**을 위해 사용.                    | 자신의 평문을 상대에게 보낼때.    |
| 암호화    | 송신자는 본인의 개인키로 암호화          | 송신자는 수신인의 공개키로 암호화 |
| 복호화    | 수신인(ex:CA)은 송신자의 공개키로 복호화 | 수신인은 수신인의 개인키로 복호화 |



---

## 12. 네트워크 구성 형태에 대한...

12. 네트워크 구성 형태에 대한 설명으로 옳지 않은 것은?

![2017_9L_12](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_12.jpg)

**답 : ③**

③ ~~트리(tree)형~~은 고리처럼 순환형으로 구성된 형태로서 네트워크 재구성이 수월하다.

==> 트리(tree)형은 부모자식 노드를 가지는 나무 뿌리형태를 가진다.

==> 링(Ring)형은 고리처럼 순환형으로 구성된 형태로서 네트워크 재구성이 수월하다.



- 네트워크 토폴로지

| 종류           | 모양                                                         | 장점                                                         | 단점                                                         |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 버스=bus       | ![5_bus](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\5_bus.png) | 설치가 간단<br />비용이 저렴                                 | 장애발견이 어려움<br />중앙 통신선 장애 시 전체 네트워크 문제 발생 |
| 링=ring        | ![5_ring](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\5_ring.png) | 모든 장치가 토큰에 접근 가능<br />순차적인 네트워크<br />컴퓨터 간 연결을 위한 네트워크 서버 불필요 | 한 노드 장애가 전체 망에 문제 발생<br />장치를 추가, 변경 시 네트워크 영향 |
| 트리=계층=tree | ![5_tree](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\5_tree.png) | 제어가 간단<br />네트워크 확장 용이                          | 병목 현상 가능<br />상위 노드에 트래픽 집중되어 병목 현상<br />상위 노드가 장애 발생되면, 하위 네트워크 장애 |
| 스타=성=star   | ![5_star](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\5_star.png) | 장애 발견이 용이<br />Netword 관리가 용이<br />한 노드 장애는 전체 영향 없음 | 중앙 노드 장애 발생시 전체 네트워크 문제 발생<br />많은 양의 케이블을 사용하므로 높은 비용 |
| 메시=mesh      | ![5_mesh](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2020_9L/\5_mesh.png) | 장애에 가장 강함<br />한 경로에 장애가 발생해도 다른 경로로 통신 가능<br /> | 연결선이 가장 많아 가장 높은 비용<br />네트워크 관리 어려움  |





---

## 13. 다음에서 설명하는 ...

13. 다음에서 설명하는 보안공격방법은?

![2017_9L_13](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_13.jpg)

**답 : ②**

① 키로거(Key Logger) ; 컴퓨터가 받아들이는 입력 정보의 기록, 그 중에서도 주로 키보드를 통한 입력의 기록을 제작하는 장치를 말한다. 대개 사용자의 동의 없이 기록을 만들고 전송하는 방식의 크래킹 도구로 사용된다.

② DDos(Distributed Denial of Service) ; 여러 대의 좀비 컴퓨터를 분산 배치하여 가상의 접속자를 만든 후 처리할 수 없을 정도로 매우 많은 양의 패킷을 동시에 발생시켜 시스템을 공격한다.

③ XSS(Cross Site Scripting) ; 게시판이나 웹 메일 등에 자바 스크립트와 같은 스크립트 코드를 삽입해 개발자가 고려하지 않은 기능을 작동하게 하는 공격 기법이다.

④ 스파이웨어(Spyware) ; 악의적인 스파이. 사용자의 동의 없이 컴퓨터에 몰래 설치되어, 중요한 개인정보 등을 수집하고 공격자의 서버로 전송한다.



---

## 14. 논리적 데이터 모델에 대한 ...

14. 논리적 데이터 모델에 대한 설명으로 옳지 않은 것은?

![2017_9L_14](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_14.jpg)

**답 : ①**

① ~~개체관계 모델은 개체와 개체 사이의 관계성을 이용하여 데이터를 모델링한다.~~

==> 개체관계(E-R) 모델은 ~~논리적 데이터 모델이 아닌~~ **개념적 데이터 모델**이다.

- 데이터 모델의 정의

  ==> 현실 세계의 정보들을 컴퓨터에 표현하기 위해서 단순화, 추상화하여 체계적으로 표현한 개념적 모형

- 데이터 모델의 종류

  - 개념적 데이터 모델 ; 현실 세계에 대한 인식을 추상적 개념으로 표현하는 과정

    - E-R 모델(Entity-Relationship) ; 개체-관계 모델. 개체 타입(Entity)과 이들 간의 관계 타입(Relationship)을 이용해 개념적으로 표현.

  - 논리적 데이터 모델 ; 개념적 모델링 과정에서 얻은 개념적 구조를 컴퓨터가 이해하고 처리할 수 있는 컴퓨터 환경에 맞도록 변환하는 과정

    - 계층형 데이터 모델(Hierarchical Data Model) ; **트리 구조**를 이용해서 데이터 상호관계를 계층적으로 정의한 구조.

      ==> 상위와 하위 레코드가 일대다(1:N) 대응 관계로 구성.

      ==> 개체 간의 관계를 부모와 자식으로 표현

    - 망(네트워크)형 데이터 모델(Network Data Model) ; 그래프 구조를 이용해서 데이터 상호 관계를 정의한 구조.

      ==> 상위와 하위 레코드가 다대다(N:M) 대응 관계로 구성.

      ==> 개체 간의 관계를 오너(Owner)와 멤버(Member)의 관계로 표현

    - 관계형 데이터 모델(Relational Data Model) ; 계층 모델과 망 모델의 복잡한 구조를 단순

      ==> 표(Table)을 이용하여 데이터 상호관계를 정의하는 DB 구조.

      ==> 기본기(Primary Key)와 이를 참조하는 외래키(Foreign Key)로 데이터 간의 관계를 표현

      ==> 대표적인 언어 : SQL

      ==> 1:1, 1:N, N:M 관계를 자유롭게 표현.

    - 객체 지향형 데이터 모델(OODB ; Object-Oriented DataBase) ; 객체 개념을 도입. 공학 분야 또는 멀티미디어 데이터와 같이 복잡한 관계를 가진 데이터들을 표현하는 데 적합.

      ==> 클래스(class) 또는 객체(Object)로 표현.

      



---

## 15. 다음에서 설명하는 소프트웨어...

15. 다음에서 설명하는 소프트웨어 개발 방법론은?

![2017_9L_15](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_15.jpg)

**답 : ②**

① 통합 프로세스(UP) : 

② 익스트림 프로그래밍(eXtreme Programming) : 

③ 스크럼 : 

④ 나선형 모델 : 



### 소프트웨어 개발 프로세스 모형

---

- 폭포수 모형(waterfall model, 선형순차 모형)

  - 정의 : 적용사례가 많고, 가장 오래되어 널리 사용되는 방법
  - 특징: 단계적. 병행 불가. 반복 비허용.각 단계별로 정의, 산출물이 명확.
  - 장점 : 기존의 시스템을 보완하는데 적합. 결과물이 명확하므로 가시성이 매우 우수.
  - 단점 : 신규 Project 부적합. 설계와 코딩 및 테스트 지연(분석에 많은 시간 소요)

- 프로토타이핑 모형(Prototyping model, 원형 모형)

  - 정의 : 개발자가 소프트웨어의 모델을 사전에 만드는 공정. 견본품(프로토타입)을 만들어 의사소통의 도구로 사용.
  - 특징 : 고객의 요구를 만족할 때까지 과정이 반복. waterfall에서 전 단계로 돌아갈 수 없는 점을 보완.
  - 개발절차 : 요구사항분석 → 신속한 설계 → 프로토타입 작성 → 사용자 평가 → 프로토타입의 정제(세련화) → 공학적 제품화
  - 장점 : 개발이 되고 있는지 명확히 확인 가능.
  - 단점 : 견본품이 과대 포장되어 발주자가 더 많은 기능을 기대. 추가 비용이 발생, 관리 및 통제가 어려움. 사용자는 견본품을 최종 제품으로 착각.

- 나선형 모형(Spiral Model)

  - 정의 : **폭포수 모델의 제어**와 **체계적인 측면에 원형 모델의 장점**을 취합. 점진적인 성과를 보면서 위험 부담을 줄일 수 있는 방법. 위험 분석을 해 나가면서 시스템을 발전.
  - 단계 : 계획수립 → 위험분석 → 공학 → 평가
  - 특징 : 대규모 시스템의 개발에 적합. 개발 단계를 반복적으로 수행하여 점차적으로 완벽한 제품을 개발.

- V-모형

  - 정의 : 개발 작업과 검증 작업 사이의 관계를 명백히 드러내 놓은 폭포수 모델의 변형으로, 폭포수 모형에서는 감춰져 있는 반복과 재작업을 드러내 놓은 것. 코딩단계를 중심으로 **분석과 설계단계는 왼편**에, **테스팅과 유지보수단계는 오른편**에 위치한다.

  - 특징: **폭포수 모형**은 **문서와 결과물 도출**에 중점. **V 모형은 작업과 결과의 검증**에 초점

    생명주기 모든 단계에서 검증과 확인 과정이 있어 오류를 줄일 수 있다. 의료제어시스템이나 원전제어시스템과 같은 높은 신뢰성이 필요한 분야에 적합.

- 점증적 모형(Incremental model)

  - 정의 : 선형 순차 모델 요소들에 프로토타입의 반복성을 결합.

    - 점증적인 방법 ; 전체 시스템을 여러 개의 서브시스템을 나누고 일부 기능만을 포함한 서브시스템을 릴리스하고 다음에 새로운 **기능을 추가**해 나가는 형태
    - 반복적인 방법 ; 처음부터 시스템 전체 기능을 대상으로 하되 릴리스 할 때마다 **기능을 보완**해 나가는 형태

  - 장점 : 소규모 기능으로 사용 교육을 할 수 있으며, 이를 통해 부족한 점을 파악할 수 있다.

    자주 릴리스하며 예상하지 못한 문제를 파악하여 신속하게 고칠 수 있다.

  - 단점 : 증분은 비교적 작아야 한다.

- UP(United Process) 모형 = RUP(Rational UP)

  - 정의 : UML 방법과 도구를 위한 프레임 워크로 설계. **유스케이스 기반, 아키텍처 중심, 반복적이고 점진적**, 점증적
  
  - 특징 : 구축, 전이, 산출 단계가 수행되는 것과 동시에 다음 소프트웨어 점증을 시작한다. **병행성**
  
  - 장점 : 반복 과정에서 높은 위험도를 잘 관리.
  
  - UP의 개발 단계
  
    - 개념 정립(도입, Inception) ; 개략적으로 파악.
    - 전개(정련, Elaboration) ; 비전을 구체화. 개발 범위 확정.
    - 구축(Construction) ; 구현하고 설치를 준비
    - 전환(전이, Transition) ; 테스트, 설치, 다음 반복 단계를 준비
  
    
  
  

### 신속한 소프트웨어 개발 모형

---

==> 기업이 소프트웨어를 신속하게 개발할 필요성.

==> 중첩된 반복적인 프로세스.

==> **설계 문서가 최소화**되거나 프로그래밍 환경에 의해 **자동적**으로 생성.

- 애자일(agile) 기법
  - Coding < Test
  - 정의 : 설계와 문서화보다는 소프트웨어 자체에 초점.
  - 원리 ; 고객 참여, 점증적인 인도, 사람은 프로세스가 아님, 변경을 수용, 단순성의 유지.
  - 문제점 ; 대규모 시스템 개발에는 적합하지 않고, **중소규모 개발에 적합**
- XP(eXtreme Programming) 모형
  - 개요
    - 중소규모 개발에 무거운 계획-기반 개발 기법(ex;나선형) 을 적용하면 불합리.
    - 가장 널리 이용되는 애자일 기법 중 하나. 점증적 방법을 변형.
    - 5가지에 기초 : **의사소통, 단순함, 피드백, 용기, 존중**
    - **"고객에게 최고의 가치를 가장빨리"**
  - 정의 : **고객의 참여를 극한(extreme) 수준까지 유도**
    - 스토리 카드 개발 ; 고객의 요구를 요약.
    - 모든 요구사항은 시나리오(사용자 스토리)로 표현
    - 프로그래머들은 **"짝"**을 이룸. **코드 작성 전, 시험을 준비**
  - 특징
    - 시험 우선
    - 시나리오로부터 점증적인 시험 개발
    - 자동화 시스템 사용.
  - 문제점
    - 구현 전에 시험 가능한 컴포넌트가 작성
  - 프로세스
    - 계획 ; 사용자 스토리 생성
    - 설계 ; 간단한 설계
    - 코딩 ; 단위 테스트 개발. pair programming
    - 테스팅 ; 코딩 전 단위 테스트 케이스 생성
- 스크럼(Scrum)
  - 정의 ; 30일마다 동작 가능한 제품을 제공하는 **스프린트(Sprint, 2~4주기마다 제품생산)**를 중심
    - 항상 팀 단위 미팅. 날마다 15분 정도 회의
- 테스트 주도 개발(Test-driven development, TDD)
  - 정의 ; 테스팅과 코드 개발을 중첩. JUnit과 같은 자동화된 테스트 프레임워크 환경이 TDD에 필수적.
    - **신규 개발에 적합** not 기존.
- RAD(Rapid Application Development) 모형



---

## 16. 다음 프로세스 집합에 대하여 ...

16. 다음 프로세스 집합에 대하여 라운드 로빈 CPU 스케줄링 알고리즘을 사용할 때, 프로세스들의 총 대기시간은? (단, 시간0에 P1, P2, P3 순서대로 도착한 것으로 하고, 시간 할당량은 4밀리초로 하며, 프로세스 간 문맥교환에 따른 오버헤드는 무시한다)

![2017_9L_16](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_16.jpg)

**답 : ②**

- RR(Round Robin) ; 시간 할당량을 통하여 프로세스에게 공평한 할당을 주기 위함.

시간 할당량(time slice) = 4

대기시간 = 작업 종료 시간 - 프로세스 도착 시간(여기서는 모두 0) - 버스트 시간(작업시간)

P1 WaitTime = 27 - 0 - 20 = 7

P2 WaitTime = 7 - 0 - 3 = 4

P3 WaitTime = 11 - 0 - 4 = 7

총 대기 시간 = 7 + 4 + 7 = 18

| 작업 중인 프로세스 | P1   | P2   | P3   | P1   | P1   | P1   | P1   |
| ------------------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 시작 시간          | 0    | 4    | 7    | 11   | 15   | 19   | 23   |
| 종료 시간          | 4    | 7    | 11   | 15   | 19   | 23   | 27   |
| 작업 시간          | 4    | 3    | 4    | 4    | 4    | 4    | 4    |
| P1 남은 시간       | 16   | 16   | 16   | 12   | 8    | 4    | 0    |
| P2 남은 시간       | 3    | 0    | 0    | 0    | 0    | 0    | 0    |
| P3 남은 시간       | 4    | 4    | 0    | 0    | 0    | 0    | 0    |



---

## 17. 다음 C 프로그램의 출력...

17. 다음 C 프로그램의 출력 값은?

![2017_9L_17](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_17.jpg)

**답 : ④**

```c
#include <stdio.h>

void funCount();

int main(void) {
    int num;
    for(num=0; num<2; num++)
        funCount(); //funCount 2번 실행
   	return 0;
}

void funCount() {
    int num=0;
    static int count; // static은 값 유지.
    
    printf("num = %d, count = %d\n",
          ++num, count++);
    // ++num 은 사전 수행.
    /* first funCount
    	num은 사전 수행. num = 1
    	count는 static이므로 초기화 0.
    	count는 현재 0, printf 이후 ++.
    */ 
    
    /* second funCount
    	num = 0, count = 1
    	num은 static이 아니므로 새롭게 정의
    	num은 사전 수행. num = 1
    	count는 현재 1, printf 이후 ++.
    */ 
}
```



---

## 18. 페이지 크기가 2,000byte인 페이징...

18. 페이지 크기가 2,000byte인 페이징 시스템에서 페이지테이블이 다음과 같을 때 논리주소에 대한 물리주소가 옳게 짝지어진 것은? (단, 논리주소와 물리주소는 각각 0에서 시작되고, 1 byte 단위로 주소가 부여된다.)

![2017_9L_18](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_18.jpg)

**답 : ③**

보기를 통해 해결 한다.

①

논리주소 : 4,300 = 2,000 * ***2*** + 300 ==> 페이지번호(논리) : ***2***

페이지번호(논리) : ***2*** ==> 페이지번호(물리) : ***5***

물리주소 : 2,000 * 5 + 300 = 10,300

②

논리주소 : 3,600 = 2,000 * ***1*** + 1,600 ==> 페이지번호(논리) : ***1***

페이지번호(논리) : ***1*** ==> 페이지번호(물리) : ***3***

물리주소 : 2,000 * 3 + 1,600 = 7,600

③

논리주소 : 2,500 = 2,000 * ***1*** + 500 ==> 페이지번호(논리) : ***1***

페이지번호(논리) : ***1*** ==> 페이지번호(물리) : ***3***

물리주소 : 2,000 * 3 + 500 = 6,500

④

논리주소 : 900 = 2,000 * ***0*** + 900==> 페이지번호(논리) : ***0***

페이지번호(논리) : ***0*** ==> 페이지번호(물리) : ***7***

물리주소 : 2,000 * 7 + 900 = 14,900



---

## 19. HTML5의 특징에 대한 설명으로...

19. HTML5의 특징에 대한 설명으로 옳지 않은 것은?

![2017_9L_19](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_19.jpg)

**답 : ③**

③ 디바이스에 ~~접근할 수 없어서 개인정보 보호 및 보안을 철저히 유지할 수 있다.~~

==> HTML은 비 표준 플러그인(Flash, ActiveX, silverlight 등)을 사용하여 동영상 재생 및 그래픽 관련 프로그램 등 운영

==> HTML5는 HTML을 보완. Audio/Video 를 포함한 확장된 태그를 지원.

==> 새롭게 추가된 기술들을 통해 새로운 보안 위협.



---

## 20. 컴퓨터의 발전 과정에...

20. 컴퓨터의 발전 과정에 대한 설명으로 옳지 않은 것은?

![2017_9L_20](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2017_9L\2017_9L_20.jpg)

**답 : ①**

① 포트란, 코볼같은 고급 언어는 집적회로(IC)가 적용된 ~~제3세대 컴퓨터~~부터 사용되었다.

==> 2세대부터 사용되었다.

6

|          | 1세대                            | 2세대                                     | 3세대                          | 4세대                                 | 5세대  |
| -------- | -------------------------------- | ----------------------------------------- | ------------------------------ | ------------------------------------- | ------ |
| 소자     | 진공관                           | 트랜지스터                                | IC(집적회로)                   | 고밀도집적회로                        | 광소자 |
| 연산속도 | ms                               | us                                        | ns                             | ps                                    | fs     |
| 언어     | 저급언어<br />기계어, 어셈블리어 | 고급언어<br />Fortran, Cobol              | 구조적 언어<br />Pascal, C언어 | 비절차적 언어(SQL)<br />객체지향 언어 | AI     |
| 특징     | 하드웨어                         | 다중 프로그래밍<br />시분할/실시간 시스템 | UNIX                           | 분산처리, 병렬처리, 가상기계          |        |

