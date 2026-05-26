import random

"""
This script asks the user to select a task category and then randomly selects an item from that category.
The purpose is to help decrease decision fatigue and just help the user to start
working on and make progress in core goal

Linna's goals:
- create videos for YouTube -> YouTube, Instagram, RedNote
- write blog articles and a weekly newsletter -> newsletter, twitter, blog
- build web apps and mobile apps -> GitHub
"""

# video projects list can be found in file: 

video_projects = [
    "continue working scheduled video: most interesting",
    "new - video using existing content - travel", 
    "new - video using existing content - house renovation", 
    "new - video inspired by notes from journal",
    "new - video interview with someone in my network (YouTube, Groups, Contacts, LinkedIn, ect)",
]

# writing projects list can be found in file: 
# Ideas - Writing for Blog and Weekly Newsletter
# Have to at least pubish weekly newsletter
# Writing to my blog is not a priority at the moment (2025-07)
writing_projects = [
    "new - build a landing page for a product and sell it",
    "edit existing blogs on website; most interesting",
    "pick from the list of ideas on: Ideas - Writing for Blog and Weekly Newsletter",
    "new - write about how you're feeling right now",
    "new - write about a topic inspired by notes from journal",
    "new - write about what you've learned today",
]

# software projects list can be found in file: 
# Ideas - Business Products and Services
# The goal is to regularly stand up software projects to get good sense of
# building from scratch
software_projects = [
    "new - build a landing page for a product and sell it",
    "pick from the list of ideas on: Ideas - Business Products and Services",
    "work on existing project; most interesting ",
    "new - build fastAPI backend using https://github.com/public-apis/",
    "new - build SST NextJS app using https://github.com/public-apis/",
    "new - build react native using https://github.com/public-apis/",
]

category = [
   "Animals", "Anime", "Anti-Malware", "Art & Design", "Authentication & Authorization", "Blockchain", "Books", "Business", "Calendar", "Cloud Storage & File Sharing", "Continuous Integration", "Cryptocurrency", "Currency Exchange", "Data Validation", "Development", "Dictionaries", "Documents & Productivity", "Email", "Entertainment", "Environment", "Events", "Finance", "Food & Drink", "Games & Comics", "Geocoding", "Government", "Health", "Jobs", "Machine Learning", "Music", "News", "Open Data", "Open Source Projects", "Patent", "Personality", "Phone", "Photography", "Programming", "Science & Math", "Security", "Shopping", "Social", "Sports & Fitness", "Test Data", "Text Analysis", "Tracking", "Transportation", "URL Shorteners", "Vehicle", "Video", "Weather"
]


# A mapping of a user input to a list variable
TASKMAP = {
    "1": video_projects,
    "2": writing_projects,
    "3": software_projects,
    "4": category,
 
}

# input for user to select a task category
task_category = input("Please select a task category:\n"
                    " 1. Work on video project (Tue, Thu, Sun) \n"
                    " 2. Work on writing project (Mon, Wed, Fri) \n"
                    " 3. Work on software project (Everyday, Sat)\n"
                    " 4. Choose a category to focus on \n"
                    )



print("The task choosen for you is:")
print(random.choice(TASKMAP[task_category]))
print('\n')
print("Choiced in the category you selected:")
print(TASKMAP[task_category])