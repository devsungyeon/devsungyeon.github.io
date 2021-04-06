---
title: "scheduling 프로세스 스케줄링"
strapline: "scheduling"
description: "scheduling"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "9Level_computerbasic"
tag:
  - "scheduling"
toc: true
last_modified_at: 2021-04-06
comments: true
---

# process scheduling

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"







| 종류   | Abbr                        | 방법                                        | 특징                                                             | 선점/비선점 |
|------|-----------------------------|-------------------------------------------|----------------------------------------------------------------|--------|
| RR   | Round Robin                 | FCFS 방식의 변형으로 일정한 시간을 부여하는 방법             | 시분할 방식에 효과적<br/>할당 시간이 크면 FCFS와 동일<br/>할당 시간이 작으면 문맥 교환이 자주 발생 | 선점     |
| SRT  | Shortest Remaining Time     | 수행도중 나머지 수행 시간이 적은 작업을 우선적으로 처리하는 방법      | 처리는 SJF와 같으나 이론적으로 가장 작은 대기 시간이 걸림                             | 선점     |
| MLQ  | Multi-Level Queue           | 서로 다른 작업을 각각의 큐에서 타임 슬라이스로 처리한다.          | 각각의 큐는 독자적인 스케줄링 알고리즘을 사용                                      | 선점     |
| MFQ  | Multi-Level Feedback Queue  | 하나의 준비 상태 큐를 통해서 여러 개의 피드백 큐를 걸쳐 일을 처리한다. | CPU와 I/O 장치의 효율을 높일 수 있음                                       | 선점     |
| 우선순위 |                             | 우선순위를 할당해 우선순위가 높은 순서대로 처리하는 방법           | 정적 우선순위<br/>동적 우선순위                                            | 비선점    |
| 기한부  |                             | 프로세스가 주어진 시간 내에 작업이 끝나게 계획하는 방법           | 마감 시간을 계산해야 하므로 막대한 오버헤드와 복잡성이 발생                              | 비선점    |
| FCFS | First Come First Serve      | 작업이 시스템에 들어온 순서대로 수행하는 방법                 | 대화형에 부적합<br/>간단하고 공평함<br/>반응 속도를 예측 가능                         | 비선점    |
| SJF  | Shortest Job First          | 수행 시간이 적은 작업을 우선적으로 처리하는 방법               | 작은 작업에 유리하고 큰 작업은 시간이 많이 걸림                                    | 비선점    |
| HRN  | Highest Response-ratio Next | SRT의 큰 작업이 시간이 많이 걸리는 점을 보완한 방법이다.        | 우선순위 = (대기시간 + 버스트시간) / 버스트시간                                  | 비선점    |




---
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM1ODY4ODE0OSwtNTgxMDE0MTg4LDI5MT
g4MzIzOCwxNjkyNjMwMDU2LDM2OTQ4NzQ1Nyw5MzExMTc3MDJd
fQ==
-->