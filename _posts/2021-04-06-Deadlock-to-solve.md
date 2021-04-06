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

- 하기 **네 가지 조건이 동시 **성립 시 교착 발생.
- 상호 배제 ; Mutual Exclusion
	- At least one resource must be held in a non-shareable way.
- 점유와 대기 ; Hold and wait
	- A process must be holding a resource and waiting for another.
- 비선점 ; No preemption
	- Resource cannot be preempted.
- 환형대기 ; Circular wait
	- A waits for B, B waits for C, C waits for A.

---


- 교착상태 해결방안
	- 예방, 회피, 발견, 회복
	- 예방 Prevention
		- 상호배제 예방 ; 상호배제 사용하지 않음(동시액세스 허락)
		- 부분할당 예방 ; 프로세스가 필요로 하는 자원을 일시에 요구/할당
		- 비선점 예방 ; 자원임시 할당해제 및 원상복구(다루기가 힘듦)
		- 환형대기 예방 ; 모든 자원 고유번호 지정하여 환형대기 예방
	- 회피(Avoidance) - Banker's Algorithm 은행가 알고리즘
		- OS는 자원의 상태를 감시
		- 프로세스는 사전에 자기 작업에서 필요한 자원의 수를 제시
		- OS는 사용자 프로세스로부터 자원의 요청이 있으면 모든 프로세스가 일정기간 내에 성공적으로 종료될 수 있는 안전한 상태인지 면밀하게 분석
		- OS는 안전한 상태를 유지할 수 있는 요구만을 수락, 그 외의 요구는 만족될 때까지 계속 거절
	- 발견 Detection
		- 시스템의 상태를 감시하는 알고리즘을 통하여 교착상태를 검사하는 알고리즘
		- 시스템의 자원할당 그래프로 교착상태검출 Graph reduction, cycle Detection, Knot detection
		- 교착상태 발생 시 자원할당 소거
	- 회복 Recovery
		- Deadlock이 없어질 때까지 프로세스를 순차적으로 Kill하여 제거
		- 프로세스 종료비용 최소화 ; 우선순위, 진행비용, 복귀비용 등
		- 자원의 우선순위 할당 ; 희생자 선택, 복귀, 기아상태
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTU4NjgwNjYsOTUyNjAzMTc3LDE5OTM4NT
gzNzcsMTY5MjYzMDA1NiwzNjk0ODc0NTcsOTMxMTE3NzAyXX0=

-->