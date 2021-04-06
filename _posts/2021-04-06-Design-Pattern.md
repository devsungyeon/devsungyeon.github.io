---
title: "디자인 패턴 Design Pattern"
strapline: "Design Pattern"
description: "Design Pattern"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "Software_engineering"
tag:
  - "Design Pattern"
toc: true
last_modified_at: 2021-04-06
comments: true
---

# 디자인 패턴 Design Pattern

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"





---


| 대분류          | 종류               | 사용 목적                                  |
|--------------|------------------|----------------------------------------|
| 객체 생성을 위한 패턴 | Factory Method   | 대행 함수(위임)를 통한 객체 생성, 인스턴스 생성 결정은 서브클래스 |
|              | Abstract Factory | 제품군(product family)별 객체 생성             |
|              | Singleton        |  클래스 인스턴스가 하나만 만들어지고 그 인스턴스의 전역접근      |
|              | Prototype        | 복제를 통한 객체 생성                           |
|              | Builder          | 부분 생성을 통한 전체 객체 생성                     |

---

| 대분류          | 종류        | 사용 목적                           |
|--------------|-----------|---------------------------------|
| 구조 생성을 위한 패턴 | Adapter   | 기존 모듈 재사용을 위한 인터페이스 변경          |
|              | Facade    | 서브시스템에 대한 통합된 인터페이스를 제공         |
|              | Bridge    | 인터페이스와 구현의 명확한 분리               |
|              | Composite | 객체간의 부분전체 관계 형성 및 관리, 재귀적 합성 이용 |
|              | Decorator | 객체의 기능을 동적으로 추가 삭제              |
|              | Flyweight | 작은 객체들의 공유                      |
|              | Proxy     | 대체(대리자) 객체를 통한 작업 수행            |


---

| 대분류          | 종류                      | 사용 목적                                                                        |
|--------------|-------------------------|------------------------------------------------------------------------------|
| 행위 개선을 위한 패턴 | Interpreter             | 간단한 문법에 기반한 검증작업 및 작업처리                                                      |
|              | Template Method         | 상위클래스에서 기본 골격을 결정. 하위클래스에서 구체적 내용 정의                                         |
|              | Command                 | 요청을 객채로 캡슐화. 수행할 작업의 일반화를 통한 조작                                              |
|              | Iterator                | 동일 자료형의 여러 객체 순차 접근                                                          |
|              | Mediator                | 객체들 간의 상호작용을 객체로 캡슐화. M:N 객체 관계를 M:1로 단순화                                    |
|              | Memento                 | 객체의 이전 상태 복원 또는 보관                                                           |
|              | Observer                | One source Multiple Use                                                      |
|              | State                   | 객체 상태 추가시 행위 수행의 원활한 변경                                                      |
|              | Strategy                | 동일 목적의 여러 알고리즘 중 선택해서 적용                                                     |
|              | Visitor                 | 오퍼레이션이 처리할 요소의 클래스를 변경하지 않고도 새로운 오퍼레이션을 정의, 구문트리 파싱 시 트리를 이루는 모든 노드를 방문하여 작업 |
|              | Chain of Responsibility | 수행 가능 객체군끼리 요청 전파                                                            |


---

| 목적          | 생성 패턴 Creation                                           | 구조 패턴 Structural                                                       | 행위 패턴 Behavioral                                                                                                          |
|-------------|----------------------------------------------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| 외우기<br/>TIP | FSABP                                                    | ABCD2FP                                                                | T2I2C2S2MVO                                                                                                               |
| 의미          | 객체의 생성방식을 결정하는 패턴                                        | 객체를 조직화하는데 유용한 패턴                                                      | 객체의 행위를 조직, 관리, 연합하는데 사용하는 패턴                                                                                             |
| 클래스         | Factory method                                           | Adapter                                                                | Template method<br/>Interpreter                                                                                           |
| 객체          | Singleton<br/>Abstract factory<br/>Builder<br/>Prototype | Bridge<br/>Composite<br/>Decorator<br/>Facade<br/>Fly weight<br/>Proxy | Iterator<br/>Command<br/>Chain of Responsibility<br/>State<br/>Strategy<br/>Mediator<br/>Memento<br/>Visitor<br/>Observer |


---


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIxMjYxNTcxOCwtMTM2Njk1MzI5OSwxOD
A1MTQzMDczLDg5Njk0OTQ0NywxNjkyNjMwMDU2LDM2OTQ4NzQ1
Nyw5MzExMTc3MDJdfQ==
-->