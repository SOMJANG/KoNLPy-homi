import time
from pprint import pprint

import konlpy_homi

konlpy_homi.patch()
import konlpy

hannaum = konlpy.tag.Hannanum()
kkma = konlpy.tag.Kkma()
komoran = konlpy.tag.Komoran()
mecab = konlpy.tag.Mecab()
okt = konlpy.tag.Okt()

handlers = [hannaum, kkma, komoran, mecab, okt]


def main(handler, text):
    tic = time.perf_counter()
    handler.pos(text)
    toc = time.perf_counter()
    value = f"{toc - tic:0.4f}"
    return value


if __name__ == '__main__':
    text = """"2003년 중화권에서 인명피해를 냈던 중증 급성 호흡기 증후군인 사스와 유사한 증상을 보이는 환자 7명이 발생했다."라는 병원 문건을 얻게 된 중국 우한시중심병원 의사 리원량은 감염 확산 가능성을 우려하였고, 2019년 12월 30일, 동료 의사 7명과 함께 소셜 미디어(SNS)를 통해 위험 상황을 알리고 널리 전파하려 하였다. 그러나 중국 당국으로부터 "허위 정보를 퍼트려 민심을 불안하게 만들고 있다."며 "관련 사실을 계속 유포할 경우 체포당할 수 있다."는 통보를 받고 리씨를 포함해 동료 의사 등 8명이 공안국에 소환돼 잘못을 인정하는 자술서를 쓰고 서명을 하였다. 중국 당국은 2020년 1월 말에 이들에게 사과하였다. 리원량은 병원에서 환자들을 돌보다 1월 8일 발열 증상으로 정밀검사를 거쳐 2월 1일 확진 판정을 받고 입원 치료 중 2월 6일 병세가 급격히 악화되어 7일 오전에 사망했다. 우한시중심병원은 "의사 리원량씨가 이날 2월 7일 오전 2시 58분쯤 사망했다."고 밝히면서 "리원량이 신종 코로나 바이러스의 확산과 싸우다 불행히도 감염됐다."며 "우리는 매우 유감스럽게 생각하며 애도한다."고 했다. WHO(세계 보건 기구)도 트위터를 통해 애도의 뜻을 밝혔다.
2020년 1월 7일, CCTV는 우한에서 원인미상의 폐렴을 일으키는 이 병원체는 새로운 종류의 코로나바이러스라고 밝혔다. 이 바이러스의 완전 염기서열은 상하이공공위생임상센터(上海公共衛生臨床中心), 우한중심의원(武漢中心医院), 화중과기대학교(華中科技大学), 우한시질병예방공제센터(武漢市疾病予防控制中心), 시드니 대학 등의 협력에 의해 해독되어 시드니 대학의 에드워드. C. 홈즈 교수의 협력 아래 상하이공공위생임상센터의 장융전(張永振) 교수에 의해 2020년 1월 11일 Virological.org에서 공개되었다. 그 후 14일에는 국제핵산배열 데이터베이스 Genbank에 정식으로 공개되었다. 홍콩대학 미생물학과 감염증 전공 윈궉융 교수의 보고에 따르면, 이 바이러스와 다른 종의 코로나바이러스와 비교하면, 중국 저장성 저우산시 박쥐에서 발견된 SARS 바이러스와 가장 가깝고, 박쥐 SARS바이러스, 인간SARS바이러스, 사향고양이SARS바이러스와도 80% 가까이 유사성을 보인다.
바이러스 발원지로 여겨지는 화난수산시장(우한 시장)은 이름은 수산물시장이나 실제로는 다양한 야생동물도 처리 및 거래되고 있어서, 대나무쥐나 오소리 등의 야생동물이 감염원일 가능성도 높은 것으로 알려져 있다."""

    text2 = "ㅋㅋㅋ 이게 됨?"

    results = {
        hand: [] for hand in handlers
    }
    for _ in range(5):
        for hand in handlers:
            results[hand] += [main(hand, text2)]
    pprint(results)
    results = {
        hand: [] for hand in handlers
    }
    for _ in range(5):
        for hand in handlers:
            results[hand] += [main(hand, text)]
    pprint(results)
