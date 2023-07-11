import pygame as pg
import random
import sys

WIDTH = 800  # ゲームウィンドウの幅
HEIGHT = 600  # ゲームウィンドウの高さ


class Time:
    """
    時間の管理を行うクラス
    """
    def __init__(self):
        self.font = pg.font.Font(None, 36)
        self.color = (125, 125, 125)
        self.tmr = 60
        self.image = self.font.render("Time: " + str(self.tmr), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = 60, 50
    
    def time_subtract(self):
        self.tmr -= 1  #timeを-1する。

    def update(self, screen: pg.Surface):
        self.image = self.font.render("Time: " + str(self.tmr), True, self.color)
        screen.blit(self.image, self.rect)

def main():
    clock = pg.time.Clock()
    frame_count = 0  #フレーム数をカウントする為の変数
    time = Time()

    # 色
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    # ウィンドウを作る
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("coin getter")

    # player初期位置
    player_x = 400
    player_y = 500

    # player
    player = pg.Rect(player_x, player_y, 50, 50)

    # コインを作る
    coins = []
    for i in range(10):
        x = random.randint(0, WIDTH - 50)
        y = random.randint(-HEIGHT, -50)
        coin = pg.Rect(x, y, 50, 50)
        coins.append(coin)

    # スコア初期値
    score = 0

    # main循環
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        #Timeが0になったらゲーム終了
        if time.tmr == 0:
            return False

        # player移動
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            player.x -= 5
        if keys[pg.K_RIGHT]:
            player.x += 5

        # ウィンドウ更新
        screen.fill(WHITE)
        pg.draw.rect(screen, YELLOW, player)

        # コインの位置を更新
        for coin in coins:
            coin.y += 1
            pg.draw.ellipse(screen, YELLOW, coin)

            # 衝突検出
            if player.colliderect(coin):
                coins.remove(coin)
                score += 1

            # コインを再生する
            if coin.y > HEIGHT:
                coin.x = random.randint(0, WIDTH - 50)
                coin.y = random.randint(-HEIGHT, -50)

        # スコア
        font = pg.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, YELLOW)
        screen.blit(text, (10, 10))

        frame_count += 1  
        time.update(screen)  
        pg.display.flip()
        #timeを200フレームごとに-1する。
        if frame_count % 200 == 0:
            time.time_subtract() 
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()