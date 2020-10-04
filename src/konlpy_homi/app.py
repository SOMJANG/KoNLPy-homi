from homi import App, Server
from homi.extend.service import health_service, reflection_service

from services.hannanum import hannanum_svc
from services.kkma import kkma_svc
from services.komoran import komoran_svc
from services.mecab import mecab_svc
from services.okt import okt_svc


app = App(
    services=[
        reflection_service,
        health_service,
        okt_svc,
        mecab_svc,
        kkma_svc,
        hannanum_svc,
        komoran_svc,
    ]
)

if __name__ == '__main__':
    server = Server(app)
    server.run()
