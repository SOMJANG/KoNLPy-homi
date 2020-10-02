from .base import KonlpyClient, make_double_list_tuple_return, make_join_able_return, make_request


class HannanumClient(KonlpyClient):  # TODO: Async call method needed?
    service_name = 'konlpy_homi.api.v0alpha.Hannanum'
    def analyze(self, phrase):
        resp = self._service.Analyze(make_request(phrase))
        return make_double_list_tuple_return(resp.get('results', []))

    def pos(self, phrase, **options):
        resp = self._service.Pos(make_request(phrase, options=options))
        return make_join_able_return(resp['results'], resp.get('options'))

    def nouns(self, phrase):
        return self._service.Nouns(make_request(phrase)).get('results', [])

    def morphs(self, phrase):
        return self._service.Morphs(make_request(phrase)).get('results', [])
