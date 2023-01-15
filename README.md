# GFriend Lyrics Frequency


<img src="https://user-images.githubusercontent.com/76632760/212512187-f008afb4-7363-4c55-a83a-65c66f5ab9bf.png" alt="GFriend" width="700"/>



[GFriend (여자친구)](https://www.youtube.com/watch?v=r_6q_-d-7Sk&list=PLWqQwarHaCFesi5VUhT4w8FJ2X4hE1AEu&index=14) was a Korean girl group that produced music between 2015 and 2021. I was a huge fan during high school. I was listening to some of their old songs today, and I started to wonder what the most common words were. It seems to me that most KPop uses the same basic personal pronouns and love-related phrases quite often. I used the LyricsGenius client to access the Genius.com API, which made it easy to grab the lyrics to 50 of GFriend's songs and analyze them. This data is not particularly shocking, but it was interesting. I have added my translation of each word in parentheses--the English words with no Korean appeared in English originally.


Areas for improvement:

- I had to hardcode the words to be excluded but was not 100% accurate (note that "&" was included as a common word)

- I tried to make a graph with MatPlotLib, but it got caught up on the fact that most of the words are, obviously, written with Hangul... I think the only way to fix this would be to have users download a Korean font and import it but perhaps there is something better.

- I just grabbed the first 50 non-instrumental songs on Genius, which included Japanese songs by GFriend... this could affect the data. I think the Japanese songs use a little more English possibly.

- Unsurprisingly, the song "Memoria," which says that word over and over, caused it to skyrocket in frequency.

```
Top 30 Most Common Words in GFriend Songs:
내 (My): 104
더 (More): 73
날 (Me+Object Particle): 61
이 (This): 60
그 (That): 58
You: 54
might: 50
also: 50
너의 (Your): 47
거야 (Particle used to form the future tense): 46
널 (You+Object Particle): 46
나를 (Me+Object Particle): 45
수 (Depends on the context, but I would guess it's from verb+ㄹ+수+있다, which means "to have the ability to do verb"): 41
me: 40
맘 (Heart): 39
내게 (To me): 39
yeah: 38
나의 (My): 36
있어 (There is/you have/I have): 35
my: 35
I: 35
너를 (You+Object Particle): 34
봐 (Sees (indicative) or Look (imperative)): 34
Memoria: 32
나 (I): 31
&: 31
you: 31
다 (All): 30
네 (You): 30
저 (I (Polite Form)): 30
```

```
List of songs used:
Song 1: "밤 (Time For The Moon Night)"
Song 2: "MAGO"
Song 3: "귀를 기울이면 (Love Whisper)"
Song 4: "여름비 (SUMMER RAIN)"
Song 5: "今日から私たちは (Me Gustas Tu) -JP ver.-"
Song 6: "해야 (Sunrise)"
Song 7: "Love Whisper -JP ver.-"
Song 8: "너 그리고 나 (NAVILLERA)"
Song 9: "그루잠 (FALLING ASLEEP AGAIN)"
Song 10: "오늘부터 우리는 (Me Gustas Tu)"
Song 11: "바람의 노래 (Hear the Wind Sing)"
Song 12: "시간을 달려서 (Rough)"
Song 13: "FINGERTIP"
Song 14: "Memoria"
Song 15: "RAINBOW"
Song 16: "トキヲコエテ (Rough) -JP ver.-"
Song 17: "여름여름해 (Sunny Summer)"
Song 18: "열대야 (Fever)"
Song 19: "Bye"
Song 20: "Love Bug"
Song 21: "Apple"
Song 22: "유리구슬 (Glass Bead)"
Song 23: "NAVILLERA -JP ver.-"
Song 24: "Glass Bead -JP ver.-"
Song 25: "FLOWER"
Song 26: "두손을모아 (AVE MARIA)"
Song 27: "교차로 (Crossroads)"
Song 28: "이분의 일 1/2 (ONE-HALF)"
Song 29: "Labyrinth"
Song 30: "휘리휘리 (Flower Garden)"
Song 31: "Better Me"
Song 32: "나의 지구를 지켜줘 (Please Save My Earth)"
Song 33: "Memoria (Korean Version)"
Song 34: "별 (You are my star)"
Song 35: "봄비 (Rain in the Spring Time)"
Song 36: "LIFE IS A PARTY"
Song 37: "You are not alone"
Song 38: "틱틱 (Tik Tik)"
Song 39: "Night Drive"
Song 40: "비행운:飛行雲 (Contrail)"
Song 41: "Wanna Be"
Song 42: "La pam pam"
Song 43: "빨간우산 (RED UMBRELLA)"
Song 44: "거울의 방 (Room of Mirrors)"
Song 45: "Love Spell"
Song 46: "Secret Diary"
Song 47: "Three of Cups"
Song 48: "GRWM"
Song 49: "SUNRISE -JP ver.-"
Song 50: "눈의 시간 (Eye of the Storm)"
```
