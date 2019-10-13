I have made assumptions that gist retrieval and edit will be done for a user(In this case
its me) so this code will run only on my github account since the ApiKeys and Gist belongs to me.
For making edits to someone else's account use their own gist ID and Apikey.

There is an "ApiKey" constant in the Base.py class which can be changed.
Similarly "ID"  constant in the Constants.py class which can be changed.

The Apikey is my private and ID for the gist is public.

NOTE:I will delete this after 4 days.

INSTALLATION:
Please install python 3.7.5 version.

library needed - requests.
    command "pip install requests"
external library for testing - pytest
    command "pip install -U pytest"

Link to my gist where you can view the UI



RUNNING:
1)
Make sure to run Setup.py FIRST for creating files in the gist
"pytest -s -q Setup.py"

2)
After installation of the required packages use following command for
running the test

"pytest -s -q Test1.py"

There are 5 test files

3)
For teardown of files use this

"pytest -s -q Teardown.py"

Please run all files individually to see what it does. Run Setup and teardown class. They can be considered as test
cases since I am creating and deleting the files.