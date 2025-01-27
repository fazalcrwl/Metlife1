import torch
from transformers import ViTModel, ViTFeatureExtractor
from PIL import Image
import numpy as np
#from utils.common import read_yaml
#from logging1 import logger
class MyModel():
    def __init__(self):

        
        
        model = ViTModel.from_pretrained('google/vit-base-patch16-224-in21k')
        self.feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224-in21k')
        self.model=model.eval()
        #logger.info("model Intilization has been completed ")
    def image_to_embedding(self,image_path):
        image = Image.open(image_path).convert('RGB')
        inputs = self.feature_extractor(images=image, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
            embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

          #  logger.info("image to embedding has been completed ")
        return embedding
        