import  konlpy_homi
konlpy_homi.patch()
import konlpy

if __name__ == '__main__':
    print(konlpy.tag.Okt().normalize('노멀라이즈 테스트 가늨ㅋㅋㅋㅋ ㅋㅋㅋㅋ'))
