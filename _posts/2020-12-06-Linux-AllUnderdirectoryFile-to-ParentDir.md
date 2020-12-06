---
title: "모든 하위 파일들 상위 폴더로 이동"
strapline: "Pipeline 명령어를 이용한 하위 파일들 상위 폴더로 이동"
description: "Linux 및 VS Code에서 pipeline 명령어로 하위 파일들 상위 폴더로 이동"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "Useful"
tag:
  - "Linux"
  - "VS Code"
  - "pipeline"
  - "하위파일들상위폴더로이동"
toc: true
last_modified_at: 2020-12-06
comments: true
---

# 모든 하위 파일들 상위 폴더로 이동

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 명령어

```bash
find -type f -execdir mv "{}" ../ \;
```

현 위치 폴더 내부의 모든 하위 폴더를 탐색하여 각 폴더의 내부 파일들을 상위 폴더로 이동.

ex)

file :

1) C:/2020_from/2020_from_1.py  ==>  C:/2020_from_1.py

2) C:/2020_from/2020_from_2.py  ==>  C:/2020_from_2.py

3) C:/2020_from/test/test.py  ==>  C:/2020_from/test.py


