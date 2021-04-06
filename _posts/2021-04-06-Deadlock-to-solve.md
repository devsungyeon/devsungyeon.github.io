---
title: "Deadlock 조건 및 해결방안"
strapline: "Deadlock and how to solve"
description: "Deadlock and how to solve"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "9Level_computerbasic"
tag:
  - "Deadlock"
toc: true
last_modified_at: 2021-04-06
comments: true
---

# Deadlock 조건 및 해결방안

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"

## 교착상태 발생 조건

- 상호 배제 ; Mutual Exclusion
	- At least one resource must be held in a non-shareable way.
- 점유와 대기 ; Hold and wait
	- A process must be holding a resource and waiting for another.
- 비선점 ; No preemption
	- Resource cannot be preempted.
- 환형대기 ; Circular wait
	- A waits for B, B waits for C, C waits for













---
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcxMzY0MTgxNiwxNjkyNjMwMDU2LDM2OT
Q4NzQ1Nyw5MzExMTc3MDJdfQ==
-->