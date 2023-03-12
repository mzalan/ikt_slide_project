from Globals import *
from Upgrade import *

def GameOver():
    if not r.dead:
        r.dead = True
        r.Coins += r.gamecoins
        ujLista = []
        with open('progress.txt') as f:
            line = f.readline()
            c = 1
            while line:
                if line.strip().split(":")[0] == "coins":
                    frissit = int(line.strip().split(":")[1]) + r.gamecoins
                    ujLista.append(f"coins:{frissit}")

                    print(frissit)
                else:
                    ujLista.append(line.strip())
                line = f.readline()
                c += 1
        f.close()
        fa = open("progress.txt", "w", encoding="utf-8")
        for i in range(len(ujLista)):
            fa.write(f"{ujLista[i]}\n")
            print(ujLista[i])
        fa.close()

    if r.Points > r.Best:
        gover_text = r.gover_font.render("NEW HIGH SCORE", True, "#5800d4")

        score_text1 = r.first_font.render("SCORE", True, "#6b0101")
        score_text2 = r.gover_font.render(str(round(r.Points,0)).split('.')[0], True, "#6b0101")

        score_rect1 = score_text1.get_rect(center=(960,400))
        r.screen.blit(score_text1,score_rect1)

        score_rect2 = score_text2.get_rect(center=(960,490))
        r.screen.blit(score_text2,score_rect2)

    else:
        gover_text = r.gover_font.render("GAME OVER", True, "red")

        score_text1 = r.first_font.render("SCORE", True, "black")
        score_text2 = r.score_font.render(str(round(r.Points,0)).split('.')[0], True, "black")

        score_rect2 = score_text2.get_rect(midright=(890,470))
        r.screen.blit(score_text2,score_rect2)

        score_rect1 = score_text1.get_rect(center=(score_rect2.x+score_rect2.width/2,400))
        r.screen.blit(score_text1,score_rect1)

        best_text1 = r.first_font.render("BEST", True, "black")
        best_text2 = r.score_font.render(str(round(r.Best,0)).split('.')[0], True, "black")

        best_rect2 = best_text2.get_rect(midleft=(1030,470))
        r.screen.blit(best_text2,best_rect2)

        best_rect1 = best_text1.get_rect(center=(best_rect2.x+best_rect2.width/2,400))
        r.screen.blit(best_text1,best_rect1)

    gover_rect = gover_text.get_rect(center=(960,240))
    r.screen.blit(gover_text,gover_rect)



    coin_text1 = r.small_font.render("COINS COLLECTED", True, "#856e1c")
    coin_text2 = r.score_font.render(str(round(r.gamecoins,0)).split('.')[0], True, "#856e1c")

    coin_rect1 = coin_text1.get_rect(center=(960,620))
    r.screen.blit(coin_text1, coin_rect1)

    coin_rect2 = coin_text2.get_rect(center=(960,680))
    r.screen.blit(coin_text2, coin_rect2)


    again_text = r.first_font.render("PRESS R TO PLAY AGAIN", True, "black")
    again_rect = again_text.get_rect(center=(960,860))
    r.screen.blit(again_text,again_rect)

    color_light = (170,170,170)
    color_dark = "#111112"
    width = r.screen.get_width()
    height = r.screen.get_height()
    mouse = pygame.mouse.get_pos()


    back_text = r.score_font.render("Back", True, "black")
    back_rect = back_text.get_rect(center=(400,870))

    back_draw_surf = pygame.Surface((200,80))
    back_draw_rect = back_draw_surf.get_rect(center=(400,870))

    #back gomb

    if back_draw_rect.x <= mouse[0] <= back_draw_rect.x+back_draw_rect.w and back_draw_rect.y <= mouse[1] <= back_draw_rect.y+back_draw_rect.height:
        drawing = pygame.draw.rect(back_draw_surf, color_light, back_draw_rect)

        back_draw_surf.fill("#f5eeda")
        r.screen.blit(back_draw_surf, drawing)

        back_text = r.score_font.render("Back", True, "black")
        back_rect = back_text.get_rect(center=(400,870))
        if r.click:
            Menu()
    else:

        drawing = pygame.draw.rect(back_draw_surf, "black",back_draw_rect)
        r.screen.blit(back_draw_surf, drawing)

        back_text = r.score_font.render("Back", True, "white")
        back_rect = back_text.get_rect(center=(400,870))
    
    r.screen.blit(back_text, back_rect)