---
title: "파일명 일괄 변경하기(Linux, VS code)"
strapline: "Pipeline 명령어를 이용한 파일명 일괄 변경"
description: "Linux 및 VS Code에서 pipeline 명령어로 하위디렉토리 및 파일명 일괄 변경"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "Useful"
tag:
  - "Linux"
  - "VS Code"
  - "pipeline"
  - "파일명일괄변경"
toc: true
last_modified_at: 2020-12-06
comments: true
---

# 파일명 일괄 변경하기(Linux, VS code)

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 명령어

```bash
find ./ -name "*from*"  | sed -e 'p' -e "s/from/to/g" |xargs -n 2 mv
```

현 위치 폴더 내부의 모든 하위 폴더를 탐색하여 "from"이 포함된 부분을 "to"로 변경한다.

ex)

file : 2020_from_1.py  ==>  2020_to_1.py

directory : 2020_from/  ==>  2020_to/

## 1) Error 발생하는 경우

폴더 명과 이름에 모두 from이 있는 경우

2020_from/2020_from_1.py  ==>  2020_to/2020_to_1.py

- 폴더명이 상위에 있으므로 폴더명을 먼저 변경하므로, 2020_to/2020_from_1.py로 변경된다.
- 폴더명으로 변경되면 기존 경로와 달라지게 되므로 오류 발생!

## 2) Error 해결

명령어를 첫 번째 실행한 후(Error 발생),

한 번 더 실행시켜준다.