---
title: "2019년 9급 전산직 컴퓨터일반 풀이"
strapline: "컴퓨터일반 풀이"
description: "2019년 9급 전산직 컴퓨터일반 풀이"
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

# 2019년 9급 전산직 컴퓨터일반 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1.  CPU 내부 레지스터로 옳지 않은 것은?

1. CPU 내부 레지스터로 옳지 않은 것은?

![2019_9L_1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_1.jpg)

**답 : ②**

- CPU ; 누산기, 프로그램 카운터, 메모리 버퍼 레지스터 ..
- 캐시 메모리 ; CPU와 메모리 사이의 속도 차이 해결.



---

## 2. 다음 전위(prefix) 표기식의 계산 결과는?

2. 다음 전위(prefix) 표기식의 계산 결과는?

![2019_9L_2](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_2.jpg)

**답 : ④**

**- 5 4 x 4 7**

**( + (- 5 4) (x 4 7) )**

**( + (5 - 4) (4 x 7) **

**( (5 - 4) + (4 x 7) ) = 1 + 28 = 29**



---

## 3.  사진이나 동영상 등의 디지털 콘텐츠에...

3. 사진이나 동영상 등의 디지털 콘텐츠에 저작권자나 판매자 정보를 삽입하여 원본의 출처 정보를 제공하는 기술은?

![2019_9L_3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_3.jpg)

**답 : ②

① 디지털 사이니지 : 공공장소 및 상업 공간에 네트워크로 제어가 가능한 디지털 디스플레이를 통하여 다양한 정보 및 광고를 전달하는 디지털 미디어

② 디지털 워터마킹 : **저작자 혹은 판매자** 정보 삽입.

- 사진이나 동영상 등의 디지털 콘텐츠에 저작권자나 판매자 정보를 삽입하여 원본의 출처 정보를 제공하는 기술.

③ 디지털 핑거프린팅 : **구매자** 정보 삽입. 

- 사용자 혹은 구매자의 정보를 멀티미디어 콘텐츠 내에 삽입하는 기술

④ 콘텐츠 필터링 : 자료 이용시 데이터의 접근을 제한하거나 필터링. ex) 자녀보호기능(앱, 게임, 영화 등 연령제한).

- 검색어 기반 필터링, 해시 기반 필터링, 특징 기반 필터링
  - 검색어 기반 필터링 ; 검색어를 데이터베이스로 디지털콘텐츠의 검색을 차단.
  - 해시 기반 필터링 ; 해시함수를 이용해 콘텐츠 고유 값을 데이터베이스로 하여 해당 콘텐츠를 인식해 차단.
  - 특징 기반 필터링 ; 음악, 영화 등의 콘텐츠가 갖고 있는 고유한 특징을 추출해 그 정보를 데이터베이스로 하여 해당 콘텐츠를 인식해 차단.



---

## 4. 1K x 4bit RAM 칩을 사용하여 8K x 16bit...

4. 1K x 4bit RAM 칩을 사용하여 8K x 16bit 기억장치 모듈을 설계할 때 필요한 RAM 칩의 최소 개수는?![2019_9L_4](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_4.jpg)

**답 : ④**

1K x 4bit RAM 칩을 사용하여 8K x 16bit 모듈 설계

1K x 4bit x N  **=**  8K x 16bit 모듈 설계

**K ; 8배차이, bit ; 4배차이.**

**8 x 4 = 32개**



---

## 5. 프로세스와 스레드(thread)에 대한...

5. 프로세스와 스레드(thread)에 대한 설명으로 옳지 않은 것은?

![2019_9L_5](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_5.jpg)

**답 : ①**

① 하나의 스레드는 여러 프로세스에 ~~포함될 수 있다.~~

==> 하나의 스레드는 반드시 하나의 프로세스에만 포함된다.

==> 하나의 프로세스는 여러 개의 스레드를 포함할 수 있다.



---

## 6. 보이스 코드 정규형(BCNF: Boyce-Codd Normal Form)을...

6. 보이스 코드 정규형(BCNF: Boyce-Codd Normal Form)을 만족하기 위한 조건에 해당하지 않는 것은?

![2019_9L_6](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_6.jpg)

**답 : ①**

① ~~조인(join) 종속성이 없어야 한다.~~

==> **조인(join) 종속성이 없어야 한다.** 

| 정규형            | 속성                                                         | 그림                                                         | 암기법 |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ |
| 1정규형           | 모든 속성은 반드시 하나의 값을 가져야 함.<br />도메인이 반드시 원자값. |                                                              | **도** |
| 2정규형           | 부분 함수 종속을 제거                                        | ![6-1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/6-1.png) | **부** |
| 3정규형           | 이행적 함수 종속 제거 = 완전함수종속<br />기본키 중에 특정 컬럼에 종속된 컬럼(부분적 종속)이 없어야 한다. | ![6-2](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/6-2.png) | **이** |
| 보이스코드 정규형 | 결정자이면서 후보키가 아닌 것 제거                           | ![6-3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/6-3.png) | **결** |
| 4정규형           | 다치 종속 제거                                               |                                                              | **다** |
| 5정규형           | 조인 종속성 제거.                                            |                                                              | **조** |



## 7. UDP(User Datagram Protocol)에 대한...

7. UDP(User Datagram Protocol)에 대한 설명으로 옳은 것만을 모두 고르면?

![2019_9L_7](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_7.jpg)

**답 : ③**

ㄹ. 혼잡제어 메커니즘을 이용하여 링크가 과도하게 혼잡해지는 것을 방지한다.

==> **TCP**에 대한 설명이다.

| TCP                                | UDP                                |
| ---------------------------------- | ---------------------------------- |
| 연결지향                           | 비연결지향                         |
| 신뢰성(안정적)                     | 비신뢰성                           |
| 혼잡제어, 흐름제어                 | ~~혼잡제어, 흐름제어~~             |
| 순서 보장                          | 비순서                             |
| 바이트(byte) 스트림을 통한 연결    | 메시지(message) 스트림을 통한 연결 |
| TCP packet ; Segment               | UDP packet ; Datagram              |
| HTTP, Email, File transfer 에 사용 | DNS, Broadcasting                  |



---

## 8. 다음 논리 회로의 출력과...

8. 다음 논리 회로의 출력과 동일한 것은?

![2019_9L_8](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_8.jpg)

**답 : ③**

![8-1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/8-1.jpg)

![8-3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/8-3.png)

~x1\*(x2 + x3) + ~x3

= ~x1\*x2 + ~x1\*x3 + ~x3

= ~x1\*x2 + (~x1\*x3 + ~x3)

= ~x1\*x2 + ( (~x1+~x3)\*(x3 + ~x3) ) // x3 + ~x3 = True = 1

= ~x1\*x2 + (~x1+~x3)

= (~x1\*x2 + ~x1) + ~x3

= (~x1\*(x2 + 1)) + ~x3

= ~x1 + ~x3



---

## 9. 다음 Java 프로그램의 출력...

9. 다음 Java 프로그램의 출력 결과는?

![2019_9L_9](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_9.jpg)

**답 : ①**

Class A가 Class P를 상속받는다. ==> 자동으로 Overriding(재정의).

```java
class ClassP {
    int func1(int a, int b) {
        return (a+b);
    }
    int func2(int a, int b) {
        return (a-b);
    }
    int func3(int a, int b) {
        return (a*b);
    }
}
public class ClassA extends ClassP {
    int func1(int a, int b) {
        return (a%b);
    }
    double func2(double a, double b) {
        return (a*b);
    }
    int func3(int a, int b) {
        return (a/b);
    }
    public static void main(String[] args) {
        ClassP P = new ClassA();
        System.out.print(P.func1(5,2) + ", " // 둘 모두 int 형이므로 ClassA의 func1을 실행(Overriding)
                        + P.func2(5,2) + ", " // 둘 모두 int 형이므로 ClassP의 func1을 실행
                        + P.func3(5,2)); // 둘 모두 int 형이므로 ClassA의 func1을 실행(Overriding)
    }
}

```





---

## 10. IPv4에서 데이터 크기가 6,000...

10. IPv4에서 데이터 크기가 6,000 바이트인 데이터그램이 3개로 단편화(fragmentation)될 때, 단편화 오프셋(offset) 값으로 가능한 것만을 모두 고르면?

![2019_9L_10](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_10.jpg)

**답 : ①**

**데이터 크기가 6,000바이트**인데 데이터그램이 **3개로 단편화**되므로, **하나당 2,000바이트**를 가진다.

따라서 각 데이터그램은 0~1999바이트, 2000~3999바이트, 4000~5999바이트로 구성된다.

각 데이터그램의 시작 값을 8로 나누어주면, 

0 ; 0/8 = 0

2000 ; 2000/8 = 250

4000 ; 4000/8 = 500

따라서, 단편화 오프셋 값으로 가능한 것은 **0, 250, 500**이다.





---

## 11. Go-Back-N 프로토콜에서 6번째...

11. Go-Back-N 프로토콜에서 6번째 프레임까지 전송한 후 4번째 프레임에서 오류가 있음을 알았을 때, 재전송 대상이 되는 프레임의 개수는?

![2019_9L_11](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_11.jpg)

**답 : ③**

- Go-Back-N 프로토콜은 전송 중에 오류가 발생한 지점부터 재전송한다.

  ==> 4번째 프레임에서 오류가 발생. 4,5,6프레임만을 재전송한다.



---

## 12. 0 ~ (64<sup>10</sup>-1)에 해당하는 정수를 ...

12. 0 ~ (64<sup>10</sup>-1)에 해당하는 정수를 이진코드로 표현하기 위해 필요한 최소 비트 수는?

![2019_9L_12](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_12.jpg)

**답 : ②**

0 ~ (64<sup>10</sup>-1) = 64<sup>10</sup>개

64<sup>10</sup>개 = 2<sup>6<sup>10</sup></sup> = 2<sup>60</sup>

따라서 60 비트.



---

## 13. 의료용 심장 모니터링 시스템과 ...

13. 의료용 심장 모니터링 시스템과 같이 정해진 짧은 시간 내에 응답해야 하는 시스템은?

![2019_9L_13](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_13.jpg)

**답 : ③**

==> 의료용 심장 모니터링 시스템과 같은 정해진 짧은 시간 내에 응답해야 하는 시스템은 **실시간 시스템**이다.

① 다중프로그래밍 시스템 ; 컴퓨터의 주기억장치 상에 2개 이상의 프로그램이 적재되어, 하나의 프로그램이 CPU를 사용하다가 입출력 동작을 하게되면 상대적으로 느린 ***입출력 장치를 수행시키는 동안 CPU로 하여금 다른 프로그램을 수행***하여 컴퓨터의 효율을 증대시키고자 하는 방법.

② 시분할 시스템 ; CPU 스케줄링과 다중 프로그래밍을 이용해서 각 사용자들에게 컴퓨터 자원을 시간적으로 분할하여 사용할 수 있게 해준다.

④ 일괄 처리 시스템 ; 컴퓨터 프로그램 흐름에 따라 순차적으로 자료를 처리하는 방식.



---

## 14. FIFO 페이지 교체 알고리즘을 ...

14. FIFO 페이지 교체 알고리즘을 사용하는 가상메모리에서 프로세스 P가 다음과 같은 페이지 번호 순서대로 페이지에 접근할 때, 페이지 부재(page-fault) 발생 횟수는? (단, 프로세스 P가 사용하는 페이지 프레임은 총 4개이고, 빈 상태에서 시작한다)

![2019_9L_14](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_14.jpg)

**답 : ③**

|            | 회차           | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   |
| ---------- | -------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|            | 페이지 번호    | 1    | 2    | 3    | 4    | 5    | 2    | 1    | 1    | 6    | 7    | 5    |
| 프레임1    | -              | 1    | 1    | 1    | 1    | 2    | 2    | 3    | 3    | 4    | 5    | 5    |
| 프레임2    | -              |      | 2    | 2    | 2    | 3    | 3    | 4    | 4    | 5    | 1    | 1    |
| 프레임3    | -              |      |      | 3    | 3    | 4    | 4    | 5    | 5    | 1    | 6    | 6    |
| 프레임4    | -              |      |      |      | 4    | 5    | 5    | 1    | 1    | 6    | 7    | 7    |
| Page-Fault | ***8회 발생*** | O    | O    | O    | O    | O    | X    | O    | X    | O    | O    | X    |



---

## 15. 재배치 가능한 형태의 기계어로...

15. 재배치 가능한 형태의 기계어로 된 오브젝트 코드나 라이브러리 등을 입력받아 이를 묶어 실행 가능한 로드 모듈로 만드는 번역기는?

![2019_9L_15](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_15.jpg)

**답 : ①**

① 링커(linker) ; 재배치 가능한 형태의 기계어로 된 오브젝트 코드나 라이브러리 등을 입력받아 이를 묶어 실행 가능한 로드 모듈로 만드는 번역기.

② 어셈블러(assembler) ; 어셈블리어를 기계어 형태의 오베직트 코드로 해석해주는 컴퓨터 언어 번역 프로그램

③ 컴파일러(complier) ; 특정 프로그래밍 언어로 쓰여 잇는 문서를 다른 프로그래밍 언어로 옮기는 프로그램.

	- 원래 문서 ; 소스코드 혹은 원시코드
	- 출력 문서 ; 목적 코드

④ 프리프로세서(preprocessor) ; 고급언어를 또 다른 고급언어로 번역하는 고급언어 변역기.

	 - 컴파일보다 먼저 실행되어 미리 처리. 다양한 언어로 각 모듈을 구축할 수 있게 됨.



---

## 16. 이메일, ERP, CRM 등 다양한...

16. 이메일, ERP, CRM 등 다양한 응용 프로그램을 서비스 형태로 제공하는 클라우드 서비스는?

![2019_9L_16](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_16.jpg)

**답 : ④**

- 클라우드 서비스

① IaaS(Infrastructure as a Service) ; 서버 혹은 저장장치 등 같은 IT 하드웨어 자원을 클라우드 서비스

② NaaS(Network as a Service) ; **Network as a service** (**NaaS**) describes services for network transport connectivity.[[1\]](https://en.wikipedia.org/wiki/Network_as_a_service#cite_note-focus-1) NaaS involves the optimization of resource allocations by considering network and computing resources as a unified whole.[[2\]](https://en.wikipedia.org/wiki/Network_as_a_service#cite_note-2)

③ PaaS(Platform as a Service) ; 업무에 필요한 소프트웨어를 개발할 수 있는 환경을 클라우드 서비스

④ SaaS(Software as a Service) ; 소프트웨어 자체를 클라우드 서비스



---

## 17. 다음 C 프로그램의 출력...

17. 다음 C 프로그램의 출력 결과는?

![2019_9L_17](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_17.jpg)

**답 : ①**

```c
#include <stdio.h>
int main() {
    char msg[50] = "Hello World!! Good Luck!";
    int i = 2, number = 0; // i가 2부터 시작한다! msg[i] = 'l'
    while (msg[i] != '!') {
        if (msg[i] == 'a' || msg[i] == 'e' || msg[i] == 'i'
            || msg[i] == 'o' || msg[i] == 'u')
            number++;
    }
    printf("%d", number);
    return 0;
}
```



---

## 18. 마이크로프로세서에 관한 ...

18. 마이크로프로세서에 관한 설명으로 옳은 것만을 모두 고르면?

![2019_9L_18](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_18.jpg)

**답 : ④**

ㄱ. 모든 명령어의 실행시간은 클럭 주기(clock period)보다 ~~작다.~~

==> 클럭 주기는 **가장 오래 걸리는 시간**으로 설정한다.



---

## 19. 소프트웨어 규모를 예측하기...

19. 소프트웨어 규모를 예측하기 위한 기능점수(function point)를 산정할 때 고려하지 않는 것은?

![2019_9L_19](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_19.jpg)

**답 : ④**

LOC는 기능점수(function point) 산정 시 고려되지 않는다.

- 기능점수(function point) ; 사용자에게 제공되는 기능 단위로 점수를 정량화하여, 소프트웨어 규모 산정.

  | 종류 |                         | 설명                                                         |
  | ---- | ----------------------- | ------------------------------------------------------------ |
  | EI   | External Input          | 외부입력, 외부에서 들어오는 데이터 및 제어정보를 처리하는 단위프로세스 |
  | EO   | External Output         | 외부출력, 데이터 및 제어정보의 조회 외에 처리 로직을 통해서 사용자에게 정보를 제공. |
  | EQ   | External inQuiry        | 외부조회, 응용시스템 외부에 데이터나 제어정보를 보내는 단위프로세스 |
  | ILF  | Internal Logical File   | 내부논리파일, 측정 대상 어플리케이션 내에 있는 논리적 데이터 |
  | EIF  | External Interface File | 외부연계파일, 측정 대상 어플리케이션 내에서 참조하지만, 실질적인 데이터는 외부에 있는 파일 |

  



---

## 20. LTE(Long-Term Evolution) 표준에 ...

20. LTE(Long-Term Evolution) 표준에 대한 설명으로 옳은 것만을 모두 고르면?

![2019_9L_20](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_computerbasic/2019_9L/2019_9L_20.jpg)

**답 : ④**

ㄴ. 4G 무선기술로서 ~~IEEE 802.16~~ 표준으로도 불린다.

==> 802.16 ; wireless Broadband

==> 802.11 ; LTE, Wifi

==> 802.15 ; Bluetooth