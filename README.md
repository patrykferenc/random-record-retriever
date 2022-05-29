# Random record retriever

A simple program that first finds a list of random words, then retrieves the records for each of them.

# How to clone the repository

Use the following command to clone the repository:

```
git clone git@github.com:patrykferenc/random-record-retriever.git [your-repository-location]
```

# Configuration

Note that you should use python 3 for this project.
Also it is recommended to use a virtual environment.


Run the following command to install the package (make sure you are in the root of the repository):

```
pip install .
```

Install the dependencies if they are not installed automatically (for whatever reason):

```
make init
```

(...or if you prefer to do it by hand):

```
pip install -r requirements.txt
```


# Usage

After you have successfully installed the program, you can use it by running the following command:

```
python -m randrecord [number-of-records-between-5-and-20]
```

# License

This program is licensed under the [BSD 2-Clause License](https://opensource.org/licenses/BSD-2-Clause).