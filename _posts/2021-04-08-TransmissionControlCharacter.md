---
title: "전송제어문자"
strapline: "Transmission Control Character"
description: "Transmission Control Character"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "TransmissionControlCharacter"
tag:
  - "TCC"
toc: true
last_modified_at: 2021-04-08
comments: true
---

# 전송제어문자

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"

- 전송제어 프로토콜
	- OSI 참조모델의 2계층인 Data link layer에서 수행하는 기능.
	
- 전송제어 절차 5단계
	- 1단계 : 일반 교환망에서의 회선접속
	- 2단계 : 데이터 링크의 확립
	- 3단계 : 정보의 전송
	- 4단계 : 데이터 링크의 해제
	- 5단계 : 회선의 절단


| 부호  | 명칭                        | 내용                                             |
|-----|---------------------------|------------------------------------------------|
| SYN | SYNchronous Idle          | 문자 동기를 유지시키거나, 어떤 데이터 또는 제어 문자가 없을 때 채우기 위해 사용 |
| SOH | Start Of Heading          | 헤딩의 시작을 나타냄                                    |
| STX | Start of TeXt             | 헤딩의 종료 및 text의 개시를 나타냄                         |
| ETX | End of TeXt               | Text의 끝                                        |
| ETB | End of Transmission Block | Block의 끝                                       |
| EOT | End Of Transmission       | 전송의 끝 및 데이터 링크의 초기화                            |
| ENQ | ENQuiry                   | 회선 사용 요구부호 또는 상대방에게 어떤 응답을 요구하는데 사용            |
| DLE | Data Link Escape          | 이 뒤에 따르는 하나 또는 둘 이상의 문자들의 의미를 바꾸거나 추가적인 제어를 제공 |
| ACK | ACKowledge                | 수신한 정보 메시지에 대한 긍정 응답                           |
| NAK | Negative AcKnowledge      | 수신한 정보 메시지에 대한 부정 응답                           |




