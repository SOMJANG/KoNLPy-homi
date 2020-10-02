
from grpc_requests import Client

if __name__ == '__main__':
    client = Client.get_by_endpoint("localhost:50051")
    print(f"support service : {client.service_names}")
    text = ''

    okt_svc = client.service('konlpy_homi.v0alpha.Okt')
    print(okt_svc.Pos({"payload":"'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'"}))

    hannanum_svc = client.service('konlpy_homi.v0alpha.Hannanum')
    print(hannanum_svc.Analyze({"payload": "'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'"}))
