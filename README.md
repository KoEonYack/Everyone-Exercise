#  국민의 운동
------------
제작일 : 19.08.23 - 19.08.24


## 서비스 개요
우리나라 국민의 기대 수명은 증가하나 저출산으로 인하여 청년 1인당 부양 인구의 비율이 높아지고 있습니다. 국민들의 주변에 많은 운동 시설이 있다는 것을 알리고, 많은 체육 행사가 있다는 것을 알리어 생활속에 운동이 스며들어 건강한 삶을 살 수 있게 돕는 것을 목표로 합니다. 이를 통해 장기적으로 1인당 의료비를 줄이는 것을 목표로 합니다.

## 서비스 구성 

### [1] 메인 화면
![main](./img/main.jpg)


### [2] 우리 지역 운동시설 
![1-1](https://github.com/KoEonYack/Everyone-Exercise/blob/master/img/1_1.JPG)
[서울시 공공체육시설 현황](http://data.seoul.go.kr/dataList/datasetView.do?infId=OA-1115&srvType=S&serviceKind=1&currentPageNo=1)의 CSV파일의 정보의 일부를 데이터베이스에 저장했습니다. 

![1-2](https://github.com/KoEonYack/Everyone-Exercise/blob/master/img/1_2.JPG)
체육 시설을 선택하면 다음과 같은 페이지가 나옵니다.(50%로 축소) 별점과 코멘트를 작성할 수 있습니다. 이를 통해 해당 시설이 어떤지 평을 하여 추후에 이용하는 사람들에게 정보를 제공해 주며, 시설 관리자들이 해당 시설을 개선하는데 여론 수렴의 역할을 할 것입니다. 


### [3] 함께 운동해요
![2-1](https://github.com/KoEonYack/Everyone-Exercise/blob/master/img/2_1.JPG)
운동할 사람을 모집하기 위해 지역 단톡방 혹은 동호회에서 모집합니다. 이는 체계적으로 모집하기 힘듭니다. 이러한 문제를 해결하고자 함께 운동할 사람을 모집할 수 있는 페이지입니다. 

![2-2](https://github.com/KoEonYack/Everyone-Exercise/blob/master/img/2_2.JPG)
게시글을 클릭하면 다음과 같은 페이지가 나옵니다. 덧글을 iMessage와 유사하게 디자인함으로 마치 체팅방에서 대화를 나누는 경험을 선사합니다. 

### [4] 우리지역 행사
![3-1](https://github.com/KoEonYack/Everyone-Exercise/blob/master/img/3_1.JPG)
지역에는 크고 작은 수 많은 행사가 열립니다. 다만 관심이 없으면 그냥 지나가버리기 마련입니다. 이러한 문제를 해결하고자 한번에 행사를 모아서 보는 페이지를 제작하였습니다. 메트로 UI와 보여지는 정보를 최소화 함으로써 한 눈에 보여주고자 하였습니다. 


### [5] 운동량 계산
![4-1](https://github.com/KoEonYack/Everyone-Exercise/blob/master/img/4_1.JPG)
자신이 먹은 음식을 선택할 수 있습니다. 

![4-2](https://github.com/KoEonYack/Everyone-Exercise/blob/master/img/4_2.JPG)
하고 싶은 운동과 몸무게를 입력하면 자신이 먹은 음식의 칼로리를 소모하기 위해서 얼마만큼의 운동을 해야 하는 지 알려줍니다.  

### [5] 계정

![login](https://github.com/KoEonYack/Everyone-Exercise/blob/master/img/login.JPG)
로그인 페이지 

![register](https://github.com/KoEonYack/Everyone-Exercise/blob/master/img/register.JPG)
회원가입 페이지


## 실행 방법
사전에 Python과 Django가 설치되어 있어야 합니다.  

``` cmd
pip install -r requirements.txt
python manage.py collectstatic
python manage.py runserver
```


## 버전 정보
- pip: 19.0.3
- python: 3.7.4
- Django: 2.2.4
- Bootstrap: 4.3.1
