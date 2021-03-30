---
title: "CC / ITSEC / TCSEC 비교"
strapline: "정보보호 거버넌스 표준 CC / ICSEC / TCSEC"
description: "정보보호 거버넌스 표준 CC / ICSEC / TCSEC"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "Information"
tag:
  - "Governance"
  - "CC"
  - "ITSEC"
  - "TCSEC"
toc: true
last_modified_at: 2021-03-30
comments: true
---

# CC / ITSEC / TCSEC 비교

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



##  평가 기준

- TCSEC 미국 국방부
- ITSEC 유럽
- CC
****

- TCSEC
	- 미국의 신뢰성 있는 컴퓨터 시스템 평가기준
	- 미국 국방성. **오렌지 북**
	- Bell-LaPadula 모델의 **기밀성.**  기밀성기반모듈. 가용x, 무결x
	- 보안 클래스
		- D - C1 - C2 - B1 - B2 - B3 - A1
		- D ; 최소보호
		- C ; 재량적(임의적) 보호 ; 임의적 접근제어
		- B ; 강제적 보호 ; 강제적 접근제어
		- A ; 검증된 정형화된 보호
- TNI
	- 미국 국방부
	- **기밀성**과 **무결성**.
	- ***레드북***
	- 등급
		- Non, C1(최소), C2(fair), B2(good)
- ITSEC
	- 유럽
	- **기밀성, 가용성, 무결성**
	- 기능성과 보증을 분리
		- Functionality ; F1 - F10 ; 기능 클래스
		- Assurance ; E0 - E6 ; 보증 수준
	- 등급
		- E1(최저) E2 E3 E4 E5 E6(최고) 6등급
		- E0 ; 부적합.(효용성 보증 하나라도 만족 못하는 경우)
- CC
	- TCSEC, ITSEC 단점을 보완
	- PP Protection Profile 보호프로파일 ; 보안 요구 사항이나 평가할 제품의 보호 항목을 명시
	- ST Security Target ; 보호목표명세서 ; 벤더나 개발자가 작성한 제품의 명세
	- 엄격한 준수 strict conformance
		- **보안목표명세서는 보호프로파일 내에 있는 모든 서술문을 포함한다.**
	- EAL Evaluation Assurance Level ; EAL0 ~ EAL7

****






<!--stackedit_data:
eyJoaXN0b3J5IjpbMjU5Mzg4NDQzLC0zMDM3MzQyMzcsLTgyOD
AyODE3Ml19
-->