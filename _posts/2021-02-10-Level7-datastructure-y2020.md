---
title: "2020년 7급 전산직 자료구조 풀이"
strapline: "자료구조 풀이"
description: "2020년 7급 전산직 자료구조 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "7Level_datastructure"
tag:
  - "7급"
  - "자료구조"
  - "7급공무원"
toc: true
last_modified_at: 2020-12-05
comments: true
---

# 2020년 7급 전산직 자료구조 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 

1. 
![2020_7L_1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_1.jpg)


**답 : **

①

②

③

④



---

## 2. 

2. 
![2020_7L_2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_2.jpg)


**답 : **

①

②

③

④



---

## 3. 

3. 
![2020_7L_3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_3.jpg)


**답 : **

①

②

③

④



---

## 4. 

4. 
![2020_7L_4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_4.jpg)


**답 : **

①

②

③

④



---

## 5. 

5. 
![2020_7L_5](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_5.jpg)


**답 : **

①

②

③

④



---

## 6. 

6. 
![2020_7L_6](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_6.jpg)


**답 : **

①

②

③

④



## 7. 

7. 
![2020_7L_7](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_7.jpg)


**답 : **

①

②

③

④



---

## 8. 

8. 
![2020_7L_8](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_8.jpg)


**답 : **

①

②

③

④



---

## 9. 

9. 
![2020_7L_9](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_9.jpg)


**답 : **

①

②

③

④



---

## 10. 

10. 
![2020_7L_10](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_10.jpg)


**답 : **

①

②

③

④



---

## 11. 

11. 
![2020_7L_11](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_11.jpg)


**답 : ①**
- 자료형 크기 
	- Struct
		- 가장 큰 변수의 크기를 기준으로 하여 나머지 변수를 **순서대로 차곡차곡** 배치하여 구조체 전체의 크기가 결정.
```
// test1의 크기는 8bytes
#include

typedef struct test1 {
	char a; // 1byte
	char b; // 1byte
	int c; // 4bytes
}
```
|byte1|byte2|byte3|byte4|
|:---|:---:|---:|---:|
|a|b|||
|c|c|c|c|
```
// test2의 크기는 12bytes
#include

typedef struct test2 {
	char a; // 1byte
	int b; // 4byte
	char c; // 1byte
}
```
|byte1|byte2|byte3|byte4|
|:---|:---:|---:|---:|
|a||||
|b|b|b|b|
|c|||

- Union
	- 공용체 멤버 변수 중 가장 큰 크기의 값을 하나 할당하고 모든 멤버가 그 메모리를 공유한다.
```
// test3의 크기는 12bytes
struct  {
	char a; // 1byte
	int b; // 4byte
	char c; // 1byte
} test3
```





---

## 12. 

12. 
![2020_7L_12](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_12.jpg)


**답 : **

①

②

③

④



---

## 13. 

13. 
![2020_7L_13](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_13.jpg)


**답 : **

①

②

③

④



---

## 14. 

14. 
![2020_7L_14](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_14.jpg)


**답 : **

①

②

③

④



---

## 15. 

15. 
![2020_7L_15](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_15.jpg)


**답 : **

①

②

③

④



---

## 16. 

16. 
![2020_7L_16](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_16.jpg)


**답 : **

①

②

③

④



---

## 17. 

17. 
![2020_7L_17](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_17.jpg)


**답 : **

①

②

③

④



---

## 18. 

18. 
![2020_7L_18](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_18.jpg)


**답 : **

①

②

③

④



---

## 19. 

19. 
![2020_7L_19](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_19.jpg)


**답 : **

①

②

③

④



---

## 20. 

20. 
![2020_7L_20](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_datastructure/2020_7L/2020_7L_20.jpg)


**답 : **

①

②

③

④
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MDgzMjY0MTQsMTM3NDcyODc0NSwyMz
A3NzQ5MzddfQ==
-->