# Project : CNDB (Cheese Nacho Database)

2022-03-14 MultiCampus 인터페이스 개발 프로젝트 2등



## 01. Project 목적

IMDB 라는 해외 Media 포털사이트를 보고, 한국식 Media 포털 사이트를 구현하기로 한다.

한국형 Movie, Drama 를 통합한 평점사이트 구현



## 02. Project 개요

**사용 툴, 언어**

Pycharm, Python, Django, JavaScript, HTML, CSS, BootStrap

TMDB API



## 03. 파일 소개

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

## 04. 주요 기능

1. API 활용 영화 순위, 세부 내용 제공
2. 회원가입 및 인증 후 별점, 리뷰 등록 등 댓글 기능 구현
3. 사용자 별 선호 장르를 참고한 영화 추천
4. 영화제목 검색 기능 (API)