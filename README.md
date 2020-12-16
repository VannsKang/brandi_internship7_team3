# 안녕하세요! 브랜디 인턴십 7기 3팀입니다 <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">

>#### Trello Link https://trello.com/b/IuhnSddJ/%EB%B8%8C%EB%9E%9C%EB%94%94%EC%9D%B8%ED%84%B4-7%EC%B0%A8-3%ED%8C%80
>#### Github Link https://github.com/VannsKang/brandi_internship7_team3
>#### Google Slide Link https://docs.google.com/presentation/d/1CLYHCH_ac6gYLRRQ3STON8rJOTeIiwCaINFPClDm4yI/edit?usp=sharing
>#### Youtube Link https://youtu.be/v2FtKqPEr_A



![](https://www.brandi.co.kr/static/3.44.19/images/og-brandi.jpg)

## 👜 프로젝트 소개
>**브랜디**는 2014년 12월에 설립되어 모바일과 소셜미디어, 패션산업을 융합한 이커머스 모델을 개발 중인 패션 이커머스 스타트업입니다.
브랜디 인턴과정에서 쇼핑몰 [브랜디 어드민 관리페이지](https://admin.brandi.co.kr/)를 클론하는 프로젝트를 진행했습니다.

## 👜 프로젝트 참가자 (Front + Back)
![](https://user-images.githubusercontent.com/4216651/102052732-df8be280-3e29-11eb-86ef-be4e5f4ab8ab.jpg)

### 🧔🏻 FrontEnd
+ 강수명

### 🧑🏻👩🏻 BackEnd
+ 김동현 [Github 주소](https://github.com/Daphne-dev)
+ 성규원

## 👜 프로젝트 기간
2020.11. 16 ~ 2020. 12. 10 약 한달간 진행


## 👜 프로젝트 마일스톤
### 1주차 (초기 세팅)
* Frontend(강수명): Webpack Setup, Vue.js, Ant Design, Vuex Study
* Backend(김동현/성규원): Flask Study

### 2주차 (프/백 연결 테스트)
* Frontend(강수명): 로그인, 회원가입, 네비게이션 메뉴, 셀러 관리 페이지 구현
* Backend(김동현/성규원): 로그인, 회원가입, 셀러관리 API 구현 

### 3주차 (Cross)
* Frontend(김동현/성규원): Vue.js Study, 상품 관리, 셀러 수정 페이지 구현
* Backend(강수명): Flask Study, 상품 등록 API 구현

### 4주차 (최종)
* Frontend(강수명): 시나리오 점검 및 예외/에러 처리
* Backend(김동현/성규원): 상품 관리, 셀러 수정 API 구현

## 👜 기술 스택
### 🧔🏻  FrontEnd
+ HTML / CSS
+ JavaScript
+ Webpack
+ Vue.js
+ Vue Router
+ Vuex (Persist, Logger)
+ Ant Design
+ Sass
+ Axios
+ Moment
+ SweatAlert2

### 🧑🏻👩🏻 BackEnd
+ Python
+ Flask / Flask-Cors
+ MySQL
+ MySQL Workbench
+ PyJWT
+ Bcrypt
+ AWS S3


### 🤼‍♂️ 협업 도구
+ Slack
+ Git + GitHub
+ Trello를 이용해 일정관리 및 작업 현황 확인
+ Postman (API 관리)

## 👜 구현한 기능
>중간에 frontend, backend 포지션을 바꿔서 backend는 frontend 레이아웃을 frontend는 backend API endpoint를 구현하였습니다.

### 🧤 Frontnd

### 로그인/ 회원가입 🧔🏻
+ 로그인/회원가입 validator 구현
+ 관련 분기별 confirm 팝업 alert 구현
+ vuex persist 로 token 유지 및 체크
+ token 없을시 403 리다이렉트 구현

### 메인 메뉴 섹션 🧔🏻
+ 로그아웃 구현
+ token 있을시 login 화면에서 다시 메뉴화면으로 redirect
+ seller_status 유무 체크후 API 호출
+ menu_item, footer 전역 관리

### 셀러 리스트 🧔🏻
+ 페이지네이션 구현 (2개 동기화)
+ 페이지 그룹 구현
+ 테이블 개별 조건별 엔터 검색 구현
+ 테이블 복수 조건별 검색 및 리셋 구현
+ 날짜 조건 구현
+ 셀러 스테이터스 갱신구현(6가지 상태)
+ 셀러 상세 페이지 라우터 연결

### 셀러 상세 페이지 구현 🧑🏻 
+ 비밀번호 변경 모달창
+ 이미지 업로드 & 변경 & 삭제 

### 상품 리스트 페이지 구현 👩🏻
+ 날짜 조건 구현
+ 셀러 속성(7가지) 및 상품 상태(3가지) 필터 검색 구현
+ 셀러명, 상품번호, 상품코드, 상품번호 검색 기능 구현

### 🧤 Back End

### 셀러 리스트 페이지 🧑🏻 
+ 셀러 리스트 API 구현(컬럼 별 검색 기능 및 페이지네이션 기능) 
+ 셀러 속성 API 구현
+ 셀러 상태 API 구현
+ 엑셀 다운로드 API 구현

### 액션에 따른 셀러 상태 변경 🧑🏻 
+ 특정 액션을 취하면 그에 대한 셀러의 상태 변경 API 구현

### 셀러 상세 페이지 🧑🏻 
+ 셀러 정보 조회 및 수정 API 구현
+ AWS S3와 연동하여 이미지 업로드 구현

### 로그인 / 회원가입 API 구현 👩🏻
+ 계정 중복 확인 및 계정 생성 API 구현
+ jwt, bcrypt 를 이용한 토큰 발행 및 로그인 API 구현
+ 이메일, 비밀번호, 전화번호 정규화

### 상품 리스트 표출 API 구현  👩🏻
+ 회원 정보에 따른 상품 리스트 접근 가능 여부 구현
+ 조건 필터별 상품 리스트 표출 API 구현
+ AWS S3와 연동하여 이미지 표출 구현

### 상품 등록 페이지 API 구현 🧔🏻
+ color, size, 1st category API 구현
+ querystring 이용 2nd category 구현
+ 다중 테이블에 상품 등록 구현

