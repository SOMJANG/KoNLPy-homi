# KoNLPy-homi
Redesigned KoNLPy (Wrapper) for Usability and Portability with gRPC(Homi).

## Requirements:
```bash
pip install requirements-dev.txt
```


## Server
```bash
cd src && homi run
```

## Make Stubs
```bash
python -m grpc_tools.protoc -I protos/ --python_out=src/ --grpc_python_out=src/ protos/konlpy_homi/api/*/*.proto
```

## Additional Links
- [KoNLPy/KoNLPy](https://github.com/konlpy/konlpy)
- [minhoryang/KoNLPy-gRPC](https://github.com/minhoryang/KoNLPy-gRPC)


## License
GNU GPLv3
