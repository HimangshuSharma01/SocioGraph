# SocioGraph
People You May Know A Python-powered recommendation engine for social networks.  What it is A simple tool that takes a JSON file of users and suggests new friends based on mutual connections. It mimics the "People You May Know" feature on platforms like Facebook or LinkedIn.

Features
JSON Integration: Loads user data from a raw JSON file.

Mutual Friend Logic: Identifies "friends of friends" who aren't already in your circle.

Ranking System: Sorts recommendations so people with the most mutual connections appear first.

Efficient Lookups: Uses Python sets for high-performance data filtering.

How it Works
Map: Parses the JSON to create a dictionary of users and their friend lists.

Scan: Iterates through a user's friends to find their connections.

Filter: Removes the user themselves and their current friends from the results.

Rank: Counts how many times each "stranger" appears and returns them in descending order.

Example Data Structure
JSON
{
  "users": [
    {"id": 1, "name": "Alice", "friends": [2, 3]},
    {"id": 2, "name": "Bob", "friends": [1, 4]}
  ]
}
Tech Stack
1. Python 3
2. JSON Module
