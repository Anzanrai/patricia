# patricia

## project environment setup
- clone the repo using the command "git clone git@github.com:Anzanrai/patricia.git"
- install the requiremnt mentioned in the requirements.txt using pip "pip3 install -r requirements.txt"

## to train the model
- rasa train (this generates the model to the models folder)

## to train interactively
- rasa interactively -m models/<model_name> --endpoints <endpointFilename><br>
  eg. rasa interactively -m models/20190816-130101.tar.gz --endpoints endpoints.yml
