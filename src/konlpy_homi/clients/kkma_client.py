from .base import KonlpyClient, make_join_able_return, make_request


class KkmaClient(KonlpyClient):  # TODO: Async call method needed?
    service_name = 'konlpy_homi.api.v0alpha.Kkma'

    def pos(self, phrase, **options):
        resp = self._service.Pos(make_request(phrase, options=options))
        return make_join_able_return(resp['results'], resp.get('options'))

    def nouns(self, phrase):
        return self._service.Nouns(make_request(phrase)).get('results', [])

    def morphs(self, phrase):
        return self._service.Morphs(make_request(phrase)).get('results', [])

    def sentences(self, phrase):
        return self._service.Sentences(make_request(phrase)).get('results', [])
