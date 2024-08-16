
import os 
from src.model import MyModel
from src.chroma_db import MyDb
#from logging import logger 


class Store_img():
    def __init__(self,dataset_path):
        self.model=MyModel()
        self.db=MyDb()
        self.collection=self.db.collection
        self.dataset_path=dataset_path
        

        


    def process_dataset_and_store_embeddings( self):
        image_files = [f for f in os.listdir(self.dataset_path) if os.path.isfile(os.path.join(self.dataset_path, f))]
        
        for idx, image_file in enumerate(image_files):
            image_path = os.path.join(self.dataset_path, image_file)
            embedding = self.model.image_to_embedding(image_path)
            image_id = f"image_{idx+1}"
            self.db.store_embedding(self.collection, embedding, image_id)
            print(f"Stored embedding for {image_file} with ID: {image_id}")
#            logger.info("vector db stored images extraction has been completed ")
    
    
    def compare_image(self, input_image_path):
        input_embedding = self.model.image_to_embedding( input_image_path)
        results = self.collection.query(query_embeddings=[input_embedding], n_results=1)  # Get the closest match
       # logger.info("comparison between the images is completed")
        return results
