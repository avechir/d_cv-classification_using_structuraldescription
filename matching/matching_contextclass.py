class MatchContextClass:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def match_images(self, bit_des_img, bit_des_etalons):
        return self.strategy.match_images(bit_des_img, bit_des_etalons)