"""
마지막 문자를 제외하고 모든것을 출력하기 위해서 라인 슬라이싱을 할수 있지만 더 간단한 방법은 문자열 오른쪽 끝에서부터 공백을 벗겨내는 rstrip
메소드를 사용하는 것이다.
"""

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

