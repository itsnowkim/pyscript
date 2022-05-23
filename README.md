> pyscript 라는 프레임워크가 있더라.<br>
파이썬이 돌아가는 것처럼 보이게만 하겠지~ 했는데 전혀 아니었다. 
**그냥 파이썬 인터프리터를 심어놓은거였다.**
그래서 파이썬으로 할 수 있는 모든 것을 할 수 있다고 보면 된다.<br>
이젠 파이썬만 할 줄 알면 진짜 못 만드는게 없겠다...!


## Hello world

당연히 헬로월드 찍어봐야지.
[pyscript getting-started](https://github.com/pyscript/pyscript/blob/main/docs/tutorials/getting-started.md)
여기 들어가서 코드 복붙해보자.
```html
<html>
  <head>
    <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  </head>
  <body>
    <py-script> print('Hello, World!') </py-script> 
  </body>
</html>
```
진짜 단순하다. 그냥 head 안에 저 한 줄 추가해주고,
파이썬 쓰고 싶은 곳에 가서 `<py-script>` 태그 사이에 `python` 문법으로 작성하면 된다.
css 적용하니까 좀 느려지는거같고 답답해서 뺐다.

![loading](https://velog.velcdn.com/images/n0wkim/post/911e0fdc-2ceb-4047-b45f-390e05d0900b/image.png)

처음에 이래 뜨더라. 생각보다 로딩이 좀 걸린다. 1~2초?

![hello world](https://velog.velcdn.com/images/n0wkim/post/64056f15-e06c-406e-860a-81e42b63dd33/image.png)
음 잘 나오네!

## 도대체 어디까지 잘할래

### 다른 파이썬 파일/패키지/모듈 가져올 수 있음

그리고 원하는 html element에 출력도 할 수 있다.
얘는 datetime 모듈 가져와서 시간 출력한거다. example에 있는거 그냥 그대로 했다.
![write specific html element](https://velog.velcdn.com/images/n0wkim/post/0a197940-15cb-4e9c-ace9-a6af2ea1779e/image.png)


> **근데 그냥 example만 돌릴거면 vscode 켠 의미가 없으니까 비슷한거 만들어보자.**

그래서 단순한 시계를 만들어 봤다. 그냥 만들면 의미 없으니까 `javascript`랑 `python` 이랑 비교해봤다.
```
<!DOCTYPE html>
<html>
  <head>
    <title>Js VS Python Clock</title>
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-env>
    - paths:
      - ./utils.py
    </py-env>
  </head>

  <body>
    <div >js clock time: <label id="jsClock"></label></div>
    <div >py clock time: <label id="pyClock"></label></div>

    <py-script>
import utils
import asyncio

async def foo():
  while True:
    await asyncio.sleep(1)
    output = utils.now()
    pyscript.write("pyClock", output)

pyscript.run_until_complete(foo())
    </py-script>
  </body>
</html>

<script>
  setInterval(()=>{
      var timer = new Date();
      var h = timer.getHours();
      var m = timer.getMinutes();
      var s = timer.getSeconds();
      document.getElementById('jsClock').innerHTML = `${h} : ${m} : ${s}`;
  },1000);
</script>
```

파이썬 코드

```python
from datetime import datetime as dt


def format_date(dt_, fmt="%H : %M : %S"):
    return dt_.strftime(fmt)


def now(fmt="%H : %M : %S"):
    return format_date(dt.now(), fmt)


def remove_class(element, class_name):
    element.element.classList.remove(class_name)


def add_class(element, class_name):
    element.element.classList.add(class_name)
```

코드가 겁나 쉽다. python 파일 만들고, 거기서 하고 싶은 모듈 만들고, html에서 그거 가져와서 쓰면 된다.

로직은 코드에서 알 수 있듯이 `js` 에서는 `settimeinterval`로 `Date()` 객체 가져와서 찍고, `python`에서는 `datetime` 모듈을 쓴다.

![simple_clock](https://velog.velcdn.com/images/n0wkim/post/2ac9d203-1136-4d9b-85ac-e10f3d93020a/image.gif)

결과는 **파이썬 시계가 조금 느렸다**. 아직 로딩 속도 이슈가 있다고 하던데, 그것 때문이 아닐까 한다. 그래도 `js` 에서 할 수 있는 것들은 이제 웬만한 것들은 `python` 에서 할 수 있다고 생각해도 되지 않을까 한다.

### ML할 때 너무 좋을듯

`js` 에도 물론 그래프 그리는 라이브러리가 있지만, 아무래도 `ML`할 때 다 파이썬을 쓰고, 워낙 생태계가 잘 되어 있어서 따라갈 수 없다. 단순한 plot을 보여줄 때나, 어떤 특정 앱의 프로토타입을 만들 때에 `python`을 써서 웹을 만들 수 있기 때문에 획기적으로 구현 속도가 올라갈 것 같다.

example에 있는 코드 돌려봤다.
![ml](https://velog.velcdn.com/images/n0wkim/post/586d787a-f84b-48a8-a3ed-02e9bafa1f1d/image.png)

대충 이렇게 나오는데, plot으로 scatter된 점들 찍어도 되고, 간단한 perceptron도 되더라.

근데 아무리 그래도 아직은 jupyter쓰는게 더 빠르고 좋아서 그냥 신기하네... 정도로 끝날 것 같다.

링크 들어가 보니까 deploy관련해서는 아직 제대로 된`Readme`도 작성되어 있지 않았고, 보안 이슈도 있고 성능 이슈도 있고 하니 좀 기다리라고 하더라. 

## 심심하니까 만든 장난감

언제나 믿음직스러운 니코쌤의 유튜브에 있는 간단한 코드로 먼저 어떻게 돌아가는지 확인했다. 실행하면 이렇게 된다. 자세한 코드는 깃허브 레포에 올려놨다. 
![simple game](https://velog.velcdn.com/images/n0wkim/post/099610f2-d2af-4f4b-9af2-56e0a31d4e4c/image.gif)

~~니코쌤... 근데 이거 이길 수 있는 거 맞죠?ㅎㅎ~~

여기서 끝내면 살~짝 아쉬우니까 근본 프로젝트 **Todolist** 도 빠르게 만들어 봤다.

![simple_todo](https://velog.velcdn.com/images/n0wkim/post/c5dd25ae-61f4-4b19-ba77-8e256dcd95d5/image.gif)

뭐... 추가만 되도록 했고, 수정, 삭제는 안했다. **더 이상은 맛보기가 아니니까**...

이거 만드는데 은근히 시간 많이 썼다. 로직 자체가 어렵다기보다 **에러를 잘 안알려주고**, **refresh 하는데 오래 걸린다**.

또, 아직 알파버전이라고 한다. 그래서 그런지 **콘솔창에 엄청나게 많은 로그**들이 실행만 해도 찍히는데, 대충 웹 어셈블리로 파이썬 코드를 해석했다~ 이제 실행해봐라~ 뭐 이런 말을 해준다.

직접 element에 접근해서 dom을 바꾸는 형식이다 보니까 내부 attribute를 알아야 되는데, 삽질을 중간에 했고, 일일히 element 내부 속성 하나하나 보면서 코딩하느라 오래 걸렸다.

> 
그래도 `python`으로 이렇게 만들 수 있다는 것 자체가 재미있는 점 같다.
진짜 조금만 더 시간이 지나면 강력한 프레임워크가 또 나와서 `python` 이 모든 것을 압도하게 되지 않을까...?

## 참고 링크

> 
자세한 원리를 알고 싶다?
https://anaconda.cloud/pyscript-python-in-the-browser
여러 데모들을 보고 싶다?
https://pyscript.net/examples/
한번 따라해 보고 싶다?
https://github.com/pyscript/pyscript
레포가 궁금하다?
https://github.com/itsnowkim/pyscript
니코쌤의 유튜브가 궁금하다?
https://www.youtube.com/watch?v=3DuyJf_XPtM&t=297s
![](https://velog.velcdn.com/images/n0wkim/post/e62e5802-c938-48d2-b91a-a0b0285e7575/image.png)

_근데 `picocss` 처음 써봤는데 너무좋다야..._
