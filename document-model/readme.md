# Document Model

Contains code needed to annotate documents & use those annotations to train & run inference on a document NER model.

# Environment Setup

* **Create a new conda environment**

 ```
conda create -n document-model python=3.9
```

* **Activate the conda environment**

 ```
conda activate document-model
```

* **Install required Python dependencies**

 ```
pip install -r requirements.txt
```

* **Install tesseract binary**

 On Mac:

 ```
brew install tesseract
 ```

 On Linux:

 ```
sudo apt-get update
sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
```

