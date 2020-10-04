# KoNLPy-homi
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/konlpy-homi?style=flat-square)](https://pypi.org/project/konlpy-homi)
[![PyPI](https://img.shields.io/pypi/v/konlpy-homi?style=flat-square)](https://pypi.org/project/konlpy-homi)
[![PyPI download month](https://img.shields.io/pypi/dm/konlpy-homi?style=flat-square)](https://pypi.org/project/konlpy-homi)
![Views](https://views.whatilearened.today/views/github/wesky93/konlpy-homi.svg)

[KoNLPy-grpc](https://github.com/minhoryang/KoNLPy-gRPC)을 homi 기반으로 리펙토링한 프로젝직트 입니다.
또한 무료로 기본 grpc 서버를 제공하고 있습니다.
그래서 학습을 목적으로 konlpy를 사용 하시는 분들이라면 로컬에서 grpc 서버 혹은 jvm 구동 없이 바로 konlpy를 사용 할 수 있습니다.


## Remote Client
### install konlpy-homi
```bash
pip install konlpy-homi
```

### patch & ues it!
```
import  konlpy_homi
# if you want connect other server
# konlpy_homi.set_endpoint('localhost:50051')
konlpy_homi.patch()
 
import konlpy

# use it same as konlpy
print(konlpy.tag.Hannanum().analyze('노멀라이즈 테스트 가늨ㅋㅋㅋㅋ ㅋㅋㅋㅋ'))
```


## 왜 무료 서버를 제공하나요?
이 프로젝트는 [homi](https://github.com/spaceone-dev/homi) 프레임워크 및 [grpc_requests](https://github.com/spaceone-dev/grpc_requests)가 실제로 쓰기 편하고 성능 적으로 문제 없는지 확인하기 위해 시작하였습니다.
참고로 GCP CloudRun으로 서비스 중이기에 실제 운영 비용은 거의 나가지 않아 저 역시 거의 무료로 서비스를 제공가능합니다.

## 맘놓고 써도 되나요?
현재는 별도의 요청 제한을 걸지 않았습니다. 다만, 트래픽이 폭증 할 경우 향후에는 요청 제한(ex. ip별 하루 최대 5000회 요청 가능)이 걸릴수도 있습니다.

## 로컬보다 속도가 느린거 같아요..
서버리스로 구축된 서버이기에 최초 요청시 cold start가 발생 할 수 있습니다. 그 외에는 아래와 같은 몇가지 요인이 있습니다.
1. 로컬에서 직접 구동하는 것과 달리 서버와 데이터를 주고 받다보니 네트워크 환경에 영향을 받습니다.
2. 현재 GCP Cloud Run은 서울리전이 아닌 도쿄 리전을 지원 하다보니 이에 대한 레이턴시가 존재합니다.(향후 서울 리전에 cloud run이 출시하면 이전할 예정입니다.)
3. 서버 최적화 이슈(cpu,memory, 서버리스 특유의 Cold start)

현재 최대한 로컬과 그 간격을 줄이기 위해 지속적으로 서버를 개선해 나갈 예정입니다.
하지만, 속도가 느리다고 완전히 효용성이 없는 것은 아닙니다. 처음 자연어 처리를 공부,가르치시는 분들은 별도의 추가적인 설치 없이 바로 konlpy를 사용할 수 있습니다.
또한 저사양 컴퓨터, AWS 람다, 라즈베리파이등 konlpy를 직접 구동하기 힘든 환경이나 멀티프로세스로 여러 분석을 동시에 시도하는 경우에 네트워크 연결만 되있다면 기존과 동일한 코드를 가지고 개발, 서비스가 가능합니다.
참고로 현재 Cloud Run 사양은 CPU 2, Memory 1.5G 입니다. 지속적인 최적화를 통해 서버 사양이 변경될순 있습니다.

## 프로덕션에서 사용 해도 되나요?
가능하면 학습 및 개발단계에서 사용하길 권해드립니다. 위에 말씀드렸다 시피 도쿄 서버이기에 레이턴시가 발생합니다.
또한 언제는든지 요청 제한이 생길수 있기에 프로덕션에선는 도커로 별도의 전용서버를 구축하시는것을 권장합니다.
(향후 helm기반으로 서버 구축 할수 있도록 지원할 예정입니다.)

## 요청이 기록 되나요?
Cloud Run에서 기록 하는 기본적인 요청정보 이외에는 그 어떠한 요청 정보(어떤 텍스트를 분석 요청했는지)도 별도로 기록&보관하지 않습니다.
기본 적인 요청 정보에는 요청자의 ip 요청 서비스 정도만 기록됩니다. 이는 디버깅 및 향후 요청 제한 기능 구축에 제한적으로 활용 될 수 있습니다.

## run own Server
```bash
python -m venv .venv
. ./.venv/bin/activate
pip install -r requirements-dev.txt
cd src && homi run konlpy_homi/app.py
```

## Make Stubs
```bash
python -m grpc_tools.protoc -I protos/ --python_out=src/ --grpc_python_out=src/ protos/konlpy_homi/api/*/*.proto
```

## Additional Links
- [KoNLPy/KoNLPy](https://github.com/konlpy/konlpy)
- [minhoryang/KoNLPy-gRPC](https://github.com/minhoryang/KoNLPy-gRPC)
- [spaceone-dev/homi](https://github.com/spaceone-dev/homi)
- [spaceone-dev/grpc_requests](https://github.com/spaceone-dev/grpc_requests)


## License
GNU GPLv3
