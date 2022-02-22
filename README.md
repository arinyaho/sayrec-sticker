# sayrec-sticker
MP3 파일 이름을 세이렉 스티커 번호에 맞게 변경하는 파이썬 스크립트

## 이게 무엇인가요
* 세이렉 스티커를 사용하기 위해서는 스티커 번호에 맞게 MP3 파일 이름을 바꿔서 세이펜의 sayrec 디렉토리에 복사해야 합니다.
* 세이렉 스티커의 파일 이름 규칙이 간단하지 않고, A, B, C 종류에 따라, 그리고 스티커 번호에 따라 차이가 납니다.
* 전집 등 수 십개의 많은 오디오북의 MP3 파일을 수작업으로 처리하는 것은 매우 고된 일입니다.
* 이 `Python` 스크립트는 디렉토리 안에 정렬된 MP3 파일들을 세이렉 스티커 규칙에 맞게 자동으로 변환합니다.
* 육퇴하고도 세이렉 야간작업을 하시는 수많은 엄마, 아빠에게 도움이 되었으면 좋겠네요. :)

## 사용 방법

### 필요한 것들
* [python3](https://www.python.org/downloads/)  

### 옵션
```
--side, -s               세이렉 스티커 종류. {A, B, C} 중 하나
--index, -i              변환할 MP3 파일들의 세이렉 스티커 시작 번호
--dir, -d                변환할 MP3 파일들이 위치한 디렉토리(폴더)
--limit, -l              변환할 MP3 파일들의 개수
--prefix-include, -p     변환할 MP3 파일 이름의 접미사
                         예) -p wayland : wayland로 시작하는 MP3 파일만 변환
--prefix-exclude, -q     변환하지 않을 MP3 파일 이름의 접미사
                         예) -q SAY50 : SAY50으로 시작하는 MP3 파일은 변환하지 않음
```

### Windows 사용 예시
바탕화면에 있는 wayland 디렉토리에 있는 MP3 파일 중 SAY로 시작하지 않는 파일들에 세이렉 스티커 번호를 C의 1121번부터 부여
```cmd
C:\Users\love> python sayrec.py -s c -i 1121 -d c:\Users\love\Desktop\wayland -q SAY
```
