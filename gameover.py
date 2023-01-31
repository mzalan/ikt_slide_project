from Globals import *

def GameOver():
    # r.screen.fill("#93bfb4")
    if r.Points > r.Best:
        gover_text = r.gover_font.render("NEW HIGHSCORE!", True, "#5800d4")
        score_text = r.gover_font.render(f"Score: {str(round(r.Points,0)).split('.')[0]}", True, "#6b0101")

    else:
        gover_text = r.gover_font.render("Game over", True, "red")
        best_text = r.score_font.render(f"Best: {str(round(r.Best,0)).split('.')[0]}", True, "black")
        score_text = r.score_font.render(f"Score: {str(round(r.Points,0)).split('.')[0]}", True, "black")
        best_rect = best_text.get_rect(center=(960,520))
        r.screen.blit(best_text,best_rect)

    gover_rect = gover_text.get_rect(center=(960,280))
    r.screen.blit(gover_text,gover_rect)


    score_rect = score_text.get_rect(center=(960,400))
    r.screen.blit(score_text,score_rect)

    again_text = r.score_font.render("Key [R] to restart", True, "black")
    again_rect = again_text.get_rect(center=(960,860))
    r.screen.blit(again_text,again_rect)
