# KoNLPy-homi
Redesigned KoNLPy (Wrapper) for Usability and Portability with gRPC(Homi).

## Requirements:
```bash
pip install poetry
pip install -r $(python manage.py requirements.txt) -r $(python manage.py requirements-dev.txt)
```

## gRPC Compile needed!
```bash
python -m grpc_tools.protoc -I protos/ --python_out=konlpy_grpc/_generated/ --grpc_python_out=konlpy_grpc/_generated/ protos/*.proto
```

## Server
```bash
python -m pip install konlpy
```

```bash
python -m konlpy_grpc server
python -m konlpy_grpc hannanum_server
python -m konlpy_grpc kkma_server
python -m konlpy_grpc komoran_server
python -m konlpy_grpc mecab_server
python -m konlpy_grpc okt_server
```

## Tests
```bash
python -m pytest
python -m pytest --grpc-fake-server
python -m pytest --grpc-real-server=[::]:50051
python -m pytest --konlpy-repo=../konlpy
```

## Release
```bash
rm -rf dist/
poetry publish --build -r test
poetry run twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```


## Additional Links
- [KoNLPy/KoNLPy](https://github.com/konlpy/konlpy)
- [Pruned KoNLPy v0.5.2-rc.1](https://github.com/minhoryang/konlpy)
  - Currently, servers rely on KoNLPy v0.5.2 version.

## License
GNU GPLv3
