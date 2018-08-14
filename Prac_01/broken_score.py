"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# score = float(input("Enter score: "))
# if (score <= 100) and (score > 0):
#     if (score <= 100) and (score >= 90):
#         print("Excellent")
#     else:
#         if (score < 90) and (score >= 50):
#             print("Passable")
#         else:
#             print("Bad")
# else:
#     print("invalid score")

score = float(input("Enter score: "))
if (score < 0) or (score > 100):
    print("invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
