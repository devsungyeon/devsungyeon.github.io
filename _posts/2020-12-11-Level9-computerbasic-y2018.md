---
title: "2018년 9급 전산직 컴퓨터일반 풀이"
strapline: "컴퓨터일반 풀이"
description: "2018년 9급 전산직 컴퓨터일반 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "9Level_computerbasic"
tag:
  - "9급"
  - "컴퓨터일반"
  - "9급공무원"
toc: true
last_modified_at: 2020-12-06
comments: true
---

# 2018년 9급 전산직 컴퓨터일반 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 유닉스 운영체제에 대한 설명으로...

1. 유닉스 운영체제에 대한 설명으로 옳지 않은 것은?

![2018_9L_1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_1.jpg)

**답 : ②**

② BSD 유닉스의 모든 코드는 ~~어셈블리 언어~~로 작성되었다.

 --> C언어로 작성되었다.

 --> BSD(Berkeley Software Distribution) 미국 캘리포니아 대학교 버클리에서 개발한 유닉스 운영 체제



---

## 2. 다음에서 설명하는 해킹 공격 ...

2. 다음에서 설명하는 해킹 공격 방법은?

![2018_9L_2](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_2.jpg)

**답 : ②**

① 스니핑(Sniffing) 

 ; "냄새를 맡다", "킁킁거리다"라는 뜻. 네트워크 상에 지나다니는 패킷들을 캡처하여 그 안에 있는 내용을 들여다보는 기술.

② 파밍(Pharming) 

 ; 도메인 네임 시스템(DNS) 또는 프락시 서버의 주소를 변조함으로써 사용자들로 하여금 진짜 사이트로 오인하여 접속하도록 유도하여 개인정보를 훔치는 새로운 컴퓨터 범죄 수법.

③ 트로이 목마(Trojan Horse)

 ; 무언가로 변장해 시스템 방어망을 뚫고 들어가는 악성코드의 한 종류. 

④ 하이재킹(Hijacking) 

 ; 시스템에 접근할 적법한 사용자 아이디와 패스워드를 모를 경우 공격 대상이 이미 시스템에 접속되어 세션이 연결되어 있는 상태를 가로채기 하는 공격, 아이디와 패스워드를 몰라도 시스템에 접근하여 자원이나 데이터를 사용할 수 있는 공격.



cf)

- 스푸핑(Spoofing) ; '속이기'라는 뜻. 외부 악의적 네트워크 침입자가 임의로 웹사이트를 구성하여 일반 사용자들의 방문을 유도. TCP/IP의 구조적 결함을 이요하여 사용자의 시스템 권한을 획득한 뒤 정보를 빼가는 해킹 수법. IP 스푸핑, DNS 스푸핑, 이메일 스푸핑, ARP 스푸핑 등...

- 스누핑(Snooping) ; '기웃거리다', '염탐하다'는 뜻. 네트워크 상에 떠도는 중요 정보를 **몰래** 획득하는 행위.

- 스니핑(Sniffing) ; "냄새를 맡다", "킁킁거리다"라는 뜻. 네트워크 상에 지나다니는 패킷들을 캡처하여 그 안에 있는 내용을 들여다보는 기술.

- 스미싱(Smishing) ; 문자메시지(SMS)와 피싱(Phishing)의 합성어, 문자 메시지의 인터넷주소 클릭하면 악성코드가 설치되어 피해자가 모르는 사이에 소액결제 피해 발생 또는 개인·금융정보 탈취하는 수법

- 스머핑(Smurfing) ; 고성능 컴퓨터를 이용해 초당 엄청난 양의 접속신호를 한 사이트에 집중적으로 보냄으로써 상대 컴퓨터의 서버를 접속 불능 상태로 만들어 버리는 해킹 수법. 핑 홍수(ping flood). 도스 공격의 일종으로 ICMP(Internet Control Message Protocol:호스트 서버와 인터넷 게이트웨이 사이에서 메시지를 제어하고 알려주는 프로토콜) 패킷을 말 그대로 홍수처럼 상대 시스템에 퍼붓는 방식

  

---

## 3. 다음 SQL 명령어에서 DDL(Data ...

3. 다음 SQL 명령어에서 DDL(Data Definition Language) 명령어만을 모두 고른 것은?

![2018_9L_3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_3.jpg)

**답 : ①**

- DDL ; CREATE, ALTER, DROP
- DML ; SELECT, UPDATE, DELETE, INSERT
- DCL ; COMMIT, ROLLBACK, GRANT(권한부여), REVOKE(권한취소)



---

## 4. 다음 수식에서 이진수 Y의 ...

4. 다음 수식에서 이진수 Y의 값은?(단, 수식의 모든 수는 8 비트 이진수이고 1의 보수로 표현된다)

![2018_9L_4](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_4.jpg)

**답 : ②**

  11110100<sub>(2)</sub> ==> 00001011<sub>(2)</sub>

\+               Y<sub>(2)</sub> ==>                 Z<sub>(2)</sub>

------------------------------

  11011111<sub>(2)</sub> ==> 00100000<sub>(2)</sub>

00001011<sub>(2)</sub> + Z<sub>(2)</sub> = 00100000<sub>(2)</sub>

Z<sub>(2)</sub> = 00100000<sub>(2)</sub> - 00001011<sub>(2)</sub> = 00010101<sub>(2)</sub>

00010101<sub>(2)</sub> ==> 11101010<sub>(2)</sub> = Y<sub>(2)</sub>



---

## 5. 다음 진리표를 만족하는 부울...

5. 다음 진리표를 만족하는 부울 함수로 옳은 것은? (단, · 은 AND, ⊕는 XOR, ⊙는 XNOR 연산을 의미한다)

![2018_9L_5](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_5.jpg)

**답 : ②**



-  **·** = AND

  | A    | B    | A·B  |
  | ---- | ---- | ---- |
  | 0    | 0    | 0    |
  | 0    | 1    | 0    |
  | 1    | 0    | 0    |
  | 1    | 1    | 1    |

- ⊕ = XOR

  | A    | B    | A⊕B  |
  | ---- | ---- | ---- |
  | 0    | 0    | 0    |
  | 0    | 1    | 1    |
  | 1    | 0    | 1    |
  | 1    | 1    | 0    |

- ⊙ = XNOR

  | A    | B    | A⊙B  |
  | ---- | ---- | ---- |
  | 0    | 0    | 1    |
  | 0    | 1    | 0    |
  | 1    | 0    | 0    |
  | 1    | 1    | 1    |



---

## 6. 스레싱(Thrashing)에 대한 설명...

6. 스레싱(Thrashing)에 대한 설명으로 옳지 않은 것은?

![2018_9L_6](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_6.jpg)

**답 : ③**

③ 각 프로세스에 설정된 작업 집합 크기와 페이지 프레임 수가 매우 큰 경우 다중 프로그래밍 정도(Degree of Multiprogramming)를 ~~증가~~시킨다.

==> 임계치에 도달하면 다중 프로그래밍 정도가 낮아진다.



- 스레싱(Thrashing) ; Page Fault(페이지 부재)가 연속적으로 발생하여 프로세스 수행시간보다 페이지 교체 시간이 많은 상태

  |                            개념도                            |                             설명                             |
  | :----------------------------------------------------------: | :----------------------------------------------------------: |
  | ![img](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/6-1) | 다중 프로그래밍 높아짐 ==> 이용률 향상<br />↓<br />임계치 도달 후 낮아짐<br />Multi-Processing System 발생 빈번<br />처리율 저하, 페이지 폴트 증가<br /> |



## 7. 인공신경망에 대한 설명으로 ...

7. 인공신경망에 대한 설명으로 옳은 것만을 모두 고른 것은?

![2018_9L_7](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_7.jpg)

**답 : ④**

ㄱ. 단층 퍼셉트론은 ~~배타적 합(Exclusive-OR)~~ 연산자를 학습할 수 있다.

==> 단층 퍼셉트론은 **XOR** 연산이 불가능하다.





---

## 8. 네트워크 기술에 대한 설명으로...

8. 네트워크 기술에 대한 설명으로 옳지 않은 것은?

![2018_9L_8](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_8.jpg)

**답 : ④**

④ SMTP(Simple Mail Transfer Protocol)는 ~~사용자 인터페이스 구성방법을 지정하는 전송 계층 프로토콜~~이다.

- 전송 계층 프로토콜 ; TCP, UDP

SMTP는 응용 계층 프로토콜이다.



---

## 9. 다음 Java 프로그램의 출력...

9. 다음 Java 프로그램의 출력 값은?

![2018_9L_9](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_9.jpg)

**답 : ③**

public class Test {
    public static void main(String[] args) {
        Super s1 = new Super('C'); // Super class 내부만 실행
        **Super s2 = new Sub('D'); // 부모 class도 실행**
    }
}

하위 코드 주석은 코드 실행 순서.

```java
class Super {
    Super() {
        System.out.print('A'); // 6
    }
    
    Super(char x) {
        System.out.print(x); // 2
    }
}

class Sub extends Super {
    Sub() {
        super(); // 5
        System.out.print('B'); // 7
    }
    
    Sub(char x) {
        this(); // 4
        System.out.print(x); // 8
    }
}

public class Test {
    public static void main(String[] args) {
        Super s1 = new Super('C'); // 1
        Super s2 = new Sub('D'); // 3
    }
}
```



---

## 10. 개발자가 사용해야 하는 ...

10. 개발자가 사용해야 하는 서브시스템의 가장 앞쪽에 위치하면서 서브시스템에 있는 객체들을 사용할 수 있도록 인터페이스 역할을 하는 디자인 패턴은?

![2018_9L_10](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_10.jpg)

**답 : ①**

① Facade 패턴 ; 서브시스템에 있는 인터페이스 집합에 대해서 하나의 통합된 인터페이스를 제공.

② Strategy 패턴 ; 각각의 알고리즘을 별도의 클래스로 캡슐화하고 이들을 상호교환이 가능한 것으로 정의. 동일 목정의 여러 알고리즘 중 선택해서 적용가능하게 하는 패턴.

③ Adapter 패턴 ; 기존 모듈 재사용을 위한 인터페이스 변경

④ Singleton 패턴 ; 클래스 인스턴스가 하나만 만들어지고 그 인스턴스의 전역접근



---

## 11. 소프트웨어 모듈 평가 기준으로...

11. 소프트웨어 모듈 평가 기준으로 판단할 때, 다음 4명 중 가장 좋게 설계한 사람과 가장 좋지 않게 설계한 사람을 순서대로 바르게 나열한 것은?

![2018_9L_11](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_11.jpg)

**답 : ③**

이상적 모듈

| 이상적인 모듈화 |               |
| --------------- | ------------- |
| 결합도          | **낮을 수록** |
| 응집도          | **높을 수록** |

|        | 자         | 스     | 제   | 외   | 공   | 내         |
| ------ | ---------- | ------ | ---- | ---- | ---- | ---------- |
| 결합도 | 자료       | 스탬프 | 제어 | 외부 | 공통 | 내용       |
|        | ***좋음*** |        |      |      |      | ***나쁨*** |

|        | 우     | 논     | 시     | 절     | 교     | 순     | 기     |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 응집도 | 우연적 | 논리적 | 시간적 | 절차적 | 교환적 | 순차적 | 기능적 |
|        | 나쁨   |        |        |        |        |        | 좋음   |



---

## 12. 자료구조에 대한 설명...

12. 자료구조에 대한 설명으로 옳지 않은 것은?

![2018_9L_12](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_12.jpg)

**답 : ①**

① 데크는 삽입과 삭제를 ~~한쪽 끝에서만~~ 수행한다.

==> 데크는 삽입과 삭제를 양쪽에서 진행한다.

Deque = Stack + Queue

![12-1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/12-1.png)

---

## 13. IPv4가 제공하는 기능만을...

13. IPv4가 제공하는 기능만을 모두 고른 것은?

![2018_9L_13](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_13.jpg)

**답 : ③**

- IPv4는 **비신뢰적**이고 비연결형인 데이터그램 프로토콜. 
- 최선형 전송 서비스(best-effort delivery service) ; IPv4 패킷이 훼손되거나 손실, 순서에 맞지 않거나 지연되어 도착할 수 있고, 네트워크에 발생시킬 수 있다.

ㄱ. 혼잡제어 ; 혼잡제어를 위해서, ICMP(Internet Control Message Protocol)을 통해 혼잡 제어 매커니즘을 추가한다.

ㄷ. 신뢰성 있는 전달 서비스 ; 신뢰성을 위해서는 TCP 처럼 신뢰성 있는 전송 계층 프로토콜과 함께 사용되어야 한다.



---

## 14. 결정 명령문 내의 각 조건식이...

14. 결정 명령문 내의 각 조건식이 참, 거짓을 한 번 이상 갖도록 조합하여 테스트 케이스를 설계하는 방법은?

![2018_9L_14](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_14.jpg)

**답 : ②**

① 문장 검증 기준(Statement Coverage)

 ; 모든 실행문의 수행 조사 

② 조건 검증 기준(Condition Coverage)

 ;  개별 조건 검사

③ 분기 검증 기준(Branch Coverage)

 ; 분기점 조사

④ 다중 조건 검증 기준(Multiple Condition Coverage)

 ; 전체 조건 검사



---

## 15. 가상 머신(Virtual Machine)에 대한...

15. 가상 머신(Virtual Machine)에 대한 설명으로 옳지 않은 것은?

![2018_9L_15](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_15.jpg)

**답 : ③**

③ 가상 머신 모니터(Virtual Machine Monitor)를 사용하여 가상화하는 경우 ~~반드시 호스트 운영체제가 필요~~하다.

==> 호스트 운영체제가 반드시 필요한 것은 아니다.



---

## 16. IEEE 802.11 무선 랜에 대한...

16. IEEE 802.11 무선 랜에 대한 설명으로 옳은 것은?

![2018_9L_16](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_16.jpg)

**답 : ④**

① IEEE 802.11a는 5 GHz 대역에서 ~~5.5 Mbps~~의 전송률을 제공한다.

② IEEE 802.11b는 직교 주파수 분할 다중화(OFDM) 방식을 사용하여 ~~최대 22 Mbps의 전송률~~을 제공한다.

③ IEEE 802.11g는 ~~5 GHz~~ 대역에서 직접 순서 확산 대역(DSSS) 방식을 사용한다.



| IEEE Standard | Frequency     | Maximum Data Rate |
| ------------- | ------------- | ----------------- |
| 802.11a       | 5GHz          | 54Mbps            |
| 802.11b       | 2.4GHz        | 11Mbps            |
| 802.11g       | 2.4GHz        | 54Mbps            |
| 802.11n       | 2.4GHz & 5GHz | 600Mbps           |
| 802.11ac      | 2.4GHz & 5GHz | 1.3Gbps           |
| 802.11ax      | 2.4GHz & 5GHz | 10-12Gbps         |



---

## 17. 데이터베이스의 동시성 ...

17. 데이터베이스의 동시성 제어에 대한 설명으로 옳지 않은 것은?

![2018_9L_17](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_17.jpg)

**답 : ④**

④ 2단계 로킹 프로토콜에서 각 트랜잭션이 정상적으로 커밋될 때까지 자신이 가진 모든 배타적 로크들을 해제하지 않는다면 ~~모든 교착상태를 방지할 수 있다.~~

2단계 로킹 프로토콜(2PL) ; 모든 교착상태를 방지할 수 **없다.**



---

## 18. 파일구조에 대한 설명으로...

18. 파일구조에 대한 설명으로 옳지 않은 것은?

![2018_9L_18](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_18.jpg)

**답 : ③**

③ ISAM은 레코드 삽입을 위한 별도의 오버플로우 영역을 ~~필요로 하지 않는다.~~

- 색인순차파일(인덱스된 순차파일, ISAM;Indexed Sequential Access Method)
  - 정적 인덱싱
  - 정적 인덱싱은 **오버플로우** 필요





---

## 19. 다음 C 프로그램의 출력...

19. 다음 C 프로그램의 출력 값은?

![2018_9L_19](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_19.jpg)

**답 : ②**

static 은 내부에서만 존재.

```c
#include <stdio.h>

int a = 10;
int b = 20;
int c = 30;

void func(void)
{
    static int a = 100;
    int b = 200;
    
    a++;
    b++;
    c = a;
}

int main(void)
{
    func(); // a:10, b:20, c:101, static a:101
    func(); // a:10, b:20, c:102, static a:102
    
    printf("a = %d, b = %d, c = %d\n", a, b, c);
    
    return 0;
}
```



---

## 20. 해싱(Hashing)에 대한 ...

20. 해싱(Hashing)에 대한 설명으로 옳지 않은 것은?

![2018_9L_20](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2018_9L/2018_9L_20.jpg)

**답 : ③**

③ 선형 조사법(Linear Probing)은 ~~연결리스트(Linked List)를 사용하여 오버플로우 문제를 해결~~한다.

- 선형 조사법은 다음(next) 빈 자리를 찾아본다.
- 체이닝(Chaining) ; 연결리스트를 통해, 충돌 발생시 연결리스트를 통해 오버플로우 문제를 해결한다.

