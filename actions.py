# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hello World!")

        return []


# class ActionQueryLibraryMembership(Action):
#     def name(self) -> Text:
#         return "action_library_membership"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         response = "To join our library, you can visit one of our branch libraries or you can register online via " \
#                    "the link https://libreg.cityofparramatta.nsw.gov.au/ Fill up the form and register. A temporary " \
#                    "library card number is provided. You have to visit one of our library branches with the number " \
#                    "and an identification document. A library card will be issued and you will be able to start " \
#                    "borrowing items. Parents or guardians of children or teens under 18 will need to provide their " \
#                    "own identification, along with documents (i.e. Medicare card) showing their relationship. If you " \
#                    "do not show ID within 6 weeks, the temporary card will be deleted."
#         dispatcher.utter_message(response)
#
#         return []