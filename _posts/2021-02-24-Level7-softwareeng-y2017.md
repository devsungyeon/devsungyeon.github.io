---
title: "2017년 7급 전산직 소프트웨어공학데이터베이스 풀이"
strapline: "소프트웨어공학데이터베이스 풀이"
description: "2017년 7급 전산직 소프트웨어공학데이터베이스 풀이"
header:
 overlay_image: /assets/images/bright.jpg
categories:
  - "7Level_softwareengdatabase"
tag:
  - "7급"
  - "소프트웨어공학데이터베이스"
  - "7급공무원"
toc: true
last_modified_at: 2021-02-24
comments: true
---

# 2017년 7급 전산직 소프트웨어공학데이터베이스 풀이

궁금한 점이나 오류는 댓글로 달아주시면, 답변 혹은 수정하겠습니다! ":)"



## 1. 소프트웨어 요구분석 ...

1. 
소프트웨어 요구분석 명세서(SRS)에 포함되는 내용이 아닌 것은?![2017_7L_1](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_1.jpg)

**답 : ②**

- 아키텍처 및 인터페이스 명세는 요구사항 단계가 아닌 설계 단계에서 포함된다.



---

## 2. 프로토타입 개발 모델에...

2. 
프로토타입 개발 모델에 대한 설명으로 옳지 않은 것은?![2017_7L_2](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_2.jpg)

**답 : ④**

④ 고객의 요구사항을 ~~초기에 구체적으로 기술하기 어렵고 중요한 문제점이 프로젝트 후반부에 가서야 발견~~된다.

==> 프로토타입의 경우, 초도품을 제작하므로 고객의 요구사항을 초기에 파악할 수 있으며, 초도품을 통해 고객의 요구사항과 상이한 문제점을 조기에 발견할 수 있다.



---

## 3. 코드의 정적 분석 도구를...

3. 
코드의 정적 분석 도구를 통하여 찾을 수 있는 오류에 해당하지 않는 것은?![2017_7L_3](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_3.jpg)

**답 : ①**

- 정적 분석 도구는 프로그램을 컴퓨터에서 수행시키지 않고, **원시코드를 직접 시험하는 것이다.**
- 따라서 메모리 사용량 초과와 같은 실행 시, 발견되는 오류는 동적 분석 시 확인된다.





---

## 4. 리팩토링에 대한 ...

4. 
리팩토링에 대한 설명으로 옳지 않은 것은?![2017_7L_4](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_4.jpg)

**답 : ②**

② 리팩토링은 실행 중인 ~~프로그램의 기능 변경이 수반되어야 한다.~~

- 리팩토링(Refactoring)
  - 코드 스멜을 없애고 코드의 품질을 향상
  - 기능(동작)의 변경 없이 내부구조를 변경하는 것.



---

## 5. 같은 유형의 소프트웨어 ...

5. 
같은 유형의 소프트웨어 테스트 기법으로만 묶은 것은?![2017_7L_5](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_5.jpg)

**답 : ③**

ㄱ. 기본 경로 테스트 - 화이트박스

ㄴ. 페어와이즈 테스트 - 블랙박스

ㄷ. 모델 기반 테스트 - 블랙박스

ㄹ. 분기 커버리지 - 화이트박스

ㅁ. 직교 배열 테스트 - 블랙박스

- 화이트 박스 시험
  - 문장 검증 기준, 노드/문장 커버리지
  - 분기 검증 기준, 간선/분기 커버리지
  - 경로 검증 기준, 경로 커버리지
  - 조건 검증 기준, 조건 커버리지
  - 기본 경로 시험
  - 루프 시험
  - 조건 시험
  - 데이터 흐름 시험
  - 그래프 행렬
- 블랙 박스 시험
  - 그래프 기반 테스팅
  - 동등 분할, 균등 분할, 동치 분할
  - 경계값 분석
  - 원인-결과 그래프
  - 오류 예측, 데이터 확인
  - 비교 검사
  - 직교 배열 테스팅
  - 페어와이즈 테스트, 조합 테스트





---

## 6. 소프트웨어 개발 작업에 ...

6. 
소프트웨어 개발 작업에 일관적이고 체계적인 구조(framework)를 제공하기 위하여 1995년에 ISO/IEC에서 제정한 소프트웨어 생명주기 공정 국제표준은?![2017_7L_6](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_6.jpg)

**답 : ③**

① ISO/IEC 9126 ; 소프트웨어 제품 품질의 특성을 정의하고 품질 평가의 Metrics를 정의한 국제 표준. 사용자 관점에서 본 소프트웨어의 제품 품질 특성에 대한 표준. 객관적이고 계량적으로 평가.

- 신사이기(에) 유효
  - 신뢰성, 사용성, 이식성, 기능성, 유지보수성, 효율성

② ISO/IEC 12119 ; 소프트웨어 품질 요구사항 및 테스트에 관한 표준안.

③ ISO/IEC 12207 ; SW 개발 지침서, 프로세스 중심의 각 활동 및 역할에 대해 기술. 소프트웨어 개발 프로세스를 위한 프레임워크.

④ ISO/IEC 25000 ; ISO에서 제정한 소프트웨어 품질평가 통합 모델의 표준. 9126 + 14598 + 12119

- ISO/IEC 14598 ; 소프트웨어 품질 인증을 위한 평가 방법 및 관리에 대한 표준안. 평가 방법과 절차를 정의.





## 7. 소프트웨어 아키텍처의...

7. 
소프트웨어 아키텍처의 4+1 관점(view)에 대한 설명으로 옳지 않은 것은?![2017_7L_7](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_7.jpg)

**답 : ②**

② 논리 관점에서는 ~~계층 구조, 제약 사항, 코드 재사용 등과 같은 시스템 구현을 위한 요건~~을 보여주는 데 초점을 둔다.

==> 구현 뷰에 대한 설명.

- 소프트웨어 아키텍처 4+1 관점 = UML의 4+1뷰 ; Unified Modeling Language

  - 유스케이스 뷰 = 사용 사례 뷰

    - 사용자 관점
    - 요구 분석 단계에서 사용.

  - 논리 뷰

    - 설계자 관점
    - 필요한 클래스나 컴포넌트의 종류와 이들의 관계에 초점.

  - 구현 뷰

    - 개발자 관점
    - 파일과 디렉터리 구조, 그리고 물리적인 배포 단위 별로 구성요소를 기술.

  - 프로세스 뷰

    - 시스템 통합자 관점
    - 모든 클래스에 관심이 있는 게 아니라, 독자적인 제어 스레드를 가질 수 있는 클래스에 초점

  - 배치 뷰

    - 시스템 엔지니어 관점
    - 서브시스템들이 물리적인 환경에서 어떻게 연산되어 실행되는지를 노드 간의 관계로 나타냄.

    



---

## 8. 테스트 주도 개발(Test-driven development)은 ...

8. 
테스트 주도 개발(Test-driven development)은 애자일 기법에서 개발되는 증분과 해당 증분을 위한 테스트 코드를 함께 작성해 나가는 방법이다. 이에 대한 설명으로 옳지 않은 것은?![2017_7L_8](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_8.jpg)

**답 : ①**

① ~~멀티 스레드를 사용하는~~ 어플리케이션의 테스트를 위해 개발되었다.

- TDD 테스트 주도 개발
  - 테스팅과 코드 개발을 중첩.
  - JUnit과 같은 자동화된 테스트 프레임워크 환경이 필수적.
  - 신규 소프트워어 개발에 가장 가치.
  - 멀터 스레드 시스템에 효과적이지 않을 수 있다. 왜냐하면 서로 다른 스레드들은 여러 번의 테스트 실행에서 서로 다른 횟수로 중첩될 수 있으므로 상이한 결과를 생성할 수 있기 때문이다.



---

## 9. CMMI의 5단계 소프트웨어...

9. 
CMMI의 5단계 소프트웨어 프로세스 성숙도 모델에서 Level 2에 해당하는 주요 프로세스 영역이 아닌 것은?![2017_7L_9](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_9.jpg)

**답 : ②**

Level 2 = Managed. 관리.

② 요구사항 개발(Requirements development) - Level3. Defined



- CMMi(Capability Maturity Model integration)

| Level                  | Focus                                  | Process Areas                                                |
| ---------------------- | -------------------------------------- | ------------------------------------------------------------ |
| Performed              |                                        |                                                              |
| Managed                | Basic<br>Project<br/>Management        | Requirements management<br/>Project planning<br/>Project monitoring and control<br/>Supplier agreement management<br/>Measurement and analysis<br/>Process and product quality assurance<br/>Configuration management |
| Defined                | Process<br/>standardization            | Requirements development<br/>Technical solution<br/>Product integration<br/>Verification<br/>Validation<br/>Organizational process focus<br/>Organizational process definition<br/>Organizational training<br/>Integrated project management<br/>Integrated supplier management<br/>Risk management<br/>Decision analysis and resolution<br/>Organizational environment for integration<br/>Integrated teaming |
| Quantitatively managed | Quantitative<br/>management            | Organizational process Performance<br/>Quantitative project management |
| Optimizing             | Continuous<br/>process<br/>improvement | Organizational innovation and deployment<br/>Causal analysis and resolution |







---

## 10. 그림과 같이 MyCustomer...

10. 
그림과 같이 MyCustomer 클래스를 대상으로 리팩토링을 실시하였다. 이와 관련 있는 리팩토링 기법만을 모두 고른 것은?![2017_7L_10](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_10.jpg)

**답 : ③**

[리백로팅 설명](https://arisu1000.tistory.com/category/%EB%A6%AC%ED%8C%A9%ED%86%A0%EB%A7%81)

[Refactoring.com](https://www.refactoring.com/catalog/)

- ㄱ. 메소드 추출[link](https://arisu1000.tistory.com/27597)
  - 메소드 행이 많을수록 메서드가 하는 일을 파악하기 어려움.
  - 읽기 쉽고, 코드의 중복을 줄이고, 독립적인 부분을 분리하여 오류의 발생 가능성을 줄이기 위함.
- ㄴ. 메소드 상향[link](https://arisu1000.tistory.com/27627)
  - 서브클래스들에 같은 결과를 반환하는 메소드들을 가지고 있다면 해당 메소드들을 슈퍼클래스로 이동.
- ㄷ. 메소드명 변경
- ㄹ. 매개변수 세트를 객체로 전환[link](https://arisu1000.tistory.com/27615)
  - 무관한 데이터 요소가 있는 경우 매개변수객체(Introduce Parameter Object)를 통해 단일 매개 변수 개체로 병합.
- ㅁ. 메소드를 매개변수로 전환[link](https://arisu1000.tistory.com/27623)
  - 몇몇 메소드들이 비슷한 작동을 하지만 메소드 내부에 다른 값들을 가지고 잇다면 그 각각의 값들을 파라미터로 사용하는 하나의 메소드를 만드시오.







---

## 11. 배열, 레코드, 구조체 등을...

11. 
배열, 레코드, 구조체 등을 매개변수로 사용하는 모듈 사이의 결합도는?![2017_7L_11](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_11.jpg)

**답 : ②**

- 결합도 ; 모듈간의 상호 의존도

| 자료                    | 스탬프       | 제어 | 외부            | 공통                        | 내용   |
| ----------------------- | ------------ | ---- | --------------- | --------------------------- | ------ |
| 약                      | <            | <    | <               | <                           | 강     |
| 좋음                    | >            | >    | >               | >                           | 안좋음 |
| 매개변수, call by value | 배열, 구조체 |      | 외부변수 extern | 전역변수, call by reference | 종속.  |









---

## 12. 요구분석 단계를 ...

12. 
요구분석 단계를 순서대로 바르게 나열한 것은?![2017_7L_12](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_12.jpg)

**답 : ②**





---

## 13. 시스템을 구성하는 ...

13. 
시스템을 구성하는 물리적인 노드와 통신 경로, 그리고 컴포넌트의 수행 환경을 표시하는 UML 다이어그램은?![2017_7L_13](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_13.jpg)

**답 : ①**

- ① 배치 다이어그램 deployment
  - 소프트웨어의 하드웨어 배치를 나타냄
- ② 통신 다이어그램 communication
  - 시스템이나 객체들이 메시지를 주고받으며 시간의 흐름에 따라 상호 작용하는 과정을 액터, 객체, 링크, 메시지 등의 요소를 사용하여 그림을 ㅗ 표현.
- ③ 타이밍 다이어그램 timing
  - 타임라인을 따라 개체와 사용자가 어떻게 행동하는지를 보여줌. 시간과 기간 제약에 따라 발생하는 변화에 초점.
- ④ 컴포지트 다이어그램 composite
  - 컴포넌트의 합성구조와 커넥션을 나타냄



- 객체지향의 개념. 객체지향 패러다임.

- UML 시스템 모델 3가지
  - 기능적 모델 functional model
    - 사용 사례 다이어그램 ; 사용자 측면에서 본 시스템 기능을 나타냄
  - 정적 모델 static model
    - 클래스 다이어그램 ; 클래스의 관계를 나타냄
    - 객체 다이어그램 ; 객체의 정적 구조를 나타냄
    - 컴포지트 다이어그램 ; 컴포넌트의 합성구조와 커넥션을 나타냄
    - 컴포넌트 다이어그램 ; 코드 구조를 나타냄
    - 패키지 다이어그램 ; 패키지로 선언한 모듈의 구조를 나타냄.
    - 배치 다이어그램 ; 소프트웨어의 하드웨어 배치를 나타냄
  - 동적 모델 dynamic model
    - 인터랙션 다이어그램 ; 객체들 사이의 메시지 교환을 나타냄
    - 상태 다이어그램 ; 하나의 객체가 가질 수 있는 상태와 상태의 변화에 의한 동작을 나타냄.
    - 액티비티 다이어그램



---

## 14. 프로그램 인스펙션(inspection)을...

14. 
프로그램 인스펙션(inspection)을 통해 결함을 검출하고자 할 때, 결함 유형에 따른 검사항목을 옳게 짝지은 것은?![2017_7L_14](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_14.jpg)

**답 : ③**

① 모든 반복문은 확실히 종료되는가? - 제어 에러

② 버퍼 오버플로우의 가능성이 있는가? - 데이터 에러

④ 예상하지 않은 입력이 문제를 일으킬 수 있는가? - 입출력 에러

- 소프트웨어 인스펙션 체크 리스트.
  - 데이터 참조 에러 ; 올바르지 못하게 선언되거나 잘못된 값으로 초기화된 data를 참조할 경우 발생하는 에러
    - 초기화되지 않은 변수가 있는가?
    - 데이터 오버플로우 처리
    - "off by one" 오버플로우 처리
    - 변수가 참조하는 메모리가 할당되어 있지 않은 경우 dangling reference
    - 변수가 맞는 타입의 값이 저장되어 있지 않은가?
    - 변수가 2개 이상의 함수에서 참조될 때 동일하지 않은 값이 참조되는가?
  - 데이터 선언 에러 ; 부적절하게 선언된 변수나 상수를 사용할 때 발생하는 에러.
    - 명시적으로 선언되었는가?
    - 올바른 타입으로 선언되었는가?
    - 선언 시점에 값이 Assign 되었는가?
    - 선언된 변수명이 명확하게 구분되는가?
    - 선언된 변수가 단 1번이라도 참조되고 있는가?
  - 계산 에러 ; 잘못된 연산으로 인해 발생하는 에러
    - 연산하는 두변수의 데이터타입이 같은가? integer, float
    - 데이터 타입은 같지만 길이가 다른 변수를 연산하는 경우
    - 데이터 타입이나 길이의 차이를 자동적으로 변환 또는 처리하는 컴파일러에 대해 고려되어야 함.
    - 왼쪽 피연산자의 데이터 타입이 오른쪽 연산 결과변수의 데이터타입보다 작은지 확인해야함.
    - 연산 중 오버프롤우가 발생할 가능성이 있는가?
  - 비교 에러 ; 다른 형태의 값을 비교하여 생기는 에러.
    - 서로 다른 타입을 비교하고 있지 않은가?
    - 비교 연산자는 올바르게 사용되었는가?
    - 불리언 연산식이 올바르게 사용되었는가?
    - 불리언 연산식이 반복해서 여러번 사용되는 경우 순서가 병확하게 드러나는가?
  - 제어 에러 ; 데이터 흐름이 잘못된 순서인 에러
    - 모든 반복이 항상 종료되는지 확인
    - 모든 프로그램, 모듈, 함수가 종료되는지 확인
    - 한번도 실행하지 않는 반복이 있는지 확인.
    - Switch~Case문 같이 값에 따라 분기되는 코드.
  - 인터페이스 에러 ; 단위 개체간 규약이 일치하지 않는 에러
    - 함출 호출 시 인자의 수와 순서가 같은가?
    - 인자의 타입과 크기는 올바르게 호출되고 있는가?
    - 인자의 값이 잘못 사용되고 있지 않은가?
    - 전역변수의 경우 여러 함수에서 동일한 값과 이름을 참조되고 있는가?
    - 상수 값이 인자로 전달되고 있지 않은가?
  - 입출력 에러 ; 파일 생성 관련 에러
    - 파일의 속성이 올바르게 생성되어 있는가?
    - 파일의 크기가 현 메모리 사이즈에 비해 적절한가?
    - 모든 파일이 사용되기 전에 열리고 있는가?
    - 사용 후에 닫히고 있는가?
    - EOF(End of File) 조건이 체크되어 처리되고 있는가?
    - 입출력에러들이 체크되어 처리되고 있는가?





---

## 15. Iterator 패턴에 대한...

15. 
Iterator 패턴에 대한 설명으로 옳지 않은 것은?![2017_7L_15](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_15.jpg)

**답 : ③**

③ ~~서로 다른 인터페이스~~를 사용하기 때문에 각각의 객체를 참조하기 위한 다형성 코드(polymorphic code)를 개발하는 것이 불가능하다.

- 반복자 Iterator
  - 자료처리 시스템과 같이 유사한 객체들의 집단을 다루어야 할 경우, 동일한 방법(인터페이스)으로 객체 집단 속의 객체가 다루어지도록 만들어진 패턴.
  - 집단 객체의 내부 표현을 드러내지 않고 집단 객체의 요소를 순차적으로 접근하는데 사용.





---

## 16. 그림과 같이 서브시스템 사이의...

16. 
그림과 같이 서브시스템 사이의 의사소통 및 종속성을 최소화하기 위하여 단순화된 하나의 인터페이스를 제공하는 디자인 패턴은?![2017_7L_16](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_16.jpg)

**답 : ④**

- Design Pattern
  - Facade - 하나의 통합된 인터페이스를 제공





---

## 17. 통합 테스트에 대한...

17. 
통합 테스트에 대한 설명으로 옳지 않은 것은?![2017_7L_17](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_17.jpg)

**답 : ①**

① 회귀 테스트는 ~~복잡하고 시간이 중요한 프로젝트에 적용하면 효율적이다.~~ ==> 스모크 테스팅(smoke testing)

- 회귀 테스트
  - 오류를 제거하거나 수정한 시스템이나 시스템 컴포넌트 또는 프로그램이 오류 제거와 수정에 의해 새로이 유입된 오류가 없는지를 확인하는 일종의 반복 시험.
  - 반복적인 시험이 필요한 이유는 오류가 제거수정되는 상당수의 시스템이 의도치 않았던 오작동이나 새로운 형태의 오류를 일으키기 때문이다.
  - 수정변형된 시스템이나 시스템 컴포넌트 또는 프로그램이 명세된 요구 사항을 충족시키는지를 확인하는 시험의 한 형태이다.
  - 변경이 돌출 행위나 추가 오류를 가져오지 않았다는 것을 보장하는 활동으로, 변경 때문에 영향을 받게 될 소프트웨어 기능에 초점을 맞춘 추가시험이다.

- 스모크 테스팅(smoke testing)
  - 소프트웨어가 개발될 때 공통적으로 사용할 수 있는 통합 테스팅 방법으로, **시간이 매우 중요한 프로젝트에서 시간을 조절하기 위한 매커니즘으로 고안.**
  - 코드로 변환된 소프트웨어 컴포넌트들은 통합되어 빌드가 된다. 빌드는 제품의 기능을 구현하는데 필요한 모든 데이터 파일, 라이브러리, 재사용 모듈, 공학이 적용된 컴포넌트를 포함한다.
  - 빌드의 기능을 제대로 수행하지 못하게 하는 오류들을 찾아내기 위한 일련을 테스트를 설계한다. 소프트웨어 프로젝트가 계획된 일정을 맞추지 못하도록 할 가능성이 가장 큰 오류를 발견하는데 목적이 있다.
  - 빌드를 통합하여 다른 빌드를 만들고 전체 제품은 매일 스모크 테스트 된다. 통합방식은 하향식 또는 상향식이다.





---

## 18. 다음 제어 흐름 그래프에 ...

18. 
다음 제어 흐름 그래프에 나타난 프로그램을 테스트할 때, 옳지 않은 것은?![2017_7L_18](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_18.jpg)

**답 : ④**

④ {(x:1, y:2, z:0), (x:5, y:0, z:0)}은 분기 커버리지를 ~~만족하지 못한다.~~ ==> 만족한다.

- 분기 커버리지 ; 모든 선택 분기점을 파악하여, 두 개의 분기점들의 **참과 거짓** 또는 **거짓과 참** 조건을 모두 테스트

- (x:1, y:2, z:0)
  - x:1, y:2 ==> T, T
  - z = -1 ==> F

- (x:5, y:0, z:0)
  - x:5, y:0 ==> T, F
  - z = 0 ==> T

① ④과 동일.

② 기본 경로 갯수 = 내부영역의 갯수 + 외부영역1개 = P + 1(P;분기 노드의 수) = E - N + 2 = 3

③ (x:2, y:2, z:0)





---

## 19. 오픈 소스 도구와 기능을...

19. 
오픈 소스 도구와 기능을 연결한 것으로 옳지 않은 것은?![2017_7L_19](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_19.jpg)

**답 : ④**

④ JaCoCo - Java 코드의 커버리즈를 체크하는 라이브러리.

자바 소스 보안 취약점 분석 도구 - Juliet



---

## 20. 국제표준과 관련된 ...

20. 
국제표준과 관련된 내용으로 옳지 않은 것은?![2017_7L_20](/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_softwareeng/2017_7L/2017_7L_20.jpg)

**답 : ③**

③ IEC 62304 ; 의료 기기 소프트웨어의 인증.

항공기 소프트웨어 안전성 표준 - IEC 61508
