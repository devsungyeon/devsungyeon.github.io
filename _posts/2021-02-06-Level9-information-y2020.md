---
title: "2020년 9급 전산직 정보보호론 풀이"
strapline: "정보보호론 풀이"
description: "2020년 9급 전산직 정보보호론 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "9Level_information"
tag:
  - "9급"
  - "정보보호론"
  - "9급공무원"
toc: true
last_modified_at: 2021-02-07
comments: true
---

# 2020년 9급 전산직 정보보호론 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1.  정보보호 위험관리에 대한...

1. 정보보호 위험관리에 대한 설명으로 옳지 않은 것은?

  ![2020_9L_1](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_1.jpg)

**답 : ②**

② 위험은 자산에 손실이 발생할 가능성과 관련되어 있으나 이로 인한 ~~부정적인 영향을 미칠 가능성과는 무관하다.~~

==> 위험은 부정적인 영향을 미칠 가능성이 존재한다.



---

## 2.  공개키 암호화에 대한...

2. 공개키 암호화에 대한 설명으로 옳지 않은 것은?

  ![2020_9L_2](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_2.jpg)

**답 : ③**

③ 전자서명 할 때는 서명하는 사용자의 ~~공개키~~로 암호화한다.

==> 서명은 자신의 서명을 타인이 검증할 수 있어야 하므로, 사용자의 개인키로 암호화 하고, 검증자는 사용자의 공개키로 검증한다.



---

## 3. X.509 인증서 형식 필드에 대한...

3. X.509 인증서 형식 필드에 대한 설명으로 옳은 것은?

  ![2020_9L_3](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_3.jpg)

**답 : ④**

① Issuer name ; 발행자 이름

인증서를 사용하는 주체의 이름과 유효기간 정보 ; Subject, Validity

② Subject name ; 소유자 이름

인증서를 발급한 인증기관의 식별 정보 ; 인증기관 키 식별자 Authority key identifier or Issuer

③ Signature algorithm ID ; Ca가 인증서 서명하기 위해 사용한 RSA 등의 알고리즘을 식별하기 위한 항목

인증서 형식의 버전 정보 ; Version



- X.509 ; 암호학에서 공개키 **인증서**와 인증알고리즘의 표준 가운데에서 공개키 기반(PKI)의 ITU-T 표준이다.

  - 인증서

    - X. 509 시스템에서 CA는 X. 500  규약에 따라 서로 구별되는 공개키를 가진 인증서를 발행한다.

  - 인증서의 구조

    - **Certificate**
      - **Version** 인증서의 버전을 나타냄
      - **Serial Number** CA가 할당한 정수로 된 고유 번호
      - **Signature** 서명 알고리즘 식별자
      - **Issuer** 발행자
      - **Validity** 유효기간
        - **Not Before** 유효기간 시작 날짜
        - **Not After** 유효기간 끝나는 날짜
      - **Subject** 소유자
      - **Subject Public Key Info** 소유자 공개 키 정보
        - **Public Key Algorithm** 공개 키 알고리즘
        - **Subject Public Key**
      - **Issuer Unique Identifier (Optional)** 발행자 고유 식별자
      - **Subject Unique Identifier (Optional)** 소유자 고유 식별자
      - **Extensions (Optional)** 확장
        - ...
    - Certificate Signature Algorithm
    - Certificate Signature

    

  

  



---

## 4. 일방향 해시함수를 사용하여 ...

4. 일방향 해시함수를 사용하여 비밀번호를 암호화할 땐 salt라는 난수를 추가하는 이유는?

  ![2020_9L_4](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_4.jpg)

**답 : ①**

- 일방향 해시함수

  ==> 단방향의 데이터를 안전하게 저장하고 무결성을 보장하는데 사용. (인증 불가 --> 인증을 위해서는 메시지 인증코드나 디지털 서명이 요구.)

  ==> 레인보우 테이블을 이용해 빠르게 원본 확인이 가능.

  예 : MD5, SHA1, SHA2(SHA256, SHA384, SHA512)

- - ㅇ
  - ㅇ

  

  

- 레인보우 테이블 ; 모든 해시의 쌍(원본:해시값)을 계산하여 저장해놓은 테이블.

  - 레인보우 테이블 공격을 방지하기 위해서 **Salt**라는 난수를 추가.
  - 문자열 앞이나 뒤 혹은 중간에 salt를 덧붙여 해시값을 계산함.

  



---

## 5. 윈도우 운영체제에서 TPM...

5. 
윈도우 운영체제에서 TPM(Trusted Platform Module)에 대한 설명으로 옳지 않은 것은?![2020_9L_5](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_5.jpg)

**답 : ①**

① TPM의 ~~공개키~~를 사용하여 플랫폼 설정정보에 서명함으로써 디지털 인증을 생성한다.

==> 개인키를 사용하여 인증을 생성한다.



- TPM(신뢰할 수 있는 플랫폼 모듈)
  - 하드웨어 기반의 보안 관련 기능을 제공하도록 설계.
  - TPM 칩은 암호화 작업을 수행하도록 설계된 보안 암호화 프로세서
  - Bitlocker 등에서 이용.
  - TPM은 시스템이 시동되면 POST(Power-On Self Test)과정에서 시스템의 무결성을 검사.







---

## 6. 키 K에 대한 블록 암호 알고리즘 ...

6. 
키 K에 대한 블록 암호 알고리즘 Ek, 평문블록 Mi, Z0는 초기벡터, Zi = Ek(Zi-1)가 주어진 경우, 이때 i=1, 2, ..., n에 대해 암호블록 Ci를 Ci = Zi xor Mi로 계산하는 운영모드는? (단, xor는 배타적 논리합이다)![2020_9L_6](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_6.jpg)

**답 : ③**

OFB ; 초기벡터를 계속해서 암호화가며, 평문블록과 XOR연산을 수행하여 암호화한다.



- 현대 대칭키 암호를 이용한 암호화 기법
  - ECB - Electric CodeBook mode
  - CBC - Cypher Block Chaining mode
  - CFB - Cipher-FeedBack mode
  - OFB - Output-FeedBack mode
  - CTR - CounTeR mode

- 블록모드 vs 스트림 암호방식의 블록 암호모드
  - 블록 모드 : ECB, CBC ; 집합을 한 번에 처리하는 암호 알고리즘을 총칭.
    - 암호화가 느리지만, 높은 확산성. **Round**를 사용하여 반복적으로 여러번 수행하여 암호화 강도를 높인다.
  - 스트림 암호방식의 블록 암호모드 : CFB, OFB, CTR ; 한번에 1비트 혹은 1바이트의 데이터 흐름(스트림)을 순차적으로 처리해가는 암호 알고리즘의 총칭.
    - 암호화는 빠르지만, 낮은 확산성. **XOR**



|             | ECB                                                          | CBC                                                          | CFB                                                          | OFB                                                          | CTR                                                          |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 특징        | 기밀성이 낮음. <br>평문 블록과 암호화 블록이 일대일 관계.<BR>재전송 공격이 가능. | 1단계 앞에서 수행된 결과인 암호문 블록에 평문 블록을 **XOR**하여 암호화<BR>패딩(Padding) ; 평문의 길이는 가변적. 따라서, 마지막 블록의 길이가 부족한 경우 임의의 비트를 채워넣음.<br>IPSec에서 통신의 기밀성을 위해 CBC 모드 이용.<br>예 : 3DES-CBC, AES-CBC, Kerberos version5<br>암호화 : 순차적<br/>복호화 : 병렬적 | 1단계 앞의 암호문 블록을 암호 알고리즘의 입력으로 사용.<br>**복호화 시, 복호화가 아닌 암호화**<br>암호화 : 순차적<br>복호화 : 병렬적<br>재전송 공격이 가능.![image-20210207135524398](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-9.jpg) | **평문 블록이 동일하면 암호문이 같아지는 ECB의 단점**과, **오류 전파가 발생하는 CBC, CFB 모드**를 개선. | CTR 모드에서는 블록을 암호화할 때마다 1씩 증가해 가는 카운터를 암호화해서 키 스트림을 만든다. |
| 암호화      | W                                                            | ![image-20210207134444038](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-3.jpg) | ![image-20210207135113152](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-7.jpg) | 오류 전파가 발생하지 않는다.<br/>![image-20210207135724327](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-10.jpg) | ![image-20210207140109563](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-12.JPG) |
| 복호화      | ![6-2](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-2.jpg) | ![image-20210207134515589](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-4.jpg) | ![image-20210207135121585](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-8.jpg) | 오류 전파가 발생하지 않는다.<br>![image-20210207135732562](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-11.jpg) | ![image-20210207140117037](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-13.jpg) |
| 암호화 영향 |                                                              | **평문 블록의 한 비트 오류는 모든 암호문에 영향.**<br>![image-20210207134752030](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-6.jpg) | CBC와 동일                                                   |                                                              |                                                              |
| 복호화 영향 |                                                              | **복호화 시, 암호문 블록이 1개 파손된 경우, 미치는 영향은 2개 블록에 머문다.**<br/>![image-20210207134739011](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-5.jpg) | CBC와 동일                                                   |                                                              |                                                              |



|                 | ECB  | CBC  | CFB  | OFB  | CTR  |
| --------------- | ---- | ---- | ---- | ---- | ---- |
| IV              |      | O    | O    | O    |      |
| 암=복 알고리즘  |      |      | O    | O    | O    |
| 병렬            | O    |      |      |      | O    |
| **연쇄** 암호화 |      | O    | O    |      |      |
| **연쇄** 복호화 |      |      |      |      |      |



## 7. 정보보호 시스템 평가 기준에...

7. 정보보호 시스템 평가 기준에 대한 설명으로 옳은 것은?

  ![2020_9L_7](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_7.jpg)

**답 : ④**

① ~~ITSEC~~의 레인보우 시리즈에는 레드 북으로 불리는 TNI(Trusted Network Interpretation)가 있다.

==> TCSEC(오렌지북)

② ~~ITSEC~~은 None부터 B2까지의 평가 등급으로 나눈다.

==> TNI ; 레드북

③ ~~TCSEC~~의 EAL~~2~~ 등급은 기능시험 결과를 의미한다.

==> CC, EAL1



- 평가기준

  - ITSEC : 유럽

    - **기밀성, 무결성, 가용성**을 다룸.
    - 등급
      - Functionality : F1 -> F10 ; 기능 클래스
      - **Assurance : E0 -> E6 ; 보증 수준**

  - TCSEC : 미국

    - 오렌지 북.
    - BLP(Bell-LaPadula Model) 기반의 **기밀성**. (가용성x, 무결성x)
    - 등급
      - **D - C1 - C2 - B1 - B2 - B3 - A1**
    - 문제점
      - 운영 시스템에만 중점.
      - **무결성과 가용성 X**
    - **TNI**(Trusted Network Interpretation)
      - 미국 국방부 제공
      - **기밀성, 무결성** 다룸.
      - **레드북**.
      - 등급
        - **None, C1(최소), C2(fair), B2(good)**

  - CC(Common Criteria)

    - 국제 표준 (ISO/IEC 15408)
    - 등급
      - EAL1 --> EAL7
    - 평가 절차
      - PP --> ST --> TOE

    | 보호프로파일(PP)                                             | 보안목표명세서(ST)                                        |
    | ------------------------------------------------------------ | --------------------------------------------------------- |
    | 구현에 독립적                                                | 구현에 종속적                                             |
    | 제품군(예 : 침입탐지시스템)                                  | 특정제품 (예 : A사의 침입탐지시스템)                      |
    | 여러 제품/시스템이 동일한 유형의 보호프로파일을 수용할 수 있음. | 하나의 제품/시슽메은 하나의 보안목표명세서를 수용해야 함. |
    | 보호프로파일은 보안목표명세서를 수용할 수 없음               | 보안목표명세서는 보호프로파일을 수용할 수 있음.           |

    | EAL 1 | 기능 시험          | 기능 명세서, 설명서          |
    | ----- | ------------------ | ---------------------------- |
    | EAL 2 | 구조 시험          | 기본설계서, 기능시험서       |
    | EAL 3 | 체계적 시험        | 생명주기, 개발보안, 오용분석 |
    | EAL 4 | 설계 시험/검토     | 상세설계, 보안정책, 상세시험 |
    | EAL 5 | 준정형화 설계/시험 | 개발문서, 보안기능 전체코드  |
    | EAL 6 | 준정형화 설계 검증 | 전체 소스 코드               |
    | EAL 7 | 정형화 설계 검증   | 개발 문서 정형화 기술        |
    
    



---

## 8. SSL(Secure Socket Layer)의 ...

8. 
SSL(Secure Socket Layer)의 Handshake 프로토콜에서 클라이언트와 서버 간에 논리적 연결 수립을 위해 클라이언트가 최초로 전송하는 ClientHello 메시지에 포함되는 정보가 아닌 것은?![2020_9L_8](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_8.jpg)

**답 : ④**

- SSL/TLS Handshake 메시지 유형

  | 메시지 유형         | 매개변수                                                     |
  | ------------------- | ------------------------------------------------------------ |
  | hello_request       | null                                                         |
  | client_hello        | version, random, session id, ciphersuite, compression method |
  | server_hello        | version, random, session id, ciphersuite, compression method |
  | certificate         | chain of X.509v3 certificates                                |
  | server_key_exchange | parameters, signature                                        |
  | certificate_request | type, authorities                                            |
  | server_hello_done   | null                                                         |
  | certificate_verify  | signature                                                    |
  | client_key_exchange | parameters, signature                                        |
  | finished            | hash value                                                   |

  





---

## 9. 개인정보 보호법 상 기본계획에 ...

9. 
개인정보 보호법 상 기본계획에 대한 조항의 일부이다. ㄱ, ㄴ에 들어갈 내용을 바르게 연결한 것은?![2020_9L_9](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_9.jpg)

**답 : ②**



---

## 10. 소수 p = 13, 원시근 g = 2...

10. 
소수 p = 13, 원시근 g = 2, 사용자 A와 B의 개인키가 각각 3, 2일 때, Diffie-Helloman 키 교환 알고리즘을 사용하여 계산한 공유 비밀키는?![2020_9L_10](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_10.jpg)

**답 : ③**

A = g<sup>a</sup> mod p = 2<sup>3</sup> mod 13 = 8

B = g<sup>b</sup> mod p = 2<sup>2</sup> mod 13 = 4

K = A<sup>b</sup> mod p = B<sup>a</sup> mod p = g<sup>ab</sup> mod p = 2 <sup>3*2</sup> mod 13 = 64 mod 13 = 12

- Diffie-Hellman

![diffie-hellman algorithm 이미지 검색결과](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\10-1.jpg)

- RSA 알고리즘

1. 두 개의 큰 소수 p, q 선택

2. n = p*q , z = (p-1) * (q-1)

3. z와 서로소인 n보다 작은 수 e 선택

4. (e*d - 1) mod z = 0 인 d 선택

   (ed mod z = 1과 동일한 의미)

5. 공개 : n, e   비공개 : d

암호화 : C = M<sup>e</sup> mod n

복호화(개인키 n,d 가 필요) : M = C<sup>d</sup> mod n

![img](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\10-2.jpg)

![img](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\10-3.jpg)



![img](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\10-4.jpg)



---

## 11. NIST의 AES(Advanced Encryption Standard) ...

11. 
NIST의 AES(Advanced Encryption Standard) 표준에 따른 암호화 시 암호키(cipher key) 길이가 256비트일 때 필요한 라운드 수는?![2020_9L_11](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_11.jpg)

**답 : ④**

|         | 키 길이 | 블록 길이 | 라운드 수 |
| ------- | ------- | --------- | --------- |
| AES 128 | 4       | 4         | 10        |
| AES 192 | 6       | 4         | 12        |
| AES 256 | 8       | 4         | 14        |



## 12. IPsec의 ESP(Encapsulating Security Payload)에...

12. 
IPsec의 ESP(Encapsulating Security Payload)에 대한 설명으로 옳지 않은 것은?![2020_9L_12](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_12.jpg)

**답 : ④**

④ 터널 모드의 ESP는 Authentication Data를 생성하기 위해 해시 함수와 ~~공개키~~를 사용한다.

==> Authentication Data(인증 데이터)

- 인증 알고리즘

  - DES와 같은 대칭키 암호 알고리즘을 기반으로 한 MAC 알고리즘

  - SHA-1(Secure Hash Algorithm) 혹은 MD5 알고리즘

    

- ESP(Encapsulating Security Payload) ; IP 데이터그램에 암호화 기능을 부가한 것.
  - 기밀성 ; 전달된 메시지가 중도에서 도청이나 해독되지 못하도록 한다.
  - 재전송 공격 방지 ; IP 데이터그램이 재전송 공격에 사용되는 것을 방지.
  - 제한된 트래픽 흐름 기밀성 ; 네트워크상의 트래픽 흐름에 대한 정보를 보호
  - 무결성 ; 전달된 메시지가 변조 혹은 위조되지 않음을 증명
  - 인증 ; 전달된 메시지가 발신지로부터 온 메시지임을 증명.



---

## 13. 네트워크나 컴퓨터 시스템의 자원 고갈을...

13. 
네트워크나 컴퓨터 시스템의 자원 고갈을 통해 시스템 성능을 저하시키는 공격에 대한 것만을 모두 고르면?![2020_9L_13](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_13.jpg)

**답 : ①**

ㄱ. Ping of Death 공격

 ; 규정 크기 이상의 ICMP 패킷으로 시스템을 마비시키는 공격.

 ; Ping 명령을 실행하면 ICMP Echo Request 패킷을 원격 IP 주소에 송신하는 ICMP 응답을 기다린다. 방화벽이 ICMP 패킷을 막지 않도록 되어 있다면 이는 시스템 공격 수단으로 이용될 수 있는데, 대표적인 것이 버퍼 크기를 초과하는 핑 패킷으로 공격대상의 IP 스택을 넘치게 하는 것이다. 이것을 'Ping of Death'라고 부른다.

ㄴ. Smurf 공격

 ; 희생자의 스푸핑된 원본 IP를 가진 수많은 인터넷 제어 메시지 프로토콜(ICMP) 패킷들이 IP 브로드캐스트 주소를 사용하여 컴퓨터 네트워크로 브로드캐스르하는 분산 서비스 거부 공격이다. 네트워크의 대부분의 장치들은 기본적으로 원본 IP 주소에 응답을 보냄으로써 이에 응답한다. 이 패킷에 응답하고 패킷을 수신하는 네트워크의 기계 수가 많다면 희생자의 컴퓨터는 트래픽으로 넘쳐나게 된다. 이로 인해 희생자의 컴퓨터는 동작이 불가능해질 정도로 느려지게 될 수 있다.

ㄷ. Heartbleed 공격

 ; 출혈이라는 의미. 해당 취약점을 이용하여 시스템 메모리에 저장되어 있는 정보의 유출의 크기는 매우 작다. 하지만 지속적으로 유출시켜 무의미한 정보들을 모아 하나의 완전한 유의미한 정보가 될 수 있다.

ㄹ. Sniffing 공격

 ; Sniff. 냄새를 맡다. 킁킁거리다. 네트워크 상에 지나다니는 패킷들을 캡처하여 그 안에 있는 내용을 들여다보는 기술을 말한다.



---

## 14. 다음 설명에 해당하는 위험분석...

14. 
다음 설명에 해당하는 위험분석 및 평가 방법을 옳게 짝지은 것은?![2020_9L_14](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_14.jpg)

**답 : ③**

델파이법 ; 전문가 집단의 토론을 통한 추정. 시간 및 비용을 절약하지만 정확도가 낮다.

과거자료 분석법 ; 과거의 발생 혹은 과거에 수집한 자료를 토대로 위험 발생 가능성을 예측.

시나리오법 ; 발생 가능한 결과들을 예측하며, 작은 정보를 가지고 전반적인 가능성을 추론할 수 있다.

순위 결정법 ; 비교우위 순위 결정표에 위험 항목들의 순위를 결정하는 방법.

기준선 접근법 ; = 베이스라인 접근법 ; 표준화된 보호대책 체크리스트를 가지고 점검하는 접근법.



---

## 15. 정보통신망 이용촉진 및 정보보호 등에...

15. 
정보통신망 이용촉진 및 정보보호 등에 관한 법률 시행렬 제19조(국내대리인 지정 대상자의 범위)에 명시된 자가 아닌 것은?![2020_9L_15](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_15.jpg)

**답 : ①**

① 전년도(법인인 경우에는 전 사업연도를 말한다) 매출액이 ~~1,000억 원~~ 이상인 자

==> 100억원 이상인 자.



---

## 16. 다음 설명에 해당하는 악성코드 ...

16. 
다음 설명에 해당하는 악성코드 분석도구를 옳게 짝지은 것은?![2020_9L_16](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_16.jpg)

**답 : ①**

Sandbox ; 가상화 기술 기반으로 악성코드의 비정상 행위를 유발하는 실험과정에서 발생할 수 있는 분석시스템으로의 침해를 방지하여 통제된 환경과 분석 기능을 제공한다.

Process Explorer ; 악성코드의 행위를 추출하기 위해 실제로 해당 코드를 실행함으로써 발생하는 비정상 행위 혹은 시스템 동작 환경의 변화를 살펴볼 수 있는 동적 분석 기능을 제공한다.

Whitebox ; 소프트웨어 내부 소스 코드를 확인하는 기법

Blackbox ; 소프트웨어 내부를 보지 않고, 입력과 출력값을 확인하여, 기능의 유효성을 판단하는 테스트 기법.

Burp Suite ; XSS(Cross Site Scripting) 공격을 통해 웹 사이트의 보안을 취약하게 할 수 있는 툴. javascript를 이용한 validation체크를 우회할 수 있다.

IDA Pro ; IDA(Interactive DisAssembler). 디스어셈블러. 다양한 프로세서 및 파일 유형을 지원함은 물론, 사용자(리버서)가 주도적ㅇ으로 편하게 리버싱을 진행할 수 있다는 점에서 사용자와 상호작용이 가능.

OllyDBG ; 바이너리 코드 분석을 위한 x86 디버거, 소스 코드가 없을 때 유용하게 사용. 레지스터를 추적하고 함수, API 호출, Switch문, 표, 상수 그리고 문자열을 인식하며, 오브젝트 파일과 라이브러리에서 루틴들의 위치를 찾아준다.





---

## 17. 윈도우 운영체제의 계정 관리에...

17. 
윈도우 운영체제의 계정 관리에 대한 설명으로 옳은 것은?![2020_9L_17](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_17.jpg)

**답 : ②**

① 'net ~~accounts~~ guest /active:no' 명령은 guest 계정을 비활성화한다.

==> net user guest /active:no

③ 'net ~~usergroup~~' 명령은 시스템 내 사용자 그룹정보를 표시한다.

==> net localgroup

==> usergroup은 없다.

==> localgroup vs group

​	localgroup ; 로컬 컴퓨터 그룹에 사용.

​	group ; 도메인 그룹에 등록할 때 사용.

④ 컴퓨터/도메인에 모든 접근권한을 가진 관리자 그룹인 ~~'Admin'~~이 기본적으로 존재한다.
==> Administrator



---

## 18. 커버로스(Kerberos) 프로토콜에 대한...

18. 
커버로스(Kerberos) 프로토콜에 대한 설명으로 옳지 않은 것은?![2020_9L_18](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_18.jpg)

**답 : ②**

② 사용자의 패스워드를 추측하거나 캡처하지 못하도록 ~~일회용~~ 패스워드를 제공한다.

==> 커버로스 시스템에서는 대칭키 암호로 빌드되며 TTP(신뢰된 서드 파티)를 요구한다. 또 특정 인증 구간에서 비대칭 키 암호 방식을 이용함으로써 선택적으로 공개키 암호 방식을 사용할 수 있다. 





---

## 19. 임의적 접근 통제(Discretionary Access Control) 모델에...

19. 
임의적 접근 통제(Discretionary Access Control) 모델에 대한 설명으로 옳은 것은?![2020_9L_19](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_19.jpg)

**답 : ①**

① 주체가 소유권을 가진 객체의 접근을 다른 사용자에게 부여할 수 있으며, 사용자 신원에 따라 객체의 접근을 제한한다.



- MAC 강제적 접근 통제 ; 주체와 객체의 **보안 등급**을 비교하여 접근 권한을 부여.

  - BLP(Bell-Lapadula) 모델 ; **기밀성.**

    - No Read Up ; 주체는 같거나 낮은 계층만 읽을 수 있다.
    - No Write Down ; 주체는 같거나 높은 계층만 쓸 수 있다.
    - Strong star property rule ; 주체는 동일레벨에서 읽기 쓰기가 가능하다.
    - 장점 ; 트로이 목마 공격이 불가능.
    - 단점 ; 무결성 유지가 어렵다. Write up이 가능하므로...

    |                | Read | Write | Read/Write |
    | -------------- | ---- | ----- | ---------- |
    | 상급자         | X    | O     | X          |
    | 동일 보안 레벨 | O    | O     | O          |
    | 하급자         | O    | X     | X          |

  - Biba 모델 ; **무결성**

    - No Write Up ; 단순 무결성
    - No Read Down ; 무결성 제한

    |                | Read | Write | Read/Write |
    | -------------- | ---- | ----- | ---------- |
    | 상급자         | O    | X     | X          |
    | 동일 보안 레벨 | O    | O     |            |
    | 하급자         | X    | O     |            |

  - Clark-Wilson 모델 ; **무결성** 중심

  - 만리장성 모델 ; 사용자의 이전 동작에 따라 변화할 수 있는 접근 통제를 제공. (MAC, DAC)

- DAC 임의적 접근 통제 ; 주체가 속해있는 그룹의 **신원**에 근거하여 객체에 대한 접근을 제한하는 방법.

  - 접근제어 행렬 ; 주체를 행, 객체를 열로 구성. 주체가 객체에 수행할 수 있는 접근 권한을 기록하여 관리.
    - 행렬의 크기가 커지고, 비어있는 셀이 많아지므로 공간적으로 비효율적.
  - 자격 목록(CL, Capability List) ; 한 주체가 갖는 자격들의 리스트. 콘텐츠의 보안성이 보장받지 못하는 분산환경에서 사용하기 적합.
    - 예) 커버로스
  - 접근제어 목록(ACLs, Access-Control Lists) ; 객체의 관점에서 객체에 어떤 주체가 어떤 접근 권한을 갖는지 명시.

- RBAC 역할기반 접근 통제



---

## 20. 정보통신망 이용촉진 및 ...

20. 
정보통신망 이용촉진 및 정보보호 등에 관한 법률 제45조 (정보통신망의 안정성 확보 등)에 정보보호조치에 관한 지침에 포함되어야 할 보호조치로 명시되지 않은 것은?![2020_9L_20](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_20.jpg)

**답 : ②**

② 사전 정보보호대책 마련 및 보안조치 설계 구현 등을 위한 기술적 보호조치.

==> 정보보호지침에는 다음 각 호의 사항이 포함되어야 한다.  <개정 2016. 3. 22., 2020. 6. 9.>

1. 정당한 권한이 없는 자가 정보통신망에 접근ㆍ침입하는 것을 방지하거나 대응하기 위한 정보보호시스템의 설치ㆍ운영 등 기술적ㆍ물리적 보호조치

2. 정보의 불법 유출ㆍ위조ㆍ변조ㆍ삭제 등을 방지하기 위한 기술적 보호조치

3. 정보통신망의 지속적인 이용이 가능한 상태를 확보하기 위한 기술적ㆍ물리적 보호조치

4. 정보통신망의 안정 및 정보보호를 위한 인력ㆍ조직ㆍ경비의 확보 및 관련 계획수립 등 관리적 보호조치

5. 정보통신망연결기기등의 정보보호를 위한 기술적 보호조치