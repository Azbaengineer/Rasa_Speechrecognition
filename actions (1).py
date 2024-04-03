# actions.py
import json
import requests
from typing import Dict, Text, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCourses(Action):
    def name(self) -> Text:
        return "action_courses"

    def run(self, dispatcher: CollectingDispatcher, 
            domain, tracker: Tracker) -> List[Dict[Text, Any]]:
      
        course_number = tracker.get_slot('course_number')
        print(f"Extracted course_number: {course_number}")

        api_url = "http://127.0.0.1:5000/courses"

        try:
            response = requests.get(api_url)

            if response.status_code == 200:
            
                courses_data = response.json().get("courses", [])
               
                print("Courses retrieved from server:", json.dumps(courses_data, indent=2))

                course = next((c for c in courses_data if c.get("course_number") == course_number), None)
     
                print("Found course:", json.dumps(course, indent=2) if course else "None")

                if course is not None:                  
                    message = f"The course {course_number} details: {json.dumps(course, indent=2)}"
                else:
                    message = f"Course {course_number} not found."
            else:
                message = f"Failed to get courses. Status Code: {response.status_code}"

        except Exception as e: 
            message = f"An error occurred: {str(e)}"
      
        dispatcher.utter_message(text=message)
        return []
    



# # actions.py
# import json
# import requests
# from typing import Dict, Text, Any, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionCourses(Action):
#     def name(self) -> Text:
#         return "action_courses"

#     def run(self, dispatcher: CollectingDispatcher, 
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
#         course_number = next(tracker.get_slot('course_number'), None)
#         print(f"Extracted course_number: {course_number}")

#         api_url = "http://127.0.0.1:5000/courses"

#         try:
#             response = requests.get(api_url)

#             if response.status_code == 200:
            
#                 courses_data = response.json()
#                 for course in courses_data:
#                     if course["course_number"] == course_number:
#                         course_info = course["course_title"]
                        
               
#                 #print("Courses retrieved from server:", json.dumps(courses_data, indent=2))

#                 #course = next((c for c in courses_data if c.get("course_number") == course_number), None)
     
#                 #print("Found course:", json.dumps(course, indent=2) if course else "None")

#                 if course_info is not None:                  
#                     message = f"The course {course_number} details: {course_info}"
#                 else:
#                     message = f"Course {course_info} not found."
#             else:
#                 message = f"Failed to get courses. Status Code: {response.status_code}"

#         except Exception as e: 
#             message = f"An error occurred: {str(e)}"
      
#         dispatcher.utter_message(text=message)
#         return []
    





