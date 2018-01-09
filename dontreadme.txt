10 January 2013

Overview:
	# Significantly tested - banolota.png, komola.jpg, komola5.jpg, komola-cam.jpg, komola-cam-dpi-changed.jpg, unnamed.png
	# ocr.py - tesseract with pytesseract, input - image file, output - text - www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
	# pytest.py - segments by lines/words and use the ocr.py as function defined as ocrpy
	# pytest.py takes much more time than ocr.py
	# pytest.py seemed better for curved images like komola.jpg
	# ocr.py failed in curved sections of komola.jpg
	# Tested --oem modes of tesseract - https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage
	# Image quality matters big time, using CamScanner gave a lot better output and better binarization
	# Best output for komola-cam.jpg
	# Changed dpi of komola-cam.jpg to komola-cam-dpi-changed.jpg which reduced time from 79s to 40s
	# Interestingly, changing the dpi gave correct ouptut for some particular words which was not the case before changing dpi
	# Bengali '।' tends to be recognized as '1' or 'I'
	# Otsu binarization did not make any difference for the images we tested
	# dpi was changed to 300 and image size reduced
	# Different modes did not make much difference except --oem 0 took 10s less
	# eng-input.jpg took only 18s with a lower quality image and output
	# Basically, good quality images matter
