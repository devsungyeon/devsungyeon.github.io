---
title: "모든 하위 빈 폴더들 삭제"
strapline: "Pipeline 명령어를 이용한 빈 하위 폴더들 삭제"
description: "Linux 및 VS Code에서 pipeline 명령어로 빈 하위 폴더들 삭제"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "Useful"
tag:
  - "Linux"
  - "VS Code"
  - "pipeline"
  - "하위빈폴더들삭제"
toc: true
last_modified_at: 2020-12-06
comments: true
---

# 모든 하위 빈 폴더들 삭제

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 명령어

```bash
find . -type d -empty -print -delete
```

현 위치 폴더 내부의 모든 하위 폴더를 탐색하여 빈 폴더들 모두 출력 후 삭제.

ex)

file :

1) C:/2020_from/ (empty)  ==>  "2020_from" 폴더 삭제

2) C:/2019_from/2020_from_2.py  ==>  폴더 삭제 X

3) C:/2019_from/test/ (empty)  ==>  "test" 폴더 삭제


