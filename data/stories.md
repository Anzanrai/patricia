## introduction path
* greet
  - utter_greet
* ask_intro
  - utter_intro

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
  
## library membership path 1
* greet
  - utter_greet
* join_library
  - utter_join_library
* goodbye
  - utter_goodbye
  
## library membership path 2
* greet
  - utter_greet
* join_library
  - utter_join_library
* get_library_branches
  - utter_library_branches
* goodbye
  - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_greet
* greet
    - utter_greet

## interactive_story_1
* ask_intro
    - utter_intro
* greet
    - utter_greet
* goodbye
    - utter_goodbye
