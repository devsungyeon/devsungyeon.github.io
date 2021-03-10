---
title: "VS code C, C++, Cpp compile error no such file or directory"
strapline: "vs code c compile error no such file or directory"
description: "in Windows, VS code C, C++, Cpp compile error no such file or directory"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "Useful"
tag:
  - "VS Code"
  - "c"
  - "cpp"
toc: true
last_modified_at: 2021-03-10
comments: true
---

# VS code C, C++, Cpp compile error no such file or directory

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 명령어 추가

```bash
"code-runner.terminalRoot": "/"
```

[참고github](https://github.com/formulahendry/vscode-code-runner/issues/296)

==> 상기 명령어를 json에 추가로 VS code compile error "no such file or directory"

- setting.json 파일 열기
	- 여는 방법1
		- 1) CTRL + SHIFT + P
		- 2 "open setting" 입력
		- 3) "OPEN SETTINGS (JSON)" 선택
	- 여는 방법2
		- File -> Preferences -> Settings -> Extensions -> "Edit in settings.json"

하기는 json 파일 예시.
![setting-json](/assets/images/VScodejson/setting-json.png)






