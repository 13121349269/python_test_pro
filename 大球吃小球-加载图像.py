#大球吃小球-加载图像

import pygame

def main():
    #初始化导入的pygame中的模块
    pygame.init()
    #初始化用于线上IDE窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    #设置窗口的标题
    pygame.display.set_caption('大球吃小球')
    #设置窗口的背景颜色(暗色是由红绿蓝三原色构成的元组)
    screen.fill((252,252,252))
    #通过指定的文件名加载图像
    ball_image = pygame.image.load('./res/ball.png')
    #窗口渲染图像
    screen.blit(ball_image, (50,50))
    #绘制一个圆(参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆)
    #pygame.draw.circle(screen, (255,0,0),(100,100),30,0)
    #刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    running = True
    #开启一个事件循环处理发生的时间
    while running:
        #从消息队列中获取时间病对时间进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()