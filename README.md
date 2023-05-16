# ddt


### 파이썬 환경 설정
``` bash
cd backend/jyp # backend root directory 이동

python -m venv venv # virtual environment 구성

source venv/Script/activate # activate virtual environment

python -m pip install --upgrade pip # upgrade pip

pip install requirements.txt # 패키지 설치

# 만약 추가해야할 패키지가 있다면 
pip freeze > rquirements.txt
```
--------------------------------------------------------------------------------------------

### vscode 디버깅 환경 세팅
``` bash
cd backend/jyp # backend root directory 이동

mkdir .vscode

cd .vscode

vim launch.json # 아래 script 작성 후 저장
```


> launch.json
``` json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/jyp/manage.py",
            "args": [
                "runsslserver",
                "포트번호지정"
            ],
            "django": true
        }
    ]
}
```
--------------------------------------------------------------------------------------------

### 제공 API (추가 예정)
1. 잡 포스팅 전체 조회
- /list_post/

2. 잡 포스팅 조회
- /detail_post/<int:post_id>/

3. 키워드로 잡 포스팅 조회
- /search_post?keyword=/

4. 유저 직무 정보 기반 잡 포스팅 추천
- /recommand_by_job/

5. 유저 log(view) 기반 잡 포스팅 추천
- /recommand_by_view_log/

6. 유저 log(search) 기반 잡 포스팅 추천
- /recommand_by_search_log/

7. 키워드 팔로우 기반 잡 포스팅 추천
- /recommand_by_follow/
