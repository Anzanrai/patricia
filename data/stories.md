## introduction path
* ask_intro
  - utter_intro

## ask_about_heritage
* greet
    - utter_greet_with_chat_options
* chat_intent
    - utter_chat_options
* ask_heritage_info
    - utter_heritage_info
* goodbye
    - utter_goodbye
    
## deny_knowledge
* greet
    - utter_greet_with_chat_options
* deny
    - utter_goodbye_with_future_offer
    
## ask_about_events
* greet
    - utter_greet_with_chat_options
* affirm
    - utter_chat_options
* events
    - utter_upcoming_events_title
* event_title_selection
    - utter_event_detail
* goodbye
    - utter_goodbye
    
## ask_about_news
* greet
    - utter_greet_with_chat_options
* affirm
    - utter_chat_options
* news
    - utter_new_news_title
* news_title_selection
    - utter_news_detail
* goodbye
    - utter_goodbye
    
## ask_about_heritage
* greet
    - utter_greet_with_chat_options
* affirm
    - utter_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "NSW Lancers Barracks and Museum"} 
    - get_heritage_detail
    - slot{"heritage_name": "Philip Ruddock Heritage Centre"}
    - utter_question_for_user_next_interest
    
## ask_about_heritage_002
* greet
    - utter_greet_with_chat_options
* affirm
    - utter_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "NSW Lancers Barracks and Museum"}
    - get_heritage_detail
    - slot{"heritage_name": "Hambledon Cottage"}
    - utter_question_for_user_next_interest
    
## ask_about_heritage_003
* greet
    - utter_greet_with_chat_options
* affirm
    - utter_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "NSW Lancers Barracks and Museum"}
    - slot{"heritage_name": "NSW Lancers Barracks and Museum"}
    - get_heritage_detail
    - slot{"heritage_name": "NSW Lancers Barracks and Museum"}
    - utter_question_for_user_next_interest
* goodbye
    - utter_goodbye
    
## ask_about_heritage_004
* greet
    - utter_greet_with_chat_options
* affirm
    - utter_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "Hambledon Cottage"}
    - slot{"heritage_name": "Hambledon Cottage"}
    - get_heritage_detail
    - slot{"heritage_name": "Hambledon Cottage"}
    - utter_question_for_user_next_interest
* goodbye
    - utter_goodbye
    
## proceed_with_cultural_heritage_after_greeting_with_affirmation
* greet
    - utter_greet_with_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "Hambledon Cottage"}
    - get_heritage_detail
    - slot{"heritage_name": "Philip Ruddock Heritage Centre"}
    - utter_question_for_user_next_interest
* affirm
    - utter_chat_options
    
## proceed_with_cultural_heritage_after_greeting_with_affirmation_002
* greet
    - utter_greet_with_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "NSW Lancers Barracks and Museum"}
    - get_heritage_detail
    - slot{"heritage_name": "Hambledon Cottage"}
    - utter_question_for_user_next_interest
* affirm
    - utter_chat_options
    
## proceed_with_cultural_heritage_after_greeting_with_affirmation_003
* greet
    - utter_greet_with_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "NSW Lancers Barracks and Museum"}
    - slot{"heritage_name": "NSW Lancers Barracks and Museum"}
    - get_heritage_detail
    - slot{"heritage_name": "NSW Lancers Barracks and Museum"}
    - utter_question_for_user_next_interest
* affirm
    - utter_chat_options

## proceed_with_cultural_heritage_after_greeting_with_affirmation_004
* greet
    - utter_greet_with_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "Hambledon Cottage"}
    - slot{"heritage_name": "Hambledon Cottage"}
    - get_heritage_detail
    - slot{"heritage_name": "Hambledon Cottage"}
    - utter_question_for_user_next_interest
* affirm
    - utter_chat_options
    
[comment]: # End with denial
## proceed_with_cultural_heritage_after_greeting_with_denial_001
* greet
    - utter_greet_with_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "Hambledon Cottage"}
    - get_heritage_detail
    - slot{"heritage_name": "Philip Ruddock Heritage Centre"}
    - utter_question_for_user_next_interest
* deny
    - utter_goodbye_with_future_offer
    
## proceed_with_cultural_heritage_after_greeting_with_affirmation_002
* greet
    - utter_greet_with_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "NSW Lancers Barracks and Museum"}
    - get_heritage_detail
    - slot{"heritage_name": "Hambledon Cottage"}
    - utter_question_for_user_next_interest
* deny
    - utter_goodbye_with_future_offer
    
## proceed_with_cultural_heritage_after_greeting_with_affirmation_003
* greet
    - utter_greet_with_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "NSW Lancers Barracks and Museum"}
    - slot{"heritage_name": "NSW Lancers Barracks and Museum"}
    - get_heritage_detail
    - slot{"heritage_name": "NSW Lancers Barracks and Museum"}
    - utter_question_for_user_next_interest
* deny
    - utter_goodbye_with_future_offer

## proceed_with_cultural_heritage_after_greeting_with_affirmation_004
* greet
    - utter_greet_with_chat_options
* heritage_title
    - get_heritage_title
* heritage_detail{"heritage_name": "Hambledon Cottage"}
    - slot{"heritage_name": "Hambledon Cottage"}
    - get_heritage_detail
    - slot{"heritage_name": "Hambledon Cottage"}
    - utter_question_for_user_next_interest
* deny
    - utter_goodbye_with_future_offer