# Project : CNDB (Cheese Nacho Database)

2022-03-14 MultiCampus 인터페이스 개발 프로젝트 2등



## 01. Purpose

IMDB 라는 해외 Media 포털사이트를 보고, 한국식 Media 포털 사이트를 구현하기로 한다.

한국형 Movie, Drama 를 통합한 평점사이트 구현



## 02. Tools

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) 

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

[TMDB API](https://www.themoviedb.org/?language=ko)



## 03. File Introduction

**폴더 내용 소개**

```bash
├── cndb 			# project main
├── mntmt_info		# project import, orm
│   ├── data		# base web page data
│   ├── models		# Movie, Series, Genre original data
│   ├── views		# import, orm 등 전체적인 기능을 담당		
│   └── templates	# main 페이지, 검색결과 페이지등
├── entmt_manage
│   ├── models		# Movie, Series의 Comment, Genre
│   └── views		# like 등 Movie, Series의 부가 정보 기능 담당
├── users
│   ├── models		# Member,  Member의 like, genre
│   ├── views		# Member의 전체적인 정보 기능 담당
│   └── templates	# userpage, login page 등
└── templates		# base.html, navbar.html
```

**models 소개**

| Movie         | Series         | Genres |
| ------------- | -------------- | ------ |
| m_id          | s_id           | g_id   |
| m_title0      | s_title        | g_name |
| m_posterPath  | s_posterPath   |        |
| m_likeCount   | s_likeCount    |        |
| m_releaseDate | s_firstAirDate |        |
| m_popularity  | s_lastAirDate  |        |
|               | s_popularity   |        |

| class Members | class Mlike  | class Slike   | class Ugenres |
| ------------- | ------------ | ------------- | ------------- |
| u_mobile      | ml_user (F)  | sI_user(F)    | ug_user (F)   |
| u_image       | ml_movie (F) | sl_series (F) | ug_genre (F)  |

| class Mcomment | class Scomment | class Mgenres | class Sgenres |
| -------------- | -------------- | ------------- | ------------- |
| mc_star        | sc_star        | mg_movie (F)  | sg_series (F) |
| mc_content     | sc_content     | mg_genre (F)  | sg_genre (F)  |
| mc_user (F)    | sc_user (F)    |               |               |
| mc_movie (F)   | sc_series (F)  |               |               |
| mc_date        | sc_date        |               |               |

## 04. Function

#### A. 주요 기능

1. API 활용 영화 순위, 세부 내용 제공
2. 회원가입 및 인증 후 별점, 리뷰 등록 등 댓글 기능 구현
3. 사용자 별 선호 장르를 참고한 영화 추천
4. 영화제목 검색 기능 (API)

#### B. 세부기능

**TNDB api** : 영화 정보 검색 api 제공 사이트

- 영화(시리즈) 고유번호 다운로드 api
- 장르 목록 다운로드 api
- 영화(시리즈) detail 다운로드 api
- 단어 검색 api

**import data**

- 페이지 구동 시 기본적으로 필요한 장르 다운로드 기능
- 페이지 구동 시 기본적으로 필요한 영화/시리즈 정보 다운로드 기능

**navbar**

- 로고 클릭 시 home으로 이동
- 팝업폼을 이용한 로그인, 로그아웃, 사인업 기능
- mypage를 클릭 시 mypage로 이동
- 검색기능을 사용하여 영화(시리즈) 검색 

**main page**

- (맨 윗쪽 슬라이더) 영화, 시리즈 (popularity기준) 인기순위로 출력(장르 함께 출력)
- (아랫쪽 슬라이더, 탭) 회원가입 시 선택한 장르별 인기 영화 추천 기능 

**research page**

- 검색어를 입력해서 관련 영화, 시리즈 검색결과(평균 별점 포함) 출력
- 영화(시리즈)의 제목, 포스터를 클릭 시 detail 페이지로 이동

**detail page**

- 영화(시리즈)의 제목, 포스터를 클릭하면 영화의 세부 사항을 출력
- 영화(시리즈) 좋아요 기능 (로그인 시 활성화)
- 영화(시리즈)의 리뷰, 별점 등록/수정/삭제 기능 (로그인 시 활성화)
- 별점을 통계내어 각 영화(시리즈)의 평균 별점을 보여줌
- 로그인한 회원의 리뷰와 다른 회원들의 리뷰를 구분해서 보여줌(모든 리뷰를 볼 때는 로그인한 회원의 리뷰가 가장 위에 오도록 구현)

**mypage** (로그인 시 활성화)

- favorite media : 내가 좋아요한 영화 목록 출력
- my ratings : 내가 작성한 리뷰 목록 출력
- profile : 프로필 이미지 설정(css로 커스텀, files 형식), 회원정보 업데이트(폼 형식으로 전달 후 저장)
- my preference : 최초 회원가입 시 선호 장르 선택, 이후 업데이트 가능
- change password : 사용자에게 변경할 비밀번호 입력받은 후 유효성 검증 실행

## 05. 구동화면

