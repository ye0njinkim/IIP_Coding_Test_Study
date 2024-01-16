def solution(genres, plays):
    answer = []
    dic = {}

    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
        else:
            dic[genres[i]] += plays[i]

    dic = sorted(dic.items(), key=lambda x: -x[1])

    for genre, _ in dic:
        genre_songs = []
        for i in range(len(genres)):
            if genres[i] == genre:
                genre_songs.append((plays[i], i))
        genre_songs = sorted(genre_songs, key=lambda x: (-x[0], x[1]))
        
        for i in range(min(len(genre_songs), 2)):
            answer.append(genre_songs[i][1])
    
    return answer