---
title: "IP TCP UDP HEADER"
strapline: "IP TCP UDP HEADER"
description: "IP TCP UDP HEADER"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "IP-TCP-UDP-HEADER"
tag:
  - "IP-TCP-UDP-HEADER"
toc: true
last_modified_at: 2021-04-13
comments: true
---

# IP TCP UDP HEADER210415 prepare

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"

[Sniffing, Spoofing, Snoofing, Smurfing, Parming](https://chojinyoung.tistory.com/m/27?category=912395)

- sniffing ; sniff 코를 킁킁거리다. 네트워크 중간에서 패킷 정보를 도청. MAC address(L2)와 IP address(L3)를 가짐. 공격자는 Promiscuous모드를 통해 target host의 2,3 계층의 필터링을 해제시킴.
	- promiscuous모드 ; 2,3 계층에서 필터링을 해제하는 랜카드의 모드.
	- Switch Jamming(MAC overflow): 스위치가 허브처럼 동작. mac주소테이블이 가득차면 모든 네트워크 세그먼트 트래픽을 브로드캐스팅하는 특징. 즉 스위치 테이블을 overflow시켜 모든 포트로 브로드캐스팅. 위조된 source mac주소를 계속 변경하며 네트워크로 흘려보내어 스위치의 mac address table 버퍼를 오버플로우 시킴.
	- 스위치 ; 근거리 통신망(LAN) 기기간 통신

- spoofing ; 
- snooping
- smurfing
- pharming



## 3
COCOMO ; 소프트웨어 개발의 공정 개발 기간의 견적 방법.
예측치 = {낙관치+(4 ×기대치) +비관치} / 6 
 산정 공식 
 개발기간 = 노력(인월) /투입인원 
 개발비용 = 노력(인월) × 단위비용 
 노력(인월) = 개발기간 × 투입인원 
= LOC / 1인당 월평균 생산 코드 라인 수 
 생산성 = LOC /노력(인월) 

*  COCOMO 소프트웨어 프로젝트 모드(=개발 유형) 
소프트웨어 개발 유형은 소프트웨어의 복잡도 혹은 원시 프로그램의 규모에 따라 
조직형(Organic Mode), 반분리형(Semi-Detached Mode), 내장형(Embedded Mode)으로 분류 할 수 있음 

- 조직형(Organic Mode) 
- 조직형은 기관 내부에서 개발된 중ㆍ소규모의 소프트웨어로 일괄 자료처리나 
과학 기술 계산용, 비즈니스 자료 처리용으로 
5만(50KDSI)라인 이하의 소프트웨어를 개발하는 유형 
-사무 처리용, 업무용, 과학용 응용 소프트웨어 개발에 적합 

- 반분리형(Semi-Detached Mode) 
- 반분리형은 조직형과 내장형의 중간형으로 
트랜잭션 처리 시스템이나 운영체제, 데이터베이스 관리 시스템 등의 
30만(300KDSI)라인 이하의 소프트웨어를 개발하는 유형 

- 내장형(Embedded Mode) 
- 내장형은 최대형 규모의 트랜잭션 처리 시스템이나 운영체제 등의 
30만 (300KDSI)라인 이상의 소프트웨어를 개발하는 유형 

-신호기 제어 시스템, 미사일 유도 시스템, 
실시간 처리 시스템 등의 시스템 프로그램 개발에 적합 


- COCOMO 모형의 종류 
COCOMO는 비용 산정 단계 및 적용 변수의 구체화 정도에 따라 
기본(Basic)형, 중간(Intermediate)형, 발전(Detailed)형으로 구분할 수 있음 

- 기본(Basic)형 COCOMO 
기본형 COCOMO는 소프트웨어의 크기(생산 코드 라인 수)와 
개발 유형(모드)만을 이용하여 비용을 산정하는 모형 

- 중간(Intermediate)형 COCOMO 
기본형 COCOMO의 공식을 토대로 사용하나, 
여러 가지 다른 요인에 의해 비용을 산정하는 모형 

- 발전(Detailed)형 COCOMO 
중간(Intermediate)형 COCOMO를 보완하여 만들어진 방법으로 
개발 공정별로 보다 자세하고 정확하게 노력을 산출하여 비용을 산정하는 모형 


- Putnam 모형 
 Putnam 모형은 소프트웨어 생명 주기의 전 과정 동안에 사용될 
노력의 분포를 가정해 주는 모형 
 푸트남(Putnam)이 제안한 것으로 생명 주기 예측 모형이라고도 함 
 시간에 따른 함수로 표현되는 Rayleigh-Norden 곡선의 노력 분포도를 기초로 함 


- SLIM 
Putnam 예측 모델과 Rayleigh-Norden 곡선을 기초로 하여 개발된 
자동화 추정 도구 

- 기능 점수 (FP, Function Point) 
기능 점수 모형은 Albrecht가 제안한 것으로, 
소프트웨어의 기능을 증대시키는 요인별로 가중치를 부여하고, 
요인별 가중치를 합산하여 총 기능 점수를 산출하며 
총 기능 점수와 영향도를 이용하여 기능 점수(FP)를 구한 후 
이를 이용하여 비용을 산정하는 기법 



- WBS(Work Breakdown Structure) : 
일을 세분화하여 일정을 짜서 역할 분담을 하는 작업의 줄임말로 작업을 단위업무로 분할하여 관리하는 구조로 프로젝트 관리 및 시스템 엔지니어링에서 프로젝트 일정관리기능 으로 많이 사용 한다.  반드시 WBS로 관리하고 단계별 산출물을 반드시 생성


## 4

[다이어그램 구조/행위](https://roynus.tistory.com/1037)



## 8

위험 관리 활동 순서
식별 - 분석 - 계획 - 관찰

## 10

재공학 ; 자동화된 도구로 현존하는 시스템을 점검 또는 수정하는 프로세스

## 11

[GoF](https://velog.io/@namezin/GoF-design-pattern)

## 13

Risk management ; 3단계 Defined

## 14

[MCDC](http://blog.skby.net/mc-dc-modified-condition-decision-coverage/)








~~~c
void hanoi(int num, char from, char by, char to) {
	if(num == 1)
		printf("1 : %c → %c\n", from, to);
	else {
		hanoi(num-1, from, to, by);
		printf("%d : %c → %c\n", int, from, to);
		hanoi(num-1, by, from, to);
	}
}
~~~
<!--stackedit_data:
eyJoaXN0b3J5IjpbODUxMDA0NzddfQ==
-->