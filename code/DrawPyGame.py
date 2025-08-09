import pygame
import os

class AssetCutter:
    def __init__(self, sheet_path):
        # 스프라이트 시트만 로드 (display는 main()에서 초기화)
        self.sheet = pygame.image.load(sheet_path).convert_alpha()

    def crop_asset(self, rect):
        x, y, w, h = rect
        sub = pygame.Surface((w, h), pygame.SRCALPHA)
        sub.blit(self.sheet, (0, 0), pygame.Rect(x, y, w, h))
        return sub

    def crop_assets(self, regions):
        return {name: self.crop_asset(r) for name, r in regions.items()}


class Draw:
    def __init__(self, ):
        self.sheet = AssetCutter("./image/walls_floor.png")
        regions = {

            "wall_left" : (16, 16, 16, 16), 
            "wall_right" : (47, 16, 16, 16), 
            "wall_top" : (), 
            "wall_bottom" : (), 




        }


        

''' 대화 상자

디코 1대1로 하나요?
저기 방에는 통화방이 없네요




'''


