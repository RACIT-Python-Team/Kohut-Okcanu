import cv2
import json

class MapEngine:
    def __init__(self, zones_list):
        self.zones = zones_list

    def create_virtual_map(self, W, H): 
        # Використовуємо твій файл mapa.jpg як макет
        map_img = cv2.imread("mapa.jpg")
        if map_img is None:
            # Якщо файлу немає, створюємо порожній кадр
            import numpy as np
            map_img = np.zeros((H, W, 3), np.uint8)
        map_img = cv2.resize(map_img, (W, H))
        return map_img

    def check_zone(self, scaled_x, scaled_y):
        for zone in self.zones:
            min_x, min_y, max_x, max_y = zone["norm_coords"]
            if min_x <= scaled_x <= max_x and min_y <= scaled_y <= max_y:
                return zone
        return None