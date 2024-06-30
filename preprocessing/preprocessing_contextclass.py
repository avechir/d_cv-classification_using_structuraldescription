class PreprocessContextClass:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def descriptors_preprocessing(self, bit_des_etalons):
        return self.strategy.descriptors_preprocessing(bit_des_etalons)