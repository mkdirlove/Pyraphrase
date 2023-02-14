<h1 align="center">
  <br>
  <a href="https://github.com/mkdirlove/Pyraphrase"><img src="https://github.com/mkdirlove/Pyraphrase/blob/main/logo.png" alt="Pyraphrase"></a>
  <br>
  Paraphrase text using the Paraphrase Genius API.
  <br>
</h1>

#### Installation

Copy-paste this into your terminal:

```
git clone https://github.com/mkdirlove/Pyraphrase
```
```
cd Pyraphrase
```
```
python3 Pyraphrase.py -h
```

#### Usage
```
╔═╗╦ ╦╦═╗╔═╗╔═╗╦ ╦╦═╗╔═╗╔═╗╔═╗
╠═╝╚╦╝╠╦╝╠═╣╠═╝╠═╣╠╦╝╠═╣╚═╗║╣
╩   ╩ ╩╚═╩ ╩╩  ╩ ╩╩╚═╩ ╩╚═╝╚═╝

usage: Pyraphrase.py [-h] [-t TEXT] [-f FILE] [-r RESULT_TYPE] [-o OUTPUT]

Pyraphrase - Paraphrase text using the Paraphrase Genius API

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  the text to paraphrase
  -f FILE, --file FILE  the input file to read text from
  -r RESULT_TYPE, --result_type RESULT_TYPE
                        the type of result to return (single or multiple)
  -o OUTPUT, --output OUTPUT
                        the output file to save the results to
```

#### Sample Usage 1

Paraphrase text from input with single output

```
python3 Pyraphrase.py -t 'Some thext here to paraphrase' -r single -o paraphrased.txt
```

#### Sample Usage 2

Paraphrase text from input with multiple output

```
python3 Pyraphrase.py -t 'Some thext here to paraphrase' -r multiple -o paraphrased.txt
```

#### Sample Usage 3

Paraphrase text from input file with single output

```
python3 Pyraphrase.py -f toParaphrase.txt -r single -o paraphrased.txt
```
