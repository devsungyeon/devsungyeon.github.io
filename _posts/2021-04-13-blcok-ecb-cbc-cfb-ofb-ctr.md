---
title: "BLOCK ECB CBC CFB OFB CTR"
strapline: "BLOCK ECB CBC CFB OFB CTR"
description: "BLOCK ECB CBC CFB OFB CTRR"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "BLCOK-CRYPT"
tag:
  - "BLCOK-CRYPT"
toc: true
last_modified_at: 2021-04-13
comments: true
---

# 블록암호 ECB CBC CFB OFB CTR

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"




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
| 특징        | 기밀성이 낮음. <br>평문 블록과 암호화 블록이 일대일 관계.<BR>재전송 공격이 가능. | 1단계 앞에서 수행된 결과인 암호문 블록에 평문 블록을 **XOR**하여 암호화<BR>패딩(Padding) ; 평문의 길이는 가변적. 따라서, 마지막 블록의 길이가 부족한 경우 임의의 비트를 채워넣음.<br>IPSec에서 통신의 기밀성을 위해 CBC 모드 이용.<br>예 : 3DES-CBC, AES-CBC, Kerberos version5<br>암호화 : 순차적<br/>복호화 : 병렬적 | 1단계 앞의 암호문 블록을 암호 알고리즘의 입력으로 사용.<br>**복호화 시, 복호화가 아닌 암호화**<br>암호화 : 순차적<br>복호화 : 병렬적<br>재전송 공격이 가능.![image-20210207135524398](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-9.jpg) | **평문 블록이 동일하면 암호문이 같아지는 ECB의 단점**과, **오류 전파가 발생하는 CBC, CFB 모드**를 개선. | CTR 모드에서는 블록을 암호화할 때마다 1씩 증가해 가는 카운터를 암호화해서 키 스트림을 만든다. |
| 암호화      | W                                                            | ![image-20210207134444038](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-3.jpg) | ![image-20210207135113152](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-7.jpg) | 오류 전파가 발생하지 않는다.<br/>![image-20210207135724327](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-10.jpg) | ![image-20210207140109563](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-12.JPG) |
| 복호화      | ![6-2](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-2.jpg) | ![image-20210207134515589](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-4.jpg) | ![image-20210207135121585](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-8.jpg) | 오류 전파가 발생하지 않는다.<br>![image-20210207135732562](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-11.jpg) | ![image-20210207140117037](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-13.jpg) |
| 암호화 영향 |                                                              | **평문 블록의 한 비트 오류는 모든 암호문에 영향.**<br>![image-20210207134752030](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-6.jpg) | CBC와 동일                                                   |                                                              |                                                              |
| 복호화 영향 |                                                              | **복호화 시, 암호문 블록이 1개 파손된 경우, 미치는 영향은 2개 블록에 머문다.**<br/>![image-20210207134739011](/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_information/2020_9L/6-5.jpg) | CBC와 동일                                                   |                                                              |                                                              |



|                 | ECB  | CBC  | CFB  | OFB  | CTR  |
| --------------- | ---- | ---- | ---- | ---- | ---- |
| IV              |      | O    | O    | O    |      |
| 암=복 알고리즘  |      |      | O    | O    | O    |
| 병렬            | O    |      |      |      | O    |
| **연쇄** 암호화 |      | O    | O    |      |      |
| **연쇄** 복호화 |      |      |      |      |      |







