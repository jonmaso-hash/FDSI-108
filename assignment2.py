#list
anime_list = ["Neon Genesis", "Attack on Titan", "When they Cry"]
print(anime_list)

print(anime_list[2])

anime_list[2] = "Gundam"
print(anime_list)

anime_list.remove("Attack on Titan")
print(anime_list)

print(len(anime_list))

#dictionary
video_game ={
    "name": "Megaman",
    "system": "Nintendo",
    "year": 2000
}
print(video_game)
print(video_game["name"])

video_game["game"] = "Mario 64"
print(video_game)

video_game.pop("game")
print(video_game)

print(len(video_game))
