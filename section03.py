# section3
# 파이썬 가상환경 개념, 설정 및 pip 사용법, vscode 연동

# 패키지 검색 : pip search simplejson
# 패키지 설치 : pip install simplejson
# 패키지 삭제 : pip uninstall simplejson
# 설치된 패키지 리스트 : pip list
# 패키지 업그레이드 : pip install --upgrade simplejson

#외부 설치 패키지 테스트
import simplejson as json

test_dict = {'1':95, '4':77, '3':65, '5':100, '2':88}

#simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))