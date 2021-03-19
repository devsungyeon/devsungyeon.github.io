---
title: "SQL with 명령어 임시테이블 생성"
strapline: "SQL create temporary table using with"
description: "SQL WITH"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "Database-SQL"
tag:
  - "데이터베이스"
  - "SQL"
toc: true
last_modified_at: 2021-03-19
comments: true
---

# SQL with 명령어 임시테이블 생성

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## Programmers 입양 시각 구하기(2)



``` sql
WITH RECURSIVE TIME AS (
SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1 FROM TIME WHERE HOUR < 23)
SELECT HOUR, COUNT(HOUR(DATETIME)) AS 'COUNT'
FROM TIME LEFT OUTER JOIN ANIMAL_OUTS
ON (HOUR=HOUR(DATETIME))
GROUP BY HOUR 
```










<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc4MzcyMzUzNCwxNzM3ODE2OTE0XX0=
-->