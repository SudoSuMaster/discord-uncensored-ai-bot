Ollama setup:
Run ollama in docker with this docker compose file 
https://github.com/SudoSuMaster/docker-compose-files/blob/main/ollama-ai/docker-compose.yml
go to the path where you pulled the compose and run it with the command: docker compose up -d

Setting Up a Discord Bot:

1. Go to the Discord Developer Portal: Visit Discord Developer Portal and log in with your Discord account.

2. Create a New Application:
  Click on the "New Application" button.

4. Configure Your Application:
  Give your application a name (this will be your bot's name) and upload an icon.
  Optionally, you can add a description to your application.

5. Enable Bot Capabilities:
  Navigate to the "Bot" tab in your application settings.
  Toggle the "MESSAGE CONTENT INTENT" switch to enable your bot to access message content.
  Generate Bot Invite Link:
![image](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/eab4acb2-e189-4546-8abd-59d02da40b31)

6. Go to the "OAuth2" tab in your application settings.
  Under "OAuth2 URL Generator," select "bot" in the "SCOPES" section.
![image](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/6c20ccba-3b91-4100-9566-4fc32b046182)

7. Configure Bot Permissions:
  Scroll down to the "BOT PERMISSIONS" section and select the required permissions for your bot, such as "Send Messages," "Read Message History," and "Read Messages" (or "View Channels").
![image](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/0a18b618-6833-4a46-a900-dc590931be1e)

9. Invite Your Bot to a Server:
  After selecting permissions, the bot invite link will be generated.
  Copy the invite link and paste it into your browser to add the bot to your server.
![image](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/a4f2b9cd-9dbe-4db0-95dd-bf8727e7e881)


Discord token:
1. Change the .env copy to .env

2. paste your discord token in the .env file
find your token in the dev portal under bot --> reset token (Dont share this with anyone)
![image](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/0897fbe9-6588-404e-b410-fd168eb749a9)

Ollama API:
change the api url, 
![image](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/af915dc7-41b1-4e6d-8270-549a8f220f3e)

to find the api url go to ollama webui --> setting --> general 
![image](https://github.com/SudoSuMaster/discord-uncensored-ai-bot/assets/75373825/fbc41311-755a-4999-90ec-1d4c24200b78)

run the main.py and you are ready to go

Note: if you have a gpu it will be used as default, if not you need to change the compose to cpu instead of gpu. Check the official documentaion for that.
