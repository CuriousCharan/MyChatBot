
# Charan's Interest's Bot

A Conversational AI chatbot created using RASA 3.3 version as part of the Final project for CMPE 252 Course: Fall 2022


## Features

- Can do the basic conversation and humalny responses with more than 30 intents and possible multi-turn conversation
- Fetch the latest news using News API
- Is able to give Info about common space queries and astronomy
- Is planned to integrate with Slack Messenger
- It can also fetch information about recent and upcoming cricket matches around the world


## Setup & Instructions to run on CLI

Project Environment
````bash
Rasa Version      :         3.3.3
Minimum Compatible Version: 3.0.0
Rasa SDK Version  :         3.3.0
Python Version    :         3.7.0
````
```bash
 Inititate Virtual python virtual Environment in your desired path
 pip upgrade and rasa installatiion
 rasa init 
 rasa train
 rasa run actions -- in different command window
 rasa shell
```
    
## Sample Stories

* Conversational Talk
   #####  Hello  
   ##### how are you doing
   ##### are you there
   ##### what can you do
   ##### tell me about space
   ##### cheer me up
   ##### you are bad
   ##### show me recent cricket matches results
   ##### what's the news
   ##### thank you
   ##### bye
* read more Inside in stories.yml and domain.yml


## Screenshots

![App Screenshot](https://drive.google.com/file/d/1849nIcucsvYc8NJxQgkl-Eapn7pbOZzk/view?usp=share_link)
![App Screenshot2](https://drive.google.com/file/d/1hjJv8qLM2yeB_sZlezoX4D34O2SuB8xN/view?usp=share_link)

## API Reference

#### Get all items

```http
  GET  https://newsapi.org/v1/articles?source=google-news&sortBy=top&apikey=<your_newsapi_key>
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET (https://api.cricapi.com/v1/ + "matches" + "?apikey=" + CRIC_API_KEY + "&offset=0")
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `CRIC_API_KEY`      | `string` | **Required**. API key of account to fetch |




## Acknowledgements

 - [RASA Documentation](https://rasa.com/docs/rasa/)
 - [Everything about NEWS API](https://newsapi.org/)
 - [RASA Issues maintained at github](https://github.com/RasaHQ/rasa/issues)
 - [CMPE 252 Course Learnings]
 - [Ofcourse Stack Overflow]

