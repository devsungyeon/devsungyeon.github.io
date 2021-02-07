---
title: "2019년 9급 전산직 정보보호론 풀이"
strapline: "정보보호론 풀이"
description: "2019년 9급 전산직 정보보호론 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "9Level_information"
tag:
  - "9급"
  - "정보보호론"
  - "9급공무원"
toc: true
last_modified_at: 2020-12-05
comments: true
---

# 2019년 9급 전산직 정보보호론 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1.  정보보호 위험관리에 대한...

1. 정보보호 위험관리에 대한 설명으로 옳지 않은 것은?

  ![2020_9L_1](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_1.jpg)

**답 : ②**

② 위험은 자산에 손실이 발생할 가능성과 관련되어 있으나 이로 인한 ~~부정적인 영향을 미칠 가능성과는 무관하다.~~

==> 위험은 부정적인 영향을 미칠 가능성이 존재한다.



---

## 2.  공개키 암호화에 대한...

2. 공개키 암호화에 대한 설명으로 옳지 않은 것은?

  ![2020_9L_2](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_2.jpg)

**답 : ③**

③ 전자서명 할 때는 서명하는 사용자의 ~~공개키~~로 암호화한다.

==> 서명은 자신의 서명을 타인이 검증할 수 있어야 하므로, 사용자의 개인키로 암호화 하고, 검증자는 사용자의 공개키로 검증한다.



---

## 3. X.509 인증서 형식 필드에 대한...

3. X.509 인증서 형식 필드에 대한 설명으로 옳은 것은?

  ![2020_9L_3](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_3.jpg)

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

  ![2020_9L_4](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_4.jpg)

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
윈도우 운영체제에서 TPM(Trusted Platform Module)에 대한 설명으로 옳지 않은 것은?![2020_9L_5](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_5.jpg)

**답 : ①**

① TPM의 ~~공개키~~를 사용하여 플랫폼 설정정보에 서명함으로써 디지털 인증을 생성한다.

==> 개인키를 사용하여 인증을 생성한다.



- TPM(신뢰할 수 있는 플랫폼 모듈)
  - 하드웨어 기반의 보안 관련 기능을 제공하도록 설계.
  - TPM 칩은 암호화 작업을 수행하도록 설계된 보안 암호화 프로세서
  - Bitlocker 등에서 이용.
  - TPM은 시스템이 시동되면 POST(Power-On Self Test)과정에서 시스템의 무결성을 검사.







---

## 6. 

6. 
![2020_9L_6](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_6.jpg)

**답 : **

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
| 특징        | 기밀성이 낮음. <br>평문 블록과 암호화 블록이 일대일 관계.    | 1단계 앞에서 수행된 결과인 암호문 블록에 평문 블록을 **XOR**하여 암호화<BR>패딩(Padding) ; 평문의 길이는 가변적. 따라서, 마지막 블록의 길이가 부족한 경우 임의의 비트를 채워넣음.<br>IPSec에서 통신의 기밀성을 위해 CBC 모드 이용.<br>예 : 3DES-CBC, AES-CBC, Kerberos version5<br>암호화 : 순차적<br/>복호화 : 병렬적 | 1단계 앞의 암호문 블록을 암호 알고리즘의 입력으로 사용.<br>**복호화 시, 복호화가 아닌 암호화**<br>암호화 : 순차적<br>복호화 : 병렬적<br>재전송 공격이 가능.![image-20210207135524398](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-9.jpg) | **평문 블록이 동일하면 암호문이 같아지는 ECB의 단점**과, **오류 전파가 발생하는 CBC, CFB 모드**를 개선. | CTR 모드에서는 블록을 암호화할 때마다 1씩 증가해 가는 카운터를 암호화해서 키 스트림을 만든다. |
| 암호화      | ![6_1](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6_1.jpg) | ![image-20210207134444038](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-3.jpg) | ![image-20210207135113152](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-7.jpg) | 오류 전파가 발생하지 않는다.<br/>![image-20210207135724327](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-10.jpg) | ![image-20210207140109563](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-12.JPG) |
| 복호화      | ![6-2](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-2.jpg) | ![image-20210207134515589](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-4.jpg) | ![image-20210207135121585](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-8.jpg) | 오류 전파가 발생하지 않는다.<br>![image-20210207135732562](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-11.jpg) | ![image-20210207140117037](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-13.jpg) |
| 암호화 영향 |                                                              | **평문 블록의 한 비트 오류는 모든 암호문에 영향.**<br>![image-20210207134752030](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-6.jpg) | CBC와 동일                                                   |                                                              |                                                              |
| 복호화 영향 |                                                              | **복호화 시, 암호문 블록이 1개 파손된 경우, 미치는 영향은 2개 블록에 머문다.**<br/>![image-20210207134739011](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_information\2020_9L\6-5.jpg) | CBC와 동일                                                   |                                                              |                                                              |



|                 | ECB  | CBC  | CFB  | OFB  | CTR  |
| --------------- | ---- | ---- | ---- | ---- | ---- |
| IV              |      | O    | O    | O    |      |
| 암=복           |      |      | O    | O    | O    |
| 병렬            | O    |      |      |      | O    |
| **연쇄** 암호화 |      | O    | O    |      |      |
| **연쇄** 복호화 |      |      |      |      |      |



## 7. 

7. 
![2020_9L_7](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_7.jpg)


**답 : **

①

②

③

④



---

## 8. 

8. 
![2020_9L_8](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_8.jpg)


**답 : **

①

②

③

④



---

## 9. 

9. 
![2020_9L_9](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_9.jpg)


**답 : **

①

②

③

④



---

## 10. 

10. 
![2020_9L_10](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_10.jpg)


**답 : **

①

②

③

④



---

## 11. 

11. 
![2020_9L_11](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_11.jpg)


**답 : **

①

②

③

④



---

## 12. 

12. 
![2020_9L_12](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_12.jpg)


**답 : **

①

②

③

④



---

## 13. 

13. 
![2020_9L_13](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_13.jpg)


**답 : **

①

②

③

④



---

## 14. 

14. 
![2020_9L_14](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_14.jpg)


**답 : **

①

②

③

④



---

## 15. 

15. 
![2020_9L_15](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_15.jpg)


**답 : **

①

②

③

④



---

## 16. 

16. 
![2020_9L_16](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_16.jpg)


**답 : **

①

②

③

④



---

## 17. 

17. 
![2020_9L_17](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_17.jpg)


**답 : **

①

②

③

④



---

## 18. 

18. 
![2020_9L_18](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_18.jpg)


**답 : **

①

②

③

④



---

## 19. 

19. 
![2020_9L_19](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_19.jpg)


**답 : **

①

②

③

④



---

## 20. 

20. 
![2020_9L_20](C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/2020_9L_20.jpg)


**답 : **

①

②

③

④