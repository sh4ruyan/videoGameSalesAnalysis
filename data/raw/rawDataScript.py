from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()

api.authenticate()


api.dataset_download_files("rush4ratio/video-game-sales-with-ratings", path="data/raw", unzip=True)
