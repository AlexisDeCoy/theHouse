# The House

The House is my first development project, a text-based, interactive fiction horror game inspired by Anchorhead, where players are tasked to explore and uncover the mysteries of their new home. This game features puzzles, grotesque locations, witchcraft, and a variety of items to collect, each of which was lovingly drawn by Bug Karplus.

## Goals

With The House, I wanted to make something relatively easy to style that still took advantage of the things I had learned. I included page routing, state variables, login and registration, a database, and a whole lot of HTML. As is, this project only took a week, and for that, I am very proud of it.

## Development

- I used Python with Flask to manage the front-end and routing.
- Every page is its own HTML file, each containing embedded links that direct to other pages.
- Data tracking is tied to a given user account, where items and certain task completion are stored in an SQL database.
- User passwords are securely stored using a hash.
- Styling was intentionally minimal, designed to feel creepy and old, like the house itself. Images were stored locally as part of the project.
- File structure was crucial for this project, since there are 48 different HTML files.

## Next Steps

When I get the chance to go back to this project, there are so many things I want to try out. I had a great time with the writing, so I want to add more to the story. I want to make more puzzles too, either with existing items or with new ones. There's also a bunch of ideas I have using animations to make things creepier. The one I'm most excited about is adding a glow around the cursor when the player is in the basement with the lighter. Adding sound effects would also be a lot of fun.
