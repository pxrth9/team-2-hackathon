# MLH Fellow Introducer Bot
Helping fellows learn more about fellows with a single word!

## Inspiration
Tired of awkward icebreakers in Zoom meetings? Ever wanted to find out more about an MLH Fellow in your pod at the mention of their name, without disturbing them? Say no more! The Introducer Bot helps you break the ice in any Discord server or channel you invite it to.

## What it does
Once the Introducer Bot is invited to a server/channel, MLH Fellows can begin interacting with it! The bot provides the ability for Fellows to store information like their name, pronouns, geographic location, favorite programming languages, and more in a secure cloud database!

**Want to learn more about another Fellow?** Try typing in `!info @fellow` in your channel! You'll see an easy-to-use embed with links to that Fellow's GitHub, LinkedIn, and their Calendly! 

**Want to edit/create your very own profile?** Try using the `!edit @fellow field value` command!

## How we built it
We utilized the following languages, frameworks, and tools:

- [**Python**](https://www.python.org/) - main back-end language
- [**discord.py**](https://discordpy.readthedocs.io/en/stable/) - a modern, easy to use, feature-rich, and async ready API wrapper Discord to handle all Discord bot logic
- [**Firebase Realtime Database**](https://firebase.google.com/docs/database) - NoSQL cloud-hosted database; stores data as JOSN and synchronizes in realtime to every connected client, providing scalability, security, flexibility, and accessibility

## Challenges we ran into

Our primary challenge was finding and scheduling time to work this week. Our team composition shifted very early on, and scheduling conflicts with full-time schooling as well as time zone differences meant that much of our work was asynchronous.

Another challenge was working with a combination of frameworks and tools we weren't familiar with. While we had varied experience with Python and Firebase, we had never utilized the discord.py library alongside Firebase. Implementing features while learning about them for the first time was challenging but immensely satisfying when we saw our bot working for the first time!

## Accomplishments that we're proud of:

- Shipping a minimum viable product, especially with all of our team's scheduling issues and time-zone conflicts
- Integrating Firebase with discord.py

## What we learned

For the majority of the team, this was our first time building a Discord bot, and even more so, utilizing Firebase and Python together to build a Discord bot. We learned how to setup a barebones Realtime Database in Firebase, edit and push changes for fellows, and dove deep into Discord bot documentation to deliver a fast, efficient bot experience for MLH Fellows to enjoy!

## What's next for the Introducer Bot
Adding tons of functionality, including:

- minigames (ex. Tic-Tac-Toe, Chess, Werewolf)
- refactoring the profile creation process
- writing robust unit tests
- setting up automatic deployment via GitHub Actions
- integrating the Introducer Bot with other MLH Fellowship server bots!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install MLH Icebreaker Bot.

```
pip install -r requirements.txt

python main.py <-- TO Run the bot locally
```

## Usage

Add the discord bot to your server using this link: [MLH Icebreaker Bot](https://discord.com/api/oauth2/authorize?client_id=890319728474750997&permissions=534723951680&scope=bot)

```
!edit @user key value-> Edit your own profile
!info @mention -> Get Info about your fellow pod mate
!schedule @user -> Schedule a time slot with your fellow pod mate
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
