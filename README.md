Project Overview:

In this project a meme generator was created to take images, quotes and the author of the quotes and combine
them together to create ready to use memes. The generator can take images from URL links or from local directories.
The quotes can either be from PDF's, Word docs, CSV's, text files or input taken directly from the user. The user 
interface is through a website that is running on a flask app server. This way the application is readily accessible 
through a web browser and the internet. There are 2 engines that are powering the app server the QuoteEngine 
and the MemeEngine.


Modules and sub-Modules:

The QuoteEngine consists of the IngestorInterface class and the QuoteModel class. The IngestorInterface class 
consists of the Ingestor sub-class, the CSVImporter sub-class, the DocxImporter sub-class, the PDFImporter 
sub-class, and the TXTImporter sub-class. The CSVImporter utilizes the pandas python package to read and parse 
CSV files. The DocxImporter utilizes the docx python package to read and parse Docx files. The PDFImporter utilizes 
the pdftotext function of the xpdf program through the command line interface and then reads and parses the text 
with built-in python packages. The TXTImporter utilizes built-in python packages to read and parse text files. 
Lastly, the Ingestor utilizes the 4 Importer sub-classes to read and parse files based on the file extension.
To test each of the Importer sub-classes there is a section in main.py called 'Test Importers' where each Importer
is listed and can be uncommented, so that when main.py is run that Importer will be executed.

The MemeEngine consists of the MemeEngine class, which utilizes the Pillow python package to resize the input 
image and to write the quote and the quote's author on the resized image to generate the meme. To test the
MemeEngine there is a section in main.py called 'Test making a meme' where variables have been defined with
examples to pass in to the make_meme function, once each line has been uncommented then when main.py is ran
the MemeEngine will be executed.

The last section in main.py called 'Generate a user defined meme from user input' tests taking user input 
from the command line interface and generating a meme from the user input.


Setting up and running the app:

In order to run the meme generating web app on the flask app server we'll use the virtual environment to run 
the application.

First create the virtual environment using the command:

python3.5 -m venv venv

Then activate the new virtual environment with:

source venv/bin/activate

Now install dependancies with:

pip install -r req.txt

Then run the flask server with the 2 commands:

export FLASK_APP=app.py

flask run --host 0.0.0.0 --port 3000 --reload

And once running the webpage can be accessed by the address 0.0.0.0 port 3000.
